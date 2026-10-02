"""
Generates 555-timer-calculator.html and led-resistor-calculator.html
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
# 1. 555 TIMER CALCULATOR
# ==========================================
TOOL_555 = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>555 Timer Calculator — Astable &amp; Monostable Circuit Frequency</title>
  <meta name="description" content="Calculate 555 timer oscillator frequency, pulse high and low times, and duty cycle for astable multivibrator and monostable one-shot pulse circuits.">
  <meta name="keywords" content="555 timer calculator, 555 astable calculator, 555 monostable calculator, 555 timer frequency, duty cycle 555 timer, ne555 pulse width, 555 timer circuit formulas">
  <link rel="canonical" href="https://calchub.org/555-timer-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "NE555 Timer Circuit Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates oscillation frequency, high/low times, duty cycle, and one-shot pulse widths for NE555 timer circuits in astable and monostable modes."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "How does a 555 timer operate in astable multivibrator mode?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In astable mode, the 555 timer operates as an autonomous free-running square wave relaxation oscillator. An external timing capacitor C charges through series resistors (R1 + R2) toward Vcc until its voltage reaches the internal upper threshold of 2/3 Vcc. At this point, the internal comparator trips the RS flip-flop, activating the internal discharge transistor (pin 7). Capacitor C then discharges through resistor R2 toward ground until its voltage falls below the lower trigger threshold of 1/3 Vcc, cycling continuously."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for 555 timer astable frequency and duty cycle?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In standard astable configuration: Time High is Th = 0.693 × (R1 + R2) × C, Time Low is Tl = 0.693 × R2 × C, total oscillation period is T = Th + Tl = 0.693 × (R1 + 2×R2) × C, and output frequency is f = 1 / T = 1.44 / [(R1 + 2×R2) × C]. The duty cycle is D = Th / T = (R1 + R2) / (R1 + 2×R2) × 100%. Notice that in standard topology, duty cycle must always exceed 50% because charging occurs through (R1 + R2) while discharging occurs through R2 alone."
            }
          },
          {
            "@type": "Question",
            "name": "How can you achieve a 50% or sub-50% duty cycle with a 555 timer?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "To achieve a true 50% square wave or low duty cycle (< 50%), connect a fast switching signal diode (such as 1N4148) in parallel across timing resistor R2 with cathode pointing toward capacitor C. During charging, current bypasses R2 through the diode directly into C via R1 (Th = 0.693 × R1 × C). During discharging, the diode is reverse-biased, forcing discharge strictly through R2 (Tl = 0.693 × R2 × C). Setting R1 = R2 yields an exact 50% duty cycle."
            }
          },
          {
            "@type": "Question",
            "name": "How is monostable one-shot pulse duration calculated in a 555 circuit?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In monostable mode, a momentary negative trigger pulse (< 1/3 Vcc) on pin 2 pulls the output high and turns off the internal discharge transistor. Capacitor C charges exponentially from 0V through resistor R1 toward Vcc. When capacitor voltage reaches 2/3 Vcc, the comparator resets the flip-flop, dropping output low and discharging C. The output pulse width duration is given by: T = ln(3) × R1 × C ≈ 1.1 × R1 × C seconds."
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
      <span class="category-tag">⚡ Analog Integrated Circuits &amp; Pulse Timing</span>
      <h1 class="calc-page-title">555 Timer Calculator</h1>
      <p class="calc-page-desc">Calculate oscillation frequency, pulse high/low intervals, and duty cycle for NE555 timer circuits in astable oscillator and monostable one-shot configurations.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>⏱️</span> NE555 Timing Component Values</h2>
            <span class="status-info">Astable &amp; Monostable Modes</span>
          </div>
          <form id="timer-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="timer-mode">Operating Circuit Mode</label>
                <select id="timer-mode" class="form-control" onchange="toggleModeFields()">
                  <option value="astable" selected>Astable Multivibrator (Continuous Oscillator)</option>
                  <option value="monostable">Monostable Mode (One-Shot Timer Pulse)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="res-r1">Resistor R1 Value</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="res-r1" class="form-control" value="10" min="0.1" max="100000" step="0.5" oninput="runTimerCalc()">
                  <select id="unit-r1" class="form-control" style="width:110px;" onchange="runTimerCalc()">
                    <option value="1000" selected>kΩ</option>
                    <option value="1">Ω</option>
                    <option value="1000000">MΩ</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group" id="group-r2">
                <label class="form-label" for="res-r2">Resistor R2 Value (Astable only)</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="res-r2" class="form-control" value="47" min="0.1" max="100000" step="0.5" oninput="runTimerCalc()">
                  <select id="unit-r2" class="form-control" style="width:110px;" onchange="runTimerCalc()">
                    <option value="1000" selected>kΩ</option>
                    <option value="1">Ω</option>
                    <option value="1000000">MΩ</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label class="form-label" for="cap-c">Timing Capacitor C1</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="cap-c" class="form-control" value="10" min="0.001" max="100000" step="0.1" oninput="runTimerCalc()">
                  <select id="unit-c" class="form-control" style="width:110px;" onchange="runTimerCalc()">
                    <option value="1e-6" selected>μF</option>
                    <option value="1e-9">nF</option>
                    <option value="1e-12">pF</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runTimerCalc()">Calculate 555 Timing</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Schematic Submittal</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Output Pulse &amp; Frequency Analysis</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div id="res-primary-label" class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Astable Oscillation Frequency</div>
            <div id="res-primary-val" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">1.38 Hz</div>
            <div id="res-primary-sub" style="font-size:1.05rem;color:#059669;font-weight:700;">Total Period T = 724.2 milliseconds</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span id="res-th-label" class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">High Time (T_high)</span>
              <span id="res-th-val" class="result-val" style="font-size:1.1rem;font-weight:700;color:#2563EB;">395.0 ms</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span id="res-tl-label" class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Low Time (T_low)</span>
              <span id="res-tl-val" class="result-val" style="font-size:1.1rem;font-weight:700;color:#DC2626;">325.7 ms</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Duty Cycle</span>
              <span id="res-duty-val" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">54.8 %</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Total RC Charge Constant</span>
              <span id="res-tau-val" class="result-val" style="font-size:1.1rem;font-weight:700;color:#7C3AED;">0.570 s</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#EFF6FF;border:1px solid #BFDBFE;font-size:0.85rem;color:#1E40AF;">
            <strong>⚡ Circuit Design Suite:</strong> Sizing series driver components? Use our <a href="ohms-law-calculator.html" style="color:#1E40AF;font-weight:700;">Ohm's Law Calculator</a>, verify branch resistance with the <a href="parallel-resistor-calculator.html" style="color:#1E40AF;font-weight:700;">Parallel Resistor Calculator</a>, or decode banding using the <a href="resistor-color-code-calculator.html" style="color:#1E40AF;font-weight:700;">Resistor Color Code Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Architecture of the NE555 Timer Integrated Circuit</h2>
        <p>Invented in 1971 by Hans Camenzind at Signetics Corporation, the <strong>NE555 Timer</strong> remains one of the most widely manufactured and ubiquitous integrated circuits in electrical engineering history. Its enduring popularity stems from its rugged simplicity, high output current drive capability (up to $\pm 200\text{ mA}$, directly driving relays, LEDs, and audio transducers), wide operating voltage range ($4.5\text{V}$ to $16.0\text{V}$ for bipolar NE555; down to $2.0\text{V}$ for CMOS LMC555), and exceptional temperature stability ($\approx 50\text{ ppm/}^\circ\text{C}$).</p>

        <p>Internally, the 555 IC derives its name from its precision voltage divider network, which consists of three identical <strong>$5\text{ k}\Omega$ internal resistors</strong> connected in series between $V_{cc}$ (Pin 8) and Ground (Pin 1). This network establishes two immutable reference voltages: the Upper Threshold voltage at $\frac{2}{3} V_{cc}$ and the Lower Trigger voltage at $\frac{1}{3} V_{cc}$. Two internal analog comparators monitor these nodes against external pins, latching an internal RS flip-flop that controls an inverted output buffer (Pin 3) and an open-collector NPN discharge transistor (Pin 7).</p>

        <h2>Mathematical Formulations for Operating Modes</h2>

        <h3>1. Astable Multivibrator Mode (Free-Running Oscillator)</h3>
        <p>In astable configuration, Pins 2 (Trigger) and 6 (Threshold) are tied together directly to the top terminal of timing capacitor $C$. Timing resistor $R_1$ connects between $V_{cc}$ and Pin 7 (Discharge), while resistor $R_2$ connects between Pin 7 and the capacitor.</p>

        <p>During the charging half-cycle, the internal discharge transistor is turned off, and capacitor $C$ charges exponentially through $(R_1 + R_2)$ from $\frac{1}{3} V_{cc}$ toward $V_{cc}$. The duration that output Pin 3 remains HIGH ($T_H$) is governed by the natural logarithm of the voltage ratio:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$T_H = \ln(2) \cdot (R_1 + R_2) \cdot C \approx 0.693 \cdot (R_1 + R_2) \cdot C$$
        </div>

        <p>When capacitor voltage reaches $\frac{2}{3} V_{cc}$, the upper comparator fires, setting the flip-flop and turning on the discharge transistor (Pin 7). The capacitor now discharges strictly through $R_2$ to ground. The duration that output Pin 3 remains LOW ($T_L$) is:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #DC2626;">
          $$T_L = \ln(2) \cdot R_2 \cdot C \approx 0.693 \cdot R_2 \cdot C$$
        </div>

        <p>The total wave period ($T$) and resulting fundamental oscillation frequency ($f$) are:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$T = T_H + T_L = 0.693 \cdot (R_1 + 2 \cdot R_2) \cdot C$$
          $$f = \frac{1}{T} = \frac{1.44}{(R_1 + 2 \cdot R_2) \cdot C}$$
        </div>

        <p>The output duty cycle ($D$) represents the percentage of each cycle the output spends at high logic level:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$D = \frac{T_H}{T} \times 100\% = \frac{R_1 + R_2}{R_1 + 2 \cdot R_2} \times 100\%$$
        </div>

        <h3>2. Monostable Mode (One-Shot Pulse Generator)</h3>
        <p>In monostable mode, the circuit rests in a quiescent low state with capacitor $C$ shorted to ground through Pin 7. Applying a negative-going trigger pulse ($V_{\text{trig}} &lt; \frac{1}{3} V_{cc}$) to Pin 2 trips the lower comparator, turning off Pin 7 and forcing output Pin 3 HIGH. Capacitor $C$ charges exponentially through single timing resistor $R_1$ toward $V_{cc}$:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #EA580C;">
          $$v_C(t) = V_{cc} \cdot \left( 1 - e^{-t / (R_1 \cdot C)} \right)$$
        </div>
        <p>When $v_C(t)$ reaches $\frac{2}{3} V_{cc}$, the upper comparator resets the circuit. Solving for $t$ yields the output pulse width ($T_{\text{pulse}}$):</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$T_{\text{pulse}} = \ln(3) \cdot R_1 \cdot C \approx 1.1 \cdot R_1 \cdot C$$
        </div>

        <h2>Standard 555 Timing Component Selection Guidelines</h2>
        <p>To avoid unstable operation, parasitic re-triggering, or excessive power consumption, practical circuit designs must observe component boundary constraints:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Component Parameter</th>
                <th style="padding:0.75rem;">Recommended Range</th>
                <th style="padding:0.75rem;">Engineering Limit Rationale</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Resistor R1 Minimum</strong></td>
                <td style="padding:0.75rem;">$\ge 1\text{ k}\Omega$</td>
                <td style="padding:0.75rem;">Protects Pin 7 discharge transistor from exceeding its $200\text{ mA}$ maximum rating when shorted to $V_{cc}$.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Resistor R1 + R2 Maximum</strong></td>
                <td style="padding:0.75rem;">$\le 3.3\text{ M}\Omega$ (Bipolar) / $20\text{ M}\Omega$ (CMOS)</td>
                <td style="padding:0.75rem;">Input bias currents into Pins 2 and 6 ($0.5\text{ }\mu\text{A}$ on NE555) cause severe threshold voltage errors if timing resistance is excessive.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Capacitor C1 Minimum</strong></td>
                <td style="padding:0.75rem;">$\ge 100\text{ pF}$</td>
                <td style="padding:0.75rem;">Stray PCB trace capacitance ($5\text{ pF}$ to $15\text{ pF}$) degrades frequency calibration below $100\text{ pF}$.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Capacitor C1 Maximum</strong></td>
                <td style="padding:0.75rem;">$\le 1,000\text{ }\mu\text{F}$</td>
                <td style="padding:0.75rem;">Electrolytic capacitors suffer high DC dielectric leakage currents that can prevent voltage from ever reaching $\frac{2}{3} V_{cc}$.</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>Bypass Capacitor (Pin 5)</strong></td>
                <td style="padding:0.75rem;">$0.01\text{ }\mu\text{F}$ Ceramic ($10\text{ nF}$)</td>
                <td style="padding:0.75rem;">Decouples internal $\frac{2}{3} V_{cc}$ reference from supply rail switching transients and RF noise.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: 1 kHz Audio Tone Generator
          </h3>
          <p><strong>Scenario:</strong> An electronics designer requires a stable $1.0\text{ kHz}$ audible square wave tone generator using a standard NE555 timer. The designer selects a standard $0.01\text{ }\mu\text{F}$ ($10\text{ nF}$) film capacitor for timing stability and seeks standard $5\%$ resistors ($R_1$ and $R_2$) with a duty cycle close to $55\%$.</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Determine Required Total Resistance ($R_1 + 2 R_2$):</strong>
              $$f = \frac{1.44}{(R_1 + 2 R_2) \cdot C} \implies R_1 + 2 R_2 = \frac{1.44}{1,000\text{ Hz} \times 10 \times 10^{-9}\text{ F}} = \frac{1.44}{10^{-5}} = 144,000\text{ }\Omega = 144\text{ k}\Omega$$
            </li>
            <li><strong>Select Resistor Ratio for ~55% Duty Cycle:</strong>
              $$D = \frac{R_1 + R_2}{R_1 + 2 R_2} = 0.55 \implies R_1 + R_2 = 0.55 \times 144\text{ k}\Omega = 79.2\text{ k}\Omega$$
              $$R_2 = 144\text{ k}\Omega - 79.2\text{ k}\Omega = 64.8\text{ k}\Omega$$
              $$R_1 = 79.2\text{ k}\Omega - 64.8\text{ k}\Omega = 14.4\text{ k}\Omega$$
            </li>
            <li><strong>Map to Nearest Standard E24 Resistor Values:</strong>
              Select standard $R_1 = 15\text{ k}\Omega$ and $R_2 = 68\text{ k}\Omega$.
            </li>
            <li><strong>Verify Actual Frequency &amp; Pulse Intervals:</strong>
              $$R_1 + 2 R_2 = 15 + 2(68) = 151\text{ k}\Omega$$
              $$f = \frac{1.44}{151,000 \times 10 \times 10^{-9}} = \frac{1.44}{0.00151} \approx 953.6\text{ Hz}$$
              $$T_H = 0.693 \times (15\text{k} + 68\text{k}) \times 10\text{nF} = 0.693 \times 83,000 \times 10^{-8} \approx 0.575\text{ ms}$$
              $$T_L = 0.693 \times 68\text{k} \times 10\text{nF} = 0.693 \times 68,000 \times 10^{-8} \approx 0.471\text{ ms}$$
              $$D = \frac{0.575}{0.575 + 0.471} \times 100\% = 55.0\%$$
            </li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why does a classic NE555 timer cause power rail supply glitches?</h4>
            <p style="margin:0;color:#64748B;">Standard bipolar NE555 ICs use an output push-pull totem pole stage consisting of an upper NPN Darlington and lower NPN transistor. During logic transitions, both output transistors momentarily conduct simultaneously for approximately 100 nanoseconds, drawing a massive "shoot-through" current spike up to 300 to 400 mA from the Vcc rail. Always place a 0.1 μF ceramic decoupling capacitor in parallel with a 10 μF tantalum capacitor immediately adjacent to Pins 8 and 1.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is the function of Control Voltage (Pin 5) on the 555 timer?</h4>
            <p style="margin:0;color:#64748B;">Pin 5 connects directly to the internal 2/3 Vcc node of the precision resistor divider. Applying an external modulating analog voltage to Pin 5 alters the upper threshold voltage, dynamically modulating the charging interval. This enables pulse-width modulation (PWM), frequency modulation (FM), and ramp generation. If unused, connect Pin 5 to ground through a 0.01 μF capacitor to prevent high-frequency noise from inducing timing jitter.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What are the advantages of CMOS 555 timers (like LMC555, TLC555) over classic bipolar NE555?</h4>
            <p style="margin:0;color:#64748B;">CMOS 555 variants use MOSFET gates that draw near-zero input bias current (< 10 pA vs 500 nA for NE555), allowing the use of high timing resistors up to 100 MΩ for ultra-long multi-hour timers. Furthermore, CMOS versions generate zero shoot-through supply glitches, consume only 100 to 250 μA of quiescent current, operate down to 1.5V or 2.0V, and can oscillate up to 2 to 3 MHz.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why should Reset (Pin 4) never be left floating in a 555 circuit?</h4>
            <p style="margin:0;color:#64748B;">Pin 4 is an active-low asynchronous reset input. When pulled below 0.7V, it immediately forces output Pin 3 LOW and discharges the timing capacitor through Pin 7 regardless of comparator states. If Pin 4 is left floating, electrostatic charge and EMI can randomly trip the reset threshold, causing erratic oscillator dropout. Always tie Pin 4 directly to Vcc if external reset is not required.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Electronics &amp; IC Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="555-timer-calculator.html" style="font-weight:700;color:#2563EB;">⏱️ 555 Timer Astable/Mono</a></li>
          <li><a href="led-resistor-calculator.html" style="color:#475569;">💡 LED Series Resistor</a></li>
          <li><a href="parallel-resistor-calculator.html" style="color:#475569;">⚡ Parallel Resistor (Req)</a></li>
          <li><a href="resistor-color-code-calculator.html" style="color:#475569;">🎨 Resistor Color Code</a></li>
          <li><a href="ohms-law-calculator.html" style="color:#475569;">⚡ Ohm's Law Calculator</a></li>
          <li><a href="battery-life-calculator.html" style="color:#475569;">🔋 Battery Life &amp; Runtime</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Electrical Systems</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="power-factor-calculator.html" style="color:#475569;">⚡ Power Factor Correction</a></li>
          <li><a href="short-circuit-calculator.html" style="color:#475569;">💥 Short-Circuit (IEC 60909)</a></li>
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
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">Analog Design References</div>
        <div style="font-size:0.85rem;line-height:2;">
          Signetics NE555 Timer Handbook<br>
          Texas Instruments LMC555 CMOS Datasheet<br>
          IEEE Standard for Electronic Pulse Measurement
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Analog Electronics Computational Suite.
    </div>
  </footer>

  <script>
    function toggleModeFields() {
      const mode = document.getElementById('timer-mode').value;
      const gR2 = document.getElementById('group-r2');
      if (mode === 'monostable') {
        gR2.style.display = 'none';
        document.getElementById('res-primary-label').textContent = 'Monostable One-Shot Pulse Width';
      } else {
        gR2.style.display = 'block';
        document.getElementById('res-primary-label').textContent = 'Astable Oscillation Frequency';
      }
      runTimerCalc();
    }

    function runTimerCalc() {
      const mode = document.getElementById('timer-mode').value;
      const r1Val = parseFloat(document.getElementById('res-r1').value) || 10;
      const r1Mult = parseFloat(document.getElementById('unit-r1').value) || 1000;
      const R1 = r1Val * r1Mult; // in Ohms

      const cVal = parseFloat(document.getElementById('cap-c').value) || 10;
      const cMult = parseFloat(document.getElementById('unit-c').value) || 1e-6;
      const C = cVal * cMult; // in Farads

      if (mode === 'astable') {
        const r2Val = parseFloat(document.getElementById('res-r2').value) || 47;
        const r2Mult = parseFloat(document.getElementById('unit-r2').value) || 1000;
        const R2 = r2Val * r2Mult; // in Ohms

        // Th = 0.693 * (R1 + R2) * C
        const Th = 0.693147 * (R1 + R2) * C;
        // Tl = 0.693 * R2 * C
        const Tl = 0.693147 * R2 * C;
        const T = Th + Tl;
        const freq = T > 0 ? 1.0 / T : 0;
        const duty = T > 0 ? (Th / T) * 100.0 : 0;
        const tau = (R1 + R2) * C;

        let freqStr = freq >= 1000 ? (freq / 1000).toFixed(2) + ' kHz' : freq.toFixed(2) + ' Hz';
        if (freq < 1.0) freqStr = freq.toFixed(3) + ' Hz';

        let tStr = T >= 1.0 ? T.toFixed(3) + ' seconds' : (T * 1000).toFixed(1) + ' milliseconds';

        document.getElementById('res-primary-val').textContent = freqStr;
        document.getElementById('res-primary-sub').textContent = 'Total Period T = ' + tStr;
        document.getElementById('res-th-label').textContent = 'High Time (T_high)';
        document.getElementById('res-th-val').textContent = Th >= 1.0 ? Th.toFixed(3) + ' s' : (Th * 1000).toFixed(1) + ' ms';
        document.getElementById('res-tl-label').textContent = 'Low Time (T_low)';
        document.getElementById('res-tl-val').textContent = Tl >= 1.0 ? Tl.toFixed(3) + ' s' : (Tl * 1000).toFixed(1) + ' ms';
        document.getElementById('res-duty-val').textContent = duty.toFixed(1) + ' %';
        document.getElementById('res-tau-val').textContent = tau.toFixed(3) + ' s';
      } else {
        // Monostable: T_pulse = 1.1 * R1 * C
        const Tpulse = 1.098612 * R1 * C; // ln(3) * R1 * C
        let pulseStr = Tpulse >= 1.0 ? Tpulse.toFixed(3) + ' seconds' : (Tpulse * 1000).toFixed(1) + ' milliseconds';
        if (Tpulse < 0.001) pulseStr = (Tpulse * 1e6).toFixed(1) + ' microseconds';

        document.getElementById('res-primary-val').textContent = pulseStr;
        document.getElementById('res-primary-sub').textContent = 'Single Pulse Output (ln(3) \u00D7 R1 \u00D7 C)';
        document.getElementById('res-th-label').textContent = 'Pulse Duration (High)';
        document.getElementById('res-th-val').textContent = pulseStr;
        document.getElementById('res-tl-label').textContent = 'Quiescent State';
        document.getElementById('res-tl-val').textContent = '0V (Ground)';
        document.getElementById('res-duty-val').textContent = 'N/A (One-Shot)';
        document.getElementById('res-tau-val').textContent = (R1 * C).toFixed(3) + ' s';
      }
    }

    window.addEventListener('DOMContentLoaded', runTimerCalc);
  </script>
</body>
</html>
"""

