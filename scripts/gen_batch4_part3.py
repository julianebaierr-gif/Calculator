"""
Generates op-amp-gain-calculator.html and three-phase-power-calculator.html
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
# 1. OP AMP GAIN CALCULATOR
# ==========================================
TOOL_OPAMP = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Op Amp Gain Calculator — Inverting &amp; Non-Inverting Voltage Gain (dB)</title>
  <meta name="description" content="Calculate operational amplifier closed-loop voltage gain (Av), gain in decibels (dB), output voltage, and -3dB bandwidth from feedback resistor values.">
  <meta name="keywords" content="op amp gain calculator, operational amplifier gain, inverting op amp gain, non inverting op amp formula, op amp db calculator, gain bandwidth product gbwp, closed loop voltage gain">
  <link rel="canonical" href="https://calchub.org/op-amp-gain-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Operational Amplifier Closed-Loop Gain Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates inverting and non-inverting op-amp voltage gain, decibel magnitude, output voltage clipping, and closed-loop cutoff bandwidth."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the formula for inverting operational amplifier closed-loop gain?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In an inverting op-amp configuration, the non-inverting terminal is grounded, creating a virtual ground at the inverting node. Negative feedback current through Rf balances input current through Rin. The closed-loop voltage gain is: Av = -Rf / Rin. The negative sign denotes a 180° phase inversion between input and output. In decibels, gain is: Gain (dB) = 20 × log10(|Rf / Rin|)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for non-inverting operational amplifier closed-loop gain?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a non-inverting op-amp configuration, input signal is applied directly to the non-inverting terminal (+), providing near-infinite input impedance. Negative feedback resistors Rf and R1 form a voltage divider to the inverting input. The closed-loop voltage gain is: Av = 1 + (Rf / R1). Because the ratio (Rf / R1) is always positive, non-inverting gain can never be less than unity (Av ≥ 1), and output remains exactly in phase (0° shift) with input."
            }
          },
          {
            "@type": "Question",
            "name": "How does Gain-Bandwidth Product (GBWP) limit op-amp high-frequency performance?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Internally compensated op-amps exhibit a single-pole open-loop roll-off at -20 dB/decade (-6 dB/octave). The Gain-Bandwidth Product (GBWP) is constant: GBWP = Closed-Loop Gain (|Av|) × Closed-Loop Bandwidth (fc). For example, with an op-amp having a GBWP of 10 MHz (like the NE5532), configuring a circuit for a voltage gain of Av = 100 (40 dB) restricts its high-frequency -3dB cutoff bandwidth to: fc = 10 MHz / 100 = 100 kHz."
            }
          },
          {
            "@type": "Question",
            "name": "What causes operational amplifier output clipping and saturation?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "An op-amp cannot output a voltage greater than its DC power supply rails (V+ and V-). In standard bipolar op-amps (e.g., LM741, TL072), output voltage swings within approximately 1.5V to 2.0V of the rails due to internal transistor Vce saturation drops. Modern rail-to-rail op-amps can swing within millivolts of the supply rails. If calculated Vout = Vin × Av exceeds rail limits, the waveform clips flat, generating severe harmonic distortion."
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
      <span class="category-tag">⚡ Analog Signal Processing &amp; Linear Amplification</span>
      <h1 class="calc-page-title">Op Amp Gain Calculator</h1>
      <p class="calc-page-desc">Calculate operational amplifier closed-loop voltage gain (Av), decibel gain (dB), output signal amplitude, and -3dB frequency bandwidth for inverting and non-inverting configurations.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>🔬</span> Amplifier Topology &amp; Resistor Values</h2>
            <span class="status-info">Inverting / Non-Inverting</span>
          </div>
          <form id="opamp-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="amp-topology">Amplifier Configuration</label>
                <select id="amp-topology" class="form-control" onchange="runOpampCalc()">
                  <option value="inverting" selected>Inverting Amplifier (Av = -Rf / Rin · 180° Phase)</option>
                  <option value="non-inverting">Non-Inverting Amplifier (Av = 1 + Rf / R1 · 0° Phase)</option>
                  <option value="buffer">Voltage Follower / Unity Gain Buffer (Av = 1.0)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="input-voltage">Input Signal Voltage ($V_{in}$ in V)</label>
                <input type="number" id="input-voltage" class="form-control" value="0.100" min="-100" max="100" step="0.01" oninput="runOpampCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="res-rf">Feedback Resistor ($R_f$)</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="res-rf" class="form-control" value="100" min="0.01" max="100000" step="1" oninput="runOpampCalc()">
                  <select id="unit-rf" class="form-control" style="width:110px;" onchange="runOpampCalc()">
                    <option value="1000" selected>kΩ</option>
                    <option value="1">Ω</option>
                    <option value="1000000">MΩ</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label class="form-label" for="res-rin">Input / Ground Resistor ($R_{in}$ or $R_1$)</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="res-rin" class="form-control" value="10" min="0.01" max="100000" step="1" oninput="runOpampCalc()">
                  <select id="unit-rin" class="form-control" style="width:110px;" onchange="runOpampCalc()">
                    <option value="1000" selected>kΩ</option>
                    <option value="1">Ω</option>
                    <option value="1000000">MΩ</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="gbwp-mhz">Op-Amp Gain-Bandwidth Product (GBWP)</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="gbwp-mhz" class="form-control" value="10" min="0.01" max="10000" step="0.5" oninput="runOpampCalc()">
                  <select id="opamp-chip-preset" class="form-control" style="width:140px;" onchange="applyOpampChip()">
                    <option value="custom">Custom GBWP</option>
                    <option value="1.0">LM741 (1.0 MHz)</option>
                    <option value="3.0">TL072 / TL082 (3 MHz)</option>
                    <option value="10.0" selected>NE5532 (10 MHz)</option>
                    <option value="16.0">OPA2134 (16 MHz)</option>
                    <option value="0.6">LM358 (0.6 MHz)</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label class="form-label" for="supply-rail">Dual Supply Rails ($\pm V_{cc}$ in V)</label>
                <input type="number" id="supply-rail" class="form-control" value="15" min="1" max="50" step="1" oninput="runOpampCalc()">
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runOpampCalc()">Calculate Op-Amp Gain</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Circuit Datasheet</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Gain &amp; Small-Signal Performance</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Closed-Loop Voltage Gain ($A_v$)</div>
            <div id="res-gain-primary" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">-10.00 V/V</div>
            <div id="res-gain-db" style="font-size:1.05rem;color:#2563EB;font-weight:700;">+20.00 dB (180° Inverted Output)</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Expected Output Voltage ($V_{out}$)</span>
              <span id="res-vout-val" class="result-val" style="font-size:1.1rem;font-weight:700;color:#059669;">-1.000 V</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Output Headroom Status</span>
              <span id="res-clipping-status" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">Clean Linear Swing</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">-3dB Cutoff Bandwidth ($f_c$)</span>
              <span id="res-bandwidth-val" class="result-val" style="font-size:1.1rem;font-weight:700;color:#7C3AED;">1,000.0 kHz (1.0 MHz)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Circuit Input Impedance ($Z_{in}$)</span>
              <span id="res-zin-val" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">10.0 kΩ</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:0.85rem;color:#166534;">
            <strong>⚡ Circuit Design Suite:</strong> Sizing feedback resistors? Find standard component codes with our <a href="resistor-color-code-calculator.html" style="color:#166534;font-weight:700;">Resistor Color Code Calculator</a> and calculate parallel trimming with the <a href="parallel-resistor-calculator.html" style="color:#166534;font-weight:700;">Parallel Resistor Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Theory of Operational Amplifiers &amp; Negative Feedback</h2>
        <p>An operational amplifier (op-amp) is an integrated direct-coupled high-gain differential electronic amplifier. An ideal op-amp possesses five textbook characteristics: infinite open-loop gain ($A_{OL} \to \infty$), infinite input impedance ($R_{in} \to \infty$, drawing zero input bias current), zero output impedance ($R_{out} = 0$), infinite bandwidth, and zero input offset voltage. In an open-loop configuration without feedback, even a microvolt difference between the inverting ($-$) and non-inverting ($+$) inputs drives the output instantly into rail saturation.</p>

        <p>To produce stable, linear, predictable amplification, engineers wrap negative feedback around the op-amp by connecting a portion of the output voltage back to the inverting input via feedback resistor $R_f$. Because $A_{OL}$ is astronomically high ($100,000$ to $10,000,000$ V/V), the negative feedback loop forces the voltage potential difference between the inverting and non-inverting inputs to zero ($V_+ - V_- \approx 0$). This core operational principle is known as the <strong>Virtual Ground Principle</strong> (or Virtual Short), and it makes closed-loop gain entirely dependent on precision external passive resistors rather than the internal silicon characteristics of the chip.</p>

        <h2>Mathematical Closed-Loop Gain Formulations</h2>

        <h3>1. Inverting Amplifier Configuration</h3>
        <p>In the inverting amplifier, the non-inverting terminal ($+$) is tied directly to 0V ground. Applying Kirchhoff's Current Law (KCL) at the inverting node ($-$), which is held at a virtual ground of 0V:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$\frac{V_{in} - 0}{R_{in}} + \frac{V_{out} - 0}{R_f} = 0$$
          $$\frac{V_{in}}{R_{in}} = -\frac{V_{out}}{R_f}$$
          $$A_v = \frac{V_{out}}{V_{in}} = -\frac{R_f}{R_{in}}$$
        </div>
        <p>The negative sign indicates an exact $180^\circ$ phase inversion between input and output waveforms. The circuit's input impedance equals exactly $R_{in}$ ($Z_{in} = R_{in}$).</p>

        <h3>2. Non-Inverting Amplifier Configuration</h3>
        <p>In the non-inverting amplifier, input signal $V_{in}$ is applied directly to the positive terminal ($+$). Because the inverting terminal ($-$) tracks the positive terminal via negative feedback, $V_- = V_{in}$. The feedback network ($R_f$ and $R_1$) forms an ordinary voltage divider from $V_{out}$ to ground:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$V_- = V_{out} \cdot \left( \frac{R_1}{R_1 + R_f} \right) = V_{in}$$
          $$A_v = \frac{V_{out}}{V_{in}} = \frac{R_1 + R_f}{R_1} = 1 + \frac{R_f}{R_1}$$
        </div>
        <p>Because $\frac{R_f}{R_1} \ge 0$, non-inverting gain is strictly $\ge 1.0$, and the output remains in phase ($0^\circ$ phase shift) with the input. Furthermore, because signal feeds directly into an insulated gate or base, input impedance is exceptionally high ($Z_{in} \approx 10^9\text{ }\Omega$ to $10^{12}\text{ }\Omega$).</p>

        <h3>3. Voltage Gain in Decibels (dB)</h3>
        <p>Engineers express voltage gain logarithmically in decibels (dB):</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$\text{Gain (dB)} = 20 \cdot \log_{10}(|A_v|)$$
        </div>

        <h3>4. Gain-Bandwidth Product (GBWP) &amp; Cutoff Frequency</h3>
        <p>Internal frequency-compensation capacitors inside the op-amp enforce a $-20\text{ dB/decade}$ roll-off to guarantee loop stability. The product of closed-loop gain magnitude and $-3\text{dB}$ high-frequency bandwidth remains constant:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #DC2626;">
          $$\text{GBWP} = |A_v| \cdot f_c \implies f_c = \frac{\text{GBWP}}{|A_v|}$$
        </div>

        <h2>Popular Op-Amp IC Specifications Reference Table</h2>
        <p>Comparing common general-purpose, audio, and precision operational amplifiers:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Op-Amp Part</th>
                <th style="padding:0.75rem;">Input Stage</th>
                <th style="padding:0.75rem;">GBWP</th>
                <th style="padding:0.75rem;">Slew Rate</th>
                <th style="padding:0.75rem;">Primary Application</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>LM741</strong></td>
                <td style="padding:0.75rem;">Bipolar (BJT)</td>
                <td style="padding:0.75rem;">1.0 MHz</td>
                <td style="padding:0.75rem;">0.5 V/μs</td>
                <td style="padding:0.75rem;">Legacy educational reference; low performance.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>TL072 / TL082</strong></td>
                <td style="padding:0.75rem;">JFET Input</td>
                <td style="padding:0.75rem;">3.0 MHz</td>
                <td style="padding:0.75rem;">13 V/μs</td>
                <td style="padding:0.75rem;">Audio mixing consoles; ultra-high input impedance.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>NE5532 / NE5534</strong></td>
                <td style="padding:0.75rem;">Low-Noise BJT</td>
                <td style="padding:0.75rem;">10.0 MHz</td>
                <td style="padding:0.75rem;">9 V/μs</td>
                <td style="padding:0.75rem;">Pro audio preamps; ultra-low $5\text{ nV/}\sqrt{\text{Hz}}$ voltage noise.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>OPA2134</strong></td>
                <td style="padding:0.75rem;">High-End SoundPlus JFET</td>
                <td style="padding:0.75rem;">16.0 MHz</td>
                <td style="padding:0.75rem;">20 V/μs</td>
                <td style="padding:0.75rem;">Audiophile DAC output buffers; distortion $0.00008\%$.</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>OP07</strong></td>
                <td style="padding:0.75rem;">Precision BJT</td>
                <td style="padding:0.75rem;">0.6 MHz</td>
                <td style="padding:0.75rem;">0.3 V/μs</td>
                <td style="padding:0.75rem;">Instrumentation &amp; thermocouples; $10\text{ }\mu\text{V}$ ultra-low offset.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: Dynamic Microphone Preamplifier
          </h3>
          <p><strong>Scenario:</strong> An audio hardware designer is building a non-inverting preamplifier for a dynamic vocal microphone ($V_{\text{in}} = 5\text{ mV RMS}$). The target closed-loop voltage gain is $A_v = 101$ ($+40.08\text{ dB}$). The circuit is powered by $\pm 15\text{V}$ rails and utilizes an NE5532 dual audio op-amp ($\text{GBWP} = 10\text{ MHz}$).</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Select Resistors for $A_v = 101$:</strong>
              $$A_v = 1 + \frac{R_f}{R_1} = 101 \implies \frac{R_f}{R_1} = 100$$
              To maintain low Johnson-Nyquist thermal noise, the designer chooses $R_1 = 1.0\text{ k}\Omega$ ($1,000\text{ }\Omega$).
              $$R_f = 100 \times 1.0\text{ k}\Omega = 100.0\text{ k}\Omega$$
            </li>
            <li><strong>Calculate Output Signal Amplitude ($V_{\text{out}}$):</strong>
              $$V_{\text{out}} = V_{\text{in}} \times A_v = 5\text{ mV} \times 101 = 505\text{ mV RMS } \approx 0.505\text{ V RMS}$$
              Peak output voltage: $V_{\text{peak}} = 0.505\text{ V} \times \sqrt{2} \approx 0.714\text{ V}$. This is well within the $\pm 13.5\text{V}$ saturation limits of the $\pm 15\text{V}$ rails, providing ample headroom ($> 25\text{ dB}$).
            </li>
            <li><strong>Calculate -3dB Small-Signal Bandwidth:</strong>
              $$f_c = \frac{\text{GBWP}}{A_v} = \frac{10,000,000\text{ Hz}}{101} \approx 99,010\text{ Hz} \approx 99.0\text{ kHz}$$
            </li>
            <li><strong>Engineering Conclusion:</strong> The $99.0\text{ kHz}$ cutoff far exceeds the human audible upper threshold ($20\text{ kHz}$), ensuring zero phase distortion or high-frequency treble roll-off across the audible band.</li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is Slew Rate and how does it cause large-signal distortion?</h4>
            <p style="margin:0;color:#64748B;">Slew rate (SR, measured in V/μs) is the maximum rate at which the op-amp's internal output stage can change voltage, limited by the internal compensation capacitor's charging current (SR = I_tail / C_comp). While small-signal bandwidth might be 1 MHz, a large output swing (e.g. 10V peak at 100 kHz) requires a minimum slew rate of SR = 2π × f × V_peak = 6.28 V/μs. If the op-amp's rating is lower (such as 0.5 V/μs for LM741), sinusoidal signals distort into triangular waves.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why is a voltage follower (buffer) amplifier useful if its gain is only 1.0?</h4>
            <p style="margin:0;color:#64748B;">A voltage follower (Av = 1.0 / 0 dB) provides impedance matching. It features near-infinite input impedance (drawing no current from high-impedance sensors like piezoelectric pickups or pH probes) and near-zero output impedance (capable of driving low-impedance cables or ADC inputs). It acts as an electrical buffer, preventing signal loading.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is Input Offset Voltage (Vos) and how does it affect high-gain circuits?</h4>
            <p style="margin:0;color:#64748B;">Input offset voltage is a slight internal mismatch between the base-emitter or gate-source voltages of the differential input transistor pair (typically 1 to 5 mV). In high-gain DC amplifiers (such as Av = 1,000), this tiny offset is amplified by the closed-loop gain: Vout_error = Vos × Av = 2 mV × 1,000 = 2.0V DC offset error at output! Precision op-amps (like OP07) trim Vos below 25 μV.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why should feedback resistors generally be kept between 1 kΩ and 100 kΩ?</h4>
            <p style="margin:0;color:#64748B;">Resistors below 1 kΩ draw excessive drive current from the op-amp's output stage, causing thermal heating and output distortion. Resistors above 100 kΩ to 1 MΩ generate significant Johnson-Nyquist thermal noise (Vn = √(4kTRB)) and interact with stray PCB capacitance to form parasitic low-pass poles that induce phase lag and high-frequency oscillation.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Electronics &amp; IC Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="op-amp-gain-calculator.html" style="font-weight:700;color:#2563EB;">🔬 Op Amp Gain Calculator</a></li>
          <li><a href="555-timer-calculator.html" style="color:#475569;">⏱️ 555 Timer Astable/Mono</a></li>
          <li><a href="led-resistor-calculator.html" style="color:#475569;">💡 LED Series Resistor</a></li>
          <li><a href="capacitive-reactance-calculator.html" style="color:#475569;">⚡ Capacitive Reactance (Xc)</a></li>
          <li><a href="inductive-reactance-calculator.html" style="color:#475569;">🌀 Inductive Reactance (Xl)</a></li>
          <li><a href="parallel-resistor-calculator.html" style="color:#475569;">⚡ Parallel Resistor (Req)</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Power Engineering Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="three-phase-power-calculator.html" style="color:#475569;">⚡ Three-Phase Power</a></li>
          <li><a href="power-factor-calculator.html" style="color:#475569;">⚡ Power Factor Correction</a></li>
          <li><a href="transformer-sizing-calculator.html" style="color:#475569;">⚡ Transformer Sizing</a></li>
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
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">Analog Engineering Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          IEEE Standard for Operational Amplifiers (IEEE 515)<br>
          JEDEC Standard No. 23 Op-Amp Definitions<br>
          Texas Instruments Op-Amps for Everyone Handbook
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Analog Signal Processing Computational Suite.
    </div>
  </footer>

  <script>
    function applyOpampChip() {
      const val = document.getElementById('opamp-chip-preset').value;
      if (val !== 'custom') {
        document.getElementById('gbwp-mhz').value = val;
      }
      runOpampCalc();
    }

    function runOpampCalc() {
      const topology = document.getElementById('amp-topology').value;
      const vin = parseFloat(document.getElementById('input-voltage').value) || 0.100;
      const rfVal = Math.max(0.01, parseFloat(document.getElementById('res-rf').value) || 100);
      const rfMult = parseFloat(document.getElementById('unit-rf').value) || 1000;
      const Rf = rfVal * rfMult;

      const rinVal = Math.max(0.01, parseFloat(document.getElementById('res-rin').value) || 10);
      const rinMult = parseFloat(document.getElementById('unit-rin').value) || 1000;
      const Rin = rinVal * rinMult;

      const gbwpMhz = Math.max(0.001, parseFloat(document.getElementById('gbwp-mhz').value) || 10.0);
      const gbwpHz = gbwpMhz * 1e6;

      const rails = Math.max(1.0, parseFloat(document.getElementById('supply-rail').value) || 15.0);
      const vMaxSwing = Math.max(0.5, rails - 1.5); // standard ~1.5V drop from rail

      let av = 1.0;
      let phaseStr = '0° (In-Phase)';
      let zin = Rin;

      if (topology === 'inverting') {
        av = - (Rf / Rin);
        phaseStr = '180° Inverted Output';
        zin = Rin;
      } else if (topology === 'non-inverting') {
        av = 1.0 + (Rf / Rin);
        phaseStr = '0° (In-Phase)';
        zin = 1e9; // JFET/BJT ~ high
      } else {
        // Buffer
        av = 1.0;
        phaseStr = '0° (Unity Buffer)';
        zin = 1e9;
      }

      const magAv = Math.abs(av);
      const gainDb = 20.0 * Math.log10(magAv);
      const rawVout = vin * av;

      // Bandwidth: fc = GBWP / magAv
      const fcHz = magAv > 0 ? (gbwpHz / magAv) : gbwpHz;

      // Clipping status
      let clipStatus = 'Clean Linear Swing';
      let actualVout = rawVout;
      if (Math.abs(rawVout) > vMaxSwing) {
        clipStatus = 'Saturated / Clipped at ±' + vMaxSwing.toFixed(1) + 'V';
        actualVout = rawVout > 0 ? vMaxSwing : -vMaxSwing;
      }

      let fcStr = '';
      if (fcHz >= 1e6) fcStr = (fcHz / 1e6).toFixed(2) + ' MHz';
      else if (fcHz >= 1e3) fcStr = (fcHz / 1e3).toFixed(1) + ' kHz';
      else fcStr = fcHz.toFixed(1) + ' Hz';

      let zinStr = '';
      if (zin >= 1e6) zinStr = '> 100 MΩ (High Z)';
      else if (zin >= 1e3) zinStr = (zin / 1e3).toFixed(1) + ' kΩ';
      else zinStr = zin.toFixed(0) + ' Ω';

      document.getElementById('res-gain-primary').textContent = av.toFixed(2) + ' V/V';
      document.getElementById('res-gain-db').textContent = (gainDb >= 0 ? '+' : '') + gainDb.toFixed(2) + ' dB (' + phaseStr + ')';
      document.getElementById('res-vout-val').textContent = actualVout.toFixed(3) + ' V' + (Math.abs(rawVout) > vMaxSwing ? ' (Clipped)' : '');
      document.getElementById('res-clipping-status').textContent = clipStatus;
      document.getElementById('res-bandwidth-val').textContent = fcStr;
      document.getElementById('res-zin-val').textContent = zinStr;
    }

    window.addEventListener('DOMContentLoaded', runOpampCalc);
  </script>
</body>
</html>
"""

