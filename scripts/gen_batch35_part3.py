# -*- coding: utf-8 -*-
"""
Generator for Batch 35 - Part 3
Tools:
5. rc-time-constant-calculator.html
6. rl-time-constant-calculator.html
"""

import os

HEADER_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://calchub.com/{slug}.html">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
    <script type="application/ld+json">
{schema_json}
    </script>
</head>
<body>
    <header class="site-header">
        <div class="header-container">
            <a href="index.html" class="logo">CalcHub</a>
            <nav class="nav-links">
                <a href="index.html">Home</a>
                <a href="math.html">Math &amp; Stats</a>
                <a href="converter.html">Converters</a>
                <a href="engineering.html">Engineering</a>
                <a href="finance.html">Finance</a>
            </nav>
        </div>
    </header>
    <div class="container">
        <div class="main-wrapper">
            <main class="content-area">
                <nav class="breadcrumb">
                    <a href="index.html">Home</a> &gt; <a href="engineering.html">Engineering &amp; Electronics</a> &gt; <span>{h1}</span>
                </nav>
                <div class="calculator-card">
                    <div class="calc-header">
                        <h1>{h1}</h1>
                        <p class="calc-desc">{short_desc}</p>
                    </div>
                    {calc_ui}
                </div>
                <article class="article-body">
                    {article_content}
                </article>
            </main>
            <aside class="sidebar">
                <div class="sidebar-card">
                    <h3>Related Engineering Tools</h3>
                    <ul class="sidebar-links">
                        <li><a href="voltage-divider-calculator.html">Voltage Divider Calculator</a></li>
                        <li><a href="parallel-resistance-calculator.html">Parallel Resistance Calculator</a></li>
                        <li><a href="capacitor-energy-calculator.html">Capacitor Energy Calculator</a></li>
                        <li><a href="resonant-frequency-calculator.html">Resonant Frequency Calculator</a></li>
                        <li><a href="rc-time-constant-calculator.html">RC Time Constant Calculator</a></li>
                        <li><a href="rl-time-constant-calculator.html">RL Time Constant Calculator</a></li>
                        <li><a href="zener-diode-calculator.html">Zener Diode Calculator</a></li>
                        <li><a href="lm317-calculator.html">LM317 Voltage Regulator</a></li>
                        <li><a href="ohms-law-calculator.html">Ohm's Law Calculator</a></li>
                        <li><a href="frequency-calculator.html">Frequency Calculator</a></li>
                    </ul>
                </div>
            </aside>
        </div>
    </div>
    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>About CalcHub</h4>
                    <p>CalcHub delivers rigorous, laboratory-verified computational tools for electrical engineers, physicists, and system designers.</p>
                </div>
                <div class="footer-col">
                    <h4>Calculator Hubs</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">All Calculators</a></li>
                        <li><a href="math.html">Mathematics &amp; Statistics</a></li>
                        <li><a href="converter.html">Unit Converters</a></li>
                        <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Transient Analysis</h4>
                    <ul class="footer-links">
                        <li><a href="rc-time-constant-calculator.html">RC Time Constant</a></li>
                        <li><a href="rl-time-constant-calculator.html">RL Time Constant</a></li>
                        <li><a href="resonant-frequency-calculator.html">LC Resonant Circuit</a></li>
                        <li><a href="capacitor-energy-calculator.html">Capacitor Energy</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CalcHub. All rights reserved. Precise transient and steady-state circuit analysis engines.</p>
            </div>
        </div>
    </footer>
    <script>
    {calc_js}
    </script>
</body>
</html>
"""

# ==============================================================================
# TOOL 5: rc-time-constant-calculator.html
# ==============================================================================
TOOL5_SLUG = "rc-time-constant-calculator"
TOOL5_TITLE = "RC Time Constant Calculator - Tau, Cutoff Frequency & Transient Response"
TOOL5_DESC = "Calculate RC circuit time constant (tau = R*C), low-pass filter cutoff frequency (fc = 1/(2*pi*RC)), 10%-90% rise time, and charging/discharging voltage at time t."
TOOL5_H1 = "RC Time Constant Calculator"
TOOL5_SHORT = "Compute circuit time constant (&tau; = RC), 3dB cutoff frequency, 10% to 90% rise time, and transient capacitor voltage curves."

TOOL5_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "RC Time Constant Calculator",
      "url": "https://calchub.com/rc-time-constant-calculator.html",
      "description": "Calculates RC time constant tau, low-pass filter cutoff frequency, rise time, and instantaneous transient charging and discharging voltages.",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
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
          "name": "What is the physical meaning of one time constant (1 tau) in an RC circuit?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One time constant tau = R * C represents the time required for a charging capacitor to reach 1 - 1/e = 63.21% of its ultimate steady-state supply voltage, or for a discharging capacitor to decay to 1/e = 36.79% of its initial charge."
          }
        },
        {
          "@type": "Question",
          "name": "How many time constants does it take to fully charge a capacitor?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Theoretically, exponential curves never reach 100%. In practical engineering, a capacitor is considered fully charged at 5 time constants (5 tau), at which point it has reached 99.33% of the supply voltage."
          }
        },
        {
          "@type": "Question",
          "name": "How is the RC time constant related to cutoff frequency (fc)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The -3 dB cutoff frequency of a first-order RC low-pass or high-pass filter is inversely proportional to tau: f_c = 1 / (2 * pi * R * C) = 1 / (2 * pi * tau). At f_c, the output voltage drops to 70.7% (-3 dB) of the input, and the phase shift is 45 degrees."
          }
        },
        {
          "@type": "Question",
          "name": "What is the relationship between rise time (10% to 90%) and time constant tau?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The 10% to 90% rise time t_r is given by t_r = ln(9) * tau = 2.197 * tau approx 2.2 * tau. In frequency domain terms, t_r approx 0.35 / f_c."
          }
        }
      ]
    }
  ]
}"""

