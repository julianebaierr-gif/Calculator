"""
Generates capacitive-reactance-calculator.html and inductive-reactance-calculator.html
Each tool includes:
- 1,200+ words of deep engineering content
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
# 1. CAPACITIVE REACTANCE CALCULATOR
# ==========================================
TOOL_XC = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Capacitive Reactance Calculator — AC Impedance (Xc) &amp; Frequency</title>
  <meta name="description" content="Calculate capacitive reactance (Xc in Ohms), AC circuit impedance, and phase angle from alternating frequency and capacitance using exact Ohm formulas.">
  <meta name="keywords" content="capacitive reactance calculator, calculate capacitive reactance, xc calculator, capacitance reactance formula, ac capacitor impedance, cut off frequency rc, 1 over 2 pi f c">
  <link rel="canonical" href="https://calchub.org/capacitive-reactance-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Capacitive Reactance & AC Impedance Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates capacitive reactance Xc in Ohms, reactive power VARs, AC current, and cutoff frequency for electronic filter networks."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is capacitive reactance (Xc) in an AC electrical circuit?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Capacitive reactance (symbol Xc) is the opposition offered by a capacitor to the flow of sinusoidal alternating current (AC). Unlike pure resistance which dissipates electrical energy irrevocably as thermal heat, capacitive reactance stores energy temporarily in an electrostatic dielectric field and returns it back to the circuit during alternate quarter cycles, introducing a 90° leading phase shift between current and voltage."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for calculating capacitive reactance?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Capacitive reactance is calculated using the reciprocal relationship: Xc = 1 / (2 × π × f × C) = 1 / (ω × C), where Xc is reactance in Ohms (Ω), f is AC frequency in Hertz (Hz), C is capacitance in Farads (F), and ω is angular frequency in radians per second (2πf). As frequency increases, capacitive reactance decreases toward zero (high frequencies pass easily); as frequency approaches zero (DC), capacitive reactance approaches infinity (capacitors block DC entirely)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the phase angle relationship between current and voltage across a capacitor?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a purely capacitive AC circuit, electric current leads voltage by exactly 90 degrees (or π/2 radians), memorized in electrical engineering by the classic mnemonic 'ICE' (in a Capacitor C, current I leads electromotive force E). In complex impedance notation, capacitive impedance is written as: Zc = -j × Xc = 1 / (j × ω × C), where the negative imaginary operator -j denotes a -90° potential phase lag."
            }
          },
          {
            "@type": "Question",
            "name": "How does capacitive reactance determine RC filter cutoff frequency?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a simple passive RC low-pass or high-pass filter, the half-power cutoff frequency (fc or -3dB point) occurs at the exact frequency where capacitive reactance equals resistance: Xc = R. Substituting the reactance formula gives: 1 / (2π × fc × C) = R, which solves directly to: fc = 1 / (2 × π × R × C). At this critical frequency, output signal power drops by exactly 50% and output voltage drops to 70.7% (1/√2) of input."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body class="cat-theme-engineering">

  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="engineering.html" class="nav-link active">⚡ Electrical</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
        </div>
        <div class="nav-row">
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="fire-safety.html" class="nav-link">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>

  <div class="calc-page-header">
    <div class="calc-page-header-inner">
      <span class="category-tag">⚡ AC Circuit Analysis &amp; Reactive Impedance</span>
      <h1 class="calc-page-title">Capacitive Reactance Calculator</h1>
      <p class="calc-page-desc">Calculate capacitive reactance (Xc in Ohms), complex AC impedance, RMS current, and reactive VAR power across frequency spectra from power grids to radio frequencies.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>⚡</span> AC Frequency &amp; Capacitance Inputs</h2>
            <span class="status-info">Xc = 1 / (2πfC)</span>
          </div>
          <form id="xc-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="ac-frequency">AC Signal Frequency ($f$)</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="ac-frequency" class="form-control" value="60" min="0.0001" max="1000000000" step="1" oninput="runXcCalc()">
                  <select id="unit-freq" class="form-control" style="width:110px;" onchange="runXcCalc()">
                    <option value="1" selected>Hz</option>
                    <option value="1000">kHz</option>
                    <option value="1000000">MHz</option>
                    <option value="1000000000">GHz</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label class="form-label" for="cap-val">Capacitance ($C$)</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="cap-val" class="form-control" value="10" min="0.0001" max="10000000" step="0.1" oninput="runXcCalc()">
                  <select id="unit-cap" class="form-control" style="width:110px;" onchange="runXcCalc()">
                    <option value="1e-6" selected>μF</option>
                    <option value="1e-9">nF</option>
                    <option value="1e-12">pF</option>
                    <option value="1">Farads (F)</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="ac-voltage">Applied AC RMS Voltage ($V_{rms}$)</label>
                <input type="number" id="ac-voltage" class="form-control" value="120" min="0.1" max="1000000" step="1" oninput="runXcCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="preset-freq">Common Application Presets</label>
                <select id="preset-freq" class="form-control" onchange="applyXcPreset()">
                  <option value="custom" selected>-- Select Frequency Preset --</option>
                  <option value="60">60 Hz (North American AC Mains)</option>
                  <option value="50">50 Hz (European / Asian AC Mains)</option>
                  <option value="1000">1 kHz (Audio Reference Frequency)</option>
                  <option value="100000">100 kHz (SMPS Switch-Mode Power Supply)</option>
                  <option value="10000000">10 MHz (High-Frequency RF Circuit)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runXcCalc()">Calculate Capacitive Reactance</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print AC Analysis Report</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Capacitive Reactance &amp; AC Response</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Capacitive Reactance ($X_c$)</div>
            <div id="res-xc-primary" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">265.3 Ω</div>
            <div id="res-impedance-complex" style="font-size:1.05rem;color:#2563EB;font-weight:700;">Complex Impedance: Z_c = 0 - j265.3 Ω (Phase: -90°)</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">RMS Alternating Current ($I_{rms}$)</span>
              <span id="res-rms-current" class="result-val" style="font-size:1.1rem;font-weight:700;color:#059669;">0.452 Amperes</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Reactive Power ($Q_c$)</span>
              <span id="res-reactive-power" class="result-val" style="font-size:1.1rem;font-weight:700;color:#DC2626;">54.28 VAR</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Angular Frequency ($\omega = 2\pi f$)</span>
              <span id="res-omega-val" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">377.0 rad/s</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Susceptance ($B_c = 1 / X_c$)</span>
              <span id="res-susceptance" class="result-val" style="font-size:1.1rem;font-weight:700;color:#7C3AED;">3.77 mS (Siemens)</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:0.85rem;color:#166534;">
            <strong>⚡ AC Engineering Tools:</strong> Calculate industrial capacitor bank sizing with our <a href="power-factor-calculator.html" style="color:#166534;font-weight:700;">Power Factor Calculator</a>, solve parallel branches with the <a href="parallel-resistor-calculator.html" style="color:#166534;font-weight:700;">Parallel Resistor Calculator</a>, or verify series drop with the <a href="ohms-law-calculator.html" style="color:#166534;font-weight:700;">Ohm's Law Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Physics of Capacitors in Alternating Current (AC) Circuits</h2>
        <p>In direct current (DC) circuits, a capacitor acts as an absolute open-circuit insulator. Once its parallel conducting plates charge to the applied supply voltage ($Q = C \cdot V$), current ceases entirely. In alternating current (AC) circuits, however, the continuous sinusoidal reversal of polarity forces charge carriers to repeatedly flow back and forth between the opposing plates. Although no physical electrons cross the non-conductive dielectric barrier, the continuous displacement current through external leads allows AC current to flow unimpeded.</p>

        <p>The opposition that a capacitor presents to this dynamic alternating current flow is termed <strong>capacitive reactance ($X_c$)</strong>. Unlike an ohmic resistor, which irreversibly converts electrical energy into heat dissipation via Joule heating ($P = I^2 R$), a reactive capacitor is an ideal energy storage component. During the voltage buildup quadrant, energy is absorbed from the power source and stored electrostatically inside the dielectric field ($E = \frac{1}{2} C V^2$). When the AC voltage wave collapses, this stored electric energy is discharged back into the power grid, resulting in a net real power dissipation of exactly zero Watts in an ideal capacitor.</p>

        <h2>Mathematical Formulations of Capacitive Reactance</h2>

        <h3>1. The Fundamental Reactance Equation</h3>
        <p>The time-domain current flowing through a capacitor is proportional to the time rate of change of voltage across its terminals:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$i(t) = C \cdot \frac{dv(t)}{dt}$$
        </div>
        <p>For a sinusoidal voltage $v(t) = V_m \sin(\omega t)$, differentiating with respect to time yields:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$i(t) = C \cdot \frac{d}{dt}[V_m \sin(\omega t)] = \omega C V_m \cos(\omega t) = \omega C V_m \sin\left(\omega t + 90^\circ\right)$$
        </div>
        <p>Dividing peak voltage by peak current gives the magnitude of opposition, defining <strong>capacitive reactance ($X_c$)</strong>:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$X_c = \frac{V_m}{I_m} = \frac{1}{\omega C} = \frac{1}{2 \cdot \pi \cdot f \cdot C}$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$X_c$</strong> = Capacitive reactance measured in Ohms ($\Omega$).</li>
          <li><strong>$f$</strong> = Cyclic AC frequency in Hertz ($\text{Hz}$).</li>
          <li><strong>$\omega$</strong> = Angular frequency in radians per second ($\text{rad/s}$), where $\omega = 2\pi f$.</li>
          <li><strong>$C$</strong> = Capacitance in Farads ($\text{F}$).</li>
        </ul>

        <h3>2. Frequency Dependency: High-Pass vs Low-Pass Behavior</h3>
        <p>Because frequency ($f$) sits in the denominator, capacitive reactance is strictly <strong>inversely proportional</strong> to frequency:</p>
        <ul>
          <li><strong>At Zero Frequency ($f \to 0\text{ Hz}$, DC):</strong> $X_c \to \infty\text{ }\Omega$. A capacitor represents an infinite impedance, functioning as a DC blocking filter.</li>
          <li><strong>At Infinite Frequency ($f \to \infty\text{ Hz}$):</strong> $X_c \to 0\text{ }\Omega$. A capacitor represents a dead electrical short circuit to high-frequency transients, acting as an RF bypass element.</li>
        </ul>

        <h3>3. Phasor Representation &amp; Complex Impedance ($Z_c$)</h3>
        <p>Because the current wave leads voltage by $90^\circ$ ($\frac{\pi}{2}$ radians), capacitive impedance in the complex frequency domain ($s = j\omega$) is expressed with a negative imaginary operator:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #DC2626;">
          $$Z_c = -j X_c = \frac{1}{j \omega C} = X_c \angle -90^\circ$$
        </div>

        <h2>Capacitive Reactance ($X_c$) Multi-Frequency Lookup Table</h2>
        <p>The following table demonstrates how standard capacitor values scale in reactance across common engineering frequencies:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Capacitance</th>
                <th style="padding:0.75rem;">60 Hz (Mains Grid)</th>
                <th style="padding:0.75rem;">1 kHz (Audio Mid)</th>
                <th style="padding:0.75rem;">100 kHz (SMPS DC-DC)</th>
                <th style="padding:0.75rem;">10 MHz (HF Radio)</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>100 pF (Ceramic Disc)</strong></td>
                <td style="padding:0.75rem;">26.53 MΩ</td>
                <td style="padding:0.75rem;">1.59 MΩ</td>
                <td style="padding:0.75rem;">15.92 kΩ</td>
                <td style="padding:0.75rem;">159.2 Ω</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>1 nF / 0.001 μF (Film)</strong></td>
                <td style="padding:0.75rem;">2.65 MΩ</td>
                <td style="padding:0.75rem;">159.2 kΩ</td>
                <td style="padding:0.75rem;">1.59 kΩ</td>
                <td style="padding:0.75rem;">15.92 Ω</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>100 nF / 0.1 μF (Bypass)</strong></td>
                <td style="padding:0.75rem;">26.53 kΩ</td>
                <td style="padding:0.75rem;">1.59 kΩ</td>
                <td style="padding:0.75rem;">15.92 Ω</td>
                <td style="padding:0.75rem;">0.159 Ω</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>10 μF (Tantalum/SMD)</strong></td>
                <td style="padding:0.75rem;">265.3 Ω</td>
                <td style="padding:0.75rem;">15.92 Ω</td>
                <td style="padding:0.75rem;">0.159 Ω</td>
                <td style="padding:0.75rem;">0.0016 Ω</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>100 μF (Electrolytic)</strong></td>
                <td style="padding:0.75rem;">26.53 Ω</td>
                <td style="padding:0.75rem;">1.59 Ω</td>
                <td style="padding:0.75rem;">0.016 Ω</td>
                <td style="padding:0.75rem;">Inductive parasitic</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: Audio Preamplifier DC Blocking
          </h3>
          <p><strong>Scenario:</strong> An analog audio engineer is designing a preamplifier input stage. The amplifier has an input impedance of $R_{\text{in}} = 47\text{ k}\Omega$ and requires a series DC blocking coupling capacitor to pass the human hearing lower limit of $f = 20\text{ Hz}$ with less than $1.0\text{ dB}$ attenuation ($X_c \le 0.1 \times R_{\text{in}} \approx 4,700\text{ }\Omega$). The engineer tests a standard $4.7\text{ }\mu\text{F}$ film capacitor.</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Calculate Angular Frequency ($\omega$):</strong>
              $$\omega = 2 \cdot \pi \cdot f = 2 \times 3.14159 \times 20\text{ Hz} = 125.66\text{ rad/s}$$
            </li>
            <li><strong>Calculate Capacitive Reactance ($X_c$) at 20 Hz:</strong>
              $$X_c = \frac{1}{2 \pi \cdot f \cdot C} = \frac{1}{125.66 \times (4.7 \times 10^{-6}\text{ F})} = \frac{1}{0.0005906} \approx 1,693.2\text{ }\Omega$$
            </li>
            <li><strong>Check Attenuation Ratio:</strong>
              Because $X_c = 1,693\text{ }\Omega$ is significantly less than the $4,700\text{ }\Omega$ upper threshold ($X_c \approx 3.6\%$ of $R_{\text{in}}$), the voltage divider drop across the capacitor is negligible:
              $$\frac{V_{\text{out}}}{V_{\text{in}}} = \frac{R_{\text{in}}}{\sqrt{R_{\text{in}}^2 + X_c^2}} = \frac{47,000}{\sqrt{(47,000)^2 + (1,693)^2}} = \frac{47,000}{47,030.5} \approx 0.9993\text{ } (-0.006\text{ dB})$$
            </li>
            <li><strong>Determine -3dB Cutoff Frequency ($f_c$):</strong>
              $$f_c = \frac{1}{2 \pi \cdot R_{\text{in}} \cdot C} = \frac{1}{2 \times 3.14159 \times 47,000 \times 4.7 \times 10^{-6}} \approx 0.72\text{ Hz}$$
              The low cutoff of $0.72\text{ Hz}$ guarantees ruler-flat audio bass response down to $20\text{ Hz}$.
            </li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is the difference between capacitive reactance (Xc) and resistance (R)?</h4>
            <p style="margin:0;color:#64748B;">Resistance (R) dissipates real electrical energy as irreversible heat (Watts) and maintains an in-phase relationship between current and voltage (0° phase shift). Capacitive reactance (Xc) does not dissipate power; it temporarily stores energy in an electric field (VARs) and introduces a 90° leading phase shift where current peaks a quarter-cycle ahead of voltage.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why do real-world capacitors behave like inductors at very high frequencies?</h4>
            <p style="margin:0;color:#64748B;">All physical capacitors have parasitic lead inductance and internal foil winding inductance (Equivalent Series Inductance, or ESL). While capacitive reactance drops with frequency, inductive reactance (XL = 2πfL) rises with frequency. At the Self-Resonant Frequency (SRF), Xc equals XL. Above the SRF, the inductive reactance dominates, and the capacitor ceases to function as a capacitor, behaving entirely as an inductor.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">How does capacitive reactance improve power factor in industrial facilities?</h4>
            <p style="margin:0;color:#64748B;">Industrial induction motors and transformers operate with lagging power factors because their magnetic fields draw lagging inductive current (voltage leads current by +90°). Shunt capacitor banks introduce leading capacitive current (current leads voltage by +90°). The two opposite 180° out-of-phase reactive currents cancel each other out algebraically, eliminating reactive kVAR draw from the utility grid.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is Equivalent Series Resistance (ESR) in a capacitor?</h4>
            <p style="margin:0;color:#64748B;">ESR represents real resistive losses inside the capacitor, including electrolyte resistance, lead wire resistance, and dielectric absorption losses. In switch-mode power supplies, high-frequency AC ripple currents flowing through the capacitor's ESR generate internal I²R heating, which can boil liquid electrolytes and cause capacitor bulging or explosion.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ AC Circuit &amp; Impedance Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="capacitive-reactance-calculator.html" style="font-weight:700;color:#2563EB;">⚡ Capacitive Reactance (Xc)</a></li>
          <li><a href="inductive-reactance-calculator.html" style="color:#475569;">🌀 Inductive Reactance (Xl)</a></li>
          <li><a href="power-factor-calculator.html" style="color:#475569;">⚡ Power Factor Correction</a></li>
          <li><a href="ohms-law-calculator.html" style="color:#475569;">⚡ Ohm's Law Calculator</a></li>
          <li><a href="parallel-resistor-calculator.html" style="color:#475569;">⚡ Parallel Resistor (Req)</a></li>
          <li><a href="555-timer-calculator.html" style="color:#475569;">⏱️ 555 Timer Calculator</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Power Systems Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="short-circuit-calculator.html" style="color:#475569;">💥 Short-Circuit (IEC 60909)</a></li>
          <li><a href="transformer-sizing-calculator.html" style="color:#475569;">⚡ Transformer Sizing</a></li>
          <li><a href="wire-ampacity-calculator.html" style="color:#475569;">🔌 Wire Ampacity (NEC)</a></li>
        </ul>
      </div>
    </aside>

  </div>

  <footer class="site-footer" style="background:#0F172A;color:#94A3B8;padding:3rem 1.25rem;margin-top:4rem;">
    <div style="max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;flex-wrap:wrap;gap:2rem;">
      <div>
        <div style="font-size:1.25rem;font-weight:800;color:#FFFFFF;margin-bottom:0.5rem;">CalcHub</div>
        <p style="font-size:0.88rem;max-width:320px;">Open-source engineering, financial, and scientific computational tools. 100% verified mathematics.</p>
      </div>
      <div>
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">AC Network Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          IEEE 1459 Standard Definitions for Electric Power<br>
          IEC 60384 Fixed Capacitors for Electronic Equipment<br>
          EIA-198 Ceramic Dielectric Capacitors
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional AC Circuit &amp; Impedance Computational Suite.
    </div>
  </footer>

  <script>
    function applyXcPreset() {
      const val = document.getElementById('preset-freq').value;
      if (val !== 'custom') {
        const num = parseFloat(val);
        if (num >= 1e6) {
          document.getElementById('ac-frequency').value = num / 1e6;
          document.getElementById('unit-freq').value = '1000000';
        } else if (num >= 1e3) {
          document.getElementById('ac-frequency').value = num / 1e3;
          document.getElementById('unit-freq').value = '1000';
        } else {
          document.getElementById('ac-frequency').value = num;
          document.getElementById('unit-freq').value = '1';
        }
      }
      runXcCalc();
    }

    function runXcCalc() {
      const fVal = Math.max(1e-6, parseFloat(document.getElementById('ac-frequency').value) || 60);
      const fMult = parseFloat(document.getElementById('unit-freq').value) || 1;
      const freq = fVal * fMult; // in Hz

      const cVal = Math.max(1e-18, parseFloat(document.getElementById('cap-val').value) || 10);
      const cMult = parseFloat(document.getElementById('unit-cap').value) || 1e-6;
      const cap = cVal * cMult; // in Farads

      const vRms = Math.max(0.001, parseFloat(document.getElementById('ac-voltage').value) || 120);

      // Xc = 1 / (2 * pi * f * C)
      const omega = 2 * Math.PI * freq;
      const xc = 1.0 / (omega * cap);

      const iRms = vRms / xc;
      const qVar = vRms * iRms;
      const susceptance = 1.0 / xc; // in Siemens

      let xcStr = '';
      if (xc >= 1e6) xcStr = (xc / 1e6).toFixed(2) + ' M\u03A9';
      else if (xc >= 1e3) xcStr = (xc / 1e3).toFixed(2) + ' k\u03A9 (' + Math.round(xc) + ' \u03A9)';
      else if (xc >= 1) xcStr = xc.toFixed(2) + ' \u03A9';
      else xcStr = (xc * 1000).toFixed(2) + ' m\u03A9';

      let currStr = '';
      if (iRms >= 1000) currStr = (iRms / 1000).toFixed(2) + ' kA';
      else if (iRms >= 1) currStr = iRms.toFixed(3) + ' Amperes';
      else if (iRms >= 1e-3) currStr = (iRms * 1e3).toFixed(2) + ' mA';
      else currStr = (iRms * 1e6).toFixed(2) + ' \u03bcA';

      let varStr = '';
      if (qVar >= 1e6) varStr = (qVar / 1e6).toFixed(2) + ' MVAR';
      else if (qVar >= 1e3) varStr = (qVar / 1e3).toFixed(2) + ' kVAR';
      else varStr = qVar.toFixed(2) + ' VAR';

      let suscStr = '';
      if (susceptance >= 1) suscStr = susceptance.toFixed(3) + ' S';
      else if (susceptance >= 1e-3) suscStr = (susceptance * 1e3).toFixed(2) + ' mS';
      else suscStr = (susceptance * 1e6).toFixed(2) + ' \u03bcS';

      document.getElementById('res-xc-primary').textContent = xcStr;
      document.getElementById('res-impedance-complex').textContent = 'Complex Impedance: Z_c = 0 - j' + (xc >= 1000 ? (xc/1000).toFixed(2) + 'k' : xc.toFixed(1)) + ' \u03A9 (Phase: -90\u00B0)';
      document.getElementById('res-rms-current').textContent = currStr;
      document.getElementById('res-reactive-power').textContent = varStr;
      document.getElementById('res-omega-val').textContent = omega >= 1e6 ? (omega / 1e6).toFixed(2) + ' Mrad/s' : omega.toFixed(1) + ' rad/s';
      document.getElementById('res-susceptance').textContent = suscStr;
    }

    window.addEventListener('DOMContentLoaded', runXcCalc);
  </script>
</body>
</html>
"""

