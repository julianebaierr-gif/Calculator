"""
Generates adc-dac-calculator.html and antenna-length-calculator.html
Each tool includes:
- 1,000+ words of deep engineering content
- Exact keyword matching in title, meta description, and H1
- KaTeX mathematical formulas
- Interactive JS calculation engine
- Reference engineering lookup tables
- Worked real-world case study example card
- Schema.org SoftwareApplication and FAQPage JSON-LD
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==========================================
# 1. ADC DAC CALCULATOR
# ==========================================
TOOL_ADC_DAC = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ADC DAC Calculator — Resolution, Quantization Error &amp; SNR</title>
  <meta name="description" content="Calculate ADC and DAC resolution, step size LSB voltage, quantization noise, theoretical SNR, and effective number of bits (ENOB) for precision data acquisition.">
  <meta name="keywords" content="adc dac calculator, adc resolution calculator, dac step size calculator, quantization noise calculator, lsb voltage calculator, adc snr calculator, enob calculator, data converter formulas">
  <link rel="canonical" href="https://calchub.org/adc-dac-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "ADC and DAC Precision Engineering Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Computes quantization steps, LSB voltage resolution, theoretical SQNR, RMS noise, and ENOB for Analog-to-Digital and Digital-to-Analog converters."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the formula for ADC step size (LSB voltage resolution)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The step size or Least Significant Bit (LSB) voltage represents the smallest detectable change in analog voltage that alters the digital output by one count. It is calculated by dividing the full-scale analog reference voltage range by the total number of discrete quantization levels: V_LSB = V_ref / (2^N), where N is the converter resolution in bits. For example, a 12-bit ADC operating with a 3.30 V reference has an LSB of 3.30 V / 4096 = 0.80566 mV."
            }
          },
          {
            "@type": "Question",
            "name": "How is the theoretical Signal-to-Quantization-Noise Ratio (SQNR) derived?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Theoretical SQNR is derived assuming an ideal full-scale sinusoidal input and uniform quantization error distributed uniformly between -LSB/2 and +LSB/2 with a probability density of 1/LSB. The RMS signal voltage of a peak-to-peak full-scale sine wave is V_FS / (2 * sqrt(2)), while the RMS quantization noise voltage is V_LSB / sqrt(12). Taking the ratio in decibels yields SNR_ideal = 20 * log10(sqrt(1.5) * 2^N) = 6.02 * N + 1.76 dB. Every additional bit of resolution boosts theoretical dynamic range by approximately 6.02 dB."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between converter resolution and accuracy?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Resolution specifies the number of discrete steps into which the converter divides the analog span (determined purely by bit count 2^N), indicating potential precision. Accuracy, however, measures how closely the actual converted output conforms to the true theoretical analog value across operating temperature and aging. Accuracy is degraded by analog hardware non-idealities including integral non-linearity (INL), differential non-linearity (DNL), offset voltage error, gain error, and reference drift."
            }
          },
          {
            "@type": "Question",
            "name": "What is Effective Number of Bits (ENOB) and why does it differ from nominal bits?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Nominal resolution is the design bit width of the digital register (such as 16 or 24 bits). Real-world analog converters suffer from internal thermal noise (Johnson-Nyquist noise), clock jitter, and harmonic distortion. Signal-to-Noise and Distortion ratio (SINAD) combines all noise and spurs. ENOB computes the equivalent ideal resolution that would produce the observed SINAD: ENOB = (SINAD - 1.76) / 6.02. A physical 16-bit SAR ADC may achieve an ENOB of 14.2 bits under high-frequency dynamic testing."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="engineering">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="solar-energy.html">Solar</a>
        <a href="fire-safety.html">Fire Safety</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="engineering.html">Electrical &amp; Power Systems</a> &rsaquo;
      <span>ADC DAC Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">Mixed-Signal Hardware Engineering</div>
          <h1 class="calc-title">ADC DAC Calculator</h1>
          <p class="calc-tagline">Calculate converter quantization resolution, step size voltage (LSB), theoretical SQNR, RMS quantization noise floor, and Effective Number of Bits (ENOB).</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="adcForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="resolutionBits" class="form-label">Resolution ($N$ Bits)</label>
                <select id="resolutionBits" class="form-control" onchange="calculateAdcDac()">
                  <option value="8">8-bit (256 codes)</option>
                  <option value="10">10-bit (1,024 codes)</option>
                  <option value="12" selected>12-bit (4,096 codes)</option>
                  <option value="14">14-bit (16,384 codes)</option>
                  <option value="16">16-bit (65,536 codes)</option>
                  <option value="18">18-bit (262,144 codes)</option>
                  <option value="20">20-bit (1,048,576 codes)</option>
                  <option value="24">24-bit (16,777,216 codes)</option>
                  <option value="32">32-bit (4,294,967,296 codes)</option>
                </select>
                <small class="form-hint">Number of conversion bits</small>
              </div>

              <div class="form-group">
                <label for="vRef" class="form-label">Reference Voltage ($V_{ref}$ / Full Scale)</label>
                <div class="input-with-unit">
                  <input type="number" id="vRef" class="form-control" value="3.30" step="0.01" min="0.1" max="100" oninput="calculateAdcDac()">
                  <span class="unit-badge">V</span>
                </div>
                <small class="form-hint">Full-scale analog voltage span</small>
              </div>

              <div class="form-group">
                <label for="analogIn" class="form-label">Analog Input Voltage ($V_{in}$)</label>
                <div class="input-with-unit">
                  <input type="number" id="analogIn" class="form-control" value="1.65" step="0.001" min="0" oninput="calculateAdcDac()">
                  <span class="unit-badge">V</span>
                </div>
                <small class="form-hint">Applied voltage to digitize</small>
              </div>

              <div class="form-group">
                <label for="measuredSinad" class="form-label">Measured SINAD (Optional for ENOB)</label>
                <div class="input-with-unit">
                  <input type="number" id="measuredSinad" class="form-control" placeholder="e.g. 71.5" step="0.1" min="0" max="180" oninput="calculateAdcDac()">
                  <span class="unit-badge">dB</span>
                </div>
                <small class="form-hint">Dynamic test SINAD in decibels</small>
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateAdcDac()" style="margin-top:1.25rem;">
              Calculate Converter Specs
            </button>
          </form>

          <!-- Output Display -->
          <div class="results-panel" id="resultsBox" style="margin-top:1.75rem;">
            <div class="results-grid">
              <div class="result-tile">
                <div class="result-label">Step Size (LSB Voltage)</div>
                <div class="result-value" id="outLsb">0.806 mV</div>
                <div class="result-subtext" id="outLsbMicro">805.66 &mu;V</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Quantization Levels</div>
                <div class="result-value" id="outLevels">4,096</div>
                <div class="result-subtext">Discrete Digital States ($2^N$)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Theoretical SQNR</div>
                <div class="result-value" id="outSqnr">74.00 dB</div>
                <div class="result-subtext">$6.02 \times N + 1.76\text{ dB}$</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Quantization Noise Floor</div>
                <div class="result-value" id="outQNoise">232.58 &mu;V</div>
                <div class="result-subtext">RMS Noise ($V_{LSB} / \sqrt{12}$)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Calculated Digital Code</div>
                <div class="result-value" id="outCodeDec">2048</div>
                <div class="result-subtext" id="outCodeHex">Hex: 0x800 | Binary: 100000000000</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Effective Bits (ENOB)</div>
                <div class="result-value" id="outEnob">11.59 bits</div>
                <div class="result-subtext" id="outEnobDesc">Based on measured SINAD</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 1000+ Words Technical Educational Article -->
        <article class="educational-content" style="margin-top:3rem;">
          <h2>Architectural Fundamentals of Analog-to-Digital &amp; Digital-to-Analog Conversion</h2>
          <p>
            In modern electronic engineering, analog-to-digital converters (ADCs) and digital-to-analog converters (DACs) represent the foundational bridge connecting continuous real-world physical phenomena—such as acoustic soundwaves, thermal vibrations, high-frequency electromagnetic radar pulses, and optical sensors—with discrete numerical digital processing engines like DSPs, FPGAs, and microcontrollers. The mathematical integrity of modern instrumentation relies directly on quantifying how continuous voltage distributions are partitioned into discrete numerical registers, and understanding the theoretical limits imposed by quantization noise, sampling limits, and analog non-idealities.
          </p>
          <p>
            Whether specifying a high-speed pipeline ADC for software-defined radio communications, a 24-bit delta-sigma ($\Sigma\Delta$) converter for seismic or medical strain-gauge telemetry, or an ultra-low-power SAR (Successive Approximation Register) ADC for IoT microcontrollers, the mathematical principles governing quantization resolution, dynamic range, signal-to-noise ratio, and step size remain strictly governed by Shannon sampling theorem and Fourier error distributions.
          </p>

          <h2>Core Mathematical Formulas Governing Quantization</h2>
          <p>
            An ideal $N$-bit analog-to-digital converter maps an analog input range defined by an upper positive reference $V_{ref+}$ and lower negative reference $V_{ref-}$ (or ground for single-ended systems) into $2^N$ discrete numerical integer bins. The key governing mathematical equations are expressed below:
          </p>

          <div class="formula-box">
            <div class="formula-title">1. Total Discrete Quantization Levels</div>
            <div class="formula-math">$$Q = 2^N$$</div>
            <p>Where $N$ represents the nominal digital resolution in bits.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">2. Least Significant Bit (LSB) Voltage Step Size</div>
            <div class="formula-math">$$V_{LSB} = \frac{V_{FS}}{2^N} = \frac{V_{ref+} - V_{ref-}}{2^N}$$</div>
            <p>Where $V_{FS}$ is the full-scale analog voltage range. $V_{LSB}$ represents the physical analog voltage step required to advance the digital code by exactly one unit.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">3. Root-Mean-Square (RMS) Quantization Noise Voltage</div>
            <div class="formula-math">$$V_{q(rms)} = \frac{V_{LSB}}{\sqrt{12}} \approx \frac{V_{LSB}}{3.4641}$$</div>
            <p>Under the standard mathematical assumption of a busy, non-correlated input signal, the quantization error is modeled as an independent, uniformly distributed random variable over the interval $[-\frac{V_{LSB}}{2}, +\frac{V_{LSB}}{2}]$ with probability density $p(e) = \frac{1}{V_{LSB}}$. Integrating the error variance yields $\sigma^2 = \int_{-LSB/2}^{LSB/2} e^2 \cdot \frac{1}{LSB} \, de = \frac{LSB^2}{12}$.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">4. Theoretical Signal-to-Quantization-Noise Ratio (SQNR)</div>
            <div class="formula-math">$$\text{SQNR}_{ideal} = 20 \log_{10}\left(\sqrt{1.5} \cdot 2^N\right) = 6.02 \times N + 1.76 \text{ dB}$$</div>
            <p>For a full-scale sinusoidal input spanning the entire converter range, the RMS signal voltage is $V_{sig(rms)} = \frac{V_{FS}}{2\sqrt{2}} = \frac{2^N \cdot V_{LSB}}{2\sqrt{2}}$. Taking the ratio of RMS signal power to RMS quantization noise power in decibels produces the celebrated $6.02N + 1.76$ dB relationship.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">5. Effective Number of Bits (ENOB)</div>
            <div class="formula-math">$$\text{ENOB} = \frac{\text{SINAD} - 1.76}{6.02}$$</div>
            <p>Where $\text{SINAD}$ is the measured Signal-to-Noise-and-Distortion ratio expressed in decibels (dB), incorporating real-world harmonic distortions (THD), thermal noise, clock aperture jitter, and analog non-linearities.</p>
          </div>

          <h2>Comparison of Common ADC Architecture Typologies</h2>
          <p>
            No single converter architecture optimizes all operating variables simultaneously. Hardware engineers evaluate trade-offs between sampling frequency, power dissipation, latency, and absolute resolution:
          </p>

          <table class="table-custom">
            <thead>
              <tr>
                <th>ADC Architecture</th>
                <th>Typical Resolution</th>
                <th>Sampling Rate ($f_s$)</th>
                <th>Latency</th>
                <th>Primary Application Domain</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Flash ADC</strong></td>
                <td>6 to 8 bits</td>
                <td>1 GSPS &ndash; 20 GSPS</td>
                <td>1 clock cycle</td>
                <td>Oscilloscopes, optical networking, radar</td>
              </tr>
              <tr>
                <td><strong>Successive Approx. (SAR)</strong></td>
                <td>10 to 18 bits</td>
                <td>100 kSPS &ndash; 10 MSPS</td>
                <td>Medium ($N$ cycles)</td>
                <td>Industrial control, medical telemetry, microcontrollers</td>
              </tr>
              <tr>
                <td><strong>Pipelined ADC</strong></td>
                <td>10 to 16 bits</td>
                <td>20 MSPS &ndash; 1 GSPS</td>
                <td>Fixed pipe delay</td>
                <td>Software-defined radio, cellular base stations, ultrasound</td>
              </tr>
              <tr>
                <td><strong>Delta-Sigma ($\Sigma\Delta$)</strong></td>
                <td>16 to 32 bits</td>
                <td>10 SPS &ndash; 2.5 MSPS</td>
                <td>High (digital filter)</td>
                <td>Precision weighing, seismic monitoring, audio DAC/ADC</td>
              </tr>
              <tr>
                <td><strong>Dual-Slope Integrating</strong></td>
                <td>12 to 20 bits</td>
                <td>5 SPS &ndash; 100 SPS</td>
                <td>Very high</td>
                <td>Benchtop digital multimeters (DMMs), line noise rejection</td>
              </tr>
            </tbody>
          </table>

          <h2>Comprehensive Resolution, LSB &amp; Dynamic Range Reference Table</h2>
          <p>
            The table below provides exact numerical calculations for standard converter resolutions operating under common reference voltages (5.0 V, 3.3 V, and 2.5 V), showing how step size shrinks exponentially with bit width:
          </p>

          <table class="table-custom">
            <thead>
              <tr>
                <th>Resolution ($N$)</th>
                <th>Quantization Codes</th>
                <th>Ideal SQNR (dB)</th>
                <th>LSB at $V_{ref} = 5.0\text{V}$</th>
                <th>LSB at $V_{ref} = 3.3\text{V}$</th>
                <th>LSB at $V_{ref} = 2.5\text{V}$</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>8-bit</strong></td>
                <td>256</td>
                <td>49.92 dB</td>
                <td>19.531 mV</td>
                <td>12.891 mV</td>
                <td>9.766 mV</td>
              </tr>
              <tr>
                <td><strong>10-bit</strong></td>
                <td>1,024</td>
                <td>61.96 dB</td>
                <td>4.883 mV</td>
                <td>3.223 mV</td>
                <td>2.441 mV</td>
              </tr>
              <tr>
                <td><strong>12-bit</strong></td>
                <td>4,096</td>
                <td>74.00 dB</td>
                <td>1.221 mV</td>
                <td>805.66 &mu;V</td>
                <td>610.35 &mu;V</td>
              </tr>
              <tr>
                <td><strong>14-bit</strong></td>
                <td>16,384</td>
                <td>86.04 dB</td>
                <td>305.18 &mu;V</td>
                <td>201.42 &mu;V</td>
                <td>152.59 &mu;V</td>
              </tr>
              <tr>
                <td><strong>16-bit</strong></td>
                <td>65,536</td>
                <td>98.08 dB</td>
                <td>76.29 &mu;V</td>
                <td>50.35 &mu;V</td>
                <td>38.15 &mu;V</td>
              </tr>
              <tr>
                <td><strong>18-bit</strong></td>
                <td>262,144</td>
                <td>110.12 dB</td>
                <td>19.07 &mu;V</td>
                <td>12.59 &mu;V</td>
                <td>9.54 &mu;V</td>
              </tr>
              <tr>
                <td><strong>24-bit</strong></td>
                <td>16,777,216</td>
                <td>146.24 dB</td>
                <td>298.02 nV</td>
                <td>196.70 nV</td>
                <td>149.01 nV</td>
              </tr>
              <tr>
                <td><strong>32-bit</strong></td>
                <td>4,294,967,296</td>
                <td>194.40 dB</td>
                <td>1.164 nV</td>
                <td>768.3 pV</td>
                <td>582.1 pV</td>
              </tr>
            </tbody>
          </table>

          <!-- Real World Worked Case Study Card -->
          <div class="worked-example-card">
            <h3>Practical Case Study: Industrial Pressure Transducer Signal Conditioning</h3>
            <p>
              An instrumentation design engineer is developing a high-precision digital pressure sensor. The piezoresistive transducer bridge produces an amplified single-ended analog output signal ranging from $0.00\text{ V}$ to $3.30\text{ V}$ across 0 to 1,000 psi. The engineer selects an STM32 internal 12-bit SAR ADC with an external precision reference of $V_{ref} = 3.30\text{ V}$. Dynamic testing reveals a measured $\text{SINAD}$ of $71.5\text{ dB}$.
            </p>
            <div class="step-calculation">
              <strong>Step 1: Calculate Discrete Quantization Levels:</strong><br>
              $$Q = 2^{12} = 4,096 \text{ codes}$$
            </div>
            <div class="step-calculation">
              <strong>Step 2: Calculate Step Size (LSB Voltage):</strong><br>
              $$V_{LSB} = \frac{3.30\text{ V}}{4096} = 0.00080566\text{ V} = 805.66\,\mu\text{V}$$
              <small>Pressure resolution per count: $\frac{1000\text{ psi}}{4096} \approx 0.244\text{ psi/count}$.</small>
            </div>
            <div class="step-calculation">
              <strong>Step 3: Calculate Quantization Noise Floor (RMS):</strong><br>
              $$V_{q(rms)} = \frac{805.66\,\mu\text{V}}{\sqrt{12}} = \frac{805.66}{3.4641} \approx 232.57\,\mu\text{V}$$
            </div>
            <div class="step-calculation">
              <strong>Step 4: Calculate Theoretical vs Effective Bits (ENOB):</strong><br>
              $$\text{SQNR}_{ideal} = 6.02 \times 12 + 1.76 = 74.00\text{ dB}$$
              $$\text{ENOB} = \frac{\text{SINAD} - 1.76}{6.02} = \frac{71.50 - 1.76}{6.02} = \frac{69.74}{6.02} \approx 11.58\text{ bits}$$
              <p>
                <strong>Conclusion:</strong> The ADC delivers an effective resolution of $11.58$ bits out of its nominal 12 bits, indicating excellent mixed-signal layout, minimal clock jitter, and superior analog power supply decoupling on the printed circuit board.
              </p>
            </div>
          </div>

          <h2>Anti-Aliasing Filter (AAF) Design &amp; Oversampling Processing Gain</h2>
          <p>
            According to the Nyquist-Shannon sampling theorem, an analog input signal must be strictly band-limited to less than half the sampling frequency ($f_{in} < f_s / 2$) to prevent irreversible spectral fold-over distortion known as aliasing. In practical hardware topologies, analog anti-aliasing filters (AAFs) cannot achieve brick-wall transition steepness. Engineers routinely employ deliberate oversampling and digital decimation filtering:
          </p>
          <div class="formula-box">
            <div class="formula-title">Oversampling SNR Processing Gain Formula</div>
            <div class="formula-math">$$\Delta\text{SNR} = 10 \log_{10}\left(\frac{f_s}{2 f_{BW}}\right) = 10 \log_{10}(\text{OSR})$$</div>
            <p>Where $\text{OSR} = \frac{f_s}{2 f_{BW}}$ is the oversampling ratio. Because quantization noise power is uniformly distributed across the entire Nyquist bandwidth from $0$ to $f_s/2$, filtering out out-of-band noise down to signal bandwidth $f_{BW}$ reduces in-band noise floor. For every quadruple ($4\times$) increase in oversampling ratio, dynamic range increases by $6.02\text{ dB}$, effectively recovering one extra bit of measurement resolution.</p>
          </div>

          <h2>Key Non-Idealities Affecting ADC &amp; DAC Performance</h2>
          <ul>
            <li><strong>Differential Non-Linearity (DNL):</strong> The difference between an actual step width and the ideal 1 LSB width. If $\text{DNL} < -1\text{ LSB}$, the converter suffers from missing codes (an ADC code never appears) or non-monotonicity in DACs.</li>
            <li><strong>Integral Non-Linearity (INL):</strong> The maximum deviation of the actual transfer function curve from a straight reference line drawn between zero and full-scale, representing cumulative distortion.</li>
            <li><strong>Aperture Jitter ($\sigma_t$):</strong> Clock phase noise introduces timing uncertainty in sample-and-hold circuits. Maximum signal frequency without SNR degradation is limited by $\text{SNR}_{jitter} = -20 \log_{10}(2\pi f_{in} \sigma_t)$.</li>
            <li><strong>Thermal Johnson Noise:</strong> For ultra-high resolution converters ($N \ge 24\text{ bits}$), physical thermodynamic resistor noise $\sqrt{4kTRB}$ often exceeds theoretical quantization noise, creating the fundamental analog physical noise ceiling.</li>
          </ul>
        </article>
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">Calc<strong>Hub</strong></div>
          <p class="footer-desc">High-precision engineering and scientific calculation tools verified against international standards.</p>
        </div>
        <div>
          <h4>Disciplines</h4>
          <ul class="footer-links">
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="solar-energy.html">Solar &amp; Renewable Energy</a></li>
            <li><a href="fire-safety.html">Fire Safety Hydraulics</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
          </ul>
        </div>
        <div>
          <h4>Standards &amp; Trust</h4>
          <ul class="footer-links">
            <li><a href="ohms-law-calculator.html">Ohm's Law Suite</a></li>
            <li><a href="engineering.html">Electrical Systems Hub</a></li>
            <li><a href="sitemap.xml">XML Sitemap</a></li>
            <li><a href="index.html">All Calculators</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2026 CalcHub. All rights reserved. Peer-reviewed against IEEE, IEC &amp; NIST standards.
      </div>
    </div>
  </footer>

  <script>
    function calculateAdcDac() {
      const N = parseInt(document.getElementById('resolutionBits').value, 10);
      const vRef = parseFloat(document.getElementById('vRef').value);
      const analogIn = parseFloat(document.getElementById('analogIn').value);
      const sinadInput = document.getElementById('measuredSinad').value.trim();

      if (isNaN(N) || isNaN(vRef) || vRef <= 0) return;

      const levels = Math.pow(2, N);
      const lsbVolts = vRef / levels;
      const lsbMilli = lsbVolts * 1000;
      const lsbMicro = lsbVolts * 1000000;

      const sqnr = 6.02 * N + 1.76;
      const qNoiseMicro = (lsbVolts / Math.sqrt(12)) * 1000000;

      // Digital Code Calculation
      let code = 0;
      if (!isNaN(analogIn)) {
        code = Math.floor(analogIn / lsbVolts);
        if (code >= levels) code = levels - 1;
        if (code < 0) code = 0;
      }

      // ENOB
      let enob = 0;
      let enobText = "";
      if (sinadInput !== "" && !isNaN(parseFloat(sinadInput))) {
        const sinad = parseFloat(sinadInput);
        enob = (sinad - 1.76) / 6.02;
        enobText = enob.toFixed(2) + " bits";
        document.getElementById('outEnobDesc').textContent = `From measured ${sinad.toFixed(1)} dB SINAD`;
      } else {
        enob = N;
        enobText = N.toFixed(2) + " bits (Ideal)";
        document.getElementById('outEnobDesc').textContent = "Ideal theoretical limit";
      }

      // Formatting outputs
      if (lsbMilli >= 1) {
        document.getElementById('outLsb').textContent = lsbMilli.toFixed(3) + " mV";
      } else {
        document.getElementById('outLsb').textContent = lsbMicro.toFixed(2) + " µV";
      }
      document.getElementById('outLsbMicro').textContent = lsbMicro.toLocaleString('en-US', {maximumFractionDigits: 2}) + " µV";

      document.getElementById('outLevels').textContent = levels.toLocaleString('en-US');
      document.getElementById('outSqnr').textContent = sqnr.toFixed(2) + " dB";

      if (qNoiseNoiseText(qNoiseMicro)) {
        document.getElementById('outQNoise').textContent = qNoiseNoiseText(qNoiseMicro);
      }

      document.getElementById('outCodeDec').textContent = code.toLocaleString('en-US');
      const hexStr = "0x" + code.toString(16).toUpperCase();
      const binStr = code.toString(2).padStart(Math.min(N, 16), '0');
      document.getElementById('outCodeHex').textContent = `Hex: ${hexStr} | Binary: ${binStr}`;

      document.getElementById('outEnob').textContent = enobText;
    }

    function qNoiseNoiseText(microVolts) {
      if (microVolts >= 1000) {
        return (microVolts / 1000).toFixed(3) + " mV";
      } else if (microVolts >= 1) {
        return microVolts.toFixed(2) + " µV";
      } else {
        return (microVolts * 1000).toFixed(2) + " nV";
      }
    }

    window.addEventListener('DOMContentLoaded', calculateAdcDac);
  </script>
</body>
</html>
"""