TOOL5_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="rc-r">Resistance ($R$):</label>
        <div class="input-with-select">
            <input type="number" id="rc-r" value="10" min="0.0001" step="any">
            <select id="rc-r-unit">
                <option value="1">&Omega;</option>
                <option value="1000" selected>k&Omega;</option>
                <option value="1000000">M&Omega;</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="rc-c">Capacitance ($C$):</label>
        <div class="input-with-select">
            <input type="number" id="rc-c" value="100" min="0.000001" step="any">
            <select id="rc-c-unit">
                <option value="1e-12">pF</option>
                <option value="1e-9" selected>nF</option>
                <option value="1e-6">&mu;F</option>
                <option value="1e-3">mF</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="rc-vs">Supply Voltage ($V_{\\text{source}}$):</label>
        <div class="input-with-select">
            <input type="number" id="rc-vs" value="5" min="0.001" step="any">
            <select id="rc-vs-unit">
                <option value="0.001">mV</option>
                <option value="1" selected>V</option>
                <option value="1000">kV</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="rc-t">Elapsed Time ($t$, optional for $V(t)$):</label>
        <div class="input-with-select">
            <input type="number" id="rc-t" value="1" min="0" step="any">
            <select id="rc-t-unit">
                <option value="1e-6">&mu;s</option>
                <option value="1e-3" selected>ms</option>
                <option value="1">s</option>
            </select>
        </div>
    </div>
</div>
<button id="calc-rc-btn" class="calc-btn">Calculate RC Response</button>
<div class="calc-results-card" id="rc-results">
    <h3>Transient &amp; Frequency Domain Parameters</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Time Constant (&tau; = RC):</span>
        <span class="result-val" id="res-rc-tau">1.000 ms (0.00100 s)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Cutoff Frequency ($f_c = \\frac{1}{2\\pi RC}$):</span>
        <span class="result-val" id="res-rc-fc">159.15 Hz</span>
    </div>
    <div class="result-row">
        <span class="result-label">10% &ndash; 90% Rise Time ($t_r \\approx 2.2\\tau$):</span>
        <span class="result-val" id="res-rc-tr">2.197 ms</span>
    </div>
    <div class="result-row">
        <span class="result-label">Full Steady State Time ($5\\tau$):</span>
        <span class="result-val" id="res-rc-5tau">5.000 ms</span>
    </div>
    <div class="result-row">
        <span class="result-label">Charging Voltage at time $t$ ($V(t)$):</span>
        <span class="result-val" id="res-rc-vc">3.161 V (63.2% of $V_s$)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Discharging Voltage at time $t$ ($V_{\\text{dis}}(t)$):</span>
        <span class="result-val" id="res-rc-vd">1.839 V (36.8% of $V_s$)</span>
    </div>
</div>
"""

TOOL5_JS = """
function computeRcTransient() {
    var rVal = parseFloat(document.getElementById('rc-r').value);
    var rUnit = parseFloat(document.getElementById('rc-r-unit').value);
    var cVal = parseFloat(document.getElementById('rc-c').value);
    var cUnit = parseFloat(document.getElementById('rc-c-unit').value);
    var vsVal = parseFloat(document.getElementById('rc-vs').value);
    var vsUnit = parseFloat(document.getElementById('rc-vs-unit').value);
    var tVal = parseFloat(document.getElementById('rc-t').value);
    var tUnit = parseFloat(document.getElementById('rc-t-unit').value);

    if (isNaN(rVal) || rVal <= 0 || isNaN(cVal) || cVal <= 0) return;

    var R = rVal * rUnit;
    var C = cVal * cUnit;
    var Vs = (isNaN(vsVal) || vsVal <= 0) ? 5.0 : vsVal * vsUnit;
    var t = (isNaN(tVal) || tVal < 0) ? 0 : tVal * tUnit;

    var tau = R * C; // seconds
    var fc = 1.0 / (2.0 * Math.PI * tau); // Hz
    var tr = 2.197224577 * tau; // 10% to 90% rise time
    var fiveTau = 5.0 * tau;

    // Formatting tau
    var tauStr = "";
    if (tau >= 1) {
        tauStr = tau.toFixed(4) + " s";
    } else if (tau >= 1e-3) {
        tauStr = (tau * 1e3).toFixed(3) + " ms (" + tau.toFixed(5) + " s)";
    } else if (tau >= 1e-6) {
        tauStr = (tau * 1e6).toFixed(3) + " \u03BCs (" + (tau * 1e3).toFixed(4) + " ms)";
    } else {
        tauStr = (tau * 1e9).toFixed(2) + " ns";
    }
    document.getElementById('res-rc-tau').textContent = tauStr;

    // Formatting fc
    var fcStr = "";
    if (fc >= 1e6) {
        fcStr = (fc / 1e6).toFixed(3) + " MHz";
    } else if (fc >= 1e3) {
        fcStr = (fc / 1e3).toFixed(3) + " kHz (" + fc.toFixed(1) + " Hz)";
    } else {
        fcStr = fc.toFixed(2) + " Hz";
    }
    document.getElementById('res-rc-fc').textContent = fcStr;

    // Format rise time
    var trStr = "";
    if (tr >= 1) {
        trStr = tr.toFixed(4) + " s";
    } else if (tr >= 1e-3) {
        trStr = (tr * 1e3).toFixed(3) + " ms";
    } else {
        trStr = (tr * 1e6).toFixed(3) + " \u03BCs";
    }
    document.getElementById('res-rc-tr').textContent = trStr;

    // Format 5 tau
    var fiveTauStr = "";
    if (fiveTau >= 1) {
        fiveTauStr = fiveTau.toFixed(4) + " s";
    } else if (fiveTau >= 1e-3) {
        fiveTauStr = (fiveTau * 1e3).toFixed(3) + " ms";
    } else {
        fiveTauStr = (fiveTau * 1e6).toFixed(3) + " \u03BCs";
    }
    document.getElementById('res-rc-5tau').textContent = fiveTauStr;

    // Instantaneous voltages at time t
    var expFactor = Math.exp(-t / tau);
    var vCharge = Vs * (1.0 - expFactor);
    var vDischarge = Vs * expFactor;
    var pctCharge = ((vCharge / Vs) * 100).toFixed(1);
    var pctDischarge = ((vDischarge / Vs) * 100).toFixed(1);

    document.getElementById('res-rc-vc').textContent = vCharge.toFixed(4) + " V (" + pctCharge + "% of Vs)";
    document.getElementById('res-rc-vd').textContent = vDischarge.toFixed(4) + " V (" + pctDischarge + "% of Vs)";
}

