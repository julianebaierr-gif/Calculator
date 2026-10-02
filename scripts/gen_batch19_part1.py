import os

def create_acceleration_converter():
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Acceleration Converter | m/s², g-force, ft/s², Gal & knot/s</title>
  <meta name="description" content="Convert acceleration units between meters per second squared (m/s²), standard g-force (g₀), feet per second squared (ft/s²), Gal, mGal, and automotive 0-60 mph metrics.">
  <link rel="canonical" href="https://calchub.cloud/acceleration-converter.html">
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
        "name": "Acceleration Converter",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Converts acceleration across SI, Imperial, Gravitational, CGS, and specialized automotive and aerospace units with standard ISO 80000-3 physical constants.",
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
            "name": "What is standard gravity (g₀) and how is it defined internationally?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard gravity (symbol g₀ or gn) is an internationally agreed standard nominal acceleration of an object in a vacuum near the surface of the Earth. It was established by the 3rd General Conference on Weights and Measures (CGPM) in 1901 as exactly 9.80665 m/s² (approximately 32.17405 ft/s²)."
            }
          },
          {
            "@type": "Question",
            "name": "What is a Gal and where is this unit used in engineering and geophysics?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The Gal (named after Galileo Galilei) is the CGS (centimeter-gram-second) unit of acceleration, defined as exactly 1 cm/s² or 0.01 m/s². In geophysics and gravimetry, variations in Earth's gravitational field are commonly expressed in milligals (1 mGal = 10⁻³ Gal = 10⁻⁵ m/s²)."
            }
          },
          {
            "@type": "Question",
            "name": "How is acceleration calculated from 0 to 60 mph vehicle times?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Assuming uniform linear acceleration, average acceleration is a = Δv / Δt. Converting 60 mph to metric gives 26.8224 m/s. Therefore, a vehicle reaching 60 mph in 3.0 seconds experiences an average acceleration of a = 26.8224 / 3.0 = 8.9408 m/s² (0.9117 g₀)."
            }
          },
          {
            "@type": "Question",
            "name": "How does Relative Centrifugal Force (RCF) convert into g-force?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Relative Centrifugal Force (RCF) measures centrifugal acceleration in laboratory centrifuges as a multiple of g-force: RCF = (r × ω²) / g₀ = 1.118 × 10⁻⁵ × r × N², where r is rotor radius in centimeters and N is rotational speed in revolutions per minute (RPM)."
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
        <h1>Acceleration Converter</h1>
        <p class="lead-text">Convert acceleration values across SI, imperial, gravitational, and CGS units including meters per second squared (\(\text{m/s}^2\)), standard g-force (\(g_0\)), feet per second squared (\(\text{ft/s}^2\)), and Galileos (\(\text{Gal}\)).</p>

        <div class="calc-card">
          <div class="calc-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="accInput">Acceleration Magnitude</label>
                <input type="number" id="accInput" value="9.80665" step="any" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="unitFrom">Input Unit</label>
                <select id="unitFrom" class="form-control">
                  <option value="mps2">Meters per second squared (m/s²)</option>
                  <option value="g" selected>Standard Earth Gravity (g₀)</option>
                  <option value="ftps2">Feet per second squared (ft/s²)</option>
                  <option value="inps2">Inches per second squared (in/s²)</option>
                  <option value="gal">Galileo (Gal = cm/s²)</option>
                  <option value="mgal">Milligal (mGal)</option>
                  <option value="kmhps">Kilometers per hour per sec (km/h/s)</option>
                  <option value="mphps">Miles per hour per sec (mph/s)</option>
                  <option value="knotps">Knots per second (kn/s)</option>
                </select>
              </div>
            </div>

            <div class="btn-group">
              <button type="button" id="calcBtn" class="btn btn-primary">Convert Acceleration</button>
              <button type="button" id="resetBtn" class="btn btn-secondary">Reset to 1 g₀</button>
            </div>
          </div>

          <div class="results-panel" id="resultsPanel">
            <h2>Equivalent Acceleration Values</h2>
            <div class="result-hero">
              <span class="hero-label">Base SI Acceleration</span>
              <span class="hero-value" id="resMps2">9.80665 m/s²</span>
            </div>

            <div class="results-grid">
              <div class="result-item">
                <span class="sub-label">Standard Gravity (g₀)</span>
                <span class="sub-value" id="resG">1.00000 g₀</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Imperial (ft/s²)</span>
                <span class="sub-value" id="resFtps2">32.1740 ft/s²</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Inches per Second²</span>
                <span class="sub-value" id="resInps2">386.089 in/s²</span>
              </div>
              <div class="result-item">
                <span class="sub-label">CGS Gal (cm/s²)</span>
                <span class="sub-value" id="resGal">980.665 Gal</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Geophysical Milligal</span>
                <span class="sub-value" id="resMgal">980,665 mGal</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Automotive (0-60 mph equiv.)</span>
                <span class="sub-value" id="resAuto">2.74 sec (0-60 mph)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Rigorous Engineering Article (1,200+ Words) -->
        <article class="article-body">
          <h2>1. Kinematics and the Fundamental Nature of Acceleration</h2>
          <p>In classical Newtonian mechanics, acceleration describes the instantaneous time rate of change of linear or angular velocity. Defined as the first derivative of velocity with respect to time and the second derivative of positional displacement:</p>
          <div class="math-block">
            $$\vec{a}(t) = \lim_{\Delta t \to 0} \frac{\Delta \vec{v}}{\Delta t} = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}$$
          </div>
          <p>Because velocity is a vector quantity possessing both magnitude (speed) and directional orientation, acceleration occurs whenever a body speeds up, slows down (deceleration or negative acceleration), or alters its trajectory in space (centripetal or radial acceleration). The International System of Units (SI) defines the coherent derived unit of acceleration as the <strong>meter per second squared (\(\text{m/s}^2\))</strong>.</p>
          <p>In structural engineering, aerospace dynamics, automotive homologation, and geophysics, acceleration is routinely expressed in non-SI units. Converting reliably between these engineering standards requires a rigorous understanding of the underlying physical invariants, gravitational anomalies, and coordinate transformation scales.</p>

          <h2>2. International Conversion Standards and Physical Constants</h2>
          <p>Every engineering conversion factor for acceleration is mathematically anchored to the SI base definition \(\text{m/s}^2\). The table below outlines the exact definitions governed by the Bureau International des Poids et Mesures (BIPM) and ISO 80000-3:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Acceleration Unit</th>
                <th>Standard Symbol</th>
                <th>Exact Factor in SI (\(\text{m/s}^2\))</th>
                <th>Engineering Application Domain</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Meter per second²</strong></td>
                <td>\(\text{m/s}^2\)</td>
                <td>\(1.000000\)</td>
                <td>SI Base Coherent Standard, Physics, Robotics</td>
              </tr>
              <tr>
                <td><strong>Standard Earth Gravity</strong></td>
                <td>\(g_0\) (or \(g_n\))</td>
                <td>\(9.806650\)</td>
                <td>Aerospace G-load, Structural Seismic Codes, Human Biometrics</td>
              </tr>
              <tr>
                <td><strong>Foot per second²</strong></td>
                <td>\(\text{ft/s}^2\)</td>
                <td>\(0.304800\)</td>
                <td>US Customary & Imperial Civil/Aeronautical Engineering</td>
              </tr>
              <tr>
                <td><strong>Inch per second²</strong></td>
                <td>\(\text{in/s}^2\)</td>
                <td>\(0.025400\)</td>
                <td>Precision Machinery, Machine Tool Spindles, Vibration Metrology</td>
              </tr>
              <tr>
                <td><strong>Galileo (Gal)</strong></td>
                <td>\(\text{Gal}\)</td>
                <td>\(0.010000\)</td>
                <td>CGS Geophysics, Geodetic Gravimetry, Seismology</td>
              </tr>
              <tr>
                <td><strong>Milligal</strong></td>
                <td>\(\text{mGal}\)</td>
                <td>\(0.000010\)</td>
                <td>Subsurface Mineral/Oil Borehole Anomaly Mapping</td>
              </tr>
              <tr>
                <td><strong>Kilometer per hour per sec</strong></td>
                <td>\(\text{km/(h}\cdot\text{s)}\)</td>
                <td>\(\frac{1}{3.6} \approx 0.277778\)</td>
                <td>Railway Braking, Transit Fleet Dynamics</td>
              </tr>
              <tr>
                <td><strong>Mile per hour per sec</strong></td>
                <td>\(\text{mph/s}\)</td>
                <td>\(0.447040\)</td>
                <td>Automotive Performance & Highway Ramp Acceleration</td>
              </tr>
              <tr>
                <td><strong>Knot per second</strong></td>
                <td>\(\text{kn/s}\)</td>
                <td>\(\frac{1852}{3600} \approx 0.514444\)</td>
                <td>Maritime Navigation, Naval Hydrodynamics</td>
              </tr>
            </tbody>
          </table>

          <h2>3. Gravitational Acceleration (\(g_0\)) vs. Local Gravity</h2>
          <p>A common engineering misconception is treating the standard gravity constant \(g_0 = 9.80665\text{ m/s}^2\) as the actual local acceleration measured anywhere on Earth's surface. In reality, \(g_0\) is an internationally stipulated contractual constant established in 1901 by the 3rd CGPM. Real-world local gravitational acceleration \(g(\phi, h)\) varies depending on geographic latitude \(\phi\) and ellipsoidal elevation above mean sea level \(h\), governed by the World Geodetic System (WGS 84) Somigliana equation:</p>
          <div class="math-block">
            $$g(\phi) = g_e \frac{1 + k \sin^2\phi}{\sqrt{1 - e^2 \sin^2\phi}}$$
          </div>
          <p>Where:</p>
          <ul>
            <li>\(g_e = 9.780327\text{ m/s}^2\) is the equatorial surface gravitational acceleration.</li>
            <li>\(k = 0.00193185\) is the normal gravity formula constant.</li>
            <li>\(e^2 = 0.00669438\) is the first square eccentricity of the reference geoid.</li>
          </ul>
          <p>Because the Earth is an oblate spheroid flattened at the poles and bulged at the equator, combined with the outward centrifugal relief of planetary diurnal rotation, local gravitational acceleration spans from approximately \(9.7803\text{ m/s}^2\) at the equator to \(9.8322\text{ m/s}^2\) at the poles. The standard nominal value \(9.80665\text{ m/s}^2\) represents an idealized mid-latitude reference near \(45^\circ\) latitude.</p>

          <h2>4. Biomedical and Aerospace G-Tolerance Limits</h2>
          <p>In aerospace flight physiology, acceleration is universally measured in g-multiples. Human physiological response depends profoundly on the directional axis relative to the human spinal column:</p>
          <ul>
            <li><strong>Positive Vertical Acceleration (\(+G_z\)):</strong> Blood pools into the lower abdomen and extremities, starving the cerebral cortex and retina of oxygen. An untrained human typically experiences gray-out at \(3.5\text{ to }4.0\text{ g}\), black-out at \(4.5\text{ to }5.0\text{ g}\), and G-induced Loss of Consciousness (G-LOC) beyond \(5.5\text{ g}\) sustained for several seconds. Fighter pilots wearing anti-G suits and performing the Anti-G Straining Maneuver (AGSM) can sustain \(9.0\text{ g}\) (\(\approx 88.26\text{ m/s}^2\)).</li>
            <li><strong>Negative Vertical Acceleration (\(-G_z\)):</strong> Forces blood toward the head, inducing retinal vascular engorgement ("red-out") and severe cerebral vascular risk at merely \(-2.0\text{ to }-3.0\text{ g}\).</li>
            <li><strong>Transverse Acceleration (\(+G_x\)):</strong> Chest-to-back ("eyeballs in") orientation utilized in crewed orbital space launches (e.g., Saturn V, Falcon 9, Soyuz). Human tolerance exceeds \(15\text{ g}\) for short durations because hydrostatic blood column displacement between heart and brain is minimized.</li>
          </ul>

          <div class="worked-example-card">
            <h3>Worked Engineering Example: High-Speed Electric Vehicle Launch</h3>
            <p><strong>Scenario:</strong> A modern tri-motor electric vehicle accelerates from \(0\text{ to }60\text{ mph}\) in exactly \(1.98\text{ seconds}\) on a prepped drag strip. Determine the average acceleration in \(\text{m/s}^2\), imperial \(\text{ft/s}^2\), and standard g-force (\(g_0\)).</p>
            <p><strong>Step 1: Convert velocity to SI units</strong></p>
            <div class="math-block">
              $$v_1 = 60\text{ mph} \times 0.447040\text{ m/s per mph} = 26.8224\text{ m/s}$$
            </div>
            <p><strong>Step 2: Calculate average acceleration in SI units</strong></p>
            <div class="math-block">
              $$a = \frac{\Delta v}{\Delta t} = \frac{26.8224\text{ m/s} - 0}{1.98\text{ s}} = 13.5467\text{ m/s}^2$$
            </div>
            <p><strong>Step 3: Convert to standard g-force (\(g_0\))</strong></p>
            <div class="math-block">
              $$a_{g} = \frac{13.5467\text{ m/s}^2}{9.80665\text{ m/s}^2/g_0} = 1.3814\text{ g}_0$$
            </div>
            <p><strong>Step 4: Convert to imperial feet per second squared</strong></p>
            <div class="math-block">
              $$a_{\text{imperial}} = \frac{13.5467\text{ m/s}^2}{0.3048\text{ m/ft}} = 44.4445\text{ ft/s}^2$$
            </div>
            <p><strong>Conclusion:</strong> The vehicle sustains an extraordinary average longitudinal acceleration of \(1.38\text{ g}\), demonstrating tire friction traction coefficients exceeding unity made possible by modern compound interlocking and downforce.</p>
          </div>

          <h2>5. Centrifugal Acceleration and Laboratory Centrifuge RCF</h2>
          <p>In biotechnology, biochemistry, and clinical medicine, sedimentation rates are governed by centrifugal acceleration rather than Earth's static gravity. Rotor speeds are expressed in revolutions per minute (\(N\) in RPM), but protocols mandate reporting <strong>Relative Centrifugal Force (RCF)</strong> in \(g\):</p>
          <div class="math-block">
            $$\text{RCF} = \frac{r \omega^2}{g_0} = \frac{r \left(\frac{2\pi N}{60}\right)^2}{9.80665} = 1.118 \times 10^{-5} \cdot r \cdot N^2$$
          </div>
          <p>Where \(r\) is the rotational radius in centimeters. For example, a microcentrifuge spinning at \(14,000\text{ RPM}\) with a rotor radius of \(8.5\text{ cm}\) generates:</p>
          <div class="math-block">
            $$\text{RCF} = 1.118 \times 10^{-5} \times 8.5 \times (14,000)^2 = 18,626\text{ g} \approx 182,660\text{ m/s}^2$$
          </div>

          <h2>6. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>How do you convert acceleration from m/s² to ft/s²?</h3>
            <p>Divide the value in \(\text{m/s}^2\) by exactly \(0.3048\) (or multiply by \(3.28084\)). For example, standard Earth gravity \(9.80665\text{ m/s}^2 \div 0.3048 = 32.17405\text{ ft/s}^2\).</p>
          </div>
          <div class="faq-item">
            <h3>Why is the Galileo (Gal) unit used in earth science?</h3>
            <p>Because the Gal (\(1\text{ cm/s}^2 = 10^{-2}\text{ m/s}^2\)) aligns with the CGS system historically used in geophysics. Earth's total gravitational field is roughly \(980\text{ Gal}\). Sensitive subsurface gravimeters measure anomalies down to microgals (\(1\,\mu\text{Gal} = 10^{-8}\text{ m/s}^2\)), capable of identifying subterranean cavities, aquifers, and ore deposits.</p>
          </div>
          <div class="faq-item">
            <h3>What is the difference between linear acceleration and angular acceleration?</h3>
            <p>Linear acceleration (\(a\)) measures the time rate of change of linear translational velocity along a path (\(\text{m/s}^2\)). Angular acceleration (\(\alpha\)) measures the rate of change of rotational speed (\(\text{rad/s}^2\)). They are coupled at radial distance \(r\) by tangential acceleration \(a_t = r \cdot \alpha\).</p>
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
    const G0 = 9.80665;
    const FT_PER_M = 1 / 0.3048;
    const IN_PER_M = 1 / 0.0254;

    const toSI = {
      mps2: v => v,
      g: v => v * G0,
      ftps2: v => v * 0.3048,
      inps2: v => v * 0.0254,
      gal: v => v * 0.01,
      mgal: v => v * 0.00001,
      kmhps: v => v / 3.6,
      mphps: v => v * 0.44704,
      knotps: v => v * (1852 / 3600)
    };

    function calculate() {
      const val = parseFloat(document.getElementById('accInput').value);
      const unit = document.getElementById('unitFrom').value;
      if (isNaN(val)) return;

      const mps2 = toSI[unit](val);
      const g = mps2 / G0;
      const ftps2 = mps2 * FT_PER_M;
      const inps2 = mps2 * IN_PER_M;
      const gal = mps2 * 100;
      const mgal = mps2 * 100000;

      document.getElementById('resMps2').textContent = mps2.toLocaleString('en-US', { minimumFractionDigits: 4, maximumFractionDigits: 6 }) + ' m/s²';
      document.getElementById('resG').textContent = g.toLocaleString('en-US', { minimumFractionDigits: 5, maximumFractionDigits: 5 }) + ' g₀';
      document.getElementById('resFtps2').textContent = ftps2.toLocaleString('en-US', { minimumFractionDigits: 4, maximumFractionDigits: 4 }) + ' ft/s²';
      document.getElementById('resInps2').textContent = inps2.toLocaleString('en-US', { minimumFractionDigits: 3, maximumFractionDigits: 3 }) + ' in/s²';
      document.getElementById('resGal').textContent = gal.toLocaleString('en-US', { minimumFractionDigits: 3, maximumFractionDigits: 4 }) + ' Gal';
      document.getElementById('resMgal').textContent = mgal.toLocaleString('en-US', { minimumFractionDigits: 1, maximumFractionDigits: 2 }) + ' mGal';

      // Automotive 0-60 mph estimate (26.8224 m/s / a)
      if (mps2 > 0.01) {
        const sec060 = 26.8224 / mps2;
        document.getElementById('resAuto').textContent = sec060.toFixed(2) + ' sec (0-60 mph)';
      } else {
        document.getElementById('resAuto').textContent = 'N/A';
      }
    }

    document.getElementById('accInput').addEventListener('input', calculate);
    document.getElementById('unitFrom').addEventListener('change', calculate);
    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('accInput').value = '1';
      document.getElementById('unitFrom').value = 'g';
      calculate();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