# ==========================================
# 2. INDUCTIVE REACTANCE CALCULATOR
# ==========================================
TOOL_XL = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Inductive Reactance Calculator — AC Impedance (Xl) &amp; Frequency</title>
  <meta name="description" content="Calculate inductive reactance (Xl in Ohms), coil impedance, and phase angle from alternating frequency and inductance using exact Ohm formulas.">
  <meta name="keywords" content="inductive reactance calculator, calculate inductive reactance, xl calculator, inductance reactance formula, ac inductor impedance, coil reactance 2 pi f l, back emf inductor">
  <link rel="canonical" href="https://calchub.org/inductive-reactance-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Inductive Reactance & AC Coil Impedance Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates inductive reactance Xl in Ohms, RMS current, reactive VAR power, and complex phase angle for inductors and chokes."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is inductive reactance (Xl) in an AC electrical circuit?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Inductive reactance (symbol Xl) is the opposition offered by an inductor or coil to the flow of sinusoidal alternating current. Per Faraday's and Lenz's laws of electromagnetic induction, a changing current generates a varying magnetic flux in the core, inducing a counter-electromotive force (back-EMF) that opposes the rate of change of current, introducing a 90° lagging phase shift between current and voltage."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for calculating inductive reactance?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Inductive reactance is calculated using: Xl = 2 × π × f × L = ω × L, where Xl is reactance in Ohms (Ω), f is AC frequency in Hertz (Hz), L is inductance in Henrys (H), and ω is angular frequency in radians per second (2πf). Inductive reactance is directly proportional to both frequency and inductance: higher frequencies encounter greater opposition."
            }
          },
          {
            "@type": "Question",
            "name": "What is the phase angle relationship in a pure inductor?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a pure inductor, voltage leads current by exactly 90 degrees (or π/2 radians), memorized by the classic engineering mnemonic 'ELI' (Electromotive force E leads current I in an Inductor L). In complex phasor notation, inductive impedance is expressed as: Zl = +j × Xl = j × ω × L, where +j denotes a positive 90° phase advance of voltage over current."
            }
          },
          {
            "@type": "Question",
            "name": "How does an inductor behave at DC versus high RF frequencies?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "At direct current (DC, f = 0 Hz), inductive reactance is zero (Xl = 0 Ω), meaning an ideal inductor behaves as a dead short circuit, opposing flow only with its tiny DC wire resistance (DCR). As frequency increases toward radio frequencies (MHz), Xl skyrockets into thousands of Ohms, allowing inductors to act as RF chokes that block high-frequency noise while passing DC and low-frequency signals without attenuation."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body class="cat-theme-engineering">

  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="engineering.html" class="nav-link active">⚡ Electrical</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
        </div>
        <div class="nav-row">
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="fire-safety.html" class="nav-link">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>

  <div class="calc-page-header">
    <div class="calc-page-header-inner">
      <span class="category-tag">⚡ AC Magnetic Induction &amp; Coil Impedance</span>
      <h1 class="calc-page-title">Inductive Reactance Calculator</h1>
      <p class="calc-page-desc">Calculate inductive reactance (Xl in Ohms), complex AC impedance, RMS current, and reactive inductive VAR power across frequency ranges from power grids to radio frequency chokes.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>🌀</span> AC Frequency &amp; Inductance Parameters</h2>
            <span class="status-info">Xl = 2πfL</span>
          </div>
          <form id="xl-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="ac-frequency-l">AC Signal Frequency ($f$)</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="ac-frequency-l" class="form-control" value="60" min="0.0001" max="1000000000" step="1" oninput="runXlCalc()">
                  <select id="unit-freq-l" class="form-control" style="width:110px;" onchange="runXlCalc()">
                    <option value="1" selected>Hz</option>
                    <option value="1000">kHz</option>
                    <option value="1000000">MHz</option>
                    <option value="1000000000">GHz</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label class="form-label" for="ind-val">Inductance ($L$)</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="ind-val" class="form-control" value="100" min="0.0001" max="1000000" step="1" oninput="runXlCalc()">
                  <select id="unit-ind" class="form-control" style="width:110px;" onchange="runXlCalc()">
                    <option value="0.001" selected>mH</option>
                    <option value="1e-6">μH</option>
                    <option value="1">Henrys (H)</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="ac-voltage-l">Applied AC RMS Voltage ($V_{rms}$)</label>
                <input type="number" id="ac-voltage-l" class="form-control" value="120" min="0.1" max="1000000" step="1" oninput="runXlCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="preset-freq-l">Common Application Presets</label>
                <select id="preset-freq-l" class="form-control" onchange="applyXlPreset()">
                  <option value="custom" selected>-- Select Frequency Preset --</option>
                  <option value="60">60 Hz (North American AC Mains)</option>
                  <option value="50">50 Hz (European / Asian AC Mains)</option>
                  <option value="1000">1 kHz (Audio Midrange Crossover)</option>
                  <option value="100000">100 kHz (Switch-Mode Buck Choke)</option>
                  <option value="10000000">10 MHz (RF Choke / Filter)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runXlCalc()">Calculate Inductive Reactance</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Inductor Analysis</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Inductive Reactance &amp; Coil Impedance</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Inductive Reactance ($X_l$)</div>
            <div id="res-xl-primary" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">37.70 Ω</div>
            <div id="res-impedance-complex-l" style="font-size:1.05rem;color:#2563EB;font-weight:700;">Complex Impedance: Z_l = 0 + j37.70 Ω (Phase: +90°)</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">RMS Alternating Current ($I_{rms}$)</span>
              <span id="res-rms-current-l" class="result-val" style="font-size:1.1rem;font-weight:700;color:#059669;">3.183 Amperes</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Reactive Power ($Q_l$)</span>
              <span id="res-reactive-power-l" class="result-val" style="font-size:1.1rem;font-weight:700;color:#DC2626;">381.9 VAR</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Angular Frequency ($\omega = 2\pi f$)</span>
              <span id="res-omega-val-l" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">377.0 rad/s</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Magnetic Energy Stored ($E_L$)</span>
              <span id="res-magnetic-energy" class="result-val" style="font-size:1.1rem;font-weight:700;color:#7C3AED;">1.01 Joules (Peak)</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:0.85rem;color:#166534;">
            <strong>⚡ AC Engineering Tools:</strong> Compare with dual capacitor networks using our <a href="capacitive-reactance-calculator.html" style="color:#166534;font-weight:700;">Capacitive Reactance Calculator</a>, size industrial power factors with the <a href="power-factor-calculator.html" style="color:#166534;font-weight:700;">Power Factor Calculator</a>, or verify basic AC drop with the <a href="ohms-law-calculator.html" style="color:#166534;font-weight:700;">Ohm's Law Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Physics of Inductors &amp; Electromagnetic Back-EMF in AC Circuits</h2>
        <p>An electrical inductor consists of a conducting coil of insulated wire wound around an air or ferromagnetic core (such as iron powder, silicon steel laminations, or ferrite). When electric current passes through the coil, Ampere's circuital law dictates that a proportional magnetic flux ($\Phi = B \cdot A$) is generated within the core. In a steady DC state, this magnetic field remains constant once established, and the inductor behaves simply as an ordinary low-resistance wire.</p>

        <p>In an alternating current (AC) circuit, however, the continuous sinusoidal oscillation of current forces the magnetic flux to continually expand, collapse, and reverse direction. Under <strong>Faraday's Law of Electromagnetic Induction</strong>, this time-varying magnetic flux induces an electromotive force (EMF) across the coil windings:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$v(t) = L \cdot \frac{di(t)}{dt}$$
        </div>
        <p>Under <strong>Lenz's Law</strong>, the polarity of this self-induced counter-electromotive force (back-EMF) always opposes the instantaneous change in current that produced it. The faster the current attempts to oscillate (higher frequency), the greater the rate of change ($\frac{di}{dt}$), and the larger the counter-voltage generated by the coil to resist current flow. This opposition is defined as <strong>inductive reactance ($X_l$)</strong>.</p>

        <h2>Mathematical Formulations of Inductive Reactance</h2>

        <h3>1. The Fundamental Reactance Equation</h3>
        <p>Assuming a sinusoidal current $i(t) = I_m \sin(\omega t)$ flows through an ideal inductor of inductance $L$ Henrys, the induced voltage drop across the inductor is:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$v(t) = L \cdot \frac{d}{dt}[I_m \sin(\omega t)] = \omega L I_m \cos(\omega t) = \omega L I_m \sin\left(\omega t + 90^\circ\right)$$
        </div>
        <p>Dividing peak voltage ($V_m = \omega L I_m$) by peak current ($I_m$) defines the magnitude of opposition, <strong>inductive reactance ($X_l$)</strong>:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$X_l = \omega L = 2 \cdot \pi \cdot f \cdot L$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$X_l$</strong> = Inductive reactance in Ohms ($\Omega$).</li>
          <li><strong>$f$</strong> = AC frequency in Hertz ($\text{Hz}$).</li>
          <li><strong>$\omega$</strong> = Angular frequency in radians per second ($\text{rad/s}$), where $\omega = 2\pi f$.</li>
          <li><strong>$L$</strong> = Inductance in Henrys ($\text{H}$).</li>
        </ul>

        <h3>2. Frequency Proportionality: Low-Pass vs RF Choke Behavior</h3>
        <p>Unlike capacitive reactance which is inversely proportional to frequency, inductive reactance is <strong>directly proportional</strong> to frequency:</p>
        <ul>
          <li><strong>At Zero Frequency ($f \to 0\text{ Hz}$, DC):</strong> $X_l = 0\text{ }\Omega$. An ideal inductor offers zero inductive reactance, presenting only its minimal DC winding resistance (DCR).</li>
          <li><strong>At High Frequencies ($f \to \infty\text{ Hz}$):</strong> $X_l \to \infty\text{ }\Omega$. An inductor presents massive impedance, functioning as a high-frequency filter (choke) that eliminates RF interference, switching ripple, and electromagnetic interference (EMI).</li>
        </ul>

        <h3>3. Phasor Representation &amp; Complex Impedance ($Z_l$)</h3>
        <p>Because the voltage waveform leads the current waveform by exactly $+90^\circ$ ($\frac{\pi}{2}$ radians), inductive impedance in the complex frequency domain ($s = j\omega$) is represented with a positive imaginary operator:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #DC2626;">
          $$Z_l = +j X_l = j \omega L = X_l \angle +90^\circ$$
        </div>

        <h2>Inductive Reactance ($X_l$) Across Common Frequencies Table</h2>
        <p>The following table demonstrates how standard inductor values scale in reactance across common engineering frequencies:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Inductance ($L$)</th>
                <th style="padding:0.75rem;">60 Hz (Power Line)</th>
                <th style="padding:0.75rem;">1 kHz (Audio)</th>
                <th style="padding:0.75rem;">100 kHz (Switching SMPS)</th>
                <th style="padding:0.75rem;">10 MHz (RF Circuit)</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>10 μH (SMD Choke)</strong></td>
                <td style="padding:0.75rem;">0.0038 Ω</td>
                <td style="padding:0.75rem;">0.0628 Ω</td>
                <td style="padding:0.75rem;">6.28 Ω</td>
                <td style="padding:0.75rem;">628.3 Ω</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>100 μH (Power Inductor)</strong></td>
                <td style="padding:0.75rem;">0.0377 Ω</td>
                <td style="padding:0.75rem;">0.628 Ω</td>
                <td style="padding:0.75rem;">62.83 Ω</td>
                <td style="padding:0.75rem;">6.28 kΩ</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>1 mH (Filter Choke)</strong></td>
                <td style="padding:0.75rem;">0.377 Ω</td>
                <td style="padding:0.75rem;">6.28 Ω</td>
                <td style="padding:0.75rem;">628.3 Ω</td>
                <td style="padding:0.75rem;">62.83 kΩ</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>10 mH (Audio Crossover)</strong></td>
                <td style="padding:0.75rem;">3.77 Ω</td>
                <td style="padding:0.75rem;">62.83 Ω</td>
                <td style="padding:0.75rem;">6.28 kΩ</td>
                <td style="padding:0.75rem;">Inter-winding capacitance</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>1 Henry (Iron Core Choke)</strong></td>
                <td style="padding:0.75rem;">376.99 Ω</td>
                <td style="padding:0.75rem;">6.28 kΩ</td>
                <td style="padding:0.75rem;">628.3 kΩ</td>
                <td style="padding:0.75rem;">Severe self-resonance</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: 100 kHz Switch-Mode Buck Inductor
          </h3>
          <p><strong>Scenario:</strong> A power supply design engineer is sizing a buck regulator LC output filter operating at a switching frequency of $f = 100\text{ kHz}$ ($100,000\text{ Hz}$). The designer specifies a $22\text{ }\mu\text{H}$ toroidal ferrite power inductor. The circuit operates at $12\text{V}$ output with an allowable peak-to-peak AC ripple voltage of $V_{\text{ripple, rms}} = 0.5\text{ V}$.</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Calculate Angular Frequency ($\omega$):</strong>
              $$\omega = 2 \cdot \pi \cdot f = 2 \times 3.14159 \times 100,000\text{ Hz} \approx 628,318\text{ rad/s}$$
            </li>
            <li><strong>Calculate Inductive Reactance ($X_l$):</strong>
              $$X_l = 2 \pi \cdot f \cdot L = 628,318 \times (22 \times 10^{-6}\text{ H}) \approx 13.82\text{ }\Omega$$
            </li>
            <li><strong>Determine AC Ripple Current ($I_{\text{ripple}}$):</strong>
              $$I_{\text{ripple, rms}} = \frac{V_{\text{ripple, rms}}}{X_l} = \frac{0.5\text{ V}}{13.82\text{ }\Omega} \approx 0.0362\text{ A} = 36.2\text{ mA}$$
            </li>
            <li><strong>Calculate Peak Stored Magnetic Energy ($E_L$):</strong>
              If the inductor carries a continuous DC load current of $I_{\text{DC}} = 3.0\text{ A}$:
              $$E_L = \frac{1}{2} \cdot L \cdot I_{\text{peak}}^2 = \frac{1}{2} \times 22 \times 10^{-6}\text{ H} \times (3.05\text{ A})^2 \approx 1.023 \times 10^{-4}\text{ Joules} = 102.3\text{ }\mu\text{J}$$
            </li>
            <li><strong>Engineering Verification:</strong> The $13.82\text{ }\Omega$ impedance effectively suppresses high-frequency $100\text{ kHz}$ square wave harmonic current while presenting near-zero resistance ($DCR \approx 0.02\text{ }\Omega$) to the direct DC output current.</li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is the Quality Factor (Q) of an inductor?</h4>
            <p style="margin:0;color:#64748B;">The Quality Factor (Q) measures the efficiency of an inductor by comparing its stored magnetic inductive reactance to its internal dissipative resistance: Q = (ω × L) / R_series. A high Q factor (> 50 to 100) indicates a highly efficient coil that stores energy with minimal thermal loss, critical for sharp selectivity in RF bandpass filters and resonant tank circuits.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why do real-world inductors exhibit Self-Resonant Frequency (SRF)?</h4>
            <p style="margin:0;color:#64748B;">Coil windings consist of insulated turns placed in close physical proximity, creating parasitic inter-turn capacitance (Distributed Capacitance, C_p). At low frequencies, inductive reactance dominates (XL = 2πfL). As frequency climbs, capacitive reactance of the parasitic winding capacitance drops (Xc = 1/2πfCp). At the Self-Resonant Frequency (SRF = 1 / [2π√(L × Cp)]), XL equals Xc. Above this frequency, the inductor reverses its behavior and acts as a capacitor!</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is magnetic core saturation and how does it affect inductive reactance?</h4>
            <p style="margin:0;color:#64748B;">Ferromagnetic cores (ferrite, iron powder) can only align a finite number of magnetic domains. When current exceeds the saturation current rating (I_sat), the core's magnetic permeability (μ) drops abruptly toward the permeability of air (μ_0). As permeability collapses, inductance L plummets, causing inductive reactance Xl to instantly drop to zero, creating a destructive short circuit across power supply switches.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is the Skin Effect in high-frequency inductor windings?</h4>
            <p style="margin:0;color:#64748B;">As AC frequency rises, eddy currents induced within the conductor's own bulk force electron flow toward the outer perimeter (skin) of the wire, reducing the effective conducting cross-sectional area. This raises high-frequency AC resistance (R_ac), degrading the inductor's Q-factor. High-frequency inductors overcome skin effect using multistrand Litz wire, copper foil strips, or silver plating.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ AC Circuit &amp; Impedance Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="inductive-reactance-calculator.html" style="font-weight:700;color:#2563EB;">🌀 Inductive Reactance (Xl)</a></li>
          <li><a href="capacitive-reactance-calculator.html" style="color:#475569;">⚡ Capacitive Reactance (Xc)</a></li>
          <li><a href="power-factor-calculator.html" style="color:#475569;">⚡ Power Factor Correction</a></li>
          <li><a href="ohms-law-calculator.html" style="color:#475569;">⚡ Ohm's Law Calculator</a></li>
          <li><a href="parallel-resistor-calculator.html" style="color:#475569;">⚡ Parallel Resistor (Req)</a></li>
          <li><a href="motor-starting-current-calculator.html" style="color:#475569;">⚙️ Motor Starting Current</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Power Systems Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="short-circuit-calculator.html" style="color:#475569;">💥 Short-Circuit (IEC 60909)</a></li>
          <li><a href="transformer-sizing-calculator.html" style="color:#475569;">⚡ Transformer Sizing</a></li>
          <li><a href="voltage-drop-calculator.html" style="color:#475569;">📉 Voltage Drop Calculator</a></li>
        </ul>
      </div>
    </aside>

  </div>

  <footer class="site-footer" style="background:#0F172A;color:#94A3B8;padding:3rem 1.25rem;margin-top:4rem;">
    <div style="max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;flex-wrap:wrap;gap:2rem;">
      <div>
        <div style="font-size:1.25rem;font-weight:800;color:#FFFFFF;margin-bottom:0.5rem;">CalcHub</div>
        <p style="font-size:0.88rem;max-width:320px;">Open-source engineering, financial, and scientific computational tools. 100% verified mathematics.</p>
      </div>
      <div>
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">Electromagnetics Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          IEEE 389 Recommended Practice for Testing Inductors<br>
          IEC 60938 Fixed Inductors for Electromagnetic Interference<br>
          MIL-PRF-27 Transformers and Inductors General Specification
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Electromagnetic &amp; Coil Computational Suite.
    </div>
  </footer>

  <script>
    function applyXlPreset() {
      const val = document.getElementById('preset-freq-l').value;
      if (val !== 'custom') {
        const num = parseFloat(val);
        if (num >= 1e6) {
          document.getElementById('ac-frequency-l').value = num / 1e6;
          document.getElementById('unit-freq-l').value = '1000000';
        } else if (num >= 1e3) {
          document.getElementById('ac-frequency-l').value = num / 1e3;
          document.getElementById('unit-freq-l').value = '1000';
        } else {
          document.getElementById('ac-frequency-l').value = num;
          document.getElementById('unit-freq-l').value = '1';
        }
      }
      runXlCalc();
    }

    function runXlCalc() {
      const fVal = Math.max(1e-6, parseFloat(document.getElementById('ac-frequency-l').value) || 60);
      const fMult = parseFloat(document.getElementById('unit-freq-l').value) || 1;
      const freq = fVal * fMult; // in Hz

      const lVal = Math.max(1e-12, parseFloat(document.getElementById('ind-val').value) || 100);
      const lMult = parseFloat(document.getElementById('unit-ind').value) || 0.001;
      const ind = lVal * lMult; // in Henrys

      const vRms = Math.max(0.001, parseFloat(document.getElementById('ac-voltage-l').value) || 120);

      // Xl = 2 * pi * f * L
      const omega = 2 * Math.PI * freq;
      const xl = omega * ind;

      const iRms = vRms / xl;
      const qVar = vRms * iRms;
      const iPeak = iRms * Math.SQRT2;
      const eJoules = 0.5 * ind * (iPeak * iPeak);

      let xlStr = '';
      if (xl >= 1e6) xlStr = (xl / 1e6).toFixed(2) + ' M\u03A9';
      else if (xl >= 1e3) xlStr = (xl / 1e3).toFixed(2) + ' k\u03A9 (' + Math.round(xl) + ' \u03A9)';
      else if (xl >= 1) xlStr = xl.toFixed(2) + ' \u03A9';
      else xlStr = (xl * 1000).toFixed(2) + ' m\u03A9';

      let currStr = '';
      if (iRms >= 1000) currStr = (iRms / 1000).toFixed(2) + ' kA';
      else if (iRms >= 1) currStr = iRms.toFixed(3) + ' Amperes';
      else if (iRms >= 1e-3) currStr = (iRms * 1e3).toFixed(2) + ' mA';
      else currStr = (iRms * 1e6).toFixed(2) + ' \u03bcA';

      let varStr = '';
      if (qVar >= 1e6) varStr = (qVar / 1e6).toFixed(2) + ' MVAR';
      else if (qVar >= 1e3) varStr = (qVar / 1e3).toFixed(2) + ' kVAR';
      else varStr = qVar.toFixed(1) + ' VAR';

      let eStr = '';
      if (eJoules >= 1) eStr = eJoules.toFixed(2) + ' Joules (Peak)';
      else if (eJoules >= 1e-3) eStr = (eJoules * 1e3).toFixed(2) + ' mJ (Peak)';
      else eStr = (eJoules * 1e6).toFixed(1) + ' \u03bcJ (Peak)';

      document.getElementById('res-xl-primary').textContent = xlStr;
      document.getElementById('res-impedance-complex-l').textContent = 'Complex Impedance: Z_l = 0 + j' + (xl >= 1000 ? (xl/1000).toFixed(2) + 'k' : xl.toFixed(1)) + ' \u03A9 (Phase: +90\u00B0)';
      document.getElementById('res-rms-current-l').textContent = currStr;
      document.getElementById('res-reactive-power-l').textContent = varStr;
      document.getElementById('res-omega-val-l').textContent = omega >= 1e6 ? (omega / 1e6).toFixed(2) + ' Mrad/s' : omega.toFixed(1) + ' rad/s';
      document.getElementById('res-magnetic-energy').textContent = eStr;
    }

    window.addEventListener('DOMContentLoaded', runXlCalc);
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "capacitive-reactance-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_XC)
print("[PASS] capacitive-reactance-calculator.html generated successfully!")

with open(os.path.join(BASE_DIR, "inductive-reactance-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_XL)
print("[PASS] inductive-reactance-calculator.html generated successfully!")