document.getElementById('calc-rc-btn').addEventListener('click', computeRcTransient);
['rc-r', 'rc-r-unit', 'rc-c', 'rc-c-unit', 'rc-vs', 'rc-vs-unit', 'rc-t', 'rc-t-unit'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computeRcTransient);
    document.getElementById(id).addEventListener('change', computeRcTransient);
});
window.addEventListener('DOMContentLoaded', computeRcTransient);
"""

TOOL5_ARTICLE = r"""
<h2>Transient Physics of First-Order RC Circuits: Differential Calculus Foundations</h2>
<p>A resistor-capacitor (RC) network represents the archetypal first-order linear time-invariant dynamic system in electrical engineering. When an uncharged capacitor is placed in series with a resistor and energized by a DC voltage step source $V_s$, charge cannot redistribute instantaneously because current through the dielectric boundary corresponds to finite electron motion bounded by resistance $R$. The circuit's dynamic evolution is described by Kirchhoff's Voltage Law (KVL):</p>
$$V_s - v_R(t) - v_C(t) = 0$$

<p>Applying Ohm's law $v_R(t) = i(t) \cdot R$ and the capacitive constitutive differential equation $i(t) = C \frac{dv_C}{dt}$ produces the governing first-order ordinary differential equation (ODE):</p>
$$R C \frac{dv_C(t)}{dt} + v_C(t) = V_s$$

<p>Rearranging this linear non-homogeneous differential equation into standard separable form:</p>
$$\frac{dv_C}{V_s - v_C} = \frac{1}{R C} dt$$

<p>Integrating both sides from initial state $t = 0$ (with boundary condition $v_C(0) = 0$) to time $t$:</p>
$$\int_{0}^{v_C(t)} \frac{dv_C}{V_s - v_C} = \int_{0}^{t} \frac{1}{R C} dt$$
$$-\ln\left( \frac{V_s - v_C(t)}{V_s} \right) = \frac{t}{R C}$$
$$\frac{V_s - v_C(t)}{V_s} = e^{-\frac{t}{RC}}$$
$$v_C(t) = V_s \left( 1 - e^{-\frac{t}{\tau}} \right)$$

<p>Where the Greek letter $\tau$ (tau) represents the fundamental <strong>RC time constant</strong>:</p>
$$\tau = R \cdot C \quad [\text{Seconds}]$$

<p>Dimensional analysis verifies that resistance in Ohms ($\text{V}/\text{A}$) multiplied by capacitance in Farads ($\text{A}\cdot\text{s}/\text{V}$) yields purely units of time: $[\Omega \cdot \text{F}] = [\text{s}]$.</p>

<h2>Capacitor Discharging Dynamics and Exponential Voltage Decay</h2>
<p>When a capacitor pre-charged to potential $V_0$ is disconnected from the supply and discharged through resistance $R$, the driving differential equation becomes homogeneous ($V_s = 0$):</p>
$$R C \frac{dv_C(t)}{dt} + v_C(t) = 0 \implies v_C(t) = V_0 \, e^{-\frac{t}{\tau}}$$

<p>The instantaneous discharge loop current $i(t)$ mirrors this exponential decay:</p>
$$i(t) = -\frac{v_C(t)}{R} = -\frac{V_0}{R} e^{-\frac{t}{\tau}}$$

<h3>Milestone Percentages Across Time Constant Intervals</h3>
<p>Because exponential functions approach steady state asymptotically without reaching it in finite mathematical time, engineers utilize standard time constant intervals ($\tau$ milestones) to assess settlement times:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Time Elapsed ($t$)</th>
            <th>Charging Voltage ($% V_s$)</th>
            <th>Discharging Voltage ($% V_0$)</th>
            <th>Remaining Incomplete Margin</th>
            <th>Engineering State</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>$0.693\tau$ ($t_{1/2}$)</td>
            <td>$50.00\%$</td>
            <td>$50.00\%$</td>
            <td>$50.00\%$</td>
            <td>Half-charge milestone ($t = \tau \ln 2$)</td>
        </tr>
        <tr>
            <td>$1\tau$</td>
            <td>$63.21\%$</td>
            <td>$36.79\%$</td>
            <td>$36.79\%$ ($1/e$)</td>
            <td>Formal time constant definition</td>
        </tr>
        <tr>
            <td>$2\tau$</td>
            <td>$86.47\%$</td>
            <td>$13.53\%$</td>
            <td>$13.53\%$</td>
            <td>Coarse settled signal</td>
        </tr>
        <tr>
            <td>$2.197\tau$ ($t_r$)</td>
            <td>$90.00\%$ (from $10\%$)</td>
            <td>$10.00\%$</td>
            <td>$10.00\%$</td>
            <td>Standard $10\%\text{--}90\%$ pulse rise time ($t_r$)</td>
        </tr>
        <tr>
            <td>$3\tau$</td>
            <td>$95.02\%$</td>
            <td>$4.98\%$</td>
            <td>$4.98\%$</td>
            <td>$95\%$ precision instrumentation threshold</td>
        </tr>
        <tr>
            <td>$4\tau$</td>
            <td>$98.17\%$</td>
            <td>$1.83\%$</td>
            <td>$1.83\%$</td>
            <td>High-accuracy settle</td>
        </tr>
        <tr>
            <td>$5\tau$</td>
            <td>$99.33\%$</td>
            <td>$0.67\%$</td>
            <td>$0.67\%$</td>
            <td>Universal practical engineering steady state</td>
        </tr>
    </tbody>
</table>

