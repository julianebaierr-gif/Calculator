# -*- coding: utf-8 -*-
"""
Script to generate Batch 18 Part 4 tools:
1. snells-law-calculator.html
2. specific-heat-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Snell's Law Calculator | Refraction Angle, Critical Angle & Fiber TIR</title>
  <meta name="description" content="Calculate light refraction angles, critical angle for total internal reflection, Brewster's angle, and numerical aperture using Snell's Law across optical media.">
  <link rel="canonical" href="https://calchub.cloud/snells-law-calculator.html">
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
        "name": "Snell's Law Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates optical refraction angles, critical angle for total internal reflection (TIR), Brewster's polarization angle, and fiber optic numerical aperture.",
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
            "name": "What is Snell's Law formula for light refraction?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Snell's Law states that the ratio of sines of the angles of incidence and refraction equals the reciprocal ratio of indices of refraction: n₁ × sin(θ₁) = n₂ × sin(θ₂), where n₁ and n₂ are refractive indices of the first and second media, θ₁ is the angle of incidence, and θ₂ is the angle of refraction relative to the surface normal."
            }
          },
          {
            "@type": "Question",
            "name": "What is total internal reflection (TIR) and how is the critical angle calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Total internal reflection occurs when light attempts to travel from an optically denser medium (higher n₁) into a rarer medium (lower n₂) at an angle exceeding the critical angle. The critical angle is calculated as θ_c = arcsin(n₂ / n₁). Beyond this angle, sin(θ₂) > 1, so 100% of light reflects internally without refractive transmission."
            }
          },
          {
            "@type": "Question",
            "name": "What is Brewster's angle in optics?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Brewster's angle (polarizing angle) is the specific angle of incidence at which light with p-polarization is perfectly transmitted through a transparent dielectric interface with zero reflection: θ_B = arctan(n₂ / n₁). Reflected light at this angle is 100% s-polarized."
            }
          },
          {
            "@type": "Question",
            "name": "How does Snell's Law govern telecommunications fiber optics?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Optical fibers consist of a high-index silica glass core (n_core ≈ 1.48) enclosed by a lower-index cladding (n_clad ≈ 1.46). Light injected into the core at angles shallower than the critical angle undergoes repeated total internal reflection, propagating data signals over hundreds of kilometers with minimal optical loss."
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
        <h1>Snell's Law Calculator</h1>
        <p class="lead-text">Calculate optical refraction angles, critical angles for total internal reflection (TIR), Brewster's polarization angle, and light speed across optical media.</p>

        <div class="calc-card">
          <div class="form-row">
            <div class="form-group col-half">
              <label for="med1Preset">Medium 1 (Incident Medium)</label>
              <select id="med1Preset" class="form-control">
                <option value="air" selected>Air (n₁ = 1.0003)</option>
                <option value="water">Water (n₁ = 1.333)</option>
                <option value="crownglass">Crown Glass (n₁ = 1.520)</option>
                <option value="flintglass">Dense Flint Glass (n₁ = 1.660)</option>
                <option value="diamond">Diamond (n₁ = 2.417)</option>
                <option value="fiber_core">Optical Fiber Core (n₁ = 1.480)</option>
                <option value="custom">Custom Refractive Index</option>
              </select>
            </div>

            <div class="form-group col-half">
              <label for="med2Preset">Medium 2 (Refracting Medium)</label>
              <select id="med2Preset" class="form-control">
                <option value="crownglass" selected>Crown Glass (n₂ = 1.520)</option>
                <option value="air">Air (n₂ = 1.0003)</option>
                <option value="water">Water (n₂ = 1.333)</option>
                <option value="flintglass">Dense Flint Glass (n₂ = 1.660)</option>
                <option value="diamond">Diamond (n₂ = 2.417)</option>
                <option value="fiber_clad">Optical Fiber Cladding (n₂ = 1.460)</option>
                <option value="custom">Custom Refractive Index</option>
              </select>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-third">
              <label for="n1Val">Refractive Index 1 (n₁)</label>
              <input type="number" id="n1Val" class="form-control" value="1.0003" step="0.0001" min="1.0">
            </div>

            <div class="form-group col-third">
              <label for="n2Val">Refractive Index 2 (n₂)</label>
              <input type="number" id="n2Val" class="form-control" value="1.520" step="0.0001" min="1.0">
            </div>

            <div class="form-group col-third">
              <label for="angle1Val">Angle of Incidence (&theta;₁)</label>
              <div class="input-with-unit">
                <input type="number" id="angle1Val" class="form-control" value="30" step="0.1" min="0" max="89.9">
                <span style="font-size:12px; padding:6px 12px; background:#fff; border:1px solid #cbd5e1; border-left:none; border-radius:0 4px 4px 0; display:flex; align-items:center;">Degrees (°)</span>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Refraction</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset to Air &rarr; Glass (30°)</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label" id="resPrimaryLabel">Angle of Refraction (&theta;₂)</div>
              <div class="result-value" id="resPrimaryVal">19.21°</div>
              <div class="result-sub" id="resPrimarySub">Light bends toward the normal (slower medium)</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Critical Angle for TIR (&theta;_c)</span>
                <span class="sub-value" id="resCritAngle">None (n₁ &le; n₂)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Brewster's Polarizing Angle (&theta;_B)</span>
                <span class="sub-value" id="resBrewster">56.65°</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Phase Velocity in Medium 1</span>
                <span class="sub-value" id="resV1">299,705 km/s (0.9997 c)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Phase Velocity in Medium 2</span>
                <span class="sub-value" id="resV2">197,232 km/s (0.6579 c)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Physical Foundations of Optical Refraction & Fermat's Principle</h2>
          <p>Refraction describes the abrupt redirection of an electromagnetic wave (such as visible light) as it passes obliquely across the interface separating two media possessing different optical phase velocities. While the temporal frequency of the wave remains completely invariant, the phase velocity \(v\) within any transparent dielectric medium is reduced relative to the vacuum speed of light (\(c = 299,792,458\text{ m/s}\)) by a dimensionless material property known as the <strong>refractive index</strong> (\(n\)):</p>
          <div class="math-block">
            $$n = \frac{c}{v}$$
          </div>
          <p>First quantified mathematically by Dutch astronomer Willebrord Snellius in 1621 and independently derived by René Descartes in 1637, <strong>Snell's Law</strong> governs the directional relationship between the angle of incidence \(\theta_1\) and angle of refraction \(\theta_2\) measured relative to the surface normal perpendicular to the boundary:</p>
          <div class="math-block">
            $$n_1 \sin\theta_1 = n_2 \sin\theta_2 \iff \frac{\sin\theta_1}{\sin\theta_2} = \frac{v_1}{v_2} = \frac{n_2}{n_1}$$
          </div>
          <p>In 1658, French mathematician Pierre de Fermat established the deep foundational physics underlying Snell's law through <strong>Fermat's Principle of Least Time</strong>: light rays traversing between two points follow the path that minimizes total elapsed transit time (\(t = \int \frac{ds}{v}\)). Just as a lifeguard runs along a sandy beach before diving into the water to reach a swimmer in the shortest time, light refracts toward the normal in a slower, optically denser medium to minimize optical path length.</p>

          <h2>2. Total Internal Reflection & The Critical Angle</h2>
          <p>When light attempts to cross from an optically denser medium into a rarer medium (\(n_1 > n_2\), such as light exiting crown glass or water into air), Snell's law reveals that the angle of refraction \(\theta_2\) is always greater than the angle of incidence \(\theta_1\) (\(\theta_2 > \theta_1\)).</p>
          <p>As the angle of incidence increases, \(\theta_2\) eventually reaches \(90^\circ\), meaning the refracted ray grazes along the boundary surface. Setting \(\theta_2 = 90^\circ\) (\(\sin 90^\circ = 1\)) defines the <strong>critical angle</strong> (\(\theta_c\)):</p>
          <div class="math-block">
            $$n_1 \sin\theta_c = n_2 \sin(90^\circ) \implies \theta_c = \arcsin\left(\frac{n_2}{n_1}\right)$$
          </div>
          <p>If the incident angle exceeds the critical angle (\(\theta_1 > \theta_c\)), Snell's equation mathematically requires \(\sin\theta_2 > 1\), which has no real trigonometric solution. Physically, refraction ceases entirely: \(100\%\) of the incident electromagnetic power reflects back into the first medium without any transmission loss—a phenomenon known as <strong>Total Internal Reflection (TIR)</strong>.</p>

          <h2>3. Optical Benchmark Refractive Index Reference Table</h2>
          <p>To assist optical lens designers, laser engineers, and gemologists, the table below documents representative refractive indices (\(n\)) measured at the standard yellow sodium D-line wavelength (\(\lambda = 589.3\text{ nm}\)) and corresponding critical angles into air (\(n_2 = 1.0003\)):</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Optical Material / Dielectric Medium</th>
                <th>Refractive Index (\(n\))</th>
                <th>Speed of Light in Medium (\(v\))</th>
                <th>Critical Angle into Air (\(\theta_c\))</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Vacuum (Physical Reference Standard)</td>
                <td>1.000000</td>
                <td>299,792 km/s (1.000 c)</td>
                <td>N/A</td>
              </tr>
              <tr>
                <td>Air (Dry, Standard Sea Level, 15°C)</td>
                <td>1.000293</td>
                <td>299,705 km/s (0.9997 c)</td>
                <td>N/A</td>
              </tr>
              <tr>
                <td>Water (Pure Distilled, 20°C)</td>
                <td>1.3330</td>
                <td>224,895 km/s (0.7502 c)</td>
                <td>48.61°</td>
              </tr>
              <tr>
                <td>Fused Silica Glass (SiO₂)</td>
                <td>1.4585</td>
                <td>205,548 km/s (0.6856 c)</td>
                <td>43.30°</td>
              </tr>
              <tr>
                <td>Crown Glass (Schott N-BK7 Standard)</td>
                <td>1.5168</td>
                <td>197,648 km/s (0.6593 c)</td>
                <td>41.26°</td>
              </tr>
              <tr>
                <td>Dense Flint Glass (Schott SF11 High-Index)</td>
                <td>1.7847</td>
                <td>167,979 km/s (0.5603 c)</td>
                <td>34.10°</td>
              </tr>
              <tr>
                <td>Sapphire Crystal (Al₂O₃)</td>
                <td>1.7682</td>
                <td>169,547 km/s (0.5656 c)</td>
                <td>34.46°</td>
              </tr>
              <tr>
                <td>Natural Diamond (Carbon Crystalline)</td>
                <td>2.4173</td>
                <td>124,020 km/s (0.4137 c)</td>
                <td>24.44° (Extreme fire & brilliance)</td>
              </tr>
            </tbody>
          </table>

          <h2>4. Worked Engineering Case Study: Fiber Optic Core Acceptance Cone</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>An optical telecommunications engineer is designing a step-index silica optical fiber for long-haul internet data transmission. The fiber features a germanium-doped silica core with refractive index \(n_{\text{core}} = 1.480\) surrounded by a pure silica cladding with refractive index \(n_{\text{clad}} = 1.460\). The fiber end-face is terminated in ambient air (\(n_0 = 1.0003\)).</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Compute the critical angle \(\theta_c\) required for total internal reflection along the core-cladding boundary.</li>
              <li>Determine the <strong>Numerical Aperture (NA)</strong> of the fiber.</li>
              <li>Calculate the maximum external acceptance half-angle \(\theta_{\text{max}}\) in air within which launched light rays will successfully guide through the cable.</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Calculate core-cladding critical angle \(\theta_c\):</strong></p>
            <div class="math-block">
              $$\theta_c = \arcsin\left(\frac{n_{\text{clad}}}{n_{\text{core}}}\right) = \arcsin\left(\frac{1.460}{1.480}\right) = \arcsin(0.986486) \approx 80.57^\circ$$
            </div>
            <p>For total internal reflection to occur, rays inside the core must strike the cladding at a grazing angle \(\ge 80.57^\circ\) relative to the cladding normal.</p>

            <p><strong>Step 2: Calculate the fiber Numerical Aperture (NA):</strong></p>
            <p>Numerical aperture quantifies the light-gathering capability of an optical fiber:</p>
            <div class="math-block">
              $$\text{NA} = \sqrt{n_{\text{core}}^2 - n_{\text{clad}}^2} = \sqrt{(1.480)^2 - (1.460)^2} = \sqrt{2.1904 - 2.1316} = \sqrt{0.0588} \approx 0.2425$$
            </div>

            <p><strong>Step 3: Calculate the maximum external acceptance angle \(\theta_{\text{max}}\) in air:</strong></p>
            <p>Applying Snell's law at the front air-core interface (\(n_0 \sin\theta_{\text{max}} = \text{NA}\)):</p>
            <div class="math-block">
              $$\sin\theta_{\text{max}} = \frac{\text{NA}}{n_0} = \frac{0.2425}{1.0003} \approx 0.2424$$
            </div>
            <div class="math-block">
              $$\theta_{\text{max}} = \arcsin(0.2424) \approx 14.03^\circ$$
            </div>
            <p><strong>Engineering Design Verdict:</strong> The fiber possesses an acceptance cone with a full apex angle of \(2\theta_{\text{max}} = 28.06^\circ\). Laser launch optics must focus the input beam within this cone to guarantee 100% total internal reflection guidance without leakage into the cladding.</p>
          </div>

          <h2>5. Polarization by Reflection & Brewster's Angle</h2>
          <p>When unpolarized light strikes a transparent dielectric surface, the reflected and refracted rays exhibit polarization dictated by the Fresnel reflection coefficients. Scottish physicist Sir David Brewster discovered in 1815 that when the angle between the reflected ray and refracted ray is exactly \(90^\circ\) (\(\theta_1 + \theta_2 = 90^\circ\)), the reflected beam is \(100\%\) linearly s-polarized perpendicular to the plane of incidence.</p>
          <p>Applying Snell's law at this condition yields <strong>Brewster's Angle</strong> (\(\theta_B\)):</p>
          <div class="math-block">
            $$n_1 \sin\theta_B = n_2 \sin(90^\circ - \theta_B) = n_2 \cos\theta_B \implies \tan\theta_B = \frac{n_2}{n_1} \implies \theta_B = \arctan\left(\frac{n_2}{n_1}\right)$$
          </div>
          <p>For an air-to-glass interface (\(n_1 = 1.0, n_2 = 1.52\)), Brewster's angle is \(\arctan(1.52) \approx 56.7^\circ\). Polarized sunglasses exploit this principle: because glare reflected from horizontal surfaces (water, wet roadways, car windshields) is predominantly horizontally polarized, vertically oriented polarizing filters extinguish the glare completely.</p>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>Why do diamonds sparkle with such intense brilliance compared to glass?</h3>
            <p>Diamond has an exceptionally high refractive index (\(n = 2.417\)), resulting in an unusually small critical angle of just \(\theta_c = 24.4^\circ\) (compared to \(41.3^\circ\) for crown glass). Lapidary master jewelers cut diamond facets so that virtually all light entering the top table undergoes multiple total internal reflections before exiting back through the crown, maximizing fire and brilliance.</p>
          </div>
          <div class="faq-item">
            <h3>What causes a mirage on hot asphalt roads during summer?</h3>
            <p>Sunlight intensely heats the dark pavement, creating a thin layer of hot, low-density air immediately above the road. Because hotter air has a lower refractive index than cooler upper air, downward-slanting light rays bend upward via continuous refraction away from the normal until undergoing total internal reflection, projecting a displaced image of the blue sky that drivers perceive as a puddle of water.</p>
          </div>
          <div class="faq-item">
            <h3>How does dispersion split white light into a rainbow in a prism?</h3>
            <p>The refractive index of transparent media is not constant across all wavelengths: due to atomic resonance, optical glasses exhibit chromatic dispersion, where shorter blue wavelengths experience a higher refractive index than longer red wavelengths (\(n_{\text{blue}} > n_{\text{red}}\)). Consequently, blue light refracts through a sharper angle than red light, fanning white light out into its constituent spectral colors.</p>
          </div>
          <div class="faq-item">
            <h3>Can Snell's Law be applied to acoustic sound waves and seismic waves?</h3>
            <p>Yes. Snell's law is a universal wave equation applicable to any wave propagating across velocity discontinuities, including seismic P-waves and S-waves traveling through Earth's crustal layers and ultrasound waves passing between soft human tissue and bone in medical imaging.</p>
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
    // Snell's Law Calculation Engine
    const c_light = 299792.458; // km/s

    const medPresets = {
      air: 1.0003,
      water: 1.3330,
      crownglass: 1.5200,
      flintglass: 1.6600,
      diamond: 2.4170,
      fiber_core: 1.4800,
      fiber_clad: 1.4600
    };

    function applyPresets() {
      const p1 = document.getElementById('med1Preset').value;
      if (p1 !== 'custom' && medPresets[p1]) {
        document.getElementById('n1Val').value = medPresets[p1];
      }
      const p2 = document.getElementById('med2Preset').value;
      if (p2 !== 'custom' && medPresets[p2]) {
        document.getElementById('n2Val').value = medPresets[p2];
      }
      calculate();
    }

    function calculate() {
      const n1 = parseFloat(document.getElementById('n1Val').value) || 1.0;
      const n2 = parseFloat(document.getElementById('n2Val').value) || 1.0;
      const theta1_deg = parseFloat(document.getElementById('angle1Val').value) || 0;

      const theta1_rad = theta1_deg * (Math.PI / 180);

      // Phase velocities
      const v1 = c_light / n1;
      const v2 = c_light / n2;

      // Brewster's angle tan(theta_B) = n2 / n1
      const brewster_rad = Math.atan(n2 / n1);
      const brewster_deg = brewster_rad * (180 / Math.PI);

      // Critical angle theta_c = asin(n2 / n1) if n1 > n2
      let crit_deg = null;
      let isTIR = false;
      if (n1 > n2) {
        const crit_rad = Math.asin(n2 / n1);
        crit_deg = crit_rad * (180 / Math.PI);
        if (theta1_deg >= crit_deg) {
          isTIR = true;
        }
      }

      // Snell's law: sin(theta2) = (n1 / n2) * sin(theta1)
      const sinTheta2 = (n1 / n2) * Math.sin(theta1_rad);

      // Render Primary Box
      if (isTIR || sinTheta2 > 1.0) {
        document.getElementById('resPrimaryLabel').textContent = "Total Internal Reflection (TIR)";
        document.getElementById('resPrimaryVal').textContent = "100% Reflection (No Refraction)";
        document.getElementById('resPrimarySub').textContent = 
          "Incident angle " + theta1_deg.toFixed(1) + "° exceeds critical angle " + (crit_deg ? crit_deg.toFixed(2) + "°" : "");
      } else {
        const theta2_rad = Math.asin(sinTheta2);
        const theta2_deg = theta2_rad * (180 / Math.PI);

        document.getElementById('resPrimaryLabel').textContent = "Angle of Refraction (θ₂)";
        document.getElementById('resPrimaryVal').textContent = theta2_deg.toFixed(2) + "°";

        let bendText = "";
        if (theta2_deg < theta1_deg) {
          bendText = "Light bends toward normal (slower denser medium)";
        } else if (theta2_deg > theta1_deg) {
          bendText = "Light bends away from normal (faster rarer medium)";
        } else {
          bendText = "Straight propagation (Identical media or normal incidence)";
        }
        document.getElementById('resPrimarySub').textContent = bendText;
      }

      // Render Grid Items
      if (crit_deg !== null) {
        document.getElementById('resCritAngle').textContent = 
          crit_deg.toFixed(2) + "° (TIR threshold)";
      } else {
        document.getElementById('resCritAngle').textContent = "None (n₁ ≤ n₂)";
      }

      document.getElementById('resBrewster').textContent = brewster_deg.toFixed(2) + "°";
      document.getElementById('resV1').textContent = 
        v1.toLocaleString('en-US', {maximumFractionDigits: 0}) + " km/s (" + (v1 / c_light).toFixed(4) + " c)";
      document.getElementById('resV2').textContent = 
        v2.toLocaleString('en-US', {maximumFractionDigits: 0}) + " km/s (" + (v2 / c_light).toFixed(4) + " c)";
    }

    document.getElementById('med1Preset').addEventListener('change', applyPresets);
    document.getElementById('med2Preset').addEventListener('change', applyPresets);
    document.querySelectorAll('input, select').forEach(el => {
      if (el.id !== 'med1Preset' && el.id !== 'med2Preset') {
        el.addEventListener('input', () => {
          if (el.id === 'n1Val') document.getElementById('med1Preset').value = 'custom';
          if (el.id === 'n2Val') document.getElementById('med2Preset').value = 'custom';
          calculate();
        });
        el.addEventListener('change', () => {
          if (el.id === 'n1Val') document.getElementById('med1Preset').value = 'custom';
          if (el.id === 'n2Val') document.getElementById('med2Preset').value = 'custom';
          calculate();
        });
      }
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('med1Preset').value = 'air';
      document.getElementById('med2Preset').value = 'crownglass';
      document.getElementById('angle1Val').value = '30';
      applyPresets();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
"""