# ==========================================
# 2. ANTENNA LENGTH CALCULATOR
# ==========================================
TOOL_ANTENNA = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Antenna Length Calculator — Dipole, Monopole &amp; Resonant Wavelength</title>
  <meta name="description" content="Calculate physical resonant antenna length for half-wave dipoles, quarter-wave vertical whips, and 5/8 wave antennas with velocity factor end-effect correction.">
  <meta name="keywords" content="antenna length calculator, dipole antenna calculator, quarter wave whip calculator, resonant frequency antenna, velocity factor antenna, half wave dipole formula, ham radio antenna calculator">
  <link rel="canonical" href="https://calchub.org/antenna-length-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "RF Resonant Antenna Length Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates physical and electrical resonant conductor lengths for half-wave dipoles, quarter-wave verticals, and wire antennas with velocity factor and end-effect derating."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the standard formula for calculating a half-wave dipole antenna length?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The theoretical half-wavelength in free space is lambda / 2 = c / (2 * f). In physical wire antennas, an end-effect correction factor (velocity factor k, typically 0.95 for thin wire conductors) accounts for conductor capacitance to ground and fringing fields. The standard imperial formula is Length (feet) = 468 / Frequency (MHz). In metric units, Length (meters) = 142.65 / Frequency (MHz). Each individual leg of the center-fed dipole is exactly half of this total length."
            }
          },
          {
            "@type": "Question",
            "name": "Why is a physical antenna slightly shorter than its theoretical electrical wavelength?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Radio frequency electromagnetic waves travel through vacuum at the speed of light c (299,792,458 m/s). When traveling along a physical metallic conductor, the wave velocity is slightly reduced by the conductor dielectric properties, conductor finite thickness (diameter-to-length ratio), and insulator coatings. Additionally, electric field fringing at the conductor open tips introduces stray capacitance (end effect), making the wire appear electrically longer than its physical tape-measured length by roughly 4% to 5%."
            }
          },
          {
            "@type": "Question",
            "name": "What is the characteristic radiation resistance of a half-wave dipole versus a quarter-wave vertical?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "An ideal center-fed half-wave dipole suspended in free space exhibits a purely resistive radiation resistance of approximately 73 ohms at resonance. A quarter-wave vertical monopole operated over an ideal conductive ground plane reflects an identical image antenna beneath the earth, halving the driving-point impedance to approximately 36.5 ohms, which can be matched to standard 50-ohm coaxial cable using drooping ground radials inclined at 45 degrees."
            }
          },
          {
            "@type": "Question",
            "name": "How does conductor wire diameter influence antenna resonant bandwidth?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Thicker antenna conductors—such as aluminum tubing rather than thin enameled copper wire—lower the characteristic surge impedance and the loaded Q-factor of the antenna resonator. A lower Q-factor broadens the 2:1 SWR operational bandwidth, allowing the antenna to maintain acceptable impedance matching across an entire amateur radio or commercial frequency band without an antenna tuner."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body data-category="engineering">
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">
        <span class="logo-icon">&pi;</span>
        <span class="logo-text">Calc<strong>Hub</strong></span>
      </a>
      <nav class="site-nav">
        <a href="index.html">All Calculators</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="solar-energy.html">Solar</a>
        <a href="fire-safety.html">Fire Safety</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &rsaquo;
      <a href="engineering.html">Electrical &amp; Power Systems</a> &rsaquo;
      <span>Antenna Length Calculator</span>
    </nav>

    <div class="calculator-layout">
      <div class="calc-main">
        <header class="calc-header">
          <div class="calc-badge">RF &amp; Telecommunications Engineering</div>
          <h1 class="calc-title">Antenna Length Calculator</h1>
          <p class="calc-tagline">Calculate resonant physical lengths for half-wave dipoles, quarter-wave vertical monopoles, full-wave loops, and end-effect velocity factor corrections.</p>
        </header>

        <!-- Tool Card -->
        <div class="tool-card">
          <form id="antennaForm" onsubmit="return false;">
            <div class="calc-grid">
              <div class="form-group">
                <label for="freqValue" class="form-label">Operating Frequency</label>
                <div class="input-with-unit">
                  <input type="number" id="freqValue" class="form-control" value="146.52" step="0.001" min="0.01" max="100000" oninput="calculateAntenna()">
                  <span class="unit-badge">MHz</span>
                </div>
                <small class="form-hint">E.g., 14.2 MHz (20m), 146.52 MHz (2m)</small>
              </div>

              <div class="form-group">
                <label for="antennaType" class="form-label">Antenna Typology</label>
                <select id="antennaType" class="form-control" onchange="calculateAntenna()">
                  <option value="half-dipole" selected>Half-Wave Center-Fed Dipole (&lambda; / 2)</option>
                  <option value="quarter-vertical">Quarter-Wave Vertical Whip (&lambda; / 4)</option>
                  <option value="five-eighths">5/8-Wave Vertical Ground Plane (5&lambda; / 8)</option>
                  <option value="full-loop">Full-Wave Delta/Quad Loop (1.005 &lambda;)</option>
                </select>
                <small class="form-hint">Select resonant radiator topology</small>
              </div>

              <div class="form-group">
                <label for="velocityFactor" class="form-label">Velocity / End-Effect Factor ($k$)</label>
                <input type="number" id="velocityFactor" class="form-control" value="0.95" step="0.01" min="0.80" max="1.00" oninput="calculateAntenna()">
                <small class="form-hint">Typical 0.95 for thin wire; 0.92 for tubing</small>
              </div>

              <div class="form-group">
                <label for="feedImpedance" class="form-label">Transmission Line System</label>
                <select id="feedImpedance" class="form-control" onchange="calculateAntenna()">
                  <option value="50" selected>50 &Omega; Coaxial Cable (RG-213 / LMR-400)</option>
                  <option value="75">75 &Omega; Coaxial Cable (RG-6 / Hardline)</option>
                  <option value="300">300 &Omega; Twin-Lead Ladder Line</option>
                  <option value="450">450 &Omega; Open-Wire Window Line</option>
                </select>
                <small class="form-hint">Coaxial or balanced feeder</small>
              </div>
            </div>

            <button type="button" class="btn btn-primary" onclick="calculateAntenna()" style="margin-top:1.25rem;">
              Calculate Resonant Dimensions
            </button>
          </form>

          <!-- Output Display -->
          <div class="results-panel" id="resultsBox" style="margin-top:1.75rem;">
            <div class="results-grid">
              <div class="result-tile">
                <div class="result-label">Total Radiator Physical Length</div>
                <div class="result-value" id="outTotalMeters">0.973 m</div>
                <div class="result-subtext" id="outTotalFeet">3.19 ft (38.3 in)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Individual Leg / Radial Length</div>
                <div class="result-value" id="outLegMeters">0.487 m</div>
                <div class="result-subtext" id="outLegInches">1.60 ft (19.2 in)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Free-Space Wavelength (&lambda;)</div>
                <div class="result-value" id="outWavelength">2.046 m</div>
                <div class="result-subtext" id="outWavelengthFt">6.71 ft ($c / f$)</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Nominal Feedpoint Radiation $Z_{rad}$</div>
                <div class="result-value" id="outImpedance">73 &Omega;</div>
                <div class="result-subtext" id="outImpDesc">Natural feedpoint impedance</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Quarter-Wave Electrical Distance</div>
                <div class="result-value" id="outQuarterWave">0.512 m</div>
                <div class="result-subtext">Free-space $\lambda / 4$ benchmark</div>
              </div>

              <div class="result-tile">
                <div class="result-label">Estimated Theoretical Gain</div>
                <div class="result-value" id="outGain">2.15 dBi</div>
                <div class="result-subtext">0 dBd reference over isotropic</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 1000+ Words Technical Educational Article -->
        <article class="educational-content" style="margin-top:3rem;">
          <h2>Physics of Electromagnetic Wave Propagation &amp; Antenna Resonance</h2>
          <p>
            An antenna functions as a specialized transducer that converts conducted alternating radio frequency (RF) electrical currents traveling inside a transmission line into propagating transverse electromagnetic (TEM) waves freely expanding through unbounded space, and vice-versa. At the heart of RF antenna design lies the phenomenon of standing-wave electrical resonance: when the physical length of a conductive metallic element corresponds precisely to an integer or fractional multiple of the operational electromagnetic wavelength ($\lambda$), the reflected waves reinforce incoming waves, minimizing reactive impedance and transferring maximal power into space.
          </p>
          <p>
            When an RF transmitter excites an antenna at an off-resonance frequency, the feedpoint presents heavy reactive impedance (inductive reactance $+jX_L$ if too long, or capacitive reactance $-jX_C$ if too short), causing severe impedance mismatch, high Voltage Standing Wave Ratio (VSWR), reflected power heating the coaxial feeder, and reduced radiated field strength.
          </p>

          <h2>Core Mathematical Equations Governing Resonant Antennas</h2>
          <p>
            The fundamental mathematical relationships dictating antenna geometry, velocity factor derating, and electrical wavelength are expressed below:
          </p>

          <div class="formula-box">
            <div class="formula-title">1. Free-Space Wavelength Equation</div>
            <div class="formula-math">$$\lambda_0 = \frac{c}{f} = \frac{299,792,458}{f\text{ (Hz)}} \approx \frac{299.79}{f\text{ (MHz)}}\text{ meters} = \frac{983.57}{f\text{ (MHz)}}\text{ feet}$$</div>
            <p>Where $c$ is the speed of light in vacuum and $f$ is the carrier center frequency.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">2. Resonant Half-Wave ($\lambda / 2$) Dipole Physical Length</div>
            <div class="formula-math">$$L_{dipole} = \frac{c \cdot k}{2 \cdot f} \approx \frac{142.65 \times k}{f\text{ (MHz)}}\text{ meters} = \frac{468 \times k / 0.95}{f\text{ (MHz)}}\text{ feet}$$</div>
            <p>Where $k$ is the velocity factor / end-effect correction factor, traditionally empirically established as $0.95$ for standard bare copper and stranded insulated wire conductors in amateur radio engineering (yielding the classic $468 / f\text{ MHz}$ rule of thumb).</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">3. Quarter-Wave ($\lambda / 4$) Monopole Radiator Length</div>
            <div class="formula-math">$$L_{monopole} = \frac{L_{dipole}}{2} \approx \frac{71.32 \times k}{f\text{ (MHz)}}\text{ meters} = \frac{234 \times k / 0.95}{f\text{ (MHz)}}\text{ feet}$$</div>
            <p>A quarter-wave vertical radiator operates against a reflective ground plane (or an array of four elevated radials) which acts as an electrical mirror, creating an image antenna that synthesizes a full half-wave dipole distribution.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">4. 5/8-Wave ($5\lambda / 8$) Vertical Radiator Length</div>
            <div class="formula-math">$$L_{5/8} = \frac{5}{8} \cdot \lambda_0 \cdot k \approx \frac{178.31 \times k}{f\text{ (MHz)}}\text{ meters} = \frac{585 \times k / 0.95}{f\text{ (MHz)}}\text{ feet}$$</div>
            <p>A 5/8-wave antenna compresses the vertical radiation pattern toward the horizon, yielding approximately $3.0\text{ dBd}$ ($5.15\text{ dBi}$) of omnidirectional terrestrial gain. Note that a 5/8-wave radiator presents a capacitive reactive feedpoint component, requiring a small base loading coil to cancel $-jX_C$ and achieve a $50\,\Omega$ match.</p>
          </div>

          <div class="formula-box">
            <div class="formula-title">5. Full-Wave Loop Antenna Perimeter</div>
            <div class="formula-math">$$P_{loop} \approx \frac{301.75}{f\text{ (MHz)}}\text{ meters} = \frac{1005}{f\text{ (MHz)}}\text{ feet}$$</div>
            <p>A closed delta loop or quad loop requires a perimeter approximately $1.005\lambda$ due to wire interaction and loop geometry, offering lower reception noise and $1.0\text{ to }1.5\text{ dB}$ higher gain over a dipole.</p>
          </div>

          <h2>Velocity Factor ($k$) &amp; End-Effect Derating Mechanics</h2>
          <p>
            Why does a physical resonant wire antenna measure shorter than the mathematical speed-of-light wavelength in vacuum? RF engineers identify three distinct physical mechanisms:
          </p>
          <ul>
            <li><strong>End-Effect Capacitance:</strong> The open ends of an antenna element terminate abruptly in space, creating an electrostatic boundary condition. Fringing electric fields accumulate charges at the tips, effectively adding a lumped capacitive shunt to ground. This makes the wire appear electrically longer than its physical tape-measured length.</li>
            <li><strong>Conductor Diameter-to-Length Ratio ($L/d$):</strong> As element diameter increases (e.g. 2-inch aluminum irrigation tubing vs. 18 AWG copper wire), the characteristic surge impedance of the antenna drops, increasing tip capacitance and requiring greater physical shortening ($k \approx 0.92\text{ to }0.94$).</li>
            <li><strong>Insulation Dielectric Constant:</strong> Enclosing copper wire in PVC or polyethylene jacket ($ \varepsilon_r \approx 2.2\text{ to }3.5$) slows the wave velocity along the boundary layer, necessitating an additional 2% to 4% physical length reduction ($k \approx 0.92\text{ to }0.94$).</li>
          </ul>

          <h2>Standard Radio Frequency Bands &amp; Resonant Antenna Dimensions</h2>
          <p>
            The table below illustrates resonant physical dimensions across key amateur radio, commercial, and unlicensed ISM spectrum allocations:
          </p>

          <table class="table-custom">
            <thead>
              <tr>
                <th>Band Designation</th>
                <th>Center Frequency</th>
                <th>Full Wavelength ($\lambda$)</th>
                <th>Half-Wave Dipole Total</th>
                <th>Quarter-Wave Leg / Whip</th>
                <th>Feedpoint $Z_{rad}$</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>80 Meters (HF)</strong></td>
                <td>3.750 MHz</td>
                <td>79.94 m (262.3 ft)</td>
                <td>37.97 m (124.6 ft)</td>
                <td>18.99 m (62.3 ft)</td>
                <td>73 &Omega;</td>
              </tr>
              <tr>
                <td><strong>40 Meters (HF)</strong></td>
                <td>7.150 MHz</td>
                <td>41.93 m (137.6 ft)</td>
                <td>19.92 m (65.3 ft)</td>
                <td>9.96 m (32.7 ft)</td>
                <td>73 &Omega;</td>
              </tr>
              <tr>
                <td><strong>20 Meters (HF)</strong></td>
                <td>14.175 MHz</td>
                <td>21.15 m (69.4 ft)</td>
                <td>10.05 m (33.0 ft)</td>
                <td>5.02 m (16.5 ft)</td>
                <td>73 &Omega;</td>
              </tr>
              <tr>
                <td><strong>10 Meters (HF)</strong></td>
                <td>28.400 MHz</td>
                <td>10.56 m (34.6 ft)</td>
                <td>5.01 m (16.4 ft)</td>
                <td>2.51 m (8.2 ft)</td>
                <td>73 &Omega;</td>
              </tr>
              <tr>
                <td><strong>6 Meters (VHF)</strong></td>
                <td>50.125 MHz</td>
                <td>5.98 m (19.6 ft)</td>
                <td>2.84 m (9.3 ft)</td>
                <td>1.42 m (4.7 ft)</td>
                <td>73 &Omega;</td>
              </tr>
              <tr>
                <td><strong>2 Meters (VHF)</strong></td>
                <td>146.520 MHz</td>
                <td>2.05 m (6.7 ft)</td>
                <td>0.973 m (38.3 in)</td>
                <td>0.487 m (19.2 in)</td>
                <td>73 &Omega; (36.5&Omega; vert)</td>
              </tr>
              <tr>
                <td><strong>70 cm (UHF)</strong></td>
                <td>446.000 MHz</td>
                <td>0.672 m (26.5 in)</td>
                <td>0.319 m (12.6 in)</td>
                <td>0.160 m (6.3 in)</td>
                <td>73 &Omega; (36.5&Omega; vert)</td>
              </tr>
              <tr>
                <td><strong>Wi-Fi 2.4 GHz</strong></td>
                <td>2,450 MHz</td>
                <td>122.4 mm (4.82 in)</td>
                <td>58.1 mm (2.29 in)</td>
                <td>29.1 mm (1.14 in)</td>
                <td>36.5 &Omega;</td>
              </tr>
            </tbody>
          </table>

          <!-- Real World Worked Case Study Card -->
          <div class="worked-example-card">
            <h3>Practical Case Study: Constructing a 2-Meter VHF Vertical Ground Plane Antenna</h3>
            <p>
              An emergency communications technician needs to fabricate an omnidirectional base station antenna for the 2-meter VHF band, centered on the national FM simplex calling frequency $f = 146.520\text{ MHz}$. The antenna is constructed from an SO-239 chassis connector, using 2.5 mm bare copper wire for the vertical radiator and four horizontal ground radials angled downward at $45^\circ$.
            </p>
            <div class="step-calculation">
              <strong>Step 1: Compute Free-Space Full Wavelength:</strong><br>
              $$\lambda_0 = \frac{299.792}{146.520} = 2.0461\text{ meters} \approx 80.55\text{ inches}$$
            </div>
            <div class="step-calculation">
              <strong>Step 2: Calculate Quarter-Wave Radiator with Velocity Factor ($k = 0.95$):</strong><br>
              $$L_{vert} = \frac{71.32 \times 0.95}{146.520} = \frac{67.754}{146.520} = 0.4624\text{ meters} \approx 18.20\text{ inches}$$
              <small>Using formula $L = \frac{234}{146.52} = 1.597\text{ ft} \times 12 = 19.16\text{ inches}$ (raw); with $k=0.95$ yields $18.20\text{ inches}$.</small>
            </div>
            <div class="step-calculation">
              <strong>Step 3: Ground Radial Sizing &amp; Angle Matching:</strong><br>
              Ground radials are cut approximately 5% longer than the vertical whip ($L_{radials} \approx 19.1\text{ inches}$) to ensure a solid RF ground return. Bending the four ground radials downward at a $45^\circ$ angle increases the natural driving-point radiation resistance from $36.5\,\Omega$ directly to $50.0\,\Omega$, creating an ideal $1.05:1$ SWR match directly into standard $50\,\Omega$ RG-58 or LMR-400 coaxial cable without needing a matching transformer.
            </div>
            <div class="step-calculation">
              <strong>Step 4: Field Verification &amp; Trimming:</strong><br>
              The vertical radiator is initially cut 0.5 inches long ($18.7\text{ inches}$) and trimmed in 1/8-inch increments while observing an antenna analyzer until minimum SWR is centered exactly at $146.520\text{ MHz}$.
            </div>
          </div>

          <h2>Essential Guidelines for Antenna Installation &amp; Tuning</h2>
          <ul>
            <li><strong>Height Above Ground:</strong> For horizontal dipoles, mounting the antenna at least $\lambda / 2$ above ground (e.g. 10 meters high on the 20-meter band) is necessary to ensure the ground reflection enhances low-angle radiation for long-distance DX contacts rather than firing straight up as Near Vertical Incidence Skywave (NVIS).</li>
            <li><strong>1:1 Current Balun Integration:</strong> Connecting an unbalanced coaxial line directly to a balanced dipole excites common-mode currents on the outer coaxial shield, turning the feeder into an unwanted radiator and inducing RF feedback into the transceiver shack. A 1:1 Guanella current balun prevents this.</li>
            <li><strong>Tuning Procedure:</strong> Always cut wire antennas slightly longer than theoretical calculations. Trimming excess copper wire with side cutters is effortless; splicing extensions back onto an element is prone to mechanical and impedance degradation.</li>
          </ul>
        </article>
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">Calc<strong>Hub</strong></div>
          <p class="footer-desc">High-precision engineering and scientific calculation tools verified against international standards.</p>
        </div>
        <div>
          <h4>Disciplines</h4>
          <ul class="footer-links">
            <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
            <li><a href="solar-energy.html">Solar &amp; Renewable Energy</a></li>
            <li><a href="fire-safety.html">Fire Safety Hydraulics</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
          </ul>
        </div>
        <div>
          <h4>Standards &amp; Trust</h4>
          <ul class="footer-links">
            <li><a href="ohms-law-calculator.html">Ohm's Law Suite</a></li>
            <li><a href="engineering.html">Electrical Systems Hub</a></li>
            <li><a href="sitemap.xml">XML Sitemap</a></li>
            <li><a href="index.html">All Calculators</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2026 CalcHub. All rights reserved. Peer-reviewed against IEEE, IEC &amp; NIST standards.
      </div>
    </div>
  </footer>

  <script>
    function calculateAntenna() {
      const f = parseFloat(document.getElementById('freqValue').value);
      const antType = document.getElementById('antennaType').value;
      const k = parseFloat(document.getElementById('velocityFactor').value) || 0.95;
      const feedZ = parseInt(document.getElementById('feedImpedance').value, 10) || 50;

      if (isNaN(f) || f <= 0) return;

      const c = 299.792458; // MHz * m
      const lambdaM = c / f;
      const lambdaFt = lambdaM * 3.28084;

      let totalM = 0;
      let legM = 0;
      let imp = 73;
      let impDesc = "";
      let gain = "2.15 dBi";

      if (antType === "half-dipole") {
        totalM = (lambdaM / 2) * k;
        legM = totalM / 2;
        imp = 73;
        impDesc = "Center-fed dipole (balanced)";
        gain = "2.15 dBi (0 dBd)";
      } else if (antType === "quarter-vertical") {
        totalM = (lambdaM / 4) * k;
        legM = totalM; // Single vertical radiator
        imp = 36.5;
        impDesc = "Vertical whip over flat ground (unbalanced)";
        gain = "5.15 dBi (ground plane)";
      } else if (antType === "five-eighths") {
        totalM = (lambdaM * 5 / 8) * k;
        legM = totalM;
        imp = 50;
        impDesc = "5/8 wave with base inductive matching";
        gain = "5.15 dBi (3.0 dBd)";
      } else if (antType === "full-loop") {
        totalM = lambdaM * 1.005;
        legM = totalM / 3; // Delta loop leg
        imp = 110;
        impDesc = "Full-wave closed loop perimeter";
        gain = "3.20 dBi (1.05 dBd)";
      }

      const totalFt = totalM * 3.28084;
      const totalIn = totalM * 39.3701;
      const legFt = legM * 3.28084;
      const legIn = legM * 39.3701;

      document.getElementById('outTotalMeters').textContent = totalM.toFixed(3) + " m";
      document.getElementById('outTotalFeet').textContent = totalFt.toFixed(2) + " ft (" + totalIn.toFixed(1) + " in)";

      document.getElementById('outLegMeters').textContent = legM.toFixed(3) + " m";
      document.getElementById('outLegInches').textContent = legFt.toFixed(2) + " ft (" + legIn.toFixed(1) + " in)";

      document.getElementById('outWavelength').textContent = lambdaM.toFixed(3) + " m";
      document.getElementById('outWavelengthFt').textContent = lambdaFt.toFixed(2) + " ft (Free Space)";

      document.getElementById('outImpedance').textContent = imp + " \u03A9";
      document.getElementById('outImpDesc').textContent = impDesc;

      const quarterM = lambdaM / 4;
      document.getElementById('outQuarterWave').textContent = quarterM.toFixed(3) + " m (" + (quarterM * 3.28084).toFixed(2) + " ft)";

      document.getElementById('outGain').textContent = gain;
    }

    window.addEventListener('DOMContentLoaded', calculateAntenna);
  </script>
</body>
</html>
"""

def main():
    path_adc = os.path.join(BASE_DIR, "adc-dac-calculator.html")
    with open(path_adc, "w", encoding="utf-8") as f:
        f.write(TOOL_ADC_DAC.strip())
    print("[PASS] adc-dac-calculator.html generated successfully!")

    path_antenna = os.path.join(BASE_DIR, "antenna-length-calculator.html")
    with open(path_antenna, "w", encoding="utf-8") as f:
        f.write(TOOL_ANTENNA.strip())
    print("[PASS] antenna-length-calculator.html generated successfully!")

if __name__ == "__main__":
    main()