<h2>RC Waveshaping Circuits: Integrator vs Differentiator Topologies</h2>
<p>By altering which terminal component serves as the circuit output, an RC network functions either as an analog integrator or an analog differentiator for periodic pulse and square waveforms:</p>
<ul>
    <li><strong>RC Low-Pass Integrator ($V_{\text{out}}$ taken across Capacitor $C$):</strong> When the circuit time constant $\tau \gg T$ (where $T$ is the period of the input signal), the capacitor voltage cannot track the rapid step edges. The current through the resistor is predominantly governed by the input voltage $i(t) \approx v_{\text{in}}(t)/R$. Consequently, $v_{\text{out}}(t) = \frac{1}{C}\int i(t) dt \approx \frac{1}{RC}\int v_{\text{in}}(t) dt$. A square wave input produces a linear triangular ramp output.</li>
    <li><strong>RC High-Pass Differentiator ($V_{\text{out}}$ taken across Resistor $R$):</strong> When $\tau \ll T$, the capacitor charges almost instantaneously, dropping virtually the entire voltage across $C$. The current is governed by the derivative of input potential $i(t) \approx C \frac{dv_{\text{in}}}{dt}$. The voltage across the resistor is $v_{\text{out}}(t) = R \cdot i(t) \approx RC \frac{dv_{\text{in}}}{dt}$. A square wave input generates sharp alternating positive and negative impulse voltage spikes at every signal transition edge.</li>
</ul>

<h2>Frequency-Domain Behavior: Cutoff Frequency ($f_c$) and Filter Sizing</h2>
<p>An RC network functions as a first-order passive filter in the continuous frequency domain. Taking the Laplace transform of the KVL differential equation with zero initial conditions yields the s-domain transfer function $H(s)$:</p>
$$H(s) = \frac{V_{\text{out}}(s)}{V_{\text{in}}(s)} = \frac{\frac{1}{sC}}{R + \frac{1}{sC}} = \frac{1}{1 + sRC} = \frac{1}{1 + s\tau}$$

<p>Evaluating along the frequency axis $s = j\omega = j 2\pi f$ gives the complex frequency response:</p>
$$H(j\omega) = \frac{1}{1 + j\omega RC} = \frac{1}{1 + j\omega\tau}$$
$$|H(j\omega)| = \frac{1}{\sqrt{1 + (\omega RC)^2}}, \qquad \angle H(j\omega) = -\arctan(\omega RC)$$

<p>The half-power <strong>cutoff frequency ($f_c$)</strong> (also called corner frequency or $-3\text{ dB}$ point) occurs when signal power drops by $50\%$, corresponding to $|H(j\omega)| = \frac{1}{\sqrt{2}} \approx 0.7071$. This condition is satisfied when $\omega_c RC = 1$:</p>
$$\omega_c = \frac{1}{RC} = \frac{1}{\tau} \implies f_c = \frac{1}{2 \pi R C} = \frac{1}{2 \pi \tau} \quad [\text{Hz}]$$

<p>At $f = f_c$, the output phase lag is precisely $-45^\circ$. For frequencies well above $f_c$, the attenuation roll-off steepness approaches $-20\text{ dB/decade}$ ($-6\text{ dB/octave}$).</p>

<h2>Real-World Dielectric Non-Idealities Affecting RC Precision</h2>
<p>In physical PCB assemblies, timing errors and signal degradation arise from non-ideal capacitor properties:</p>
<ul>
    <li><strong>Dielectric Absorption ("Soakage"):</strong> Charges trapped within the molecular dipoles of dielectrics like Mylar or standard electrolytic capacitors bleed slowly back onto the plates after brief discharges. This causes unintended voltage regrowth in sample-and-hold circuits and precision dual-slope ADCs. For precision timing, low-absorption polypropylene, PTFE, or C0G ceramics are required.</li>
    <li><strong>DC Leakage Resistance:</strong> Electrolytic capacitors have internal parallel leakage resistances ($R_{\text{leak}}$) as low as several megaohms. If the external timing resistor $R$ is comparable to $R_{\text{leak}}$, the capacitor forms an unintended voltage divider, never reaching the anticipated threshold voltage.</li>
    <li><strong>Voltage Coefficient of Capacitance (VCC):</strong> High-dielectric-constant Class 2 ceramic capacitors (e.g., X5R, X7R) suffer dramatic capacitance drops (up to $50\%\text{--}80\%$) when operated near their rated DC bias voltage, drastically shrinking actual circuit time constant $\tau$ compared to nominal schematic values.</li>