# ==========================================
# 2. THREE PHASE POWER CALCULATOR
# ==========================================
TOOL_3PHASE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Three Phase Power Calculator — kW, kVA, kVAR &amp; Line Amps (Star &amp; Delta)</title>
  <meta name="description" content="Calculate balanced three-phase real power (kW), apparent power (kVA), reactive power (kVAR), and full-load line current for Star and Delta AC electrical loads.">
  <meta name="keywords" content="three phase power calculator, 3 phase power formula, calculate 3 phase kw, three phase line current, star delta 3 phase power, 3 phase kva to kw, square root 3 power formula">
  <link rel="canonical" href="https://calchub.org/three-phase-power-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Three-Phase Electrical Power Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates active kW, reactive kVAR, apparent kVA, and line current for 3-phase Star and Delta balanced loads per IEEE 1459 standards."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the formula for calculating three-phase real power (kW)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Three-phase real working power is calculated using line-to-line values: P = √3 × V_LL × I_L × cos(θ) / 1000, where P is real power in kilowatts (kW), √3 ≈ 1.73205, V_LL is line-to-line RMS voltage in Volts, I_L is line current in Amperes, and cos(θ) is the electrical load power factor. Alternatively, using phase values: P = 3 × V_phase × I_phase × cos(θ) / 1000."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between Star (Wye) and Delta (Δ) three-phase configurations?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In a Star (Wye, Y) connection: Line voltage is √3 times phase voltage (V_LL = √3 × V_LN), but line current equals phase current (I_L = I_phase). Star systems provide a common neutral conductor for 1-phase loads (e.g., 480Y/277V or 208Y/120V). In a Delta (Δ) connection: Line voltage equals phase voltage (V_LL = V_phase), but line current is √3 times phase current (I_L = √3 × I_phase). Delta is commonly used for heavy industrial induction motors."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calculate full-load line current (FLC) from three-phase kVA or kW?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "To find line current from apparent power: I_L = (kVA × 1000) / (√3 × V_LL). To find line current from real power: I_L = (kW × 1000) / (√3 × V_LL × cos(θ)). For example, a 100 kW load at 480V with a 0.85 power factor draws: (100 × 1000) / (1.732 × 480 × 0.85) = 100,000 / 706.7 = 141.5 Amperes."
            }
          },
          {
            "@type": "Question",
            "name": "Why is three-phase power superior to single-phase for industrial distribution?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Three-phase power delivers constant instantaneous power (the sum of three 120° displaced sinewaves yields zero power pulsing), eliminating mechanical vibration in motor shafts. Furthermore, three-phase systems transmit 73% more power than single-phase using the same amount of copper conductor material, dramatically reducing electrical infrastructure costs."
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
      <span class="category-tag">⚡ Industrial AC Power Transmission &amp; IEEE 1459</span>
      <h1 class="calc-page-title">Three Phase Power Calculator</h1>
      <p class="calc-page-desc">Calculate balanced three-phase active power (kW), apparent power (kVA), reactive power (kVAR), and line current (Amps) for Star (Wye) and Delta AC distribution systems.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>⚡</span> 3-Phase System Parameters</h2>
            <span class="status-info">P = √3 · V · I · cos θ</span>
          </div>
          <form id="threephase-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="calc-mode-3p">Calculation Target</label>
                <select id="calc-mode-3p" class="form-control" onchange="toggle3pFields()">
                  <option value="find-power" selected>Calculate Power (kW &amp; kVA) from Current</option>
                  <option value="find-current">Calculate Line Current (Amps) from kW Rating</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="wiring-topology">System Connection Topology</label>
                <select id="wiring-topology" class="form-control" onchange="run3pCalc()">
                  <option value="wye" selected>Star / Wye (Y — with Neutral / V_LL = √3 V_LN)</option>
                  <option value="delta">Delta (Δ — 3-Wire / I_L = √3 I_phase)</option>
                </select>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="line-voltage-3p">Line-to-Line Voltage ($V_{LL}$ in V)</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="line-voltage-3p" class="form-control" value="480" min="10" max="500000" step="10" oninput="run3pCalc()">
                  <select id="voltage-presets-3p" class="form-control" style="width:130px;" onchange="apply3pVoltagePreset()">
                    <option value="custom">Preset Voltage</option>
                    <option value="480" selected>480V (US Ind)</option>
                    <option value="208">208V (US Com)</option>
                    <option value="400">400V (EU/IEC)</option>
                    <option value="600">600V (Canada)</option>
                    <option value="4160">4.16 kV (Medium)</option>
                  </select>
                </div>
              </div>
              <div class="form-group" id="group-current-input">
                <label class="form-label" for="line-current-3p">Line Current ($I_L$ in Amperes)</label>
                <input type="number" id="line-current-3p" class="form-control" value="125" min="0.1" max="100000" step="5" oninput="run3pCalc()">
              </div>
              <div class="form-group" id="group-kw-input" style="display:none;">
                <label class="form-label" for="real-kw-input">Active Real Power ($P$ in kW)</label>
                <input type="number" id="real-kw-input" class="form-control" value="85" min="0.1" max="1000000" step="5" oninput="run3pCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="power-factor-3p">Electrical Power Factor ($\cos\theta$)</label>
                <input type="number" id="power-factor-3p" class="form-control" value="0.85" min="0.10" max="1.00" step="0.01" oninput="run3pCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="efficiency-3p">Equipment Efficiency ($\eta$ %)</label>
                <input type="number" id="efficiency-3p" class="form-control" value="100" min="10" max="100" step="1" oninput="run3pCalc()">
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="run3pCalc()">Calculate 3-Phase Power</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Power Schedule</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Three-Phase Power Analysis Summary</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div id="res-3p-primary-label" class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Active Working Power (P)</div>
            <div id="res-3p-primary-val" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">88.3 kW</div>
            <div id="res-3p-primary-sub" style="font-size:1.05rem;color:#059669;font-weight:700;">118.4 Horsepower (HP equivalent)</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Apparent Total Power ($S$)</span>
              <span id="res-3p-s-kva" class="result-val" style="font-size:1.1rem;font-weight:700;color:#2563EB;">103.9 kVA</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Reactive Magnetizing Power ($Q$)</span>
              <span id="res-3p-q-kvar" class="result-val" style="font-size:1.1rem;font-weight:700;color:#DC2626;">54.7 kVAR</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Line Current ($I_L$)</span>
              <span id="res-3p-line-current" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">125.0 Amperes</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Line-to-Neutral Phase Voltage ($V_{LN}$)</span>
              <span id="res-3p-vln" class="result-val" style="font-size:1.1rem;font-weight:700;color:#7C3AED;">277.1 Volts (Star Y)</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#EFF6FF;border:1px solid #BFDBFE;font-size:0.85rem;color:#1E40AF;">
            <strong>⚡ Downstream Power Distribution:</strong> Size conductors for this load with our <a href="cable-sizing-calculator.html" style="color:#1E40AF;font-weight:700;">Cable Sizing Calculator</a>, check conduit bundling with the <a href="conduit-fill-calculator.html" style="color:#1E40AF;font-weight:700;">Conduit Fill Calculator</a>, or verify substation transformers with the <a href="transformer-sizing-calculator.html" style="color:#1E40AF;font-weight:700;">Transformer Sizing Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Physics of Polyphase Three-Phase AC Electrical Systems</h2>
        <p>Invented independently by Nikola Tesla and Mikhail Dolivo-Dobrovolsky in the late 1880s, <strong>three-phase alternating current (3-phase AC)</strong> is the universal global standard for commercial electrical energy generation, high-voltage transmission, and heavy industrial power utilization. A balanced three-phase generator generates three separate alternating voltages that possess identical amplitudes and frequencies, but are systematically separated in time by a phase displacement angle of exactly <strong>$120^\circ$ ($\frac{2\pi}{3}$ radians)</strong>.</p>

        <p>Because the trigonometric sum of three equal sinusoidal waves displaced by $120^\circ$ is identically zero at every instant in time ($\sin(\omega t) + \sin(\omega t - 120^\circ) + \sin(\omega t + 120^\circ) = 0$), a balanced three-phase system requires zero neutral return current. Crucially, the instantaneous power delivered to a balanced 3-phase load is completely constant and ripple-free ($p(t) = P_{\text{constant}}$), unlike single-phase AC which pulses from zero to peak at twice line frequency ($120\text{ Hz}$). This pulsation-free torque enables induction motors to start smoothly without vibrating or requiring phase-shifting start capacitors.</p>

        <h2>Mathematical 3-Phase Power Equations</h2>

        <h3>1. The Universal Line-to-Line Formula</h3>
        <p>In power engineering, measurements taken on electrical panels and switchgear are universally line-to-line RMS voltages ($V_{LL}$) and line currents ($I_L$). Total three-phase active real power ($P$), apparent power ($S$), and reactive power ($Q$) are formulated as:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$P = \sqrt{3} \cdot V_{LL} \cdot I_L \cdot \cos(\theta) \quad [\text{Watts}]$$
          $$S = \sqrt{3} \cdot V_{LL} \cdot I_L \quad [\text{Volt-Amperes, VA}]$$
          $$Q = \sqrt{3} \cdot V_{LL} \cdot I_L \cdot \sin(\theta) \quad [\text{Volt-Amperes Reactive, VAR}]$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$\sqrt{3} \approx 1.73205$</strong> = Geometric factor representing vector summation in a $120^\circ$ planar coordinate system.</li>
          <li><strong>$V_{LL}$</strong> = Line-to-line RMS voltage (e.g., $480\text{V}$, $400\text{V}$, $208\text{V}$).</li>
          <li><strong>$I_L$</strong> = Line conductor RMS current in Amperes.</li>
          <li><strong>$\cos(\theta)$</strong> = Power factor ($PF = \frac{P}{S}$), where $\theta$ is the phase angle between voltage and current.</li>
        </ul>

        <h3>2. Star (Wye, Y) vs Delta ($\Delta$) Topologies</h3>
        <p>Depending on winding geometry, the relationship between line and phase quantities varies:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Parameter</th>
                <th style="padding:0.75rem;">Star / Wye (Y) Connection</th>
                <th style="padding:0.75rem;">Delta ($\Delta$) Connection</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Line vs Phase Voltage</strong></td>
                <td style="padding:0.75rem;">$V_{LL} = \sqrt{3} \cdot V_{LN} \approx 1.732 \cdot V_{LN}$</td>
                <td style="padding:0.75rem;">$V_{LL} = V_{\text{phase}}$</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Line vs Phase Current</strong></td>
                <td style="padding:0.75rem;">$I_L = I_{\text{phase}}$</td>
                <td style="padding:0.75rem;">$I_L = \sqrt{3} \cdot I_{\text{phase}} \approx 1.732 \cdot I_{\text{phase}}$</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Neutral Conductor</strong></td>
                <td style="padding:0.75rem;">Yes (Center star point provides Neutral)</td>
                <td style="padding:0.75rem;">No (3-wire ungrounded or corner-grounded)</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>Total Real Power</strong></td>
                <td style="padding:0.75rem;">$3 \cdot V_{LN} \cdot I_L \cdot \cos(\theta) = \sqrt{3} \cdot V_{LL} \cdot I_L \cdot \cos(\theta)$</td>
                <td style="padding:0.75rem;">$3 \cdot V_{LL} \cdot I_{\text{phase}} \cdot \cos(\theta) = \sqrt{3} \cdot V_{LL} \cdot I_L \cdot \cos(\theta)$</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Standard International 3-Phase Distribution Voltages Table</h2>
        <p>Three-phase nominal voltage standards worldwide:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Region / Standard</th>
                <th style="padding:0.75rem;">Line-to-Line ($V_{LL}$)</th>
                <th style="padding:0.75rem;">Line-to-Neutral ($V_{LN}$)</th>
                <th style="padding:0.75rem;">Primary Use Case</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>North America (US Industrial)</strong></td>
                <td style="padding:0.75rem;">480 V</td>
                <td style="padding:0.75rem;">277 V</td>
                <td style="padding:0.75rem;">Manufacturing plants, commercial HVAC, 277V lighting.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>North America (US Commercial)</strong></td>
                <td style="padding:0.75rem;">208 V</td>
                <td style="padding:0.75rem;">120 V</td>
                <td style="padding:0.75rem;">Offices, data centers, mixed 120V convenience receptacles.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Europe / UK / Asia / IEC</strong></td>
                <td style="padding:0.75rem;">400 V</td>
                <td style="padding:0.75rem;">230 V</td>
                <td style="padding:0.75rem;">Universal grid; powers both 400V 3-phase and 230V single-phase.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Canada (Industrial Standard)</strong></td>
                <td style="padding:0.75rem;">600 V</td>
                <td style="padding:0.75rem;">347 V</td>
                <td style="padding:0.75rem;">Heavy industrial plants, mining, 347V lighting ballasts.</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>Medium Voltage Distribution</strong></td>
                <td style="padding:0.75rem;">4,160 V / 13,800 V</td>
                <td style="padding:0.75rem;">2,400 V / 7,960 V</td>
                <td style="padding:0.75rem;">Campus utility loops, large multi-megawatt chillers.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: 75 HP Factory Chiller Motor
          </h3>
          <p><strong>Scenario:</strong> A plant electrical engineer is sizing the feeder breaker and conductor for a $75\text{ HP}$ ($55.95\text{ kW}$ mechanical shaft output) three-phase induction motor operating on a $480\text{V}$ Wye distribution system. The motor nameplate specifies: $480\text{V}$, efficiency $\eta = 92.5\%$, and full-load power factor $\cos\theta = 0.86$.</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Calculate Total Electrical Active Power Input ($P_{\text{elec}}$):</strong>
              $$P_{\text{elec}} = \frac{P_{\text{mech}}}{\eta} = \frac{55.95\text{ kW}}{0.925} \approx 60.49\text{ kW} = 60,490\text{ Watts}$$
            </li>
            <li><strong>Calculate Apparent Power Demand ($S$):</strong>
              $$S = \frac{P_{\text{elec}}}{\cos\theta} = \frac{60.49\text{ kW}}{0.86} \approx 70.34\text{ kVA}$$
            </li>
            <li><strong>Calculate Reactive Magnetizing Power ($Q$):</strong>
              $$\theta = \arccos(0.86) \approx 30.68^\circ \implies \sin(30.68^\circ) \approx 0.5103$$
              $$Q = S \cdot \sin(\theta) = 70.34 \times 0.5103 \approx 35.89\text{ kVAR}$$
            </li>
            <li><strong>Determine Full-Load Line Amperes ($I_L$):</strong>
              $$I_L = \frac{P_{\text{elec}}}{\sqrt{3} \cdot V_{LL} \cdot \cos\theta} = \frac{60,490}{\sqrt{3} \times 480 \times 0.86} = \frac{60,490}{1.732 \times 480 \times 0.86} = \frac{60,490}{714.98} \approx 84.60\text{ Amperes}$$
            </li>
            <li><strong>Check Line-to-Neutral Voltage:</strong>
              $$V_{LN} = \frac{V_{LL}}{\sqrt{3}} = \frac{480}{1.732} \approx 277.1\text{ Volts}$$
            </li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">How is three-phase power measured using the Two-Wattmeter Method?</h4>
            <p style="margin:0;color:#64748B;">Under Blondel's Theorem, any N-wire system can be fully measured using N-1 wattmeters. In a 3-wire 3-phase system, two wattmeters are connected with current coils in lines A and C, and potential coils referencing line B. Total active power is the algebraic sum of both readings: P_total = W1 + W2. If load power factor is below 0.5, one wattmeter will produce a negative reading!</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What happens if a three-phase motor loses one phase (Single-Phasing)?</h4>
            <p style="margin:0;color:#64748B;">If one supply phase is severed due to a blown fuse, the remaining two operational phases must deliver the full power demand, increasing line current in the surviving windings by √3 (173%). This massive overcurrent generates extreme internal ohmic heating, causing winding insulation breakdown and motor burnout in minutes unless protected by an overload relay or phase-loss monitor.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is neutral current in an unbalanced 3-phase Star system?</h4>
            <p style="margin:0;color:#64748B;">In a balanced system, neutral current is zero. In an unbalanced system, neutral current is the vector sum of line currents: I_N = I_A + I_B + I_C. In commercial buildings with heavy non-linear loads (computers, LED drivers), 3rd harmonic triplen currents (180 Hz) do not cancel out in the neutral; instead, they add in phase, causing neutral current to exceed line current!</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Can a Delta connected load be converted to an equivalent Wye load?</h4>
            <p style="margin:0;color:#64748B;">Yes! By the Delta-Wye (Δ-Y) transformation theorem, three identical Delta impedances of value Z_delta are mathematically equivalent to three Star impedances of value Z_wye = Z_delta / 3. This principle is utilized in Star-Delta motor starters to reduce starting inrush current and torque by two-thirds (33% of full voltage values).</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Industrial Power Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="three-phase-power-calculator.html" style="font-weight:700;color:#2563EB;">⚡ Three-Phase Power (kW)</a></li>
          <li><a href="power-factor-calculator.html" style="color:#475569;">⚡ Power Factor Correction</a></li>
          <li><a href="transformer-sizing-calculator.html" style="color:#475569;">⚡ Transformer Sizing (NEC)</a></li>
          <li><a href="motor-starting-current-calculator.html" style="color:#475569;">⚙️ Motor Starting Current</a></li>
          <li><a href="short-circuit-calculator.html" style="color:#475569;">💥 Short-Circuit (IEC 60909)</a></li>
          <li><a href="wire-ampacity-calculator.html" style="color:#475569;">🔌 Wire Ampacity (NEC)</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Hardware &amp; Analog Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="op-amp-gain-calculator.html" style="color:#475569;">🔬 Op Amp Gain Calculator</a></li>
          <li><a href="voltage-drop-calculator.html" style="color:#475569;">📉 Voltage Drop Calculator</a></li>
          <li><a href="cable-sizing-calculator.html" style="color:#475569;">🔌 Cable Sizing Calculator</a></li>
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
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">Power Grid Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          IEEE 1459 Standard Definitions for Electric Power<br>
          NFPA 70 National Electrical Code (NEC)<br>
          IEC 60038 Standard Voltages
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Industrial Polyphase Power Computational Suite.
    </div>
  </footer>

  <script>
    function toggle3pFields() {
      const mode = document.getElementById('calc-mode-3p').value;
      const gCurr = document.getElementById('group-current-input');
      const gKw = document.getElementById('group-kw-input');
      if (mode === 'find-power') {
        gCurr.style.display = 'block';
        gKw.style.display = 'none';
        document.getElementById('res-3p-primary-label').textContent = 'Active Working Power (P)';
      } else {
        gCurr.style.display = 'none';
        gKw.style.display = 'block';
        document.getElementById('res-3p-primary-label').textContent = 'Required Line Current (I_L)';
      }
      run3pCalc();
    }

    function apply3pVoltagePreset() {
      const val = document.getElementById('voltage-presets-3p').value;
      if (val !== 'custom') {
        document.getElementById('line-voltage-3p').value = val;
      }
      run3pCalc();
    }

    function run3pCalc() {
      const mode = document.getElementById('calc-mode-3p').value;
      const topo = document.getElementById('wiring-topology').value;
      const vll = Math.max(1.0, parseFloat(document.getElementById('line-voltage-3p').value) || 480);
      const pf = Math.min(1.0, Math.max(0.1, parseFloat(document.getElementById('power-factor-3p').value) || 0.85));
      const eff = Math.min(100, Math.max(10, parseFloat(document.getElementById('efficiency-3p').value) || 100)) / 100.0;

      const vln = vll / Math.SQRT3;

      let P = 0, S = 0, Q = 0, Il = 0;

      if (mode === 'find-power') {
        Il = Math.max(0.01, parseFloat(document.getElementById('line-current-3p').value) || 125);
        // S = sqrt(3) * V_LL * I_L in VA
        const sVa = Math.SQRT3 * vll * Il;
        S = sVa / 1000.0; // in kVA
        // P = S * pf * eff in kW
        P = S * pf * eff; // in kW
        // Q = S * sin(theta) in kVAR
        const sinTheta = Math.sqrt(Math.max(0, 1.0 - pf * pf));
        Q = S * sinTheta;

        const hp = P * 1.34102;

        document.getElementById('res-3p-primary-val').textContent = P.toFixed(1) + ' kW';
        document.getElementById('res-3p-primary-sub').textContent = hp.toFixed(1) + ' Horsepower (HP equivalent)';
      } else {
        const kw = Math.max(0.01, parseFloat(document.getElementById('real-kw-input').value) || 85);
        // P_elec = kw / eff
        const pElecKw = kw / eff;
        S = pElecKw / pf; // kVA
        // Il = (S * 1000) / (sqrt(3) * vll)
        Il = (S * 1000.0) / (Math.SQRT3 * vll);
        const sinTheta = Math.sqrt(Math.max(0, 1.0 - pf * pf));
        Q = S * sinTheta;
        P = kw;

        document.getElementById('res-3p-primary-val').textContent = Il.toFixed(1) + ' Amperes';
        document.getElementById('res-3p-primary-sub').textContent = 'Full Load Amps (FLA) at ' + vll + 'V ' + (topo === 'wye' ? 'Star Y' : 'Delta \u0394');
      }

      document.getElementById('res-3p-s-kva').textContent = S.toFixed(1) + ' kVA';
      document.getElementById('res-3p-q-kvar').textContent = Q.toFixed(1) + ' kVAR';
      document.getElementById('res-3p-line-current').textContent = Il.toFixed(1) + ' Amperes';
      document.getElementById('res-3p-vln').textContent = (topo === 'wye' ? vln.toFixed(1) + ' Volts (Phase)' : vll.toFixed(0) + ' Volts (Phase = Line)');
    }

    window.addEventListener('DOMContentLoaded', run3pCalc);
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "op-amp-gain-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_OPAMP)
print("[PASS] op-amp-gain-calculator.html generated successfully!")

with open(os.path.join(BASE_DIR, "three-phase-power-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_3PHASE)
print("[PASS] three-phase-power-calculator.html generated successfully!")