# ==========================================
# 2. LED RESISTOR CALCULATOR
# ==========================================
TOOL_LED = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LED Resistor Calculator — Current Limiting Resistor &amp; Power Rating</title>
  <meta name="description" content="Calculate LED current limiting series resistor resistance (Ohms), power dissipation (Watts), and nearest E24/E12 standard resistor values for single and series LED arrays.">
  <meta name="keywords" content="led resistor calculator, led series resistor, led current limiting resistor, led resistance formula, led forward voltage drop, resistor power rating led, e24 resistor values">
  <link rel="canonical" href="https://calchub.org/led-resistor-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "LED Series Current Limiting Resistor Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates required series resistance, thermal power dissipation, and standard E12/E24 commercial resistor selections for single and series LED circuits."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Why does a light emitting diode (LED) always require a series current limiting resistor?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A light emitting diode is a non-linear PN junction semiconductor with an exponential forward I-V characteristic and negative temperature coefficient of resistance. Once supply voltage exceeds its forward threshold (Vf), its internal dynamic resistance plummets toward near zero. Connecting an LED directly to a constant voltage source causes thermal runaway, drawing destructive currents that melt the wire bond within milliseconds. A series resistor enforces a fixed linear voltage drop and limits forward current to safe design ratings."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for calculating an LED series resistor?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per Ohm's Law and Kirchhoff's Voltage Law (KVL), the series resistance is: R = (Vs - N × Vf) / If, where Vs is the DC power supply voltage in Volts, N is the number of series LEDs, Vf is the forward voltage drop per LED in Volts, and If is the desired forward current in Amperes (typically 0.015A to 0.020A for standard indicator LEDs)."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calculate the power rating required for an LED resistor?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The power dissipated as heat in the series resistor is: P = (Vs - N × Vf) × If = If² × R. To prevent thermal overheating and failure, good engineering practice mandates a 2× derating safety factor. For example, if calculated dissipation is 0.18 Watts, specify at least a 1/2 Watt (0.50W) resistor rather than a 1/4 Watt (0.25W) unit."
            }
          },
          {
            "@type": "Question",
            "name": "Why shouldn't you wire multiple LEDs directly in parallel with a single shared resistor?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Paralleling LEDs across a single shared resistor causes 'current hogging'. Because forward voltage Vf varies slightly between individual diodes due to manufacturing tolerances (e.g., 2.05V vs 2.15V), the LED with the lowest Vf will conduct far more current. As it conducts more current, it heats up, further lowering its Vf and drawing even more current (thermal runaway) until it burns out. Once it fails open-circuit, the remaining LEDs absorb the excess current and burn out in rapid cascade. Always give every parallel branch its own dedicated resistor."
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
      <span class="category-tag">⚡ Optoelectronics &amp; Circuit Design</span>
      <h1 class="calc-page-title">LED Resistor Calculator</h1>
      <p class="calc-page-desc">Calculate the exact series current limiting resistance, thermal wattage dissipation, and standard commercial E24 resistor selections for single and multi-LED strings.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>💡</span> Power Supply &amp; Diode Parameters</h2>
            <span class="status-info">Ohm's &amp; Joule's Laws</span>
          </div>
          <form id="led-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="supply-voltage">Power Supply Voltage ($V_s$)</label>
                <input type="number" id="supply-voltage" class="form-control" value="12.0" min="1.0" max="1000.0" step="0.1" oninput="runLedCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="led-type">LED Color / Forward Voltage ($V_f$)</label>
                <select id="led-type" class="form-control" onchange="applyLedColor()">
                  <option value="2.0" selected>Red LED (Standard / 2.0 V)</option>
                  <option value="2.1">Orange / Amber LED (2.1 V)</option>
                  <option value="2.2">Yellow LED (2.2 V)</option>
                  <option value="3.2">Green LED (Pure / 3.2 V)</option>
                  <option value="3.3">Blue LED (Standard / 3.3 V)</option>
                  <option value="3.3">White LED (High Brightness / 3.3 V)</option>
                  <option value="1.5">Infrared (IR) LED (1.5 V)</option>
                  <option value="3.6">UV / Ultraviolet LED (3.6 V)</option>
                  <option value="custom">Custom Forward Voltage</option>
                </select>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="forward-voltage">LED Forward Voltage Drop ($V_f$ in V)</label>
                <input type="number" id="forward-voltage" class="form-control" value="2.0" min="0.5" max="50.0" step="0.1" oninput="runLedCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="forward-current">Desired Forward Current ($I_f$ in mA)</label>
                <input type="number" id="forward-current" class="form-control" value="20.0" min="0.1" max="5000.0" step="1.0" oninput="runLedCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="num-leds">Number of Series LEDs in String ($N$)</label>
                <input type="number" id="num-leds" class="form-control" value="1" min="1" max="100" step="1" oninput="runLedCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="resistor-series">Standard Resistor Series</label>
                <select id="resistor-series" class="form-control" onchange="runLedCalc()">
                  <option value="e24" selected>E24 Standard (5% Tolerance — Most Common)</option>
                  <option value="e12">E12 Standard (10% Tolerance)</option>
                  <option value="e96">E96 Precision (1% Metal Film)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runLedCalc()">Calculate Resistor Specs</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Hardware Bill-of-Materials</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Resistor Sizing &amp; Power Rating</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Nearest Standard Commercial Resistor</div>
            <div id="res-standard-ohm" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">510 Ω</div>
            <div id="res-color-code" style="font-size:1.05rem;color:#2563EB;font-weight:700;">Green · Brown · Brown · Gold (5%)</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Exact Theoretical Resistance</span>
              <span id="res-exact-ohm" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">500.0 Ω</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Resistor Power Dissipation</span>
              <span id="res-resistor-power" class="result-val" style="font-size:1.1rem;font-weight:700;color:#DC2626;">0.200 Watts (200 mW)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Recommended Power Rating</span>
              <span id="res-rec-power" class="result-val" style="font-size:1.1rem;font-weight:700;color:#059669;">1/2 Watt (0.50 W — 2× Margin)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Actual Current with Standard Resistor</span>
              <span id="res-actual-current" class="result-val" style="font-size:1.1rem;font-weight:700;color:#7C3AED;">19.61 mA</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:0.85rem;color:#166534;">
            <strong>🎨 Color Code Lookup:</strong> Verify resistor color bands with our <a href="resistor-color-code-calculator.html" style="color:#166534;font-weight:700;">Resistor Color Code Calculator</a> or analyze network branch currents with the <a href="parallel-resistor-calculator.html" style="color:#166534;font-weight:700;">Parallel Resistor Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Physics of Semiconductor Light Emission &amp; Negative Resistance</h2>
        <p>A light emitting diode (LED) is a specialized compound semiconductor PN junction diode composed of materials such as Gallium Arsenide (GaAs), Gallium Nitride (GaN), or Indium Gallium Aluminum Phosphide (InGaAlP). When forward biased, electrons from the N-region and holes from the P-region are injected into the active junction zone where they undergo radiative recombination, releasing discrete packets of electromagnetic radiation (photons) whose wavelength ($\lambda$) corresponds to the material's semiconductor bandgap energy ($E_g = \frac{h \cdot c}{\lambda}$).</p>

        <p>Unlike linear ohmic resistors, LEDs are non-linear electronic devices governed by the Shockley diode equation:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$I = I_s \cdot \left( e^{\frac{q \cdot V_d}{\eta \cdot k_B \cdot T}} - 1 \right)$$
        </div>
        <p>Below the threshold forward voltage ($V_f$), the diode is virtually non-conductive. Once applied voltage reaches $V_f$, the curve rises nearly vertically. A minute increase in voltage of just $0.1\text{ V}$ can cause forward current to jump by $300\%$ to $500\%$. Furthermore, as the junction heats up during conduction, its forward voltage drop decreases at approximately $-2\text{ mV/}^\circ\text{C}$ (negative thermal coefficient). If connected directly to a fixed voltage rail without a series ballast resistor, this positive thermal feedback loop induces <strong>thermal runaway</strong>, destroying the diode in fractions of a second.</p>

        <h2>Mathematical Current Limiting Formulations</h2>

        <h3>1. Calculating Series Resistance ($R$)</h3>
        <p>By applying Kirchhoff's Voltage Law (KVL) around a single closed circuit containing a DC supply voltage $V_s$, a current limiting resistor $R$, and $N$ series connected LEDs:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$V_s - V_R - \sum_{i=1}^N V_{f,i} = 0$$
          $$V_R = V_s - (N \cdot V_f)$$
        </div>
        <p>Applying Ohm's Law ($R = \frac{V_R}{I_f}$), the exact required resistance is:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$R = \frac{V_s - (N \cdot V_f)}{I_f}$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$V_s$</strong> = DC power supply voltage in Volts ($\text{V}$).</li>
          <li><strong>$N$</strong> = Total quantity of series LEDs wired in the string.</li>
          <li><strong>$V_f$</strong> = Forward voltage drop of each LED in Volts ($\text{V}$).</li>
          <li><strong>$I_f$</strong> = Target forward design current in Amperes ($\text{A}$). Note: convert milliamperes to amperes ($\text{mA} \div 1000$).</li>
        </ul>

        <h3>2. Resistor Thermal Power Dissipation &amp; Derating</h3>
        <p>Electric current passing through the series resistor converts electrical potential energy into thermal heat energy via Joule heating:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #DC2626;">
          $$P_{\text{resistor}} = V_R \cdot I_f = I_f^2 \cdot R = \frac{(V_s - N \cdot V_f)^2}{R}$$
        </div>
        <p>Standard industrial component guidelines mandate a <strong>$50\%$ thermal derating rule ($2\times$ wattage factor)</strong>. Operating a resistor continuously at $100\%$ of its nominal wattage rating elevates surface temperatures above $100^\circ\text{C}$, scorching PCB substrate materials, drifting resistance value, and inducing premature solder fatigue.</p>

        <h2>LED Color, Forward Voltage ($V_f$) &amp; Semiconductor Bandgap Table</h2>
        <p>Because photon energy is inversely proportional to wavelength, shorter wavelength light (blue, ultraviolet) requires higher bandgap energy, directly dictating higher forward operating voltages:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Color Spectrum</th>
                <th style="padding:0.75rem;">Semiconductor Material</th>
                <th style="padding:0.75rem;">Wavelength ($\lambda$)</th>
                <th style="padding:0.75rem;">Typical $V_f$ Drop</th>
                <th style="padding:0.75rem;">Typical $I_f$ Rating</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Infrared (IR)</strong></td>
                <td style="padding:0.75rem;">Gallium Arsenide (GaAs)</td>
                <td style="padding:0.75rem;">850 – 940 nm</td>
                <td style="padding:0.75rem;">1.2 – 1.6 V</td>
                <td style="padding:0.75rem;">20 – 50 mA</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Red</strong></td>
                <td style="padding:0.75rem;">AlGaAs / GaAsP</td>
                <td style="padding:0.75rem;">620 – 660 nm</td>
                <td style="padding:0.75rem;">1.8 – 2.2 V</td>
                <td style="padding:0.75rem;">15 – 20 mA</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Orange / Amber</strong></td>
                <td style="padding:0.75rem;">GaAsP / AlInGaP</td>
                <td style="padding:0.75rem;">590 – 610 nm</td>
                <td style="padding:0.75rem;">2.0 – 2.3 V</td>
                <td style="padding:0.75rem;">20 mA</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Yellow</strong></td>
                <td style="padding:0.75rem;">GaAsP / AlInGaP</td>
                <td style="padding:0.75rem;">570 – 590 nm</td>
                <td style="padding:0.75rem;">2.1 – 2.4 V</td>
                <td style="padding:0.75rem;">20 mA</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Pure Green</strong></td>
                <td style="padding:0.75rem;">Indium Gallium Nitride (InGaN)</td>
                <td style="padding:0.75rem;">515 – 535 nm</td>
                <td style="padding:0.75rem;">3.0 – 3.4 V</td>
                <td style="padding:0.75rem;">20 mA</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Blue</strong></td>
                <td style="padding:0.75rem;">Indium Gallium Nitride (InGaN)</td>
                <td style="padding:0.75rem;">450 – 475 nm</td>
                <td style="padding:0.75rem;">3.1 – 3.5 V</td>
                <td style="padding:0.75rem;">20 mA</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>White (Phosphor)</strong></td>
                <td style="padding:0.75rem;">InGaN Blue + YAG:Ce Phosphor</td>
                <td style="padding:0.75rem;">Broad Spectrum</td>
                <td style="padding:0.75rem;">3.1 – 3.6 V</td>
                <td style="padding:0.75rem;">20 – 30 mA</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: 12V Automotive Dash LED String
          </h3>
          <p><strong>Scenario:</strong> An automotive electronics engineer is designing an instrument cluster backlighting circuit powered by a nominal $12.0\text{V}$ vehicle accessory rail. The design calls for three series-connected blue indicator LEDs ($V_f = 3.3\text{ V}$ each), operating at a conservative $I_f = 15\text{ mA}$ ($0.015\text{ A}$) to maximize service life.</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Calculate Cumulative LED Forward Voltage Drop:</strong>
              $$V_{\text{LED, total}} = N \cdot V_f = 3 \times 3.3\text{ V} = 9.9\text{ V}$$
            </li>
            <li><strong>Determine Voltage Drop Across the Series Resistor:</strong>
              $$V_R = V_s - V_{\text{LED, total}} = 12.0\text{ V} - 9.9\text{ V} = 2.1\text{ V}$$
            </li>
            <li><strong>Calculate Exact Resistance ($R$):</strong>
              $$R = \frac{V_R}{I_f} = \frac{2.1\text{ V}}{0.015\text{ A}} = 140.0\text{ }\Omega$$
            </li>
            <li><strong>Select Standard E24 Commercial Resistor:</strong>
              The nearest standard E24 resistor value is <strong>$150\text{ }\Omega$</strong> (Brown · Green · Brown · Gold).
            </li>
            <li><strong>Verify Actual Operating Current with 150 Ω Resistor:</strong>
              $$I_{\text{actual}} = \frac{2.1\text{ V}}{150\text{ }\Omega} = 0.014\text{ A} = 14.0\text{ mA}$$
            </li>
            <li><strong>Calculate Resistor Heat Dissipation &amp; Specify Wattage:</strong>
              $$P = V_R \times I_{\text{actual}} = 2.1\text{ V} \times 0.014\text{ A} = 0.0294\text{ Watts } (29.4\text{ mW})$$
              With a $2\times$ derating requirement ($2 \times 29.4\text{ mW} = 58.8\text{ mW}$), a standard miniature <strong>$1/4\text{ Watt}$ ($0.25\text{W}$ / $250\text{ mW}$)</strong> carbon film or SMD 0805 resistor will run cool and provide decades of continuous operation.
            </li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What happens if the supply voltage is lower than the LED forward voltage?</h4>
            <p style="margin:0;color:#64748B;">If DC supply voltage Vs is less than total string forward voltage (N × Vf), the diode remains in its non-conductive region. No current flows through the circuit, and the LED will emit zero light. For instance, powering a 3.3V blue LED with a 3.0V battery requires an active inductive DC-DC boost converter or charge-pump driver (like a Joule Thief) to step voltage above the diode's bandgap threshold.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">When should you use an active constant current driver instead of a resistor?</h4>
            <p style="margin:0;color:#64748B;">Resistors are simple and cost-effective for low-power indicator LEDs (< 50 mA). However, in high-power lighting (1W, 3W, 10W COBs drawing 350 mA to 3 A), or in automotive circuits where battery voltage swings between 11.5V and 14.8V, series resistors waste excessive battery power as heat and cause visible brightness flickering. High-power systems require switch-mode buck constant current regulators (e.g., based on PT4115 or LM3409) that maintain steady amperage with > 90% electrical efficiency.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What are the standard E-series resistor values (E12, E24, E96)?</h4>
            <p style="margin:0;color:#64748B;">Standardized by the International Electrotechnical Commission (IEC 60063), E-series divide each decade logarithmic decade (e.g., 10 to 100 Ω) into mathematically equal geometric intervals based on component tolerance. E12 (10% tolerance) provides 12 values per decade (10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82). E24 (5% tolerance) provides 24 values per decade, and E96 (1% tolerance) provides 96 precision values.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Can an AC power supply be used to power LEDs directly with a resistor?</h4>
            <p style="margin:0;color:#64748B;">LEDs only conduct during the forward half-cycle of an AC wave, but have very low peak reverse breakdown voltage ratings (typically V_R,max is only 5V). Applying unrectified 12V or 120V AC will reverse-bias the diode past breakdown, causing avalanche punch-through and destroying the chip. Always use a full-wave bridge rectifier, or wire an antiparallel 1N4148 diode across the LED to clamp reverse voltage safely below 0.7V.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Electronics &amp; Hardware</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="led-resistor-calculator.html" style="font-weight:700;color:#2563EB;">💡 LED Series Resistor</a></li>
          <li><a href="555-timer-calculator.html" style="color:#475569;">⏱️ 555 Timer Astable/Mono</a></li>
          <li><a href="parallel-resistor-calculator.html" style="color:#475569;">⚡ Parallel Resistor (Req)</a></li>
          <li><a href="resistor-color-code-calculator.html" style="color:#475569;">🎨 Resistor Color Code</a></li>
          <li><a href="ohms-law-calculator.html" style="color:#475569;">⚡ Ohm's Law Calculator</a></li>
          <li><a href="battery-life-calculator.html" style="color:#475569;">🔋 Battery Life &amp; Runtime</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Power &amp; Installation Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="voltage-drop-calculator.html" style="color:#475569;">📉 Voltage Drop Calculator</a></li>
          <li><a href="wire-ampacity-calculator.html" style="color:#475569;">🔌 Wire Ampacity (NEC)</a></li>
          <li><a href="conduit-fill-calculator.html" style="color:#475569;">🪢 Conduit Fill Calculator</a></li>
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
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">Component Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          IEC 60063 Preferred Number Series for Resistors<br>
          JEDEC JESD22-A108 LED Reliability Testing<br>
          EIA-RS-279 Color Coding of Fixed Resistors
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Optoelectronics &amp; Circuit Design Suite.
    </div>
  </footer>

  <script>
    // Standard E24 base numbers
    const E24 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1];
    const E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2];

    function applyLedColor() {
      const val = document.getElementById('led-type').value;
      if (val !== 'custom') {
        document.getElementById('forward-voltage').value = val;
      }
      runLedCalc();
    }

    function findNearestStandard(rTarget, seriesList) {
      if (rTarget <= 0) return 0;
      const decade = Math.pow(10, Math.floor(Math.log10(rTarget)));
      const norm = rTarget / decade;

      let bestVal = seriesList[0] * decade;
      let minDiff = Math.abs(rTarget - bestVal);

      for (let i = 0; i < seriesList.length; i++) {
        const candidate = seriesList[i] * decade;
        const diff = Math.abs(rTarget - candidate);
        if (diff < minDiff) {
          minDiff = diff;
          bestVal = candidate;
        }
        // Also check upper decade first element
        const candidateUp = seriesList[i] * decade * 10;
        const diffUp = Math.abs(rTarget - candidateUp);
        if (diffUp < minDiff) {
          minDiff = diffUp;
          bestVal = candidateUp;
        }
      }
      return bestVal;
    }

    const COLOR_NAMES = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Gray', 'White'];

    function get4BandCode(rVal) {
      if (rVal < 1) return 'Special Value (< 1 Ω)';
      const str = Math.round(rVal).toString();
      let d1 = 0, d2 = 0, mult = 0;
      if (rVal < 10) {
        d1 = Math.floor(rVal);
        d2 = Math.round((rVal - d1) * 10);
        return COLOR_NAMES[d1] + ' \u00B7 ' + COLOR_NAMES[d2] + ' \u00B7 Gold \u00B7 Gold (5%)';
      }
      const decade = Math.floor(Math.log10(rVal));
      const multVal = decade - 1;
      const firstTwo = Math.round(rVal / Math.pow(10, multVal));
      d1 = Math.floor(firstTwo / 10);
      d2 = firstTwo % 10;
      
      const c1 = COLOR_NAMES[d1] || 'Brown';
      const c2 = COLOR_NAMES[d2] || 'Black';
      const cMult = COLOR_NAMES[multVal] || 'Brown';
      return c1 + ' \u00B7 ' + c2 + ' \u00B7 ' + cMult + ' \u00B7 Gold (5%)';
    }

    function runLedCalc() {
      const vs = Math.max(0.1, parseFloat(document.getElementById('supply-voltage').value) || 12.0);
      const vf = Math.max(0.1, parseFloat(document.getElementById('forward-voltage').value) || 2.0);
      const ifMa = Math.max(0.01, parseFloat(document.getElementById('forward-current').value) || 20.0);
      const ifAmp = ifMa / 1000.0;
      const n = Math.max(1, parseInt(document.getElementById('num-leds').value) || 1);
      const seriesType = document.getElementById('resistor-series').value;

      const totalVf = n * vf;
      const vr = vs - totalVf;

      if (vr <= 0) {
        document.getElementById('res-standard-ohm').textContent = 'Insufficient Voltage';
        document.getElementById('res-color-code').textContent = 'Supply ' + vs.toFixed(1) + 'V < LEDs ' + totalVf.toFixed(1) + 'V';
        document.getElementById('res-exact-ohm').textContent = '0 Ω';
        document.getElementById('res-resistor-power').textContent = '0 W';
        document.getElementById('res-rec-power').textContent = 'Increase Vs or reduce LED count';
        document.getElementById('res-actual-current').textContent = '0 mA';
        return;
      }

      const rExact = vr / ifAmp;
      const series = seriesType === 'e12' ? E12 : E24;
      const rStandard = findNearestStandard(rExact, series);

      const pActualResistor = (vr * vr) / rStandard;
      const ifActualMa = (vr / rStandard) * 1000.0;

      let recWattage = '1/4 Watt (0.25 W)';
      if (pActualResistor > 0.125 && pActualResistor <= 0.25) recWattage = '1/2 Watt (0.50 W)';
      else if (pActualResistor > 0.25 && pActualResistor <= 0.50) recWattage = '1 Watt (1.00 W)';
      else if (pActualResistor > 0.50 && pActualResistor <= 1.0) recWattage = '2 Watts (2.00 W)';
      else if (pActualResistor > 1.0) recWattage = (Math.ceil(pActualResistor * 2)) + ' Watts (Wirewound / Ceramic)';

      let ohmDisplay = '';
      if (rStandard >= 1000000) ohmDisplay = (rStandard / 1000000).toFixed(2) + ' M\u03A9';
      else if (rStandard >= 1000) ohmDisplay = (rStandard / 1000).toFixed(1) + ' k\u03A9 (' + Math.round(rStandard) + ' \u03A9)';
      else ohmDisplay = Math.round(rStandard) + ' \u03A9';

      document.getElementById('res-standard-ohm').textContent = ohmDisplay;
      document.getElementById('res-color-code').textContent = get4BandCode(rStandard);
      document.getElementById('res-exact-ohm').textContent = rExact.toFixed(1) + ' \u03A9';
      document.getElementById('res-resistor-power').textContent = pActualResistor.toFixed(3) + ' Watts (' + (pActualResistor * 1000).toFixed(0) + ' mW)';
      document.getElementById('res-rec-power').textContent = recWattage;
      document.getElementById('res-actual-current').textContent = ifActualMa.toFixed(2) + ' mA';
    }

    window.addEventListener('DOMContentLoaded', runLedCalc);
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "555-timer-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_555)
print("[PASS] 555-timer-calculator.html generated successfully!")

with open(os.path.join(BASE_DIR, "led-resistor-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_LED)
print("[PASS] led-resistor-calculator.html generated successfully!")