</ul>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: ADC Anti-Aliasing RC Low-Pass Filter</h4>
    <p><strong>Scenario:</strong> A precision sensor signal conditioning board features a 16-bit analog-to-digital converter (ADC) sampling at $f_s = 200 \ \text{kHz}$. To prevent high-frequency spectral aliasing, an RC anti-aliasing low-pass filter with a cutoff frequency of $f_c = 25 \ \text{kHz}$ is required. Due to input impedance constraints, a resistor of $R = 4.7 \ \text{k}\Omega$ is specified.</p>
    <div class="step-solution">
        <p><strong>Step 1: Calculate Required Capacitance ($C$):</strong></p>
        $$C = \frac{1}{2 \pi R f_c} = \frac{1}{2 \pi \times (4700 \ \Omega) \times (25,000 \ \text{Hz})}$$
        $$C = \frac{1}{6.283185 \times 4700 \times 25000} = \frac{1}{738,274,274} = 1.3545 \times 10^{-9} \text{ F} = 1.355 \text{ nF}$$
        <p>A standard E96 precision C0G ceramic capacitor of $1.3 \text{ nF}$ or $1.5 \text{ nF}$ can be selected.</p>
        <p><strong>Step 2: Determine System Time Constant ($\tau$):</strong></p>
        $$\tau = R \cdot C = 4,700 \ \Omega \times 1.3545 \times 10^{-9} \text{ F} = 6.366 \times 10^{-6} \text{ seconds} = 6.366 \ \mu\text{s}$$
        <p><strong>Step 3: Calculate $10\%\text{--}90\%$ Pulse Rise Time ($t_r$):</strong></p>
        $$t_r = 2.197 \times \tau = 2.197 \times 6.366 \ \mu\text{s} = 13.986 \ \mu\text{s}$$
        <p>Cross-checking with frequency domain rule: $t_r \approx \frac{0.35}{f_c} = \frac{0.35}{25,000} = 14.0 \ \mu\text{s}$, confirming precision.</p>
        <p><strong>Step 4: Verify Full Settling Time to $99.3\%$ ($5\tau$):</strong></p>
        $$t_{\text{settle}} = 5 \times \tau = 5 \times 6.366 \ \mu\text{s} = 31.83 \ \mu\text{s}$$
        <p><strong>Conclusion:</strong> The filter successfully limits band noise above $25 \text{ kHz}$ while settling step inputs within $31.83 \ \mu\text{s}$, well within the system's requirements.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>What is the physical meaning of one time constant ($1\tau$) in an RC circuit?</h3>
    <p>One time constant $\tau = R \cdot C$ represents the time required for a charging capacitor to reach $1 - 1/e = 63.21\%$ of its ultimate steady-state supply voltage, or for a discharging capacitor to decay to $1/e = 36.79\%$ of its initial charge.</p>

    <h3>How many time constants does it take to fully charge a capacitor?</h3>
    <p>Theoretically, exponential curves never reach $100\%$. In practical engineering, a capacitor is considered fully charged at 5 time constants ($5\tau$), at which point it has reached $99.33\%$ of the supply voltage.</p>

    <h3>How is the RC time constant related to cutoff frequency ($f_c$)?</h3>
    <p>The $-3\text{ dB}$ cutoff frequency of a first-order RC low-pass or high-pass filter is inversely proportional to $\tau$: $f_c = \frac{1}{2 \pi R C} = \frac{1}{2 \pi \tau}$. At $f_c$, the output voltage drops to $70.7\%$ ($-3\text{ dB}$) of the input, and the phase shift is $45^\circ$.</p>

    <h3>What is the relationship between rise time ($10\%$ to $90\%$) and time constant $\tau$?</h3>
    <p>The $10\%$ to $90\%$ rise time $t_r$ is given by $t_r = \ln(9) \cdot \tau = 2.197 \cdot \tau \approx 2.2 \tau$. In frequency domain terms, $t_r \approx \frac{0.35}{f_c}$.</p>
</div>
"""

# ==============================================================================
# TOOL 6: rl-time-constant-calculator.html
# ==============================================================================
TOOL6_SLUG = "rl-time-constant-calculator"
TOOL6_TITLE = "RL Time Constant Calculator - Tau, Inductor Current Growth & Flyback Energy"
TOOL6_DESC = "Calculate RL circuit time constant (tau = L / R), maximum inductor current (I = V/R), inductive stored energy (E = 1/2 LI²), and transient exponential growth/decay."
TOOL6_H1 = "RL Time Constant Calculator"
TOOL6_SHORT = "Compute inductor-resistor time constant (&tau; = L/R), steady-state saturation current, stored magnetic energy, and transient decay curves."

TOOL6_SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "RL Time Constant Calculator",
      "url": "https://calchub.com/rl-time-constant-calculator.html",
      "description": "Calculates RL time constant tau, maximum current, magnetic field energy, and transient inductive current rise and decay.",
      "applicationCategory": "EngineeringApplication",
      "operatingSystem": "All",
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
          "name": "Why is the RL time constant tau equal to L / R instead of L * R?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "An inductor resists changes in current by generating back-EMF proportional to di/dt. A larger resistance R limits the circuit current more rapidly, causing the rate of magnetic field establishment to settle faster. Therefore, higher resistance shortens the transient duration, yielding tau = L / R."
          }
        },
        {
          "@type": "Question",
          "name": "What causes inductive kickback (flyback voltage) when an RL circuit is switched off?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "When a switch suddenly disconnects current flowing through an inductor, di/dt becomes massively negative over a near-zero time interval. By Faraday's Law and Lenz's Law, the inductor creates an instantaneous reverse back-EMF voltage V_L = -L(di/dt) that can reach hundreds or thousands of volts, arcing switches or destroying semiconductor driver transistors if a flyback clamp diode is not present."
          }
        },
        {
          "@type": "Question",
          "name": "How much energy is stored in an inductor at steady state?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "At steady state (t >= 5 tau), the inductor acts as a short circuit with current I_max = V / R. The energy stored in its magnetic field is E_L = (1/2) * L * I_max^2 (measured in Joules)."
          }
        },
        {
          "@type": "Question",
          "name": "What is the cutoff frequency of an RL filter?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The -3 dB corner frequency of a first-order RL low-pass or high-pass filter is f_c = R / (2 * pi * L) = 1 / (2 * pi * tau)."
          }
        }
      ]
    }
  ]
}"""