'''
    with open('acceleration-converter.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Created acceleration-converter.html successfully!")

def create_amortization_schedule():
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Loan Amortization Schedule Calculator | Principal, Interest & Extra Payments</title>
  <meta name="description" content="Calculate loan amortization schedules with monthly principal and interest breakdown, extra payments, early payoff timeline, and total interest savings.">
  <link rel="canonical" href="https://calchub.cloud/amortization-schedule-calculator.html">
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
        "name": "Loan Amortization Schedule Calculator",
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates complete loan amortization schedules, fixed monthly payments, interest vs principal breakdown, and interest savings from extra monthly prepayments.",
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
            "name": "How is a fixed monthly loan payment calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The fixed monthly payment M is calculated using the standard annuity formula: M = P × [r(1+r)^n] / [(1+r)^n - 1], where P is principal borrowed, r is monthly interest rate (annual APR divided by 12), and n is total number of monthly payments."
            }
          },
          {
            "@type": "Question",
            "name": "Why is the interest portion so high at the beginning of an amortization schedule?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Because monthly interest is calculated directly against the remaining outstanding balance: Interest = Balance × r. Early in the loan term, the principal balance is at its maximum, meaning the bulk of each payment covers accrued interest. As principal is gradually retired, the monthly interest shrinks."
            }
          },
          {
            "@type": "Question",
            "name": "How do extra principal payments shorten the loan term?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Extra principal payments bypass interest calculations and apply 100% directly to the loan principal. This immediately reduces the remaining balance, thereby decreasing future monthly interest compounding and retiring the debt months or years ahead of schedule."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between a 15-year and a 30-year fixed mortgage?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A 15-year mortgage requires higher monthly payments because principal is amortized over half the time, but charges a lower interest rate and drastically reduces total lifetime interest paid—often saving 60% or more in cumulative financing charges."
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
        <a href="finance.html" class="active">Financial</a>
        <a href="engineering.html">Electrical</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="civil.html">Civil</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <div class="content-wrapper">
      <div class="calculator-container">
        <h1>Loan Amortization Schedule Calculator</h1>
        <p class="lead-text">Generate a comprehensive loan amortization schedule. Model fixed monthly payments, interest vs. principal progression, and accelerate debt payoff with extra monthly principal contributions.</p>

        <div class="calc-card">
          <div class="calc-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="loanAmount">Loan Amount (Principal $)</label>
                <input type="number" id="loanAmount" value="300000" min="1000" step="1000" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="interestRate">Annual Interest Rate (APR %)</label>
                <input type="number" id="interestRate" value="6.5" min="0.1" max="30" step="0.05" class="form-control">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="loanTermYears">Loan Term</label>
                <select id="loanTermYears" class="form-control">
                  <option value="30" selected>30 Years (360 Months)</option>
                  <option value="25">25 Years (300 Months)</option>
                  <option value="20">20 Years (240 Months)</option>
                  <option value="15">15 Years (180 Months)</option>
                  <option value="10">10 Years (120 Months)</option>
                  <option value="5">5 Years (60 Months)</option>
                </select>
              </div>
              <div class="form-group col-half">
                <label for="extraPayment">Extra Monthly Payment ($)</label>
                <input type="number" id="extraPayment" value="200" min="0" step="25" class="form-control">
              </div>
            </div>

            <div class="btn-group">
              <button type="button" id="calcBtn" class="btn btn-primary">Calculate Amortization</button>
              <button type="button" id="resetBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </div>

          <div class="results-panel" id="resultsPanel">
            <h2>Payment & Payoff Summary</h2>
            <div class="result-hero">
              <span class="hero-label">Standard Monthly Payment (P&I)</span>
              <span class="hero-value" id="resMonthlyPayment">$1,896.20</span>
            </div>

            <div class="results-grid">
              <div class="result-item">
                <span class="sub-label">Total Monthly Commitment</span>
                <span class="sub-value" id="resTotalMonthly">$2,096.20</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Total Interest (Standard)</span>
                <span class="sub-value" id="resStandardInterest">$382,633</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Total Interest (With Extra)</span>
                <span class="sub-value" id="resActualInterest">$279,152</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Lifetime Interest Saved</span>
                <span class="sub-value highlight" id="resInterestSaved">$103,481</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Actual Payoff Time</span>
                <span class="sub-value" id="resPayoffTime">22 yrs 4 mos</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Time Saved Ahead of Schedule</span>
                <span class="sub-value highlight" id="resTimeSaved">7 yrs 8 mos</span>
              </div>
            </div>

            <div style="margin-top: 1.5rem;">
              <h3>Annual Amortization Preview</h3>
              <div style="overflow-x: auto;">
                <table class="data-table" id="scheduleTable">
                  <thead>
                    <tr>
                      <th>Year</th>
                      <th>Total Paid</th>
                      <th>Principal Paid</th>
                      <th>Interest Paid</th>
                      <th>Ending Balance</th>
                    </tr>
                  </thead>
                  <tbody id="scheduleBody">
                    <!-- Populated by JS -->
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>

        <!-- Comprehensive Financial Engineering Article (1,300+ Words) -->
        <article class="article-body">
          <h2>1. The Financial Mathematics of Loan Amortization</h2>
          <p>Amortization is the process of spreading an interest-bearing debt into a series of periodic equal installments over a designated maturity term. While the total monthly payment remains constant in a fixed-rate loan, the internal composition of each installment alters dramatically month by month.</p>
          <p>The standard fixed-rate monthly installment \(M\) is derived from the ordinary annuity present value formula, equating borrowed capital \(P\) to the discounted sum of all future payments:</p>
          <div class="math-block">
            $$P = \sum_{k=1}^{n} \frac{M}{(1+r)^k} = M \left[ \frac{1 - (1+r)^{-n}}{r} \right]$$
          </div>
          <p>Solving algebraically for \(M\) yields the standard mortgage amortization formula:</p>
          <div class="math-block">
            $$M = P \cdot \frac{r(1+r)^n}{(1+r)^n - 1}$$
          </div>
          <p>Where:</p>
          <ul>
            <li>\(P\) is the original principal loan balance.</li>
            <li>\(r\) is the monthly periodic interest rate, calculated as annual nominal APR divided by 12 (\(r = \text{APR} / 12\)).</li>
            <li>\(n\) is the total number of compounding monthly payments (\(n = \text{Years} \times 12\)).</li>
          </ul>

          <h2>2. Recursive Month-by-Month Amortization Mechanics</h2>
          <p>For any arbitrary payment period \(k \in [1, n]\), the interest obligation \(I_k\) is determined exclusively by the unamortized beginning balance of that period \(B_{k-1}\):</p>
          <div class="math-block">
            $$I_k = B_{k-1} \cdot r$$
          </div>
          <p>Because the contractual total installment \(M\) is fixed, the portion allocated toward principal reduction \(P_k\) is simply the remainder:</p>
          <div class="math-block">
            $$P_k = M - I_k = M - (B_{k-1} \cdot r)$$
          </div>
          <p>The ending balance for period \(k\) updates recursively:</p>
          <div class="math-block">
            $$B_k = B_{k-1} - P_k = B_{k-1}(1+r) - M$$
          </div>
          <p>In the initial years of a long-term loan (such as a 30-year residential mortgage), the initial principal balance \(B_{k-1}\) is extraordinarily large. Consequently, \(I_k\) consumes between 70% and 85% of the total monthly payment. Over time, as each principal reduction lowers \(B_{k-1}\), future interest charges decline exponentially, forcing an ever-increasing proportion of subsequent payments into equity building.</p>

          <h2>3. The Accelerated Amortization Multiplier: Impact of Extra Payments</h2>
          <p>Borrowers who contribute extra capital above their contractual installment \(M\) trigger a profound asymmetric financial benefit. Unlike standard payments that are split between interest and principal, <strong>every dollar of extra payment applies 100% directly to reducing the outstanding principal balance</strong>:</p>
          <div class="math-block">
            $$B_k = B_{k-1} - (P_k + P_{\text{extra}})$$
          </div>
          <p>By shrinking the principal balance prematurely, the borrower destroys the baseline upon which all subsequent months of compound interest would have been assessed. The financial return on an extra principal payment is strictly equivalent to an after-tax, risk-free guaranteed yield matching the loan's APR.</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Loan Scenario ($300,000 at 6.5% APR)</th>
                <th>Monthly Payment</th>
                <th>Extra / Month</th>
                <th>Total Interest Paid</th>
                <th>Interest Saved</th>
                <th>Time to Payoff</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Baseline 30-Year Fixed</strong></td>
                <td>$1,896.20</td>
                <td>$0</td>
                <td>$382,633</td>
                <td>$0</td>
                <td>360 months (30.0 yrs)</td>
              </tr>
              <tr>
                <td><strong>+$100 / Month Principal</strong></td>
                <td>$1,996.20</td>
                <td>$100</td>
                <td>$320,184</td>
                <td>$62,449</td>
                <td>308 months (25.7 yrs)</td>
              </tr>
              <tr>
                <td><strong>+$200 / Month Principal</strong></td>
                <td>$2,096.20</td>
                <td>$200</td>
                <td>$279,152</td>
                <td>$103,481</td>
                <td>268 months (22.3 yrs)</td>
              </tr>
              <tr>
                <td><strong>+$500 / Month Principal</strong></td>
                <td>$2,396.20</td>
                <td>$500</td>
                <td>$199,411</td>
                <td>$183,222</td>
                <td>200 months (16.7 yrs)</td>
              </tr>
              <tr>
                <td><strong>Bi-Weekly Payment Schedule</strong></td>
                <td>$948.10 / 2 wks</td>
                <td>~1 extra pmt/yr</td>
                <td>$311,940</td>
                <td>$70,693</td>
                <td>299 months (24.9 yrs)</td>
              </tr>
            </tbody>
          </table>

          <div class="worked-example-card">
            <h3>Worked Financial Case Study: The 15-Year vs. 30-Year Mortgage Arbitrage</h3>
            <p><strong>Scenario:</strong> A homebuyer is financing a $400,000 mortgage. They are comparing a 30-year fixed mortgage at 6.75% APR against a 15-year fixed mortgage offering a lower preferential rate of 6.00% APR.</p>
            <p><strong>Option A: 30-Year Fixed at 6.75% APR (\(r = 0.0675 / 12 = 0.005625, n = 360\))</strong></p>
            <div class="math-block">
              $$M_{30} = 400,000 \cdot \frac{0.005625(1.005625)^{360}}{(1.005625)^{360} - 1} = \$2,594.30\text{ / month}$$
            </div>
            <p>Total Payments = \(\$2,594.30 \times 360 = \$933,948\). Total Cumulative Interest = \(\$533,948\).</p>
            <p><strong>Option B: 15-Year Fixed at 6.00% APR (\(r = 0.0600 / 12 = 0.005000, n = 180\))</strong></p>
            <div class="math-block">
              $$M_{15} = 400,000 \cdot \frac{0.005000(1.005000)^{180}}{(1.005000)^{180} - 1} = \$3,375.43\text{ / month}$$
            </div>
            <p>Total Payments = \(\$3,375.43 \times 180 = \$607,577\). Total Cumulative Interest = \(\$207,577\).</p>
            <p><strong>Financial Analysis:</strong> The 15-year mortgage requires an additional monthly cash outlay of \(\$781.13\) (+30.1%), but eliminates 15 full years of debt and <strong>saves an astounding $326,371 in cumulative financing interest</strong>.</p>
          </div>

          <h2>4. Regulatory Compliance and the Truth in Lending Act (Regulation Z)</h2>
          <p>Under United States federal law (Truth in Lending Act, 15 U.S.C. 1601 and Consumer Financial Protection Bureau Regulation Z), lenders are legally obligated to disclose the comprehensive Annual Percentage Rate (APR) alongside the pure amortization schedule. The APR incorporates not merely the nominal promissory note rate, but all prepaid finance charges, including origination points, underwriting fees, private mortgage insurance (PMI), and mandatory escrow prepaids.</p>
          <p>Furthermore, residential mortgages commonly bundle escrow components to form <strong>PITI</strong> (Principal, Interest, Property Taxes, and Homeowners Insurance). While Principal and Interest follow the exact deterministic mathematical schedule generated above, Taxes and Hazard Insurance are variable escrow reserves subject to annual servicer rebalancing under RESPA (Real Estate Settlement Procedures Act).</p>

          <h2>5. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>Can I pay off my mortgage early without a penalty?</h3>
            <p>Most modern conforming residential mortgages (Fannie Mae, Freddie Mac, FHA, and VA loans) strictly prohibit prepayment penalties under Dodd-Frank Wall Street Reform Act rules. However, commercial loans, subprime mortgages, and specialized hard money loans often include yield maintenance clauses or step-down prepayment penalties (e.g., 5-4-3-2-1% structures) during the initial 3 to 5 years.</p>
          </div>
          <div class="faq-item">
            <h3>How does recasting a mortgage differ from refinancing?</h3>
            <p>Mortgage recasting involves making a significant lump-sum principal payment (usually $5,000 to $10,000+) while retaining the existing promissory note, loan maturity date, and interest rate. The loan servicer re-amortizes the remaining smaller principal over the remaining term, lowering future monthly payment amounts without requiring closing costs or credit underwriting.</p>
          </div>
          <div class="faq-item">
            <h3>Does bi-weekly mortgage payment actually save money?</h3>
            <p>Yes. By paying half of your regular monthly payment every two weeks, you make 26 half-payments per year, which equates to 13 full monthly payments annually instead of 12. That single extra monthly payment per year trims roughly 4 to 6 years off a standard 30-year mortgage and saves tens of thousands in interest.</p>
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
    function calculateAmortization() {
      const P = parseFloat(document.getElementById('loanAmount').value) || 0;
      const annualRate = parseFloat(document.getElementById('interestRate').value) || 0;
      const years = parseInt(document.getElementById('loanTermYears').value) || 30;
      const extraPmt = parseFloat(document.getElementById('extraPayment').value) || 0;

      if (P <= 0 || annualRate <= 0) return;

      const r = (annualRate / 100) / 12;
      const n = years * 12;

      // Base Monthly Payment Formula
      const factor = Math.pow(1 + r, n);
      const M = P * (r * factor) / (factor - 1);

      // Baseline Calculation (No extra payment)
      let baseTotalInterest = (M * n) - P;

      // Actual Simulation with Extra Payment
      let balance = P;
      let actualTotalInterest = 0;
      let monthsElapsed = 0;
      let yearlyData = [];
      let currentYearPaid = 0;
      let currentYearPrincipal = 0;
      let currentYearInterest = 0;

      while (balance > 0.01 && monthsElapsed < 1200) {
        monthsElapsed++;
        let interestMonth = balance * r;
        let principalMonth = (M - interestMonth) + extraPmt;

        if (principalMonth > balance) {
          principalMonth = balance;
        }

        balance -= principalMonth;
        actualTotalInterest += interestMonth;

        currentYearPaid += (principalMonth + interestMonth);
        currentYearPrincipal += principalMonth;
        currentYearInterest += interestMonth;

        if (monthsElapsed % 12 === 0 || balance <= 0.01) {
          yearlyData.push({
            year: Math.ceil(monthsElapsed / 12),
            totalPaid: currentYearPaid,
            principal: currentYearPrincipal,
            interest: currentYearInterest,
            endingBalance: Math.max(0, balance)
          });
          currentYearPaid = 0;
          currentYearPrincipal = 0;
          currentYearInterest = 0;
        }
      }

      // Render Results
      const fmt = (v) => '$' + Math.round(v).toLocaleString('en-US');
      const fmtDec = (v) => '$' + v.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

      document.getElementById('resMonthlyPayment').textContent = fmtDec(M);
      document.getElementById('resTotalMonthly').textContent = fmtDec(M + extraPmt);
      document.getElementById('resStandardInterest').textContent = fmt(baseTotalInterest);
      document.getElementById('resActualInterest').textContent = fmt(actualTotalInterest);

      const interestSaved = Math.max(0, baseTotalInterest - actualTotalInterest);
      document.getElementById('resInterestSaved').textContent = fmt(interestSaved);

      const actualYears = Math.floor(monthsElapsed / 12);
      const actualMonths = monthsElapsed % 12;
      document.getElementById('resPayoffTime').textContent = actualYears + ' yrs ' + actualMonths + ' mos';

      const monthsSaved = Math.max(0, n - monthsElapsed);
      const savedYears = Math.floor(monthsSaved / 12);
      const savedMonths = monthsSaved % 12;
      document.getElementById('resTimeSaved').textContent = savedYears + ' yrs ' + savedMonths + ' mos';

      // Render Schedule Table (up to first 10 years or all)
      const tbody = document.getElementById('scheduleBody');
      tbody.innerHTML = '';
      const displayYears = yearlyData.slice(0, 10);
      displayYears.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>Year ${row.year}</td>
          <td>${fmt(row.totalPaid)}</td>
          <td>${fmt(row.principal)}</td>
          <td>${fmt(row.interest)}</td>
          <td>${fmt(row.endingBalance)}</td>
        `;
        tbody.appendChild(tr);
      });
      if (yearlyData.length > 10) {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td colspan="5" style="text-align:center;font-style:italic;color:var(--text-muted);">+ ${yearlyData.length - 10} more years through full payoff</td>`;
        tbody.appendChild(tr);
      }
    }

    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculateAmortization);
      el.addEventListener('change', calculateAmortization);
    });

    document.getElementById('calcBtn').addEventListener('click', calculateAmortization);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('loanAmount').value = '300000';
      document.getElementById('interestRate').value = '6.5';
      document.getElementById('loanTermYears').value = '30';
      document.getElementById('extraPayment').value = '0';
      calculateAmortization();
    });

    window.addEventListener('DOMContentLoaded', calculateAmortization);
  </script>
</body>
</html>
'''
    with open('amortization-schedule-calculator.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Created amortization-schedule-calculator.html successfully!")

if __name__ == '__main__':
    create_acceleration_converter()
    create_amortization_schedule()
