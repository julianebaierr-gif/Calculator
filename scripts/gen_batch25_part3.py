import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 5. FREQUENCY CONVERTER
# -------------------------------------------------------------
frequency_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Frequency Converter — Hz, kHz, MHz, GHz, RPM, rad/s | CalcHub</title>
  <meta name="description" content="Convert frequency and angular velocity units between Hertz (Hz), kilohertz (kHz), megahertz (MHz), gigahertz (GHz), RPM, radians per second (rad/s), and THz with precision engineering metrology.">
  <meta name="keywords" content="frequency converter, hz to rpm, mhz to ghz, rpm to rad/s, angular velocity converter, hertz to radians per second, nyquist sampling rate, electrical grid frequency, rf frequency converter">
  <meta name="author" content="CalcHub Electrical & Rotational Dynamics Engineering Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/frequency-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Frequency Converter — Hz, kHz, MHz, GHz, RPM, rad/s | CalcHub">
  <meta property="og:description" content="Convert frequency and angular velocity units between Hertz (Hz), kilohertz (kHz), megahertz (MHz), gigahertz (GHz), RPM, radians per second (rad/s), and THz with precision engineering metrology.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/frequency-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/frequency-converter.html#app",
      "name": "Precision Frequency & Rotational Velocity Converter",
      "url": "https://calchub.org/frequency-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Engineering-grade frequency and angular velocity converter covering SI Hertz spectrum, rotational RPM, and circular angular radian frequencies."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Frequency Converter", "item": "https://calchub.org/frequency-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How do you mathematically convert Revolutions Per Minute (RPM) to Hertz (Hz)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Because 1 Hertz is defined as one complete cycle (or revolution) per second, and 1 minute contains precisely 60 seconds, the conversion formula is Hz = RPM / 60. Conversely, RPM = Hz × 60. For example, a 4-pole synchronous AC motor spinning at 1,800 RPM operates at a mechanical rotational frequency of 1,800 / 60 = 30 Hz."
          }
        },
        {
          "@type": "Question",
          "name": "What is the physical relationship between ordinary cyclical frequency (f in Hz) and angular frequency (ω in rad/s)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One complete cyclical oscillation traverses 2π radians (approx. 6.2831853 radians) of circular angle. Consequently, angular frequency ω equals 2π × f, and cyclical frequency f = ω / (2π). In a North American 60 Hz electric power grid, the angular frequency is ω = 2π × 60 ≈ 376.99 rad/s, whereas in a 50 Hz European grid, ω = 2π × 50 ≈ 314.16 rad/s."
          }
        },
        {
          "@type": "Question",
          "name": "How does the Nyquist-Shannon Sampling Theorem apply cyclical frequency to digital signal processing?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Nyquist-Shannon sampling theorem states that to reconstruct an analog signal without aliasing distortion, the sampling frequency (f_s) must strictly exceed twice the highest frequency component (f_max) present in the bandlimited signal: f_s > 2 f_max. For standard compact disc (CD) audio with a human hearing ceiling of 20 kHz (20,000 Hz), the standardized sampling rate is 44.1 kHz, satisfying the theorem with an antialiasing transition margin."
          }
        },
        {
          "@type": "Question",
          "name": "What is the relationship between electromagnetic frequency and free-space wavelength?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Electromagnetic radiation travels in a vacuum at the speed of light c ≈ 299,792,458 m/s. The wavelength λ and frequency f are related inversely by λ = c / f. For a 2.4 GHz Wi-Fi radio carrier, the wavelength in vacuum or dry air is λ = 299,792,458 / 2,400,000,000 ≈ 0.1249 meters (12.49 cm), which dictates the physical size of resonant antenna traces."
          }
        }
      ]
    }
  ]
}
  </script>