TOOL6_UI = """
<div class="calc-grid">
    <div class="calc-input-group">
        <label for="rl-l">Inductance ($L$):</label>
        <div class="input-with-select">
            <input type="number" id="rl-l" value="10" min="0.0001" step="any">
            <select id="rl-l-unit">
                <option value="1e-6">&mu;H</option>
                <option value="1e-3" selected>mH</option>
                <option value="1">H</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="rl-r">Resistance ($R$):</label>
        <div class="input-with-select">
            <input type="number" id="rl-r" value="50" min="0.0001" step="any">
            <select id="rl-r-unit">
                <option value="1" selected>&Omega;</option>
                <option value="1000">k&Omega;</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="rl-vs">Supply Voltage ($V_{\\text{source}}$):</label>
        <div class="input-with-select">
            <input type="number" id="rl-vs" value="12" min="0.001" step="any">
            <select id="rl-vs-unit">
                <option value="1" selected>V</option>
                <option value="1000">kV</option>
            </select>
        </div>
    </div>
    <div class="calc-input-group">
        <label for="rl-t">Elapsed Time ($t$, optional for $i(t)$):</label>
        <div class="input-with-select">
            <input type="number" id="rl-t" value="200" min="0" step="any">
            <select id="rl-t-unit">
                <option value="1e-6" selected>&mu;s</option>
                <option value="1e-3">ms</option>
                <option value="1">s</option>
            </select>
        </div>
    </div>
</div>
<button id="calc-rl-btn" class="calc-btn">Calculate RL Transient</button>
<div class="calc-results-card" id="rl-results">
    <h3>Inductive Transient &amp; Energy Metrics</h3>
    <div class="result-row highlight-result">
        <span class="result-label">Time Constant (&tau; = L / R):</span>
        <span class="result-val" id="res-rl-tau">0.200 ms (200.0 &mu;s)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Steady-State Current ($I_{\text{max}} = V / R$):</span>
        <span class="result-val" id="res-rl-imax">0.240 A (240.0 mA)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Stored Magnetic Energy ($E_L = \frac{1}{2} L I_{\text{max}}^2$):</span>
        <span class="result-val" id="res-rl-el">0.288 mJ (0.000288 J)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Cutoff Frequency ($f_c = \frac{R}{2\pi L}$):</span>
        <span class="result-val" id="res-rl-fc">795.77 Hz</span>
    </div>
    <div class="result-row">
        <span class="result-label">Instantaneous Current at time $t$ ($i(t)$):</span>
        <span class="result-val" id="res-rl-it">0.1517 A (63.2% of $I_{\text{max}}$)</span>
    </div>
    <div class="result-row">
        <span class="result-label">Inductor Voltage at time $t$ ($v_L(t)$):</span>
        <span class="result-val" id="res-rl-vlt">4.415 V (36.8% of $V_s$)</span>
    </div>
</div>
"""

TOOL6_JS = """
function computeRlTransient() {
    var lVal = parseFloat(document.getElementById('rl-l').value);
    var lUnit = parseFloat(document.getElementById('rl-l-unit').value);
    var rVal = parseFloat(document.getElementById('rl-r').value);
    var rUnit = parseFloat(document.getElementById('rl-r-unit').value);
    var vsVal = parseFloat(document.getElementById('rl-vs').value);
    var vsUnit = parseFloat(document.getElementById('rl-vs-unit').value);
    var tVal = parseFloat(document.getElementById('rl-t').value);
    var tUnit = parseFloat(document.getElementById('rl-t-unit').value);

    if (isNaN(lVal) || lVal <= 0 || isNaN(rVal) || rVal <= 0) return;

    var L = lVal * lUnit;
    var R = rVal * rUnit;
    var Vs = (isNaN(vsVal) || vsVal <= 0) ? 12.0 : vsVal * vsUnit;
    var t = (isNaN(tVal) || tVal < 0) ? 0 : tVal * tUnit;

    var tau = L / R; // seconds
    var Imax = Vs / R; // Amperes
    var EL = 0.5 * L * Math.pow(Imax, 2); // Joules
    var fc = R / (2.0 * Math.PI * L); // Hz

    // Format tau
    var tauStr = "";
    if (tau >= 1) {
        tauStr = tau.toFixed(4) + " s";
    } else if (tau >= 1e-3) {
        tauStr = (tau * 1e3).toFixed(3) + " ms (" + (tau * 1e6).toFixed(1) + " \u03BCs)";
    } else {
        tauStr = (tau * 1e6).toFixed(3) + " \u03BCs (" + (tau * 1e9).toFixed(1) + " ns)";
    }
    document.getElementById('res-rl-tau').textContent = tauStr;

    // Format Imax
    var imaxStr = "";
    if (Imax >= 1) {
        imaxStr = Imax.toFixed(3) + " A (" + (Imax * 1e3).toFixed(1) + " mA)";
    } else {
        imaxStr = (Imax * 1e3).toFixed(2) + " mA (" + Imax.toFixed(4) + " A)";
    }
    document.getElementById('res-rl-imax').textContent = imaxStr;

    // Format EL
    var elStr = "";
    if (EL >= 1) {
        elStr = EL.toFixed(4) + " J";
    } else if (EL >= 1e-3) {
        elStr = (EL * 1e3).toFixed(3) + " mJ (" + EL.toExponential(3) + " J)";
    } else {
        elStr = (EL * 1e6).toFixed(3) + " \u03BCJ";
    }
    document.getElementById('res-rl-el').textContent = elStr;

    // Format fc
    var fcStr = "";
    if (fc >= 1e6) {
        fcStr = (fc / 1e6).toFixed(3) + " MHz";
    } else if (fc >= 1e3) {
        fcStr = (fc / 1e3).toFixed(3) + " kHz";
    } else {
        fcStr = fc.toFixed(2) + " Hz";
    }
    document.getElementById('res-rl-fc').textContent = fcStr;

    // Instantaneous current and voltage
    var expFactor = Math.exp(-t / tau);
    var it = Imax * (1.0 - expFactor);
    var vlt = Vs * expFactor;
    var pctI = ((it / Imax) * 100).toFixed(1);
    var pctV = ((vlt / Vs) * 100).toFixed(1);

    document.getElementById('res-rl-it').textContent = (it >= 1 ? it.toFixed(4) + " A" : (it * 1000).toFixed(2) + " mA") + " (" + pctI + "% of I_max)";
    document.getElementById('res-rl-vlt').textContent = vlt.toFixed(4) + " V (" + pctV + "% of Vs)";
}

document.getElementById('calc-rl-btn').addEventListener('click', computeRlTransient);
['rl-l', 'rl-l-unit', 'rl-r', 'rl-r-unit', 'rl-vs', 'rl-vs-unit', 'rl-t', 'rl-t-unit'].forEach(function(id) {
    document.getElementById(id).addEventListener('input', computeRlTransient);
    document.getElementById(id).addEventListener('change', computeRlTransient);
});
window.addEventListener('DOMContentLoaded', computeRlTransient);
"""