TOOL_2_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Specific Heat Calculator | Heat Transfer Q = mcΔT & Calorimetry</title>
  <meta name="description" content="Calculate heat energy transferred (Q), specific heat capacity (c), mass, temperature change, and thermal equilibrium mixing using Q = mcΔT.">
  <link rel="canonical" href="https://calchub.cloud/specific-heat-calculator.html">
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
        "name": "Specific Heat Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates thermodynamic sensible heat transfer Q = mcΔT, specific heat capacity, heating electrical runtime, and calorimeter thermal equilibrium.",
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
            "name": "What is the formula for heat energy transfer?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The primary thermodynamic sensible heat equation is Q = m × c × ΔT, where 'Q' is thermal heat energy transferred in Joules, 'm' is mass in kilograms, 'c' is specific heat capacity in J/(kg·K) or J/(kg·°C), and 'ΔT' is temperature change (T_final - T_initial) in Kelvin or degrees Celsius."
            }
          },
          {
            "@type": "Question",
            "name": "What is the specific heat capacity of liquid water?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Pure liquid water possesses an exceptionally high specific heat capacity of approximately 4,184 J/(kg·°C) or 1.000 cal/(g·°C). This allows water to absorb or release immense quantities of thermal energy with minimal temperature shifts, making it the universal fluid for hydronic HVAC heating and engine cooling."
            }
          },
          {
            "@type": "Question",
            "name": "How is thermal equilibrium temperature calculated when two substances mix?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Assuming an insulated calorimeter where heat loss to the surroundings is zero (Q_lost + Q_gained = 0), the equilibrium temperature is: T_eq = (m₁·c₁·T₁ + m₂·c₂·T₂) / (m₁·c₁ + m₂·c₂)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between heat capacity and specific heat capacity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Specific heat capacity (c) is an intensive physical property representing heat required per unit mass (J/(kg·K)). Heat capacity (C = m × c) is an extensive property representing total heat required to raise the temperature of the entire object by 1 degree (J/K)."
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
        <h1>Specific Heat Calculator</h1>
        <p class="lead-text">Calculate thermodynamic heat transfer (Q = mcΔT), specific heat capacity, temperature change, and thermal equilibrium mixing temperatures.</p>

        <div class="calc-card">
          <div class="form-row">
            <div class="form-group col-half">
              <label for="solveTarget">Calculation Target</label>
              <select id="solveTarget" class="form-control">
                <option value="solve_q" selected>Solve for Heat Energy (Q) [Given m, c, ΔT]</option>
                <option value="solve_c">Solve for Specific Heat (c) [Given Q, m, ΔT]</option>
                <option value="solve_m">Solve for Required Mass (m) [Given Q, c, ΔT]</option>
                <option value="solve_dt">Solve for Temperature Change (ΔT) [Given Q, m, c]</option>
              </select>
            </div>

            <div class="form-group col-half">
              <label for="matPreset">Material Specific Heat Preset</label>
              <select id="matPreset" class="form-control">
                <option value="water" selected>Liquid Water (c = 4,184 J/kg·K)</option>
                <option value="ice">Ice (-10°C, c = 2,090 J/kg·K)</option>
                <option value="steam">Steam (100°C, c = 2,010 J/kg·K)</option>
                <option value="aluminum">Aluminum (c = 900 J/kg·K)</option>
                <option value="iron">Iron / Structural Steel (c = 450 J/kg·K)</option>
                <option value="copper">Pure Copper (c = 385 J/kg·K)</option>
                <option value="concrete">Concrete / Masonry (c = 880 J/kg·K)</option>
                <option value="oil">Engine Oil (c = 1,900 J/kg·K)</option>
                <option value="air">Dry Air (c_p = 1,005 J/kg·K)</option>
                <option value="custom">Custom Specific Heat</option>
              </select>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-third" id="grpMass">
              <label for="valMass">Substance Mass (m)</label>
              <div class="input-with-unit">
                <input type="number" id="valMass" class="form-control" value="50" step="any" min="0.001">
                <select id="unitMass" class="unit-select">
                  <option value="kg" selected>kg</option>
                  <option value="g">grams (g)</option>
                  <option value="lbs">lbs</option>
                  <option value="ton">Metric Tons</option>
                </select>
              </div>
            </div>

            <div class="form-group col-third" id="grpC">
              <label for="valC">Specific Heat Capacity (c)</label>
              <div class="input-with-unit">
                <input type="number" id="valC" class="form-control" value="4184" step="any" min="1">
                <span style="font-size:12px; padding:6px 8px; background:#fff; border:1px solid #cbd5e1; border-left:none; border-radius:0 4px 4px 0; display:flex; align-items:center;">J/kg·K</span>
              </div>
            </div>

            <div class="form-group col-third" id="grpDT">
              <label for="valDT">Temperature Change (&Delta;T)</label>
              <div class="input-with-unit">
                <input type="number" id="valDT" class="form-control" value="40" step="any">
                <select id="unitDT" class="unit-select">
                  <option value="c" selected>&Delta;&deg;C / K</option>
                  <option value="f">&Delta;&deg;F</option>
                </select>
              </div>
            </div>

            <div class="form-group col-third" id="grpQ" style="display:none;">
              <label for="valQ">Thermal Heat Energy (Q)</label>
              <div class="input-with-unit">
                <input type="number" id="valQ" class="form-control" value="8368" step="any">
                <select id="unitQ" class="unit-select">
                  <option value="kj" selected>kJ</option>
                  <option value="j">Joules (J)</option>
                  <option value="kwh">kWh</option>
                  <option value="btu">BTU</option>
                </select>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Thermal Energy</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset to 50 kg Water (40°C Rise)</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label" id="resPrimaryLabel">Heat Energy Transferred (Q)</div>
              <div class="result-value" id="resPrimaryVal">8,368.0 kJ</div>
              <div class="result-sub" id="resPrimarySub">8.368 Megajoules • 2.324 kWh • 7,931 BTU</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Heat Capacity (C = m·c)</span>
                <span class="sub-value" id="resHeatCap">209.2 kJ/K</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Nutritional Food Calories</span>
                <span class="sub-value" id="resKcal">2,000 kcal (Cal)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Electrical Heating Time (at 3 kW)</span>
                <span class="sub-value" id="resTime3kW">46.5 minutes</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Equivalent Temperature Rise</span>
                <span class="sub-value" id="resTempRise">40.0°C (72.0°F)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Thermodynamic Foundations of Sensible Heat Transfer</h2>
          <p>In classical thermodynamics, thermal energy transfer occurring across a temperature gradient without inducing a physical phase change is designated as <strong>sensible heat</strong>. When heat energy \(Q\) is transferred into a substance, it increases the microscopic kinetic energy of its constituent atoms and molecules—accelerating translational motion, molecular rotational spinning, and interatomic vibrational oscillations.</p>
          <p>The mathematical relationship governing sensible heat transfer is defined by the fundamental calorimetric formula:</p>
          <div class="math-block">
            $$Q = m \cdot c \cdot \Delta T = m \cdot c \cdot (T_{\text{final}} - T_{\text{initial}})$$
          </div>
          <p>Where:</p>
          <ul>
            <li>\(Q\) = Sensible heat thermal energy transferred in Joules (\(\text{J}\))</li>
            <li>\(m\) = Mass of the substance in kilograms (\(\text{kg}\))</li>
            <li>\(c\) = <strong>Specific heat capacity</strong> of the material in Joules per kilogram-Kelvin (\(\text{J}/(\text{kg}\cdot\text{K})\) or \(\text{J}/(\text{kg}\cdot^\circ\text{C})\))</li>
            <li>\(\Delta T\) = Temperature difference (\(T_f - T_i\)) in Kelvin or degrees Celsius</li>
          </ul>
          <p>The <strong>specific heat capacity</strong> \(c\) is an intensive physical property measuring the quantity of thermal energy required to elevate the temperature of one kilogram of a given substance by exactly one Kelvin (or one degree Celsius). By contrast, total <strong>heat capacity</strong> (\(C = m \cdot c\)) is an extensive property measuring the heat required to raise the entire physical body by one degree.</p>

          <h2>2. Benchmark Specific Heat Capacity Reference Table</h2>
          <p>To assist HVAC mechanical engineers, metallurgical process designers, and physics students, the reference table below outlines standard specific heat capacities across common solids, liquids, and gases measured at standard atmospheric pressure (\(1\text{ atm}\), \(25^\circ\text{C}\)):</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Substance / Material</th>
                <th>Specific Heat \(c\) (\(\text{J/kg}\cdot\text{K}\))</th>
                <th>Specific Heat (\(\text{cal/g}\cdot^\circ\text{C}\))</th>
                <th>Engineering Thermal Role</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Liquid Water (\(\text{H}_2\text{O}\), 20°C)</td>
                <td>4,184</td>
                <td>1.000</td>
                <td>Hydronic heating, cooling towers, global climate thermal sink</td>
              </tr>
              <tr>
                <td>Solid Ice (\(-10^\circ\text{C}\))</td>
                <td>2,090</td>
                <td>0.499</td>
                <td>Cryogenic food storage and thermal ice-bank HVAC storage</td>
              </tr>
              <tr>
                <td>Water Vapor / Steam (100°C)</td>
                <td>2,010</td>
                <td>0.480</td>
                <td>Steam turbine rankine cycles and industrial heating</td>
              </tr>
              <tr>
                <td>Engine Oil (Synthetic SAE 5W-30)</td>
                <td>1,900 – 2,100</td>
                <td>0.454 – 0.502</td>
                <td>Internal combustion engine piston and cylinder cooling</td>
              </tr>
              <tr>
                <td>Dry Air (Isobaric \(c_p\), Sea Level)</td>
                <td>1,005</td>
                <td>0.240</td>
                <td>HVAC psychrometric ductwork sensible heating/cooling</td>
              </tr>
              <tr>
                <td>Aluminum Alloy (6061-T6)</td>
                <td>897</td>
                <td>0.214</td>
                <td>Electronics heatsinks and automotive engine blocks</td>
              </tr>
              <tr>
                <td>Dense Concrete / Solid Masonry</td>
                <td>880</td>
                <td>0.210</td>
                <td>Passive solar thermal building mass and floor radiant heating</td>
              </tr>
              <tr>
                <td>Carbon Steel / Cast Iron</td>
                <td>450 – 490</td>
                <td>0.108 – 0.117</td>
                <td>Industrial pressure vessels, boilers, and brake rotors</td>
              </tr>
              <tr>
                <td>Pure Copper (ETP UNS C11000)</td>
                <td>385</td>
                <td>0.092</td>
                <td>High-efficiency shell-and-tube heat exchanger tubing</td>
              </tr>
              <tr>
                <td>Pure Lead (\(\text{Pb}\))</td>
                <td>129</td>
                <td>0.031</td>
                <td>Radiation shielding (rapid heating due to low thermal capacity)</td>
              </tr>
            </tbody>
          </table>

          <h2>3. Calorimetry & Thermal Equilibrium Mixtures</h2>
          <p>According to the <strong>First Law of Thermodynamics</strong> (conservation of energy), in an isolated calorimeter where thermal exchange with the surrounding environment is negligible, the total heat lost by warm bodies must identically equal the total heat gained by cold bodies:</p>
          <div class="math-block">
            $$\Sigma Q = Q_{\text{lost}} + Q_{\text{gained}} = 0$$
          </div>
          <p>When mixing two substances of masses \(m_1\) and \(m_2\), specific heat capacities \(c_1\) and \(c_2\), and initial temperatures \(T_1\) and \(T_2\), setting \(m_1 c_1 (T_{\text{final}} - T_1) + m_2 c_2 (T_{\text{final}} - T_2) = 0\) allows direct algebraic isolation of the final <strong>thermal equilibrium temperature</strong> (\(T_{\text{final}}\)):</p>
          <div class="math-block">
            $$T_{\text{final}} = \frac{m_1 c_1 T_1 + m_2 c_2 T_2}{m_1 c_1 + m_2 c_2}$$
          </div>

          <h2>4. Worked Engineering Case Study: Commercial Water Heater Sizing</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>A commercial hotel requires an electric storage water heater to supply a 300-liter storage tank (\(m = 300\text{ kg}\)). Cold municipal water enters the facility at an initial temperature of \(T_i = 15^\circ\text{C}\). The domestic hot water standard mandates raising the tank to \(T_f = 60^\circ\text{C}\) (a temperature rise of \(\Delta T = 45^\circ\text{C}\)) to prevent <em>Legionella pneumophila</em> bacterial colonization. The heating tank is powered by an electric immersion heater rated at \(P = 9.0\text{ kW}\) (\(9,000\text{ J/s}\)). Specific heat of water is \(c = 4,184\text{ J/kg}\cdot\text{K}\).</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Compute the total sensible heat energy \(Q\) in Joules, megajoules, and kilowatt-hours (kWh).</li>
              <li>Calculate the theoretical recovery time \(t\) required to heat the cold tank to \(60^\circ\text{C}\) assuming zero standby jacket loss.</li>
              <li>Determine the monthly electrical energy cost assuming one full tank recovery per day at an industrial electricity tariff of \(\$0.14\text{ per kWh}\).</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Calculate sensible heat energy \(Q\):</strong></p>
            <div class="math-block">
              $$Q = m \cdot c \cdot \Delta T = 300\text{ kg} \times 4,184\text{ J/kg}\cdot\text{K} \times 45\text{ K}$$
            </div>
            <div class="math-block">
              $$Q = 1,255,200 \times 45 = 56,484,000\text{ Joules (56.484 MJ)}$$
            </div>

            <p><strong>Step 2: Convert heat energy to kilowatt-hours (kWh):</strong></p>
            <p>Because \(1\text{ kWh} = 3,600,000\text{ Joules}\):</p>
            <div class="math-block">
              $$E_{\text{elec}} = \frac{56,484,000\text{ J}}{3,600,000\text{ J/kWh}} \approx 15.69\text{ kWh}$$
            </div>

            <p><strong>Step 3: Calculate heating recovery time \(t\):</strong></p>
            <div class="math-block">
              $$t = \frac{Q}{P} = \frac{56,484,000\text{ J}}{9,000\text{ W}} = 6,276\text{ seconds}$$
            </div>
            <p>Converting to minutes and hours: \(6,276 \div 60 = 104.6\text{ minutes (1 hour 44.6 minutes)}\).</p>

            <p><strong>Step 4: Calculate monthly electricity operational cost:</strong></p>
            <div class="math-block">
              $$\text{Daily Cost} = 15.69\text{ kWh} \times \$0.14/\text{kWh} \approx \$2.20\text{ per day}$$
            </div>
            <div class="math-block">
              $$\text{Monthly Cost} = \$2.1966 \times 30\text{ days} \approx \$65.90\text{ per month}$$
            </div>
            <p><strong>Engineering Conclusion:</strong> The 9 kW immersion element recovers the 300-liter water heater in under 1.75 hours, meeting commercial hospitality hot water peak demand requirements.</p>
          </div>

          <h2>5. The Anomalous High Specific Heat of Water & Global Climate</h2>
          <p>Liquid water possesses one of the highest specific heat capacities of any known substance on Earth (\(4,184\text{ J/kg}\cdot\text{K}\)), more than four times greater than aluminum and over nine times greater than iron. This extreme value arises from strong intermolecular <strong>hydrogen bonding</strong>: extensive hydrogen bond networks absorb substantial thermal energy into vibrational bending modes before exhibiting increases in molecular kinetic velocity.</p>
          <p>This thermodynamic anomaly is vital for terrestrial life. Earth's oceans act as vast planetary thermal buffers, absorbing enormous solar heat loads during summer and slowly releasing thermal energy during winter. Consequently, coastal maritime climates experience mild temperature swings, in stark contrast to continental deserts where low-specific-heat sand and dry air produce extreme diurnal temperature swings exceeding \(35^\circ\text{C}\) between day and night.</p>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>How do specific heat units of J/(kg·K) relate to cal/(g·°C) and BTU/(lb·°F)?</h3>
            <p>By international definition, \(1\text{ cal/(g}\cdot^\circ\text{C}) = 1\text{ BTU/(lb}\cdot^\circ\text{F}) = 4,184\text{ J/(kg}\cdot\text{K})\). Water has a specific heat of exactly \(1.0\text{ cal/(g}\cdot^\circ\text{C})\) and \(1.0\text{ BTU/(lb}\cdot^\circ\text{F})\), serving as the foundational calibration reference for both metric and Imperial thermal systems.</p>
          </div>
          <div class="faq-item">
            <h3>Does specific heat capacity vary with temperature?</h3>
            <p>Yes. For solids, specific heat drops toward zero as temperatures approach absolute zero (\(0\text{ K}\)) following the Debye \(T^3\) law. In engineering ranges (\(0^\circ\text{C}\text{ to }100^\circ\text{C}\)), specific heat for most structural solids and liquids is treated as constant with less than \(1\%\) error.</p>
          </div>
          <div class="faq-item">
            <h3>Why do metals heat up and cool down much faster than water?</h3>
            <p>Metals like copper (\(385\text{ J/kg}\cdot\text{K}\)) and iron (\(450\text{ J/kg}\cdot\text{K}\)) require less than one-tenth the thermal energy per kilogram compared to water to undergo the same temperature increase. Combined with their high thermal conductivities, metals respond rapidly to heating and cooling cycles.</p>
          </div>
          <div class="faq-item">
            <h3>What is the difference between Cp (constant pressure) and Cv (constant volume)?</h3>
            <p>For incompressible solids and liquids, \(c_p \approx c_v\). For gases, heating at constant pressure requires additional energy to perform boundary expansion work against the atmosphere (\(P\Delta V = nR\Delta T\)). Consequently, for ideal gases, \(c_p = c_v + R_{\text{specific}}\), giving \(c_p > c_v\).</p>
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
    // Specific Heat Calculation Engine
    const presets = {
      water: 4184,
      ice: 2090,
      steam: 2010,
      aluminum: 900,
      iron: 450,
      copper: 385,
      concrete: 880,
      oil: 1900,
      air: 1005
    };

    const toKg = (m, unit) => {
      switch(unit) {
        case 'g': return m / 1000;
        case 'lbs': return m * 0.45359237;
        case 'ton': return m * 1000;
        default: return m;
      }
    };
    const toDeltaK = (dt, unit) => {
      return unit === 'f' ? dt * (5 / 9) : dt;
    };
    const toJoules = (q, unit) => {
      switch(unit) {
        case 'kj': return q * 1000;
        case 'kwh': return q * 3600000;
        case 'btu': return q * 1055.05585;
        default: return q;
      }
    };

    function updateTarget() {
      const mode = document.getElementById('solveTarget').value;
      document.getElementById('grpMass').style.display = mode === 'solve_m' ? 'none' : 'block';
      document.getElementById('grpC').style.display = mode === 'solve_c' ? 'none' : 'block';
      document.getElementById('grpDT').style.display = mode === 'solve_dt' ? 'none' : 'block';
      document.getElementById('grpQ').style.display = mode === 'solve_q' ? 'none' : 'block';
      calculate();
    }

    function applyPreset() {
      const p = document.getElementById('matPreset').value;
      if (p !== 'custom' && presets[p]) {
        document.getElementById('valC').value = presets[p];
      }
      calculate();
    }

    function calculate() {
      const mode = document.getElementById('solveTarget').value;

      let calc_q = 0, calc_m = 0, calc_c = 0, calc_dt = 0;

      if (mode === 'solve_q') {
        calc_m = toKg(parseFloat(document.getElementById('valMass').value) || 0, document.getElementById('unitMass').value);
        calc_c = parseFloat(document.getElementById('valC').value) || 4184;
        calc_dt = toDeltaK(parseFloat(document.getElementById('valDT').value) || 0, document.getElementById('unitDT').value);
        calc_q = calc_m * calc_c * calc_dt;
      } else if (mode === 'solve_c') {
        calc_q = toJoules(parseFloat(document.getElementById('valQ').value) || 0, document.getElementById('unitQ').value);
        calc_m = toKg(parseFloat(document.getElementById('valMass').value) || 1, document.getElementById('unitMass').value);
        calc_dt = toDeltaK(parseFloat(document.getElementById('valDT').value) || 1, document.getElementById('unitDT').value);
        calc_c = (calc_m * calc_dt > 0) ? calc_q / (calc_m * calc_dt) : 0;
      } else if (mode === 'solve_m') {
        calc_q = toJoules(parseFloat(document.getElementById('valQ').value) || 0, document.getElementById('unitQ').value);
        calc_c = parseFloat(document.getElementById('valC').value) || 4184;
        calc_dt = toDeltaK(parseFloat(document.getElementById('valDT').value) || 1, document.getElementById('unitDT').value);
        calc_m = (calc_c * calc_dt > 0) ? calc_q / (calc_c * calc_dt) : 0;
      } else if (mode === 'solve_dt') {
        calc_q = toJoules(parseFloat(document.getElementById('valQ').value) || 0, document.getElementById('unitQ').value);
        calc_m = toKg(parseFloat(document.getElementById('valMass').value) || 1, document.getElementById('unitMass').value);
        calc_c = parseFloat(document.getElementById('valC').value) || 4184;
        calc_dt = (calc_m * calc_c > 0) ? calc_q / (calc_m * calc_c) : 0;
      }

      // Render Primary Box
      if (mode === 'solve_q') {
        document.getElementById('resPrimaryLabel').textContent = "Heat Energy Transferred (Q)";
        if (calc_q > 1e9) {
          document.getElementById('resPrimaryVal').textContent = (calc_q / 1e9).toFixed(3) + " GJ";
        } else if (calc_q > 1e6) {
          document.getElementById('resPrimaryVal').textContent = (calc_q / 1e6).toFixed(3) + " MJ";
        } else if (calc_q > 1000) {
          document.getElementById('resPrimaryVal').textContent = (calc_q / 1000).toFixed(1) + " kJ";
        } else {
          document.getElementById('resPrimaryVal').textContent = calc_q.toFixed(1) + " Joules";
        }

        const kWh = calc_q / 3600000;
        const btu = calc_q / 1055.056;
        document.getElementById('resPrimarySub').textContent = 
          kWh.toFixed(3) + " kWh • " + btu.toLocaleString('en-US', {maximumFractionDigits: 0}) + " BTU";
      } else if (mode === 'solve_c') {
        document.getElementById('resPrimaryLabel').textContent = "Calculated Specific Heat (c)";
        document.getElementById('resPrimaryVal').textContent = calc_c.toFixed(1) + " J/(kg·K)";
        document.getElementById('resPrimarySub').textContent = (calc_c / 4184).toFixed(4) + " cal/(g·°C)";
      } else if (mode === 'solve_m') {
        document.getElementById('resPrimaryLabel').textContent = "Calculated Mass (m)";
        document.getElementById('resPrimaryVal').textContent = calc_m.toFixed(2) + " kg";
        document.getElementById('resPrimarySub').textContent = (calc_m * 2.20462).toFixed(2) + " lbs";
      } else if (mode === 'solve_dt') {
        document.getElementById('resPrimaryLabel').textContent = "Temperature Change (ΔT)";
        document.getElementById('resPrimaryVal').textContent = calc_dt.toFixed(2) + " °C (K)";
        document.getElementById('resPrimarySub').textContent = (calc_dt * 1.8).toFixed(2) + " °F change";
      }

      // Secondary Grid Items
      const heatCapacity = calc_m * calc_c;
      if (heatCapacity > 1000) {
        document.getElementById('resHeatCap').textContent = (heatCapacity / 1000).toFixed(2) + " kJ/K";
      } else {
        document.getElementById('resHeatCap').textContent = heatCapacity.toFixed(1) + " J/K";
      }

      const kcal = calc_q / 4184;
      document.getElementById('resKcal').textContent = 
        kcal.toLocaleString('en-US', {maximumFractionDigits: 1}) + " kcal (Food Cal)";

      // Time at 3 kW: t = Q / 3000
      const seconds3kW = calc_q / 3000;
      if (seconds3kW > 3600) {
        document.getElementById('resTime3kW').textContent = (seconds3kW / 3600).toFixed(2) + " hours";
      } else {
        document.getElementById('resTime3kW').textContent = (seconds3kW / 60).toFixed(1) + " minutes";
      }

      document.getElementById('resTempRise').textContent = 
        calc_dt.toFixed(1) + "°C (" + (calc_dt * 1.8).toFixed(1) + "°F)";
    }

    document.getElementById('solveTarget').addEventListener('change', updateTarget);
    document.getElementById('matPreset').addEventListener('change', applyPreset);
    document.querySelectorAll('input, select').forEach(el => {
      if (el.id !== 'solveTarget' && el.id !== 'matPreset') {
        el.addEventListener('input', () => {
          if (el.id === 'valC') document.getElementById('matPreset').value = 'custom';
          calculate();
        });
        el.addEventListener('change', () => {
          if (el.id === 'valC') document.getElementById('matPreset').value = 'custom';
          calculate();
        });
      }
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('solveTarget').value = 'solve_q';
      document.getElementById('matPreset').value = 'water';
      document.getElementById('valMass').value = '50';
      document.getElementById('unitMass').value = 'kg';
      document.getElementById('valDT').value = '40';
      document.getElementById('unitDT').value = 'c';
      applyPreset();
      updateTarget();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(base_dir, "snells-law-calculator.html")
    p2 = os.path.join(base_dir, "specific-heat-calculator.html")

    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML)
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML)
    print(f"Generated {p2}")

if __name__ == "__main__":
    main()