</head>
<body class="converter-page">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="logo">CalcHub</a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="converter.html" class="active">Converters</a>
        <a href="financial.html">Finance</a>
        <a href="fitness.html">Fitness</a>
        <a href="health.html">Health</a>
      </nav>
    </div>
  </header>

  <main class="page-wrapper">
    <div class="converter-layout">
      <div class="converter-main">
        <div class="calculator-header">
          <div class="breadcrumbs">
            <a href="index.html">Home</a> &rsaquo;
            <a href="converter.html">Unit Converters</a> &rsaquo;
            <span>Frequency Converter</span>
          </div>
          <span class="badge">Acoustic, RF &amp; Rotational Metrology</span>
          <h1>Precision Frequency Converter</h1>
          <p class="tagline">Convert between cyclical frequencies (Hz, kHz, MHz, GHz, THz), rotational speed (RPM), and angular velocity (rad/s) with SI-standard precision.</p>
        </div>

        <div class="calculator-container card-surface">
          <div class="converter-box">
            <div class="converter-inputs-grid">
              <div class="input-col">
                <label for="freqFromVal" class="input-label">From Value</label>
                <input type="number" id="freqFromVal" class="converter-num-input" value="1000" step="any" placeholder="Enter frequency">
                <label for="freqFromUnit" class="input-label sub-label">From Unit</label>
                <select id="freqFromUnit" class="converter-select">
                  <option value="hz">Hertz (Hz)</option>
                  <option value="khz" selected>Kilohertz (kHz)</option>
                  <option value="mhz">Megahertz (MHz)</option>
                  <option value="ghz">Gigahertz (GHz)</option>
                  <option value="thz">Terahertz (THz)</option>
                  <option value="rpm">Revolutions / Min (RPM)</option>
                  <option value="rad_s">Radians / Sec (rad/s)</option>
                  <option value="cps">Cycles / Sec (cps)</option>
                </select>
              </div>

              <div class="swap-col">
                <button type="button" id="freqSwapBtn" class="swap-button" title="Swap input and output units" aria-label="Swap units">
                  &#8644;
                </button>
              </div>

              <div class="input-col">
                <label for="freqToVal" class="input-label">Converted Value</label>
                <input type="text" id="freqToVal" class="converter-num-input output-val" readonly value="1">
                <label for="freqToUnit" class="input-label sub-label">To Unit</label>
                <select id="freqToUnit" class="converter-select">
                  <option value="hz">Hertz (Hz)</option>
                  <option value="khz">Kilohertz (kHz)</option>
                  <option value="mhz" selected>Megahertz (MHz)</option>
                  <option value="ghz">Gigahertz (GHz)</option>
                  <option value="thz">Terahertz (THz)</option>
                  <option value="rpm">Revolutions / Min (RPM)</option>
                  <option value="rad_s">Radians / Sec (rad/s)</option>
                  <option value="cps">Cycles / Sec (cps)</option>
                </select>
              </div>
            </div>

            <div class="converter-quick-presets">
              <span class="preset-label">Standard Reference Benchmarks:</span>
              <button type="button" class="preset-chip" data-val="50" data-from="hz" data-to="rad_s">50 Hz AC Grid (314 rad/s)</button>
              <button type="button" class="preset-chip" data-val="60" data-from="hz" data-to="rad_s">60 Hz AC Grid (377 rad/s)</button>
              <button type="button" class="preset-chip" data-val="3000" data-from="rpm" data-to="hz">3000 RPM (50 Hz)</button>
              <button type="button" class="preset-chip" data-val="2.4" data-from="ghz" data-to="mhz">2.4 GHz Wi-Fi (2400 MHz)</button>
            </div>

            <div class="conversion-summary-panel" id="freqSummaryCard">
              <div class="summary-line">
                <span class="summary-label">Direct Relation:</span>
                <span class="summary-formula" id="freqEquation">1,000 kHz = 1 MHz</span>
              </div>
              <div class="summary-submetrics">
                <div class="submetric-item">
                  <span class="submetric-name">Wave Period (T):</span>
                  <span class="submetric-val" id="freqPeriodVal">1.000 μs</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Angular Freq (ω):</span>
                  <span class="submetric-val" id="freqOmegaVal">6,283,185.3 rad/s</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Vacuum Wavelength (λ):</span>
                  <span class="submetric-val" id="freqLambdaVal">299.79 m</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <section>
            <h2>Fundamental Metrology of Frequency, Angular Velocity &amp; Cyclical Oscillations</h2>
            <p>
              Frequency measures the recurrence rate of any periodic phenomenon per unit time. In the International System of Units (SI), the derived unit of frequency is the <strong>Hertz (Hz)</strong>, defined explicitly as one cyclical oscillation per second (\(1\text{ Hz} = 1\text{ s}^{-1}\)), named in honor of Heinrich Rudolf Hertz who experimentally confirmed James Clerk Maxwell's electromagnetic wave theory. Whether analyzing high-frequency microwave transmission lines, structural vibration harmonics in turbo-machinery, acoustic audio soundscapes, or rotating shafts, frequency conversions form the backbone of modern physical and electrical engineering.
            </p>
            <p>
              Engineers routinely navigate between two distinct branches of periodic kinematics:
            </p>
            <ol>
              <li><strong>Cyclic Frequency (\(f\)):</strong> Measured in Hertz (\(\text{Hz}\)), cycles per second (\(\text{cps}\)), or rotational speed in revolutions per minute (\(\text{RPM}\)). This quantifies the count of whole 360-degree cycles executed within a given time interval.</li>
              <li><strong>Angular Frequency (\(\omega\)):</strong> Measured in radians per second (\(\text{rad/s}\)). Because a single complete rotation sweeps through an arc of \(2\pi\) radians, angular frequency quantifies the rate of circular phase progression across time, widely utilized in differential equations, sinusoidal wave descriptions, and AC circuit phasors.</li>
            </ol>
          </section>

          <section>
            <h2>Exact Mathematical Conversion Formulas &amp; Kinematic Equivalences</h2>
            <p>
              Converting between cyclical frequency, angular frequency, rotational shaft speed, and periodic duration requires rigorous application of conversion constants. The fundamental mathematical models are governed by the following analytical relationships:
            </p>

            <div class="formula-card">
              <h3>Core Mathematical Transformations</h3>
              <p>$$\text{Cyclical Frequency to Angular Frequency: } \omega = 2\pi f \quad \Longleftrightarrow \quad f = \frac{\omega}{2\pi}$$</p>
              <p>$$\text{Rotational Speed to Cyclic Frequency: } f_{\text{Hz}} = \frac{\text{RPM}}{60} \quad \Longleftrightarrow \quad \text{RPM} = 60 \times f_{\text{Hz}}$$</p>
              <p>$$\text{Rotational Speed to Angular Velocity: } \omega_{\text{rad/s}} = \frac{2\pi \times \text{RPM}}{60} = \frac{\pi \times \text{RPM}}{30} \approx 0.104719755 \times \text{RPM}$$</p>
              <p>$$\text{Oscillation Period: } T = \frac{1}{f} = \frac{2\pi}{\omega}$$</p>
              <p>$$\text{Vacuum Electromagnetic Wavelength: } \lambda = \frac{c}{f} = \frac{299,792,458\text{ m/s}}{f_{\text{Hz}}}$$</p>
            </div>

            <p>
              When dealing with metric prefixes in the RF and optical spectrum, SI multipliers scale purely by decimal powers of ten:
            </p>
            <ul>
              <li><strong>Kilohertz (kHz):</strong> \(1\text{ kHz} = 10^3\text{ Hz} = 1,000\text{ Hz}\) (LF and MF radio bands, ultrasound).</li>
              <li><strong>Megahertz (MHz):</strong> \(1\text{ MHz} = 10^6\text{ Hz} = 1,000,000\text{ Hz}\) (VHF broadcast radio, microcontrollers, FM).</li>
              <li><strong>Gigahertz (GHz):</strong> \(1\text{ GHz} = 10^9\text{ Hz}\) (Microwaves, Wi-Fi 5/6/7, 5G NR, radar, desktop CPU clocks).</li>
              <li><strong>Terahertz (THz):</strong> \(1\text{ THz} = 10^{12}\text{ Hz}\) (Submillimeter astronomy, far-infrared spectroscopy, THz security scanners).</li>
            </ul>
          </section>

          <section>
            <h2>Electromagnetic Spectrum Allocation &amp; Practical Applications</h2>
            <p>
              The physical behavior of alternating electric fields, acoustic pressure waves, and mechanical vibrations changes dramatically depending on their frequency regime. The engineering matrix below details the official frequency bands recognized by the International Telecommunication Union (ITU) and mechanical dynamic standards:
            </p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Frequency Spectrum / Band</th>
                  <th>Nominal Frequency Range</th>
                  <th>Corresponding Period (T)</th>
                  <th>Wavelength in Vacuum (\(\lambda\))</th>
                  <th>Primary Real-World Applications</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Rotational Machinery (Industrial)</strong></td>
                  <td>600 &ndash; 3,600 RPM (10 &ndash; 60 Hz)</td>
                  <td>16.67 &ndash; 100 ms</td>
                  <td>N/A (Mechanical)</td>
                  <td>Gas turbines, 2/4-pole generators, diesel engine crankshafts</td>
                </tr>
                <tr>
                  <td><strong>AC Grid Power Frequency</strong></td>
                  <td>50 Hz / 60 Hz</td>
                  <td>20 ms / 16.67 ms</td>
                  <td>5,996 km / 4,997 km</td>
                  <td>National transmission grids, transformers, synchronous motors</td>
                </tr>
                <tr>
                  <td><strong>Acoustic Audio Range</strong></td>
                  <td>20 Hz &ndash; 20,000 Hz (20 kHz)</td>
                  <td>50 ms &ndash; 50 μs</td>
                  <td>17.15 m &ndash; 1.71 cm (in air)</td>
                  <td>Human hearing threshold, hi-fi music recording, voice telephony</td>
                </tr>
                <tr>
                  <td><strong>Medium Frequency (MF) Radio</strong></td>
                  <td>300 kHz &ndash; 3,000 kHz (3 MHz)</td>
                  <td>3.33 μs &ndash; 333 ns</td>
                  <td>1 km &ndash; 100 m</td>
                  <td>AM broadcast radio, maritime navigation, avalanche transceivers</td>
                </tr>
                <tr>
                  <td><strong>Very High Frequency (VHF)</strong></td>
                  <td>30 MHz &ndash; 300 MHz</td>
                  <td>33.3 ns &ndash; 3.33 ns</td>
                  <td>10 m &ndash; 1 m</td>
                  <td>FM radio broadcast (88-108 MHz), air traffic control voice (118-137 MHz)</td>
                </tr>
                <tr>
                  <td><strong>Ultra High Frequency (UHF)</strong></td>
                  <td>300 MHz &ndash; 3,000 MHz (3 GHz)</td>
                  <td>3.33 ns &ndash; 333 ps</td>
                  <td>1 m &ndash; 10 cm</td>
                  <td>Wi-Fi (2.4 GHz), 4G/5G LTE cellular, GPS L1 (1.575 GHz), Bluetooth</td>
                </tr>
                <tr>
                  <td><strong>Super High Frequency (SHF)</strong></td>
                  <td>3 GHz &ndash; 30 GHz</td>
                  <td>333 ps &ndash; 33.3 ps</td>
                  <td>10 cm &ndash; 1 cm</td>
                  <td>5 GHz / 6 GHz Wi-Fi, satellite Ku-band radar, airport surface detection</td>
                </tr>
                <tr>
                  <td><strong>Extremely High Frequency (EHF)</strong></td>
                  <td>30 GHz &ndash; 300 GHz</td>
                  <td>33.3 ps &ndash; 3.33 ps</td>
                  <td>10 mm &ndash; 1 mm (Millimeter Wave)</td>
                  <td>Automotive collision radar (77 GHz), high-capacity 5G mmWave backhaul</td>
                </tr>
              </tbody>
            </table>
          </section>

          <section>
            <h2>Rotational Dynamics, Grid Synchronization &amp; Nyquist-Shannon Sampling</h2>
            <p>
              In electro-mechanical power conversion, the electrical grid frequency produced by a generator is tied directly to its physical mechanical shaft rotation speed and magnetic pole count:
            </p>
            <p>
              $$f_e = \frac{P \times N}{120}$$
            </p>
            <p>
              Where \(f_e\) is the generated alternating electrical frequency in Hertz, \(P\) is the number of magnetic poles in the rotor assembly, and \(N\) is the shaft speed in revolutions per minute (RPM). In a 60 Hz grid (such as the United States), a 2-pole synchronous turbine must rotate at exactly \(N = (120 \times 60)/2 = 3,600\text{ RPM}\). In Europe or Asia running at 50 Hz, a 2-pole machine rotates at \(3,000\text{ RPM}\), while a 4-pole machine turns at \(1,500\text{ RPM}\).
            </p>
            <p>
              In digital signal processing (DSP) and automated sensor instrumentation, the <strong>Nyquist-Shannon Sampling Theorem</strong> establishes the absolute mathematical boundary for digitizing analog oscillations without irreversible spectral aliasing. If an analog signal contains continuous components up to frequency \(B\) (bandwidth in Hz), it must be sampled uniformly at a frequency \(f_s\) exceeding twice the highest frequency:
            </p>
            <p>
              $$f_s > 2 B$$
            </p>
            <p>
              If a vibration sensor monitors a gearbox exhibiting mesh harmonics at 4,200 Hz, sampling at less than 8,400 samples/sec (8.4 kHz) folds high-frequency energy back into the baseband, creating phantom low-frequency vibrations that deceive predictive maintenance algorithms.
            </p>
          </section>

          <section>
            <h2>Worked Engineering Case Study: High-Speed CNC Spindle Analysis</h2>
            <div class="worked-example-card">
              <h3>Engineering Scenario: High-Speed Machining Spindle Metrology</h3>
              <p>
                An aerospace precision milling center operates an electric spindle rated at <strong>24,000 RPM</strong>. The spindle is driven by a variable frequency drive (VFD) controlling an 8-pole synchronous permanent magnet motor. The tooling engineer needs to determine:
              </p>
              <ol>
                <li>The mechanical angular frequency (\(\omega_m\)) in radians per second.</li>
                <li>The mechanical shaft rotational frequency in Hertz (\(f_m\)).</li>
                <li>The required electrical stator drive frequency (\(f_e\)) delivered by the VFD.</li>
                <li>The rotational period per single cut revolution in milliseconds.</li>
              </ol>

              <h4>Step-by-Step Calculation:</h4>
              <p><strong>1. Mechanical Frequency in Hertz:</strong></p>
              <p>$$f_m = \frac{\text{RPM}}{60} = \frac{24,000}{60} = 400\text{ Hz}$$</p>

              <p><strong>2. Mechanical Angular Velocity (\(\omega_m\)):</strong></p>
              <p>$$\omega_m = 2 \pi \times f_m = 2 \times 3.14159265 \times 400 \approx 2,513.27\text{ rad/s}$$</p>

              <p><strong>3. VFD Electrical Stator Drive Frequency (\(f_e\)):</strong></p>
              <p>$$f_e = \frac{P \times N}{120} = \frac{8 \times 24,000}{120} = \frac{192,000}{120} = 1,600\text{ Hz} \quad (1.6\text{ kHz})$$</p>

              <p><strong>4. Single Revolution Time Period (\(T\)):</strong></p>
              <p>$$T = \frac{1}{f_m} = \frac{1}{400\text{ s}^{-1}} = 0.0025\text{ seconds} = 2.50\text{ milliseconds}$$</p>

              <p>
                <strong>Engineering Conclusion:</strong> The cutting bit turns once every 2.5 ms at an angular velocity of \(2,513.3\text{ rad/s}\). The drive electronics must supply clean 1.6 kHz 3-phase sinusoidal AC waveforms without harmonics to prevent thermal failure of the stator windings.
              </p>
            </div>
          </section>

          <section class="faq-section">
            <h2>Frequently Asked Questions Regarding Frequency &amp; Rotational Units</h2>
            <div class="faq-item">
              <h3>What is the difference between Hertz (Hz) and Becquerel (Bq) if both are 1/s?</h3>
              <p>While both units have the base SI dimension of reciprocal seconds (\(\text{s}^{-1}\)), the <strong>Hertz (Hz)</strong> is reserved strictly for periodic, deterministic cycles and oscillations where events occur at regular temporal spacing. The <strong>Becquerel (Bq)</strong> is designated strictly for radioactive decay events, which represent stochastic, random nuclear disintegrations that are not cyclical.</p>
            </div>
            <div class="faq-item">
              <h3>Why do different countries use 50 Hz vs. 60 Hz electric power grids?</h3>
              <p>The 60 Hz standard originated with Nikola Tesla and Westinghouse in the United States, optimized to prevent visible incandescent lamp flicker while maintaining optimal transformer core performance. In Europe, AEG adopted 50 Hz to conform with the metric system's decimal conventions. At 50 Hz, transformers require approximately 20% more core magnetic steel to avoid saturation compared to 60 Hz, but transmission lines exhibit lower reactive impedance losses over long geographical distances.</p>
            </div>
            <div class="faq-item">
              <h3>How does Doppler shift alter the observed frequency of waves?</h3>
              <p>When a wave source moves relative to an observer at velocity \(v_s\), the perceived frequency \(f'\) shifts according to \(f' = f_0 \left(\frac{v \pm v_0}{v \mp v_s}\right)\), where \(v\) is the propagation speed of the medium. For radar or astronomical light, an approaching object compresses wavelengths and increases frequency (blue-shift), while receding objects exhibit lowered frequency (red-shift), forming the operational basis of weather radar and speed traps.</p>
            </div>
            <div class="faq-item">
              <h3>What is meant by the 'Terahertz Gap' in physics and communications?</h3>
              <p>The Terahertz gap spans 0.1 THz to 10 THz (wavelengths 3 mm to 30 μm). It represents the spectral transition zone between traditional solid-state electronic semiconductor oscillators (which struggle at gigahertz limits due to carrier transit times) and optical photonics (which require cryogenic cooling for low-energy quantum emission). Modern high-electron-mobility transistors (HEMTs) and quantum cascade lasers are actively closing this gap for 6G telecommunications.</p>
            </div>
          </section>
        </article>
      </div>

      <aside class="converter-sidebar">
        <div class="sidebar-card">
          <h3>Related Physical &amp; Digital Converters</h3>
          <ul class="sidebar-links">
            <li><a href="power-converter.html">Power Converter (W, kW, HP)</a></li>
            <li><a href="force-converter.html">Force Converter (N, lbf, kN)</a></li>
            <li><a href="speed-converter.html">Speed Converter (m/s, km/h, mph)</a></li>
            <li><a href="energy-converter.html">Energy Converter (J, kWh, BTU)</a></li>
            <li><a href="data-transfer-rate-converter.html">Data Transfer Rate Converter (Mbps, Gbps)</a></li>
            <li><a href="data-storage-converter.html">Data Storage Converter (GB, TB, GiB)</a></li>
            <li><a href="flow-rate-converter.html">Flow Rate Converter (GPM, L/min, m³/h)</a></li>
            <li><a href="pressure-converter.html">Pressure Converter (Pa, bar, psi)</a></li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Rotational Reference</h3>
          <p class="sidebar-tip">
            Remember the quick rule of thumb for electric motors: To convert RPM to Hz, divide by 60. For 1,800 RPM, \(1,800 / 60 = 30\text{ Hz}\). For 3,600 RPM, \(3,600 / 60 = 60\text{ Hz}\).
          </p>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo">CalcHub</div>
          <p>The open-access platform for professional scientific, engineering, financial, and physiological calculations and unit conversions.</p>
        </div>
        <div class="footer-links">
          <h4>Converter Hubs</h4>
          <ul>
            <li><a href="converter.html">All Unit Converters</a></li>
            <li><a href="length-converter.html">Length Converter</a></li>
            <li><a href="weight-converter.html">Weight Converter</a></li>
            <li><a href="temperature-converter.html">Temperature Converter</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Engineering Tools</h4>
          <ul>
            <li><a href="power-converter.html">Power Converter</a></li>
            <li><a href="force-converter.html">Force Converter</a></li>
            <li><a href="pressure-converter.html">Pressure Converter</a></li>
            <li><a href="energy-converter.html">Energy Converter</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Company &amp; Legal</h4>
          <ul>
            <li><a href="about.html">About CalcHub</a></li>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="privacy.html">Privacy Policy</a></li>
            <li><a href="terms.html">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. Standard-grade metrology verified against NIST Special Publication 811 and ISO 80000 standards.</p>
      </div>
    </div>
  </footer>

  <script>
    (function() {
      // Conversion factors to base unit: Hertz (Hz)
      var factors = {
        hz: 1.0,
        khz: 1000.0,
        mhz: 1000000.0,
        ghz: 1000000000.0,
        thz: 1000000000000.0,
        rpm: 1.0 / 60.0,
        rad_s: 1.0 / (2.0 * Math.PI),
        cps: 1.0
      };

      var unitLabels = {
        hz: 'Hz',
        khz: 'kHz',
        mhz: 'MHz',
        ghz: 'GHz',
        thz: 'THz',
        rpm: 'RPM',
        rad_s: 'rad/s',
        cps: 'cps'
      };

      var fromInput = document.getElementById('freqFromVal');
      var fromSelect = document.getElementById('freqFromUnit');
      var toInput = document.getElementById('freqToVal');
      var toSelect = document.getElementById('freqToUnit');
      var swapBtn = document.getElementById('freqSwapBtn');

      var equationEl = document.getElementById('freqEquation');
      var periodEl = document.getElementById('freqPeriodVal');
      var omegaEl = document.getElementById('freqOmegaVal');
      var lambdaEl = document.getElementById('freqLambdaVal');

      function calculate() {
        var val = parseFloat(fromInput.value);
        if (isNaN(val)) {
          toInput.value = '';
          return;
        }

        var fromUnit = fromSelect.value;
        var toUnit = toSelect.value;

        // Convert to base Hz
        var baseHz = val * factors[fromUnit];
        // Convert from Hz to target
        var result = baseHz / factors[toUnit];

        // Format result nicely
        if (Math.abs(result) >= 1e7 || (Math.abs(result) < 1e-4 && result !== 0)) {
          toInput.value = result.toExponential(6);
        } else {
          toInput.value = parseFloat(result.toPrecision(8)).toString();
        }

        // Update Equation Text
        if (equationEl) {
          equationEl.textContent = val + " " + unitLabels[fromUnit] + " = " + toInput.value + " " + unitLabels[toUnit];
        }

        // Submetrics based on baseHz
        if (baseHz > 0) {
          // Period T = 1 / f
          var periodSec = 1.0 / baseHz;
          if (periodSec < 1e-9) {
            periodEl.textContent = (periodSec * 1e12).toFixed(3) + " ps";
          } else if (periodSec < 1e-6) {
            periodEl.textContent = (periodSec * 1e9).toFixed(3) + " ns";
          } else if (periodSec < 1e-3) {
            periodEl.textContent = (periodSec * 1e6).toFixed(3) + " μs";
          } else if (periodSec < 1) {
            periodEl.textContent = (periodSec * 1000).toFixed(3) + " ms";
          } else {
            periodEl.textContent = periodSec.toFixed(4) + " s";
          }

          // Angular frequency omega = 2 * pi * f
          var omega = 2.0 * Math.PI * baseHz;
          if (omega >= 1e6) {
            omegaEl.textContent = omega.toExponential(4) + " rad/s";
          } else {
            omegaEl.textContent = omega.toLocaleString(undefined, {maximumFractionDigits: 2}) + " rad/s";
          }

          // Wavelength lambda = c / f (c = 299792458 m/s)
          var c = 299792458.0;
          var lambda = c / baseHz;
          if (lambda >= 1000) {
            lambdaEl.textContent = (lambda / 1000).toFixed(2) + " km";
          } else if (lambda >= 1) {
            lambdaEl.textContent = lambda.toFixed(2) + " m";
          } else if (lambda >= 0.01) {
            lambdaEl.textContent = (lambda * 100).toFixed(2) + " cm";
          } else if (lambda >= 0.001) {
            lambdaEl.textContent = (lambda * 1000).toFixed(2) + " mm";
          } else {
            lambdaEl.textContent = (lambda * 1e6).toFixed(2) + " μm";
          }
        } else {
          periodEl.textContent = "N/A";
          omegaEl.textContent = "0 rad/s";
          lambdaEl.textContent = "N/A";
        }
      }

      fromInput.addEventListener('input', calculate);
      fromSelect.addEventListener('change', calculate);
      toSelect.addEventListener('change', calculate);

      swapBtn.addEventListener('click', function() {
        var temp = fromSelect.value;
        fromSelect.value = toSelect.value;
        toSelect.value = temp;
        calculate();
      });

      var presets = document.querySelectorAll('.preset-chip');
      presets.forEach(function(chip) {
        chip.addEventListener('click', function() {
          fromInput.value = this.dataset.val;
          fromSelect.value = this.dataset.from;
          toSelect.value = this.dataset.to;
          calculate();
        });
      });

      calculate();
    })();
  </script>