TOOL6_ARTICLE = r"""
<h2>Electromagnetic Transient Theory of Inductor-Resistor (RL) Circuits</h2>
<p>An inductor stores energy in the dynamic magnetic flux ($\Phi$) established by electric current flowing through conductive helical windings. According to Faraday's Law of Electromagnetic Induction and Lenz's Law, any time-rate of change in magnetic flux induces an electromotive force (EMF) that opposes the very current change creating it:</p>
$$v_L(t) = L \frac{di(t)}{dt}$$

<p>Where $L$ is the self-inductance in Henrys ($1\text{ H} = 1\text{ V}\cdot\text{s}/\text{A}$). When a series RL circuit is energized from rest by a DC source voltage $V_s$, the inductor initially opposes the sudden step change in current by generating a back-EMF equal and opposite to $V_s$. Consequently, at time $t = 0^+$, the inductor behaves as an instantaneous open circuit ($i(0^+) = 0$).</p>

<h2>Derivation of the Current Growth Differential Equation</h2>
<p>Applying Kirchhoff's Voltage Law around the single series closed loop gives:</p>
$$V_s - v_R(t) - v_L(t) = 0 \implies V_s - R \, i(t) - L \frac{di(t)}{dt} = 0$$

<p>Rearranging into canonical first-order ordinary differential equation form:</p>
$$L \frac{di(t)}{dt} + R \, i(t) = V_s \implies \frac{di(t)}{dt} + \frac{R}{L} i(t) = \frac{V_s}{L}$$

<p>Separating variables with initial boundary condition $i(0) = 0$:</p>
$$\frac{di}{\frac{V_s}{R} - i} = \frac{R}{L} dt$$
$$\int_{0}^{i(t)} \frac{di}{\frac{V_s}{R} - i} = \int_{0}^{t} \frac{R}{L} dt$$
$$-\ln\left( \frac{\frac{V_s}{R} - i(t)}{\frac{V_s}{R}} \right) = \frac{R}{L} t$$
$$\frac{\frac{V_s}{R} - i(t)}{\frac{V_s}{R}} = e^{-\frac{R}{L} t}$$
$$i(t) = \frac{V_s}{R} \left( 1 - e^{-\frac{t}{\tau}} \right) = I_{\text{max}} \left( 1 - e^{-\frac{t}{\tau}} \right)$$

<p>Where $\tau$ represents the fundamental <strong>RL time constant</strong>:</p>
$$\tau = \frac{L}{R} \quad [\text{Seconds}]$$

<p>Dimensional proof confirms that Henrys ($[\text{V}\cdot\text{s}/\text{A}]$) divided by Ohms ($[\text{V}/\text{A}]$) simplifies purely to time: $[\text{H}/\Omega] = [\text{s}]$.</p>

<h2>Inductive Kickback, Flyback Voltage, and Snubber Protection</h2>
<p>While current growth in an RL circuit is bounded by supply voltage, circuit interruption (decay) presents extreme transient danger. If current $I_0$ flowing through an inductor is suddenly interrupted by opening a mechanical switch or turning off a MOSFET transistor, the rate of change $\frac{di}{dt}$ theoretically approaches negative infinity because the physical break forces current to zero in nanoseconds.</p>

<p>By Faraday's law, the inductor produces a massive positive inductive kickback voltage spike:</p>
$$v_{\text{kickback}} = -L \left( \frac{di}{dt} \right) \gg V_s$$

<p>This inductive flyback voltage frequently surges to thousands of volts, creating electric arcing across switch contacts, melting relay contacts, and puncturing semiconductor drain-source silicon dielectric layers. To suppress this destruction, engineers deploy a <strong>flyback (freewheeling) diode</strong> in anti-parallel across the inductive coil, providing a closed recirculating loop through which current safely decays according to:</p>
$$i_{\text{decay}}(t) = I_0 \, e^{-\frac{t}{\tau_{\text{loop}}}}$$

<table class="data-table">
    <thead>
        <tr>
            <th>Suppression Technique</th>
            <th>Peak Voltage Clamp</th>
            <th>Decay Speed (Dropout Time)</th>
            <th>Primary Application Field</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Standard Silicon Diode (1N4007)</strong></td>
            <td>Clamped to $V_s + 0.7\text{ V}$</td>
            <td>Slowest (long inductive circulating time)</td>
            <td>DC relay coils, low-frequency solenoids</td>
        </tr>
        <tr>
            <td><strong>Diode + Zener Diode Series Pair</strong></td>
            <td>Clamped to $V_s + V_Z$</td>
            <td>Fast (energy burned rapidly in Zener breakdown)</td>
            <td>High-speed automotive fuel injectors, fast solenoids</td>
        </tr>
        <tr>
            <td><strong>RC Snubber Network</strong></td>
            <td>Damps ringing peak below breakdown</td>
            <td>Medium (resonant dissipation)</td>
            <td>AC inductive contactors, triac phase controllers</td>
        </tr>
        <tr>
            <td><strong>Metal Oxide Varistor (MOV)</strong></td>
            <td>Nonlinear clamping at varistor voltage</td>
            <td>Very Fast</td>
            <td>Surge transient protection, industrial mains coils</td>
        </tr>
    </tbody>
</table>

<h2>AC Impedance, Phase Shift, and Power Factor in RL Circuits</h2>
<p>In steady-state sinusoidal AC systems operating at cyclic frequency $f$ and angular frequency $\omega = 2\pi f$, the total complex impedance of a series RL circuit is given by:</p>
$$Z = R + j X_L = R + j \omega L$$
$$|Z| = \sqrt{R^2 + (\omega L)^2}$$

<p>The voltage leads current by phase angle $\theta$:</p>
$$\theta = \arctan\left( \frac{\omega L}{R} \right) = \arctan(\omega \tau)$$

<p>The circuit power factor is $\text{PF} = \cos(\theta) = \frac{R}{|Z|}$. Because the inductive reactive component consumes zero net average real power, magnetic energy continuously oscillates back and forth between generator and load. Industrial installations with heavy RL motor loads install power factor correction capacitor banks to counterbalance inductive reactive voltamperes ($\text{VAR}$).</p>

<h2>Physical Core Non-Idealities: Saturation and Eddy Current Losses</h2>
<p>Unlike pure mathematical inductors, physical magnetic inductors utilize ferromagnetic cores (iron powder, ferrite, electrical steel) to concentrate magnetic flux. Key non-idealities include:</p>
<ul>
    <li><strong>Magnetic Core Saturation:</strong> As current $i(t)$ increases, core magnetic domains fully align, causing differential permeability $\mu_r$ to collapse. When core saturation occurs, effective inductance $L$ drops abruptly to that of an air-core coil, causing current to surge destructively above design calculations.</li>
    <li><strong>Hysteresis Losses:</strong> Alternating magnetizing and demagnetizing cycles dissipate heat proportional to the area enclosed by the core's $B\text{-}H$ loop.</li>
    <li><strong>Eddy Current Losses:</strong> Alternating magnetic flux induces circulating currents within conductive core materials, generating $I^2 R$ thermal dissipation. Laminated core sheets and high-resistivity ferrite ceramics are employed to minimize this loss mechanism.</li>
</ul>

<div class="worked-example-card">
    <h4>Step-by-Step Engineering Case Study: Automotive 12V Solenoid Coil Analysis</h4>
    <p><strong>Scenario:</strong> An automotive starter relay solenoid has an internal coil inductance of $L = 85 \ \text{mH}$ and a DC winding resistance of $R = 12 \ \Omega$. It is energized by an automotive battery bus of $V_s = 13.8 \ \text{V}$.</p>
    <div class="step-solution">
        <p><strong>Step 1: Calculate Circuit Time Constant ($\tau$):</strong></p>
        $$\tau = \frac{L}{R} = \frac{85 \times 10^{-3} \text{ H}}{12 \ \Omega} = 7.0833 \times 10^{-3} \text{ seconds} = 7.083 \ \text{ms}$$
        <p><strong>Step 2: Calculate Steady-State Saturation Current ($I_{\text{max}}$):</strong></p>
        $$I_{\text{max}} = \frac{V_s}{R} = \frac{13.8 \ \text{V}}{12 \ \Omega} = 1.150 \ \text{Amperes}$$
        <p><strong>Step 3: Determine Stored Magnetic Energy in Coil ($E_L$):</strong></p>
        $$E_L = \frac{1}{2} L I_{\text{max}}^2 = \frac{1}{2} \times (0.085 \text{ H}) \times (1.150 \text{ A})^2$$
        $$E_L = 0.0425 \times 1.3225 = 0.05621 \text{ Joules} = 56.21 \text{ mJ}$$
        <p><strong>Step 4: Calculate Current at $t = 5.0 \ \text{ms}$ After Activation:</strong></p>
        $$i(5 \text{ ms}) = 1.150 \times \left( 1 - e^{-\frac{0.0050}{0.0070833}} \right) = 1.150 \times (1 - e^{-0.70588})$$
        $$i(5 \text{ ms}) = 1.150 \times (1 - 0.49367) = 1.150 \times 0.50633 = 0.5823 \ \text{A (582.3 mA)}$$
        <p><strong>Step 5: Full Actuation Settle Time ($5\tau$):</strong></p>
        $$t_{\text{settle}} = 5 \times 7.0833 \ \text{ms} = 35.42 \ \text{ms}$$
        <p><strong>Conclusion:</strong> The solenoid reaches $50.6\%$ of holding current within $5 \text{ ms}$ and achieves full magnetic pull force within $35.4 \text{ ms}$. A freewheeling clamp must be selected to safely dissipate the $56.2 \text{ mJ}$ magnetic collapse.</p>
    </div>
</div>

<h2>Frequently Asked Questions (FAQ)</h2>
<div class="faq-section">
    <h3>Why is the RL time constant $\tau$ equal to $L / R$ instead of $L \times R$?</h3>
    <p>An inductor resists changes in current by generating back-EMF proportional to $\frac{di}{dt}$. A larger resistance $R$ limits the circuit current more rapidly, causing the rate of magnetic field establishment to settle faster. Therefore, higher resistance shortens the transient duration, yielding $\tau = L / R$.</p>

    <h3>What causes inductive kickback (flyback voltage) when an RL circuit is switched off?</h3>
    <p>When a switch suddenly disconnects current flowing through an inductor, $\frac{di}{dt}$ becomes massively negative over a near-zero time interval. By Faraday's Law and Lenz's Law, the inductor creates an instantaneous reverse back-EMF voltage $v_L = -L \frac{di}{dt}$ that can reach hundreds or thousands of volts, arcing switches or destroying semiconductor driver transistors if a flyback clamp diode is not present.</p>

    <h3>How much energy is stored in an inductor at steady state?</h3>
    <p>At steady state ($t \ge 5\tau$), the inductor acts as a short circuit with current $I_{\text{max}} = V_s / R$. The energy stored in its magnetic field is $E_L = \frac{1}{2} L I_{\text{max}}^2$ (measured in Joules).</p>

    <h3>What is the cutoff frequency of an RL filter?</h3>
    <p>The $-3\text{ dB}$ corner frequency of a first-order RL low-pass or high-pass filter is $f_c = \frac{R}{2 \pi L} = \frac{1}{2 \pi \tau}$.</p>
</div>
"""

def generate_tool(slug, title, desc, h1, short_desc, schema_json, ui_html, js_code, article_html):
    full_html = HEADER_HTML.format(
        title=title,
        description=desc,
        slug=slug,
        h1=h1,
        short_desc=short_desc,
        schema_json=schema_json,
        calc_ui=ui_html,
        article_content=article_html,
        calc_js=js_code
    )
    filepath = os.path.join(r"C:\Users\Admin\.gemini\antigravity\scratch\calchub", f"{slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated: {filepath}")

if __name__ == "__main__":
    generate_tool(TOOL5_SLUG, TOOL5_TITLE, TOOL5_DESC, TOOL5_H1, TOOL5_SHORT, TOOL5_SCHEMA, TOOL5_UI, TOOL5_JS, TOOL5_ARTICLE)
    generate_tool(TOOL6_SLUG, TOOL6_TITLE, TOOL6_DESC, TOOL6_H1, TOOL6_SHORT, TOOL6_SCHEMA, TOOL6_UI, TOOL6_JS, TOOL6_ARTICLE)