</body>
</html>
"""

# -------------------------------------------------------------
# 6. FLOW RATE CONVERTER
# -------------------------------------------------------------
flow_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flow Rate Converter — GPM, L/min, m³/h, CFS, BPD | CalcHub</title>
  <meta name="description" content="Convert volumetric fluid flow rates across GPM (US and Imperial), L/min, m³/h, m³/s, cubic feet per second (CFS), and petroleum barrels per day (BPD) with hydraulic engineering precision.">
  <meta name="keywords" content="flow rate converter, gpm to l/min, m3/h to gpm, cfs to gpm, barrels per day to gpm, hydraulic flow converter, pipe velocity calculator, volumetric flow rate, water flow rate conversion">
  <meta name="author" content="CalcHub Hydraulic & Mechanical Fluids Engineering Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/flow-rate-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Flow Rate Converter — GPM, L/min, m³/h, CFS, BPD | CalcHub">
  <meta property="og:description" content="Convert volumetric fluid flow rates across GPM (US and Imperial), L/min, m³/h, m³/s, cubic feet per second (CFS), and petroleum barrels per day (BPD) with hydraulic engineering precision.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/flow-rate-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/flow-rate-converter.html#app",
      "name": "Precision Volumetric Fluid Flow Rate Converter",
      "url": "https://calchub.org/flow-rate-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "Industrial hydraulic flow rate converter translating between SI volumetric rates (m³/s, m³/h, L/min) and imperial engineering standards (US GPM, UK GPM, CFS, BPD)."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Flow Rate Converter", "item": "https://calchub.org/flow-rate-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the exact conversion factor between US Gallons per Minute (GPM) and Liters per Minute (L/min)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One US liquid gallon equals exactly 3.785411784 liters. Consequently, 1 US GPM = 3.785411784 L/min. To convert from L/min to US GPM, multiply by approximately 0.264172 (or divide by 3.78541). For example, a commercial fire suppression sprinkler discharging 50 US GPM discharges 50 × 3.785411784 = 189.27 L/min."
          }
        },
        {
          "@type": "Question",
          "name": "How does cubic meters per hour (m³/h) convert to US Gallons per Minute (GPM)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Because 1 m³ = 1,000 liters and 1 hour = 60 minutes, 1 m³/h equals 1,000 / 60 ≈ 16.6667 L/min. Converting this into US gallons yields 1 m³/h ≈ 4.402868 US GPM. Conversely, 1 US GPM ≈ 0.227125 m³/h. An industrial HVAC chilled water circulation pump rated at 100 m³/h conveys approximately 440.29 US GPM."
          }
        },
        {
          "@type": "Question",
          "name": "What distinguishes US Gallons per Minute from Imperial (UK) Gallons per Minute?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The US liquid gallon is defined as exactly 231 cubic inches (approx. 3.785412 liters), whereas the British Imperial gallon is defined as exactly 4.54609 liters. Therefore, 1 Imperial GPM equals 1.20095 US GPM (approx. 20% larger). Failure to differentiate between US and UK gallons in offshore petroleum or marine cooling systems can cause a 20% pump undersizing error."
          }
        },
        {
          "@type": "Question",
          "name": "How do you calculate linear fluid velocity in a pipe from volumetric flow rate?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "By the hydraulic principle of continuity, volumetric flow rate Q equals cross-sectional internal area A multiplied by mean linear fluid velocity v: Q = A × v. Rearranging for velocity gives v = Q / A = (4 × Q) / (π × D²), where D is internal pipe diameter. In water supply engineering, pipe velocities are typically maintained between 1.0 m/s and 2.5 m/s (3 to 8 ft/s) to balance head friction loss against water hammer and erosion."
          }
        }
      ]
    }
  ]
}
  </script>
</head>
<body class="converter-page">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="logo">CalcHub</a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="converter.html" class="active">Converters</a>
        <a href="financial.html">Finance</a>
        <a href="fitness.html">Fitness</a>
        <a href="health.html">Health</a>
      </nav>
    </div>
  </header>

  <main class="page-wrapper">
    <div class="converter-layout">
      <div class="converter-main">
        <div class="calculator-header">
          <div class="breadcrumbs">
            <a href="index.html">Home</a> &rsaquo;
            <a href="converter.html">Unit Converters</a> &rsaquo;
            <span>Flow Rate Converter</span>
          </div>
          <span class="badge">Hydraulics, HVAC &amp; Process Piping</span>
          <h1>Precision Flow Rate Converter</h1>
          <p class="tagline">Convert volumetric fluid flow rates between GPM, L/min, m³/h, m³/s, CFS, and petroleum barrels per day (BPD) with hydraulic engineering accuracy.</p>
        </div>

        <div class="calculator-container card-surface">
          <div class="converter-box">
            <div class="converter-inputs-grid">
              <div class="input-col">
                <label for="flowFromVal" class="input-label">From Value</label>
                <input type="number" id="flowFromVal" class="converter-num-input" value="100" step="any" placeholder="Enter flow rate">
                <label for="flowFromUnit" class="input-label sub-label">From Unit</label>
                <select id="flowFromUnit" class="converter-select">
                  <option value="gpm_us" selected>Gallons / Min (US GPM)</option>
                  <option value="l_min">Liters / Min (L/min)</option>
                  <option value="m3_h">Cubic Meters / Hour (m³/h)</option>
                  <option value="cfs">Cubic Feet / Sec (CFS)</option>
                  <option value="l_s">Liters / Sec (L/s)</option>
                  <option value="m3_s">Cubic Meters / Sec (m³/s)</option>
                  <option value="gpm_uk">Gallons / Min (Imperial GPM)</option>
                  <option value="bpd">Petroleum Barrels / Day (BPD)</option>
                  <option value="mgd">Million Gallons / Day (MGD)</option>
                </select>
              </div>

              <div class="swap-col">
                <button type="button" id="flowSwapBtn" class="swap-button" title="Swap input and output units" aria-label="Swap units">
                  &#8644;
                </button>
              </div>

              <div class="input-col">
                <label for="flowToVal" class="input-label">Converted Value</label>
                <input type="text" id="flowToVal" class="converter-num-input output-val" readonly value="378.54">
                <label for="flowToUnit" class="input-label sub-label">To Unit</label>
                <select id="flowToUnit" class="converter-select">
                  <option value="gpm_us">Gallons / Min (US GPM)</option>
                  <option value="l_min" selected>Liters / Min (L/min)</option>
                  <option value="m3_h">Cubic Meters / Hour (m³/h)</option>
                  <option value="cfs">Cubic Feet / Sec (CFS)</option>
                  <option value="l_s">Liters / Sec (L/s)</option>
                  <option value="m3_s">Cubic Meters / Sec (m³/s)</option>
                  <option value="gpm_uk">Gallons / Min (Imperial GPM)</option>
                  <option value="bpd">Petroleum Barrels / Day (BPD)</option>
                  <option value="mgd">Million Gallons / Day (MGD)</option>
                </select>
              </div>
            </div>

            <div class="converter-quick-presets">
              <span class="preset-label">Standard Hydraulic Benchmarks:</span>
              <button type="button" class="preset-chip" data-val="100" data-from="gpm_us" data-to="m3_h">100 US GPM (22.7 m³/h)</button>
              <button type="button" class="preset-chip" data-val="10" data-from="cfs" data-to="gpm_us">10 CFS (4,488 GPM)</button>
              <button type="button" class="preset-chip" data-val="1000" data-from="bpd" data-to="gpm_us">1,000 BPD (29.2 GPM)</button>
              <button type="button" class="preset-chip" data-val="1" data-from="mgd" data-to="gpm_us">1 MGD (694.4 GPM)</button>
            </div>

            <div class="conversion-summary-panel" id="flowSummaryCard">
              <div class="summary-line">
                <span class="summary-label">Direct Relation:</span>
                <span class="summary-formula" id="flowEquation">100 US GPM = 378.541 L/min</span>
              </div>
              <div class="summary-submetrics">
                <div class="submetric-item">
                  <span class="submetric-name">SI Metric Base:</span>
                  <span class="submetric-val" id="flowBaseVal">0.006309 m³/s</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Flow in 4" Pipe (Velocity):</span>
                  <span class="submetric-val" id="flowPipe4Val">0.774 m/s (2.54 ft/s)</span>
                </div>
                <div class="submetric-item">
                  <span class="submetric-name">Hourly Mass (Water):</span>
                  <span class="submetric-val" id="flowMassVal">22,712 kg/h</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <section>
            <h2>Hydraulic Foundations of Volumetric Fluid Flow Rate</h2>
            <p>
              Volumetric fluid flow rate represents the physical volume of fluid passing through a given cross-sectional area per unit of time. Denoted traditionally by the symbol \(Q\) (or \(\dot{V}\)), it is a central operational parameter across civil hydraulics, chemical processing plants, oil and gas transmission pipelines, mechanical heating, ventilation, and air conditioning (HVAC) systems, and municipal water utilities.
            </p>
            <p>
              In the International System of Units (SI), the coherent derived unit of volumetric flow is the <strong>cubic meter per second (\(\text{m}^3\text{/s}\))</strong>. Because one cubic meter per second constitutes an enormous volume of fluid (equal to 1,000 liters every single second, or over 15,850 US gallons per minute), everyday engineering projects rely heavily on practical working units tailored to specific industrial contexts:
            </p>
            <ul>
              <li><strong>Cubic Meters per Hour (\(\text{m}^3/\text{h}\)):</strong> The ubiquitous European and global metric benchmark for municipal water pumps, wastewater clarifiers, and industrial centrifugal machinery.</li>
              <li><strong>Liters per Minute (\(\text{L/min}\)):</strong> The universal metric standard for laboratory fluidics, hydraulic power packs, automotive fuel systems, and plumbing fixtures.</li>
              <li><strong>Gallons per Minute (\(\text{US GPM}\)):</strong> The foundational benchmark of North American building services, commercial sprinkler fire protection systems (NFPA standards), and chiller circulators.</li>
              <li><strong>Cubic Feet per Second (\(\text{CFS}\) or cusec):</strong> The gold-standard hydrological unit employed by the US Geological Survey (USGS) and US Army Corps of Engineers for river discharge, open irrigation canals, and dam spillway monitoring.</li>
              <li><strong>Petroleum Barrels per Day (\(\text{BPD}\)):</strong> The international petroleum industry standard, where one 42-gallon barrel equals approximately 158.987 liters of crude or refined hydrocarbon liquid.</li>
            </ul>
          </section>

          <section>
            <h2>Governing Fluid Dynamics Equations &amp; Mathematical Equivalences</h2>
            <p>
              Flow rate conversions must respect the exact mathematical definitions established by international standards organizations such as ISO, NIST, and ANSI. The base SI definitions and exact conversion relationships are defined below:
            </p>

            <div class="formula-card">
              <h3>Analytical Flow Rate Relationships</h3>
              <p>$$\text{Continuity Principle: } Q = A \cdot v = \frac{\pi D^2}{4} v$$</p>
              <p>$$\text{Linear Velocity from Flow: } v = \frac{4 Q}{\pi D^2}$$</p>
              <p>$$\text{US Gallon Definition: } 1\text{ US Gallon} \equiv 231\text{ in}^3 = 0.003785411784\text{ m}^3$$</p>
              <p>$$\text{Imperial Gallon Definition: } 1\text{ UK Gallon} \equiv 4.54609\text{ Liters} = 0.00454609\text{ m}^3$$</p>
              <p>$$\text{Cubic Foot Definition: } 1\text{ ft}^3 = (0.3048\text{ m})^3 \equiv 0.028316846592\text{ m}^3$$</p>
              <p>$$\text{Petroleum Barrel: } 1\text{ bbl} \equiv 42\text{ US Gallons} \approx 0.158987295\text{ m}^3$$</p>
            </div>

            <p>
              From these exact physical definitions, the explicit conversion multipliers relative to the base SI unit (\(\text{m}^3/\text{s}\)) are derived:
            </p>
            <ul>
              <li>\(1\text{ m}^3/\text{s} = 3,600\text{ m}^3/\text{h} = 60,000\text{ L/min} = 1,000\text{ L/s}\)</li>
              <li>\(1\text{ US GPM} = \frac{0.003785411784}{60}\text{ m}^3/\text{s} \approx 6.30901964 \times 10^{-5}\text{ m}^3/\text{s}\)</li>
              <li>\(1\text{ Imperial GPM} = \frac{0.00454609}{60}\text{ m}^3/\text{s} \approx 7.57681667 \times 10^{-5}\text{ m}^3/\text{s}\)</li>
              <li>\(1\text{ CFS} = 0.028316846592\text{ m}^3/\text{s} \approx 448.831169\text{ US GPM}\)</li>
              <li>\(1\text{ BPD} = \frac{42 \times 0.003785411784}{86,400}\text{ m}^3/\text{s} \approx 1.8401307 \times 10^{-6}\text{ m}^3/\text{s} \approx 0.0291667\text{ US GPM}\)</li>
              <li>\(1\text{ MGD} = \frac{10^6 \times 0.003785411784}{86,400}\text{ m}^3/\text{s} \approx 0.043812636\text{ m}^3/\text{s} \approx 694.444\text{ US GPM}\)</li>
            </ul>
          </section>

          <section>
            <h2>Industrial Flow Rate Benchmark Matrix</h2>
            <p>
              Understanding the magnitude of fluid flow across distinct commercial, ecological, and industrial contexts is crucial for specifying pumps, valves, and flow meters. The comparative engineering matrix below illustrates typical operational flow rates across critical infrastructure:
            </p>

            <table class="data-table">
              <thead>
                <tr>
                  <th>Fluid System Application</th>
                  <th>Nominal Flow Rate</th>
                  <th>Equivalent Metric (\(\text{m}^3/\text{h}\))</th>
                  <th>Equivalent (\(\text{L/min}\))</th>
                  <th>Standard Pipe Size &amp; Velocity</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Residential Kitchen Sink Faucet</strong></td>
                  <td>1.5 &ndash; 2.2 US GPM</td>
                  <td>0.34 &ndash; 0.50 m³/h</td>
                  <td>5.68 &ndash; 8.33 L/min</td>
                  <td>1/2" Copper (approx. 1.2 &ndash; 1.8 m/s)</td>
                </tr>
                <tr>
                  <td><strong>Commercial Fire Sprinkler Head (K=5.6)</strong></td>
                  <td>25 &ndash; 40 US GPM</td>
                  <td>5.68 &ndash; 9.08 m³/h</td>
                  <td>94.6 &ndash; 151.4 L/min</td>
                  <td>1" &ndash; 1-1/4" Sch 40 Steel (approx. 2.5 &ndash; 3.0 m/s)</td>
                </tr>
                <tr>
                  <td><strong>Hydraulic Power Unit (HPU) Machine Tool</strong></td>
                  <td>15 &ndash; 60 L/min</td>
                  <td>0.90 &ndash; 3.60 m³/h</td>
                  <td>15.0 &ndash; 60.0 L/min</td>
                  <td>3/4" High-Pressure Steel Tube</td>
                </tr>
                <tr>
                  <td><strong>Commercial Building Chilled Water Pump</strong></td>
                  <td>250 &ndash; 1,200 US GPM</td>
                  <td>56.8 &ndash; 272.5 m³/h</td>
                  <td>946 &ndash; 4,542 L/min</td>
                  <td>6" &ndash; 10" Carbon Steel (approx. 1.8 &ndash; 2.4 m/s)</td>
                </tr>
                <tr>
                  <td><strong>Municipal Wastewater Lift Station</strong></td>
                  <td>5,000 &ndash; 15,000 US GPM</td>
                  <td>1,135 &ndash; 3,406 m³/h</td>
                  <td>18,927 &ndash; 56,781 L/min</td>
                  <td>16" &ndash; 24" Ductile Iron (approx. 2.0 &ndash; 2.7 m/s)</td>
                </tr>
                <tr>
                  <td><strong>Crude Oil Cross-Country Pipeline (36-inch)</strong></td>
                  <td>500,000 BPD</td>
                  <td>3,312 m³/h</td>
                  <td>55,200 L/min</td>
                  <td>36" API 5L Steel (approx. 1.5 &ndash; 2.0 m/s)</td>
                </tr>
                <tr>
                  <td><strong>Niagara Falls (Average Tourist Flow)</strong></td>
                  <td>85,000 CFS</td>
                  <td>8,665,000 m³/h</td>
                  <td>144,417,000 L/min</td>
                  <td>Natural riverbed discharge (approx. 2,407 m³/s)</td>
                </tr>
              </tbody>
            </table>
          </section>

          <section>
            <h2>Frictional Head Loss &amp; Darcy-Weisbach Pipeline Sizing</h2>
            <p>
              When sizing piping networks, converting flow rates correctly is merely the preliminary step. The volumetric rate \(Q\) directly dictates the head loss caused by viscous shear friction against the pipe inner walls, described by the fundamental <strong>Darcy-Weisbach Equation</strong>:
            </p>
            <p>
              $$h_f = f \cdot \frac{L}{D} \cdot \frac{v^2}{2g} = f \cdot \frac{8 L Q^2}{\pi^2 g D^5}$$
            </p>
            <p>
              Where \(h_f\) is friction head loss in meters of fluid column, \(f\) is the dimensionless Darcy friction factor (determined via the Colebrook-White formula or Moody diagram based on Reynolds number \(Re\)), \(L\) is the total pipe length, \(D\) is internal diameter, and \(g\) is gravitational acceleration (\(9.80665\text{ m/s}^2\)).
            </p>
            <p>
              Notice that frictional head loss scales with the <strong>square of volumetric flow rate (\(Q^2\))</strong> and inversely with the <strong>fifth power of pipe diameter (\(D^5\))</strong>. An error of 20% caused by mistaking Imperial GPM for US GPM magnifies into an approximate \((1.20)^2 = 1.44\) (44%) increase in system friction loss, which can cause severe cavitation, excessive pump motor amperage draw, and catastrophic pump impeller erosion.
            </p>
          </section>

          <section>
            <h2>Worked Engineering Case Study: Municipal Water Booster Station Sizing</h2>
            <div class="worked-example-card">
              <h3>Engineering Scenario: Pump Station Spec Conversion &amp; Velocity Verification</h3>
              <p>
                A civil consulting engineering firm in North America is procuring European-manufactured horizontal split-case pumps for a regional water district. The municipal design specification calls for a firm delivery rate of <strong>1,800 US GPM</strong> of potable water through a <strong>10-inch Schedule 40 steel transmission pipe</strong> (internal diameter \(D = 10.02\text{ inches} = 0.2545\text{ meters}\)).
              </p>
              <p>The engineering team must verify:</p>
              <ol>
                <li>The required pump capacity rating in metric cubic meters per hour (\(\text{m}^3/\text{h}\)).</li>
                <li>The volumetric flow rate in Liters per minute (\(\text{L/min}\)).</li>
                <li>The mean linear fluid flow velocity in the 10-inch pipe in meters per second (\(\text{m/s}\)).</li>
                <li>Whether the calculated velocity conforms with the AWWA recommended design velocity range of 1.2 to 2.4 m/s (4 to 8 ft/s).</li>
              </ol>

              <h4>Step-by-Step Calculation:</h4>
              <p><strong>1. Convert US GPM to \(\text{m}^3/\text{h}\):</strong></p>
              <p>$$Q_{\text{m}^3/\text{h}} = 1,800\text{ US GPM} \times 0.227124707\text{ m}^3/\text{h per GPM} = 408.824\text{ m}^3/\text{h}$$</p>

              <p><strong>2. Convert US GPM to \(\text{L/min}\):</strong></p>
              <p>$$Q_{\text{L/min}} = 1,800\text{ US GPM} \times 3.785411784\text{ L/min per GPM} = 6,813.74\text{ L/min}$$</p>

              <p><strong>3. Convert Flow to Base SI Units (\(\text{m}^3/\text{s}\)):</strong></p>
              <p>$$Q_{\text{m}^3/\text{s}} = \frac{408.824}{3,600} = 0.113562\text{ m}^3/\text{s}$$</p>

              <p><strong>4. Compute Pipe Cross-Sectional Area and Velocity:</strong></p>
              <p>$$A = \frac{\pi \times D^2}{4} = \frac{\pi \times (0.2545\text{ m})^2}{4} = 0.050873\text{ m}^2$$</p>
              <p>$$v = \frac{Q}{A} = \frac{0.113562\text{ m}^3/\text{s}}{0.050873\text{ m}^2} \approx 2.232\text{ m/s} \quad (7.32\text{ ft/s})$$</p>

              <p>
                <strong>Engineering Verification:</strong> The European pumps must be procured with a certified duty point of \(408.8\text{ m}^3/\text{h}\). The resulting linear velocity in the 10-inch pipe is \(2.23\text{ m/s}\), falling safely within the American Water Works Association (AWWA) upper velocity limit of \(2.4\text{ m/s}\), guaranteeing adequate scouring action while preventing premature pipeline erosion.
              </p>
            </div>
          </section>

          <section class="faq-section">
            <h2>Frequently Asked Questions Regarding Volumetric Flow Units</h2>
            <div class="faq-item">
              <h3>What is the difference between volumetric flow rate and mass flow rate?</h3>
              <p>Volumetric flow rate (\(Q\) or \(\dot{V}\)) measures the physical geometric volume of fluid passing a point per second (e.g., \(\text{m}^3/\text{s}\) or GPM). Mass flow rate (\(\dot{m}\)) measures the actual mass moving per second (e.g., \(\text{kg/s}\) or \(\text{lb/hr}\)), related by \(\dot{m} = \rho \cdot Q\), where \(\rho\) is fluid density. For compressible gases, volumetric flow changes with temperature and pressure, whereas mass flow remains invariant throughout the system.</p>
            </div>
            <div class="faq-item">
              <h3>What are SCFM and ACFM in compressed air systems?</h3>
              <p>In pneumatic engineering, <strong>ACFM (Actual Cubic Feet per Minute)</strong> measures the real volumetric flow rate under existing temperature, pressure, and humidity at the compressor inlet or discharge. <strong>SCFM (Standard Cubic Feet per Minute)</strong> normalizes this volumetric flow to standardized conditions (typically 14.696 psia, 68°F, and 0% relative humidity according to ASME/CAGI), representing an effective mass flow rate measurement.</p>
            </div>
            <div class="faq-item">
              <h3>How does a rotameter or orifice plate meter measure flow rate?</h3>
              <p>Differential pressure flow meters (such as orifice plates and Venturi tubes) measure flow based on Bernoulli's principle: restricting the fluid passage accelerates flow, converting static pressure energy into kinetic energy. By measuring the differential pressure drop (\(\Delta P\)) across the restriction, flow is calculated via \(Q = C_d A_2 \sqrt{\frac{2 \Delta P}{\rho (1 - \beta^4)}}\), where \(C_d\) is discharge coefficient and \(\beta\) is orifice-to-pipe diameter ratio.</p>
            </div>
            <div class="faq-item">
              <h3>Why is CFS (Cubic Feet per Second) used instead of GPM for environmental hydrology?</h3>
              <p>Rivers, flood plains, and dam discharges handle immense volumes of water where gallons become unwieldy. One CFS represents a 1-foot cube of water passing every second, equivalent to 448.8 GPM or 28.32 liters per second. Measuring the Mississippi River (which averages 590,000 CFS) in GPM would yield numbers in the hundreds of millions, increasing potential rounding and data entry errors.</p>
            </div>
          </section>
        </article>
      </div>

      <aside class="converter-sidebar">
        <div class="sidebar-card">
          <h3>Related Fluid &amp; Pressure Tools</h3>
          <ul class="sidebar-links">
            <li><a href="pressure-converter.html">Pressure Converter (psi, bar, kPa)</a></li>
            <li><a href="volume-converter.html">Volume Converter (liters, gallons, m³)</a></li>
            <li><a href="speed-converter.html">Speed Converter (m/s, km/h, mph)</a></li>
            <li><a href="power-converter.html">Power Converter (kW, HP)</a></li>
            <li><a href="energy-converter.html">Energy Converter (Joules, BTU)</a></li>
            <li><a href="force-converter.html">Force Converter (N, lbf)</a></li>
            <li><a href="frequency-converter.html">Frequency Converter (Hz, RPM)</a></li>
            <li><a href="temperature-converter.html">Temperature Converter (°C, °F, K)</a></li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Piping Rule of Thumb</h3>
          <p class="sidebar-tip">
            For water distribution lines, target a fluid velocity of <strong>1.5 to 2.0 m/s (5 to 7 ft/s)</strong>. Velocities below 1.0 m/s encourage sedimentation, while velocities above 2.5 m/s dramatically escalate pipe friction and hydraulic water hammer risks.
          </p>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo">CalcHub</div>
          <p>The open-access platform for professional scientific, engineering, financial, and physiological calculations and unit conversions.</p>
        </div>
        <div class="footer-links">
          <h4>Converter Hubs</h4>
          <ul>
            <li><a href="converter.html">All Unit Converters</a></li>
            <li><a href="length-converter.html">Length Converter</a></li>
            <li><a href="weight-converter.html">Weight Converter</a></li>
            <li><a href="temperature-converter.html">Temperature Converter</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Engineering Tools</h4>
          <ul>
            <li><a href="flow-rate-converter.html">Flow Rate Converter</a></li>
            <li><a href="pressure-converter.html">Pressure Converter</a></li>
            <li><a href="power-converter.html">Power Converter</a></li>
            <li><a href="energy-converter.html">Energy Converter</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Company &amp; Legal</h4>
          <ul>
            <li><a href="about.html">About CalcHub</a></li>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="privacy.html">Privacy Policy</a></li>
            <li><a href="terms.html">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. Standard-grade metrology verified against NIST Special Publication 811 and ISO 80000 standards.</p>
      </div>
    </div>
  </footer>

  <script>
    (function() {
      // Base unit: m^3/s
      var factors = {
        m3_s: 1.0,
        m3_h: 1.0 / 3600.0,
        l_s: 0.001,
        l_min: 0.001 / 60.0,
        gpm_us: 0.003785411784 / 60.0,
        gpm_uk: 0.00454609 / 60.0,
        cfs: 0.028316846592,
        bpd: (42.0 * 0.003785411784) / 86400.0,
        mgd: (1000000.0 * 0.003785411784) / 86400.0
      };

      var unitLabels = {
        m3_s: 'm³/s',
        m3_h: 'm³/h',
        l_s: 'L/s',
        l_min: 'L/min',
        gpm_us: 'US GPM',
        gpm_uk: 'Imperial GPM',
        cfs: 'CFS',
        bpd: 'BPD',
        mgd: 'MGD'
      };

      var fromInput = document.getElementById('flowFromVal');
      var fromSelect = document.getElementById('flowFromUnit');
      var toInput = document.getElementById('flowToVal');
      var toSelect = document.getElementById('flowToUnit');
      var swapBtn = document.getElementById('flowSwapBtn');

      var equationEl = document.getElementById('flowEquation');
      var baseValEl = document.getElementById('flowBaseVal');
      var pipe4ValEl = document.getElementById('flowPipe4Val');
      var massValEl = document.getElementById('flowMassVal');

      function calculate() {
        var val = parseFloat(fromInput.value);
        if (isNaN(val)) {
          toInput.value = '';
          return;
        }

        var fromUnit = fromSelect.value;
        var toUnit = toSelect.value;

        // Base m^3/s
        var baseM3s = val * factors[fromUnit];
        var result = baseM3s / factors[toUnit];

        if (Math.abs(result) >= 1e7 || (Math.abs(result) < 1e-4 && result !== 0)) {
          toInput.value = result.toExponential(6);
        } else {
          toInput.value = parseFloat(result.toPrecision(8)).toString();
        }

        if (equationEl) {
          equationEl.textContent = val + " " + unitLabels[fromUnit] + " = " + toInput.value + " " + unitLabels[toUnit];
        }

        if (baseValEl) {
          if (baseM3s >= 1e-3) {
            baseValEl.textContent = baseM3s.toFixed(6) + " m³/s";
          } else {
            baseValEl.textContent = baseM3s.toExponential(4) + " m³/s";
          }
        }

        // Velocity in 4" Sch 40 pipe (Internal Diameter = 4.026 inches = 0.10226 m)
        // Area = pi * (0.10226)^2 / 4 = 0.008213 m^2
        if (pipe4ValEl) {
          var area4 = 0.008213;
          var velMs = baseM3s / area4;
          var velFts = velMs * 3.28084;
          pipe4ValEl.textContent = velMs.toFixed(3) + " m/s (" + velFts.toFixed(2) + " ft/s)";
        }

        // Hourly mass of water (density ~ 1000 kg/m^3)
        // m3/h = baseM3s * 3600 -> mass kg = m3/h * 1000
        if (massValEl) {
          var kgPerHour = baseM3s * 3600.0 * 1000.0;
          if (kgPerHour >= 1e6) {
            massValEl.textContent = (kgPerHour / 1000.0).toLocaleString(undefined, {maximumFractionDigits: 1}) + " tonnes/h";
          } else {
            massValEl.textContent = Math.round(kgPerHour).toLocaleString() + " kg/h";
          }
        }
      }

      fromInput.addEventListener('input', calculate);
      fromSelect.addEventListener('change', calculate);
      toSelect.addEventListener('change', calculate);

      swapBtn.addEventListener('click', function() {
        var temp = fromSelect.value;
        fromSelect.value = toSelect.value;
        toSelect.value = temp;
        calculate();
      });

      var presets = document.querySelectorAll('.preset-chip');
      presets.forEach(function(chip) {
        chip.addEventListener('click', function() {
          fromInput.value = this.dataset.val;
          fromSelect.value = this.dataset.from;
          toSelect.value = this.dataset.to;
          calculate();
        });
      });

      calculate();
    })();
  </script>
</body>
</html>
"""

# Write files
with open(os.path.join(BASE_DIR, 'frequency-converter.html'), 'w', encoding='utf-8') as f:
    f.write(frequency_html.strip() + '\n')
print("Generated frequency-converter.html successfully!")

with open(os.path.join(BASE_DIR, 'flow-rate-converter.html'), 'w', encoding='utf-8') as f:
    f.write(flow_html.strip() + '\n')
print("Generated flow-rate-converter.html successfully!")
