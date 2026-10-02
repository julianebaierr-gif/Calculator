# -*- coding: utf-8 -*-
"""
Script to generate Batch 18 Part 3 tools:
1. photon-energy-calculator.html
2. simple-pendulum-calculator.html
"""
import os

TOOL_1_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Photon Energy Calculator | Wavelength, Frequency & Planck's Law</title>
  <meta name="description" content="Calculate photon energy in electron-volts (eV) and Joules from wavelength or frequency using Planck's relation E = hf = hc/λ across the EM spectrum.">
  <link rel="canonical" href="https://calchub.cloud/photon-energy-calculator.html">
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
        "name": "Photon Energy Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates quantum photon energy in Joules and electron-volts (eV), photon momentum, molar photon energy (kJ/mol), and electromagnetic spectrum classifications.",
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
            "name": "What is the Planck-Einstein relation formula for photon energy?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The Planck-Einstein relation states that photon energy is directly proportional to electromagnetic frequency: E = h × f, or in terms of vacuum wavelength, E = (h × c) / λ, where 'h' is Planck's constant (6.62607015 × 10⁻³⁴ J·s), 'c' is the speed of light in vacuum (299,792,458 m/s), and 'λ' is wavelength in meters."
            }
          },
          {
            "@type": "Question",
            "name": "What is the practical shortcut formula for calculating photon energy in electron-volts?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Multiplying Planck's constant by the speed of light yields hc ≈ 1239.8419 eV·nm. Therefore, photon energy in electron-volts can be calculated rapidly as E (eV) ≈ 1239.84 / λ (nm). For example, green light at 500 nm has an energy of roughly 1239.84 / 500 ≈ 2.48 eV."
            }
          },
          {
            "@type": "Question",
            "name": "How does photon energy relate to the photoelectric effect?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In the photoelectric effect, electrons are ejected from a metal surface only if the incident photon energy exceeds the material's surface work function (E_photon ≥ Φ). Excess photon energy is transferred to the ejected photoelectron as kinetic energy: E_k = hf - Φ."
            }
          },
          {
            "@type": "Question",
            "name": "Can a massless photon possess linear momentum?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. Although photons possess zero invariant rest mass (m₀ = 0), Einstein's relativistic energy-momentum relation E² = (pc)² + (m₀c²)² simplifies for photons to E = pc. Consequently, photon momentum is p = E / c = h / λ, enabling radiation pressure and solar sail propulsion."
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
        <h1>Photon Energy Calculator</h1>
        <p class="lead-text">Calculate single photon quantum energy in electron-volts (eV) and Joules, photon momentum, and molar energy from wavelength or frequency.</p>

        <div class="calc-card">
          <div class="form-row">
            <div class="form-group col-half">
              <label for="inputMode">Input Parameter</label>
              <select id="inputMode" class="form-control">
                <option value="wavelength" selected>Wavelength (&lambda;)</option>
                <option value="frequency">Frequency (f)</option>
                <option value="energy_ev">Energy in Electron-Volts (eV)</option>
                <option value="energy_j">Energy in Joules (J)</option>
              </select>
            </div>

            <div class="form-group col-half">
              <label for="emPreset">Electromagnetic Spectrum Preset</label>
              <select id="emPreset" class="form-control">
                <option value="green_532" selected>Green Laser Pointer (532 nm)</option>
                <option value="red_633">He-Ne Red Laser (632.8 nm)</option>
                <option value="blue_450">Blue GaN Laser (450 nm)</option>
                <option value="uv_254">Germicidal UV-C (254 nm)</option>
                <option value="ir_1550">Telecom Fiber IR (1550 nm)</option>
                <option value="xray_01">Medical Diagnostic X-Ray (0.1 nm)</option>
                <option value="wifi_24">WiFi Microwave (2.4 GHz)</option>
                <option value="custom">Custom Value</option>
              </select>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-full" id="grpInputVal">
              <label for="valInput" id="lblInputVal">Electromagnetic Wavelength (&lambda;)</label>
              <div class="input-with-unit">
                <input type="number" id="valInput" class="form-control" value="532" step="any" min="0">
                <select id="unitInput" class="unit-select">
                  <option value="nm" selected>Nanometers (nm)</option>
                  <option value="um">Micrometers (&mu;m)</option>
                  <option value="angstrom">&Aring;ngstr&ouml;ms (&Aring;)</option>
                  <option value="m">Meters (m)</option>
                </select>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Quantum Energy</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset to Green Laser (532 nm)</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label">Photon Energy (E)</div>
              <div class="result-value" id="resEnergyEv">2.331 eV</div>
              <div class="result-sub" id="resEnergyJ">3.734 × 10⁻¹⁹ Joules • 224.9 kJ/mol (Einstein)</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Electromagnetic Frequency (f)</span>
                <span class="sub-value" id="resFreq">563.5 THz (5.635 × 10¹⁴ Hz)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Vacuum Wavelength (&lambda;)</span>
                <span class="sub-value" id="resWavelength">532.0 nm (0.532 &mu;m)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Photon Momentum (p = h/&lambda;)</span>
                <span class="sub-value" id="resMomentum">1.245 × 10⁻²⁷ kg·m/s</span>
              </div>
              <div class="result-item">
                <span class="sub-label">EM Spectrum Classification</span>
                <span class="sub-value" id="resBand">Visible Light (Green)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Quantum Mechanics of the Photon & Planck's Relation</h2>
          <p>In modern physics, light and all electromagnetic radiation exhibit a fundamental dual nature known as wave-particle duality. While macroscopic electromagnetic phenomena (such as reflection, refraction, and radio transmission) are described by James Clerk Maxwell's classical wave equations, interactions of light with matter at the atomic scale occur in discrete, indivisible packets of localized energy called <strong>photons</strong>.</p>
          <p>The quantum revolution began in 1900 when German physicist Max Planck resolved the classical blackbody radiation paradox (the "ultraviolet catastrophe") by proposing that atomic oscillators can only absorb or emit electromagnetic radiation in discrete energy quanta proportional to frequency:</p>
          <div class="math-block">
            $$E = h \cdot f = \frac{h \cdot c}{\lambda}$$
          </div>
          <p>Where:</p>
          <ul>
            <li>\(E\) = Quantum energy of a single photon in Joules (\(\text{J}\)) or electron-volts (\(\text{eV}\))</li>
            <li>\(h\) = Planck's constant (\(6.62607015 \times 10^{-34}\text{ J}\cdot\text{s} = 4.135667696 \times 10^{-15}\text{ eV}\cdot\text{s}\))</li>
            <li>\(f\) = Electromagnetic frequency in Hertz (\(\text{Hz}\))</li>
            <li>\(c\) = Speed of light in vacuum (\(299,792,458\text{ m/s}\))</li>
            <li>\(\lambda\) = Wavelength in vacuum in meters (\(\text{m}\))</li>
          </ul>
          <p>In 1905, Albert Einstein extended Planck's concept to explain the <strong>Photoelectric Effect</strong>, proving that the electromagnetic field itself is physically quantized into photons. For this discovery, Einstein was awarded the 1921 Nobel Prize in Physics.</p>

          <h2>2. Mathematical Shortcuts: The 1239.84 eV·nm Rule</h2>
          <p>In solid-state physics, optical spectroscopy, and semiconductor engineering, photon energy is universally expressed in electron-volts (\(\text{eV}\)), defined as the kinetic energy acquired by a single electron accelerated across an electric potential difference of one volt:</p>
          <div class="math-block">
            $$1\text{ eV} = 1.602176634 \times 10^{-19}\text{ Joules}$$
          </div>
          <p>Multiplying Planck's constant \(h\) in \(\text{eV}\cdot\text{s}\) by the speed of light \(c\) in \(\text{nm/s}\) yields the fundamental physical constant product:</p>
          <div class="math-block">
            $$h \cdot c \approx (4.1356677 \times 10^{-15}\text{ eV}\cdot\text{s}) \times (2.99792458 \times 10^{17}\text{ nm/s}) \approx 1239.8419\text{ eV}\cdot\text{nm}$$
          </div>
          <p>This provides optoelectronics engineers with an invaluable mental math equation connecting wavelength directly to bandgap energy:</p>
          <div class="math-block">
            $$E \,(\text{eV}) \approx \frac{1239.84}{\lambda \,(\text{nm})} \quad \iff \quad \lambda \,(\text{nm}) \approx \frac{1239.84}{E \,(\text{eV})}$$
          </div>
          <p>For example, a gallium nitride (GaN) blue LED emitting at \(\lambda = 450\text{ nm}\) requires a semiconductor bandgap of \(E_g \approx 1239.84 / 450 \approx 2.76\text{ eV}\).</p>

          <h2>3. Electromagnetic Spectrum Reference Benchmark Table</h2>
          <p>To assist optics specialists, laser technicians, and telecommunications engineers, the table below documents representative photon energies across the entire electromagnetic spectrum:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Electromagnetic Band</th>
                <th>Typical Wavelength (\(\lambda\))</th>
                <th>Frequency (\(f\))</th>
                <th>Photon Energy (\(E\))</th>
                <th>Primary Application / Phenomenon</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Extremely High-Energy Gamma Rays</td>
                <td>0.001 nm (\(1\text{ pm}\))</td>
                <td>300 EHz (\(10^{20}\text{ Hz}\))</td>
                <td>1.24 MeV (\(1.98 \times 10^{-13}\text{ J}\))</td>
                <td>Nuclear decay, cancer radiotherapy, cosmic ray air showers</td>
              </tr>
              <tr>
                <td>Medical Diagnostic X-Rays</td>
                <td>0.03 nm (\(0.3\text{ Å}\))</td>
                <td>10 PHz (\(10^{16}\text{ Hz}\))</td>
                <td>41.3 keV (\(6.62 \times 10^{-15}\text{ J}\))</td>
                <td>Computed tomography (CT) scans, bone radiography</td>
              </tr>
              <tr>
                <td>Deep Ultraviolet (UV-C)</td>
                <td>254 nm</td>
                <td>1.18 PHz</td>
                <td>4.88 eV (\(7.82 \times 10^{-19}\text{ J}\))</td>
                <td>Pathogen DNA/RNA germicidal sterilization lamps</td>
              </tr>
              <tr>
                <td>Visible Violet (Edge of Sight)</td>
                <td>400 nm</td>
                <td>750 THz</td>
                <td>3.10 eV (\(4.97 \times 10^{-19}\text{ J}\))</td>
                <td>Human visual perception short-wavelength boundary</td>
              </tr>
              <tr>
                <td>Visible Green (Peak Eye Sensitivity)</td>
                <td>555 nm</td>
                <td>540 THz</td>
                <td>2.23 eV (\(3.58 \times 10^{-19}\text{ J}\))</td>
                <td>Photopic vision peak sensitivity (CIE luminous efficiency)</td>
              </tr>
              <tr>
                <td>Visible Red (He-Ne Laser)</td>
                <td>632.8 nm</td>
                <td>473.8 THz</td>
                <td>1.96 eV (\(3.14 \times 10^{-19}\text{ J}\))</td>
                <td>Barcode scanners, optical alignment, holography</td>
              </tr>
              <tr>
                <td>Telecom Near-Infrared (C-Band)</td>
                <td>1,550 nm (1.55 µm)</td>
                <td>193.4 THz</td>
                <td>0.80 eV (\(1.28 \times 10^{-19}\text{ J}\))</td>
                <td>Minimum attenuation window in silica fiber-optic cables</td>
              </tr>
              <tr>
                <td>WiFi / Microwave Oven</td>
                <td>12.24 cm</td>
                <td>2.45 GHz</td>
                <td>\(1.01 \times 10^{-5}\text{ eV}\) (\(1.62 \times 10^{-24}\text{ J}\))</td>
                <td>Dielectric heating of water molecules, 802.11b/g/n WLAN</td>
              </tr>
              <tr>
                <td>FM Radio Broadcast Band</td>
                <td>3.0 meters</td>
                <td>100 MHz</td>
                <td>\(4.14 \times 10^{-7}\text{ eV}\) (\(6.63 \times 10^{-26}\text{ J}\))</td>
                <td>Commercial VHF frequency-modulated audio broadcasts</td>
              </tr>
            </tbody>
          </table>

          <h2>4. Worked Engineering Case Study: Silicon Photovoltaic Solar Cell Cutoff</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>Monocrystalline silicon (Si) has an indirect semiconductor bandgap energy of \(E_g = 1.12\text{ eV}\) at standard room temperature (\(300\text{ K}\)). In a photovoltaic solar panel, an incoming photon from the Sun can excite an electron from the valence band to the conduction band only if its individual photon energy equals or exceeds the silicon bandgap (\(E_{\text{photon}} \ge E_g\)).</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Compute the photon energy in Joules corresponding to the silicon bandgap.</li>
              <li>Determine the maximum cutoff wavelength \(\lambda_{\text{cutoff}}\) (in nanometers and micrometers) that can generate electricity in a silicon solar cell.</li>
              <li>Explain what occurs when photons with \(\lambda = 1,400\text{ nm}\) (infrared) and \(\lambda = 450\text{ nm}\) (blue) strike the silicon wafer.</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Convert bandgap energy to standard SI Joules:</strong></p>
            <div class="math-block">
              $$E_g = 1.12\text{ eV} \times (1.602176634 \times 10^{-19}\text{ J/eV}) \approx 1.7944 \times 10^{-19}\text{ Joules}$$
            </div>

            <p><strong>Step 2: Calculate the cutoff wavelength \(\lambda_{\text{cutoff}}\):</strong></p>
            <div class="math-block">
              $$\lambda_{\text{cutoff}} = \frac{h \cdot c}{E_g} = \frac{1239.8419\text{ eV}\cdot\text{nm}}{1.12\text{ eV}} \approx 1,107.0\text{ nm (1.107 µm)}$$
            </div>
            <p>The critical absorption edge for crystalline silicon occurs in the near-infrared at approximately \(1,107\text{ nanometers}\).</p>

            <p><strong>Step 3: Analyze photon absorption behavior:</strong></p>
            <ul>
              <li><strong>For Infrared Light (\(\lambda = 1,400\text{ nm}\)):</strong>
                <div class="math-block">
                  $$E_{\text{photon}} = \frac{1239.84}{1400} \approx 0.886\text{ eV}$$
                </div>
                Because \(0.886\text{ eV} < 1.12\text{ eV}\), individual photons lack sufficient quantum energy to excite an electron across the bandgap. The silicon wafer appears optically transparent to 1,400 nm light, and the photons pass through without generating electrical current (transmission loss).
              </li>
              <li><strong>For Blue Light (\(\lambda = 450\text{ nm}\)):</strong>
                <div class="math-block">
                  $$E_{\text{photon}} = \frac{1239.84}{450} \approx 2.755\text{ eV}$$
                </div>
                Because \(2.755\text{ eV} > 1.12\text{ eV}\), a single blue photon readily generates an electron-hole pair. However, the excess energy (\(2.755 - 1.12 = 1.635\text{ eV}\), or \(59.3\%\) of the photon's energy) is rapidly lost within picoseconds as lattice thermal vibrations (phonon emissions)—a fundamental limitation established by the Shockley-Queisser solar cell efficiency limit.
              </li>
            </ul>
          </div>

          <h2>5. Photon Momentum and Radiation Pressure</h2>
          <p>Although photons possess zero rest mass (\(m_0 = 0\)), Albert Einstein and Arthur Compton proved that photons transport physical linear momentum. According to de Broglie’s relation:</p>
          <div class="math-block">
            $$p = \frac{E}{c} = \frac{h}{\lambda}$$
          </div>
          <p>When a continuous stream of light reflects off a surface, the momentum transfer exerts a physical force per unit area termed <strong>radiation pressure</strong>. For a perfectly reflective surface (such as an aluminized Mylar solar sail in interplanetary space), the momentum change doubles upon reflection (\(\Delta p = 2p\)), yielding radiation pressure \(P = 2I / c\), where \(I\) is solar irradiance in \(\text{W/m}^2\). Near Earth orbit (\(I \approx 1,361\text{ W/m}^2\)), solar radiation pressure exerts roughly \(9.08\text{ µN/m}^2\), enabling propellantless space exploration.</p>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>What is an "Einstein" in photochemistry?</h3>
            <p>In photochemistry and plant biology, an <strong>Einstein</strong> is defined as one mole of photons (\(N_A = 6.02214076 \times 10^{23}\) photons). Molar photon energy is calculated as \(E_{\text{mole}} = N_A \times hf = N_A \times (hc / \lambda)\), typically expressed in kilojoules per mole (\(\text{kJ/mol}\)) to compare directly with chemical bond enthalpies.</p>
          </div>
          <div class="faq-item">
            <h3>Why can ultraviolet light cause sunburn while intense visible light cannot?</h3>
            <p>Biological photochemical damage is governed strictly by the energy of <em>individual photons</em>, not the total intensity. UV-B photons (\(\approx 300\text{ nm}\), \(4.13\text{ eV}\)) carry enough discrete quantum energy to break covalent bonds in cellular DNA molecules, inducing pyrimidine dimers. Visible photons (\(\approx 2.0\text{ eV}\)) lack the threshold energy required to initiate this chemical reaction regardless of how bright the light is.</p>
          </div>
          <div class="faq-item">
            <h3>How does photon energy change when light passes into glass or water?</h3>
            <p>When light enters an optical medium with refractive index \(n > 1\), its frequency \(f\) remains completely unchanged because frequency is determined solely by the source oscillator. Because speed decreases (\(v = c / n\)), wavelength compresses (\(\lambda_{\text{medium}} = \lambda_0 / n\)). However, photon quantum energy \(E = hf\) remains constant.</p>
          </div>
          <div class="faq-item">
            <h3>What is the minimum photon energy required to produce an electron-positron pair?</h3>
            <p>According to mass-energy equivalence (\(E = mc^2\)), creating an electron-positron pair from a single photon in the field of an atomic nucleus requires an energy threshold equal to the combined rest mass of both particles: \(E_{\min} = 2 m_e c^2 = 2 \times 0.511\text{ MeV} = 1.022\text{ MeV}\) (\(\lambda \le 0.00121\text{ nm}\)).</p>
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
    // Universal Quantum Physical Constants
    const h_J = 6.62607015e-34;     // J·s
    const h_eV = 4.135667696e-15;   // eV·s
    const c = 299792458;            // m/s
    const hc_eV_nm = 1239.84193;    // eV·nm
    const q_e = 1.602176634e-19;    // J/eV
    const N_A = 6.02214076e23;      // mol^-1

    const presets = {
      green_532: { mode: 'wavelength', val: 532, unit: 'nm' },
      red_633: { mode: 'wavelength', val: 632.8, unit: 'nm' },
      blue_450: { mode: 'wavelength', val: 450, unit: 'nm' },
      uv_254: { mode: 'wavelength', val: 254, unit: 'nm' },
      ir_1550: { mode: 'wavelength', val: 1550, unit: 'nm' },
      xray_01: { mode: 'wavelength', val: 0.1, unit: 'nm' },
      wifi_24: { mode: 'frequency', val: 2.45, unit: 'ghz' }
    };

    function updateInputMode() {
      const mode = document.getElementById('inputMode').value;
      const lbl = document.getElementById('lblInputVal');
      const unitSelect = document.getElementById('unitInput');

      unitSelect.innerHTML = '';

      if (mode === 'wavelength') {
        lbl.textContent = "Electromagnetic Wavelength (λ)";
        unitSelect.innerHTML = `
          <option value="nm" selected>Nanometers (nm)</option>
          <option value="um">Micrometers (µm)</option>
          <option value="angstrom">Ångströms (Å)</option>
          <option value="m">Meters (m)</option>
        `;
        document.getElementById('valInput').value = '532';
      } else if (mode === 'frequency') {
        lbl.textContent = "Electromagnetic Frequency (f)";
        unitSelect.innerHTML = `
          <option value="thz" selected>Terahertz (THz)</option>
          <option value="ghz">Gigahertz (GHz)</option>
          <option value="mhz">Megahertz (MHz)</option>
          <option value="hz">Hertz (Hz)</option>
        `;
        document.getElementById('valInput').value = '563.5';
      } else if (mode === 'energy_ev') {
        lbl.textContent = "Photon Energy in Electron-Volts (eV)";
        unitSelect.innerHTML = `
          <option value="ev" selected>eV</option>
          <option value="mev">MeV</option>
          <option value="kev">keV</option>
          <option value="uev">µeV</option>
        `;
        document.getElementById('valInput').value = '2.331';
      } else if (mode === 'energy_j') {
        lbl.textContent = "Photon Energy in Joules (J)";
        unitSelect.innerHTML = `
          <option value="j" selected>Joules (J)</option>
          <option value="kj">Kilojoules (kJ)</option>
        `;
        document.getElementById('valInput').value = '3.734e-19';
      }
      calculate();
    }

    function applyPreset() {
      const p = document.getElementById('emPreset').value;
      if (p !== 'custom' && presets[p]) {
        const data = presets[p];
        document.getElementById('inputMode').value = data.mode;
        updateInputMode();
        document.getElementById('valInput').value = data.val;
        document.getElementById('unitInput').value = data.unit;
      }
      calculate();
    }

    function getBand(lambda_m) {
      if (lambda_m < 1e-11) return "Gamma Rays";
      if (lambda_m < 1e-8) return "X-Rays";
      if (lambda_m < 3.8e-7) return "Ultraviolet (UV)";
      if (lambda_m <= 7.5e-7) {
        if (lambda_m < 4.5e-7) return "Visible (Violet / Blue)";
        if (lambda_m < 4.95e-7) return "Visible (Cyan)";
        if (lambda_m < 5.7e-7) return "Visible (Green)";
        if (lambda_m < 5.9e-7) return "Visible (Yellow)";
        if (lambda_m < 6.2e-7) return "Visible (Orange)";
        return "Visible (Red)";
      }
      if (lambda_m < 1e-3) return "Infrared (IR)";
      if (lambda_m < 1.0) return "Microwave";
      return "Radio Waves";
    }

    function calculate() {
      const mode = document.getElementById('inputMode').value;
      const rawVal = parseFloat(document.getElementById('valInput').value) || 0;
      const unit = document.getElementById('unitInput').value;

      let lambda_m = 0;

      if (mode === 'wavelength') {
        switch(unit) {
          case 'nm': lambda_m = rawVal * 1e-9; break;
          case 'um': lambda_m = rawVal * 1e-6; break;
          case 'angstrom': lambda_m = rawVal * 1e-10; break;
          default: lambda_m = rawVal;
        }
      } else if (mode === 'frequency') {
        let f_hz = rawVal;
        switch(unit) {
          case 'thz': f_hz = rawVal * 1e12; break;
          case 'ghz': f_hz = rawVal * 1e9; break;
          case 'mhz': f_hz = rawVal * 1e6; break;
        }
        lambda_m = f_hz > 0 ? c / f_hz : 0;
      } else if (mode === 'energy_ev') {
        let ev = rawVal;
        switch(unit) {
          case 'mev': ev = rawVal * 1e6; break;
          case 'kev': ev = rawVal * 1e3; break;
          case 'uev': ev = rawVal * 1e-6; break;
        }
        lambda_m = ev > 0 ? (hc_eV_nm * 1e-9) / ev : 0;
      } else if (mode === 'energy_j') {
        let j = rawVal;
        if (unit === 'kj') j = rawVal * 1000;
        lambda_m = j > 0 ? (h_J * c) / j : 0;
      }

      if (lambda_m <= 0) return;

      const f = c / lambda_m;
      const E_J = h_J * f;
      const E_eV = E_J / q_e;
      const E_kJ_mol = (E_J * N_A) / 1000;
      const p = h_J / lambda_m;

      // Render Primary Box
      if (E_eV > 1e6) {
        document.getElementById('resEnergyEv').textContent = (E_eV / 1e6).toFixed(3) + " MeV";
      } else if (E_eV > 1e3) {
        document.getElementById('resEnergyEv').textContent = (E_eV / 1e3).toFixed(3) + " keV";
      } else if (E_eV < 0.001) {
        document.getElementById('resEnergyEv').textContent = (E_eV * 1e6).toFixed(3) + " µeV";
      } else {
        document.getElementById('resEnergyEv').textContent = E_eV.toFixed(3) + " eV";
      }

      document.getElementById('resEnergyJ').textContent = 
        E_J.toExponential(3) + " Joules • " + E_kJ_mol.toLocaleString('en-US', {maximumFractionDigits: 1}) + " kJ/mol (Einstein)";

      // Render Grid Items
      if (f > 1e15) {
        document.getElementById('resFreq').textContent = (f / 1e15).toFixed(2) + " PHz (" + f.toExponential(3) + " Hz)";
      } else if (f > 1e12) {
        document.getElementById('resFreq').textContent = (f / 1e12).toFixed(2) + " THz";
      } else if (f > 1e9) {
        document.getElementById('resFreq').textContent = (f / 1e9).toFixed(2) + " GHz";
      } else {
        document.getElementById('resFreq').textContent = (f / 1e6).toFixed(2) + " MHz";
      }

      const lambda_nm = lambda_m * 1e9;
      if (lambda_nm < 1) {
        document.getElementById('resWavelength').textContent = (lambda_m * 1e10).toFixed(2) + " Å (" + (lambda_m * 1e12).toFixed(1) + " pm)";
      } else if (lambda_nm > 10000) {
        document.getElementById('resWavelength').textContent = (lambda_m * 100).toFixed(2) + " cm (" + lambda_m.toFixed(3) + " m)";
      } else {
        document.getElementById('resWavelength').textContent = lambda_nm.toFixed(1) + " nm (" + (lambda_m * 1e6).toFixed(3) + " µm)";
      }

      document.getElementById('resMomentum').textContent = p.toExponential(3) + " kg·m/s";
      document.getElementById('resBand').textContent = getBand(lambda_m);
    }

    document.getElementById('inputMode').addEventListener('change', updateInputMode);
    document.getElementById('emPreset').addEventListener('change', applyPreset);
    document.querySelectorAll('input, select').forEach(el => {
      if (el.id !== 'inputMode' && el.id !== 'emPreset') {
        el.addEventListener('input', () => {
          document.getElementById('emPreset').value = 'custom';
          calculate();
        });
        el.addEventListener('change', () => {
          document.getElementById('emPreset').value = 'custom';
          calculate();
        });
      }
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('emPreset').value = 'green_532';
      applyPreset();
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
  <title>Simple Pendulum Calculator | Period, Length & Gravitational Oscillation</title>
  <meta name="description" content="Calculate simple pendulum oscillation period, frequency, pendulum length, local gravity (g), and large angle amplitude corrections.">
  <link rel="canonical" href="https://calchub.cloud/simple-pendulum-calculator.html">
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
        "name": "Simple Pendulum Calculator",
        "applicationCategory": "EngineeringApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates simple harmonic pendulum period, cycle frequency, required rod length, local gravitational acceleration, and large-angle Borda amplitude series expansions.",
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
            "name": "What is the formula for the period of a simple pendulum?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "For small angular amplitudes (θ < 15°), the period of a simple pendulum is T = 2π × √(L / g), where 'T' is oscillation period in seconds, 'L' is pendulum length in meters, and 'g' is local gravitational acceleration (9.80665 m/s² on Earth)."
            }
          },
          {
            "@type": "Question",
            "name": "Does the mass of the pendulum bob affect the period?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "No. In an ideal simple pendulum, the period is completely independent of the mass of the bob. Both the gravitational driving torque (τ = mgL sin θ) and the rotational inertia (I = mL²) scale linearly with mass, causing mass to cancel out of the equation of motion."
            }
          },
          {
            "@type": "Question",
            "name": "What is a 'seconds pendulum'?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A seconds pendulum is a pendulum whose half-period (the time for one swing or 'tick') is precisely one second, meaning its full back-and-forth period is T = 2.000 seconds. On Earth (g = 9.81 m/s²), a seconds pendulum requires a length of L = g / π² ≈ 0.9936 meters (39.12 inches)."
            }
          },
          {
            "@type": "Question",
            "name": "How does large amplitude affect the pendulum period?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "At larger amplitudes where sin θ cannot be approximated by θ, the period lengthens according to the Borda series expansion: T ≈ T₀ × [1 + (1/16)θ₀² + (11/3072)θ₀⁴], where θ₀ is maximum release angle in radians. At θ₀ = 30°, the period increases by roughly 1.7%."
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
        <h1>Simple Pendulum Calculator</h1>
        <p class="lead-text">Calculate pendulum oscillation period, cycle frequency, required length, local gravity (g), and peak bottom swing velocity with large-angle amplitude corrections.</p>

        <div class="calc-card">
          <div class="form-row">
            <div class="form-group col-half">
              <label for="solveTarget">Calculation Target</label>
              <select id="solveTarget" class="form-control">
                <option value="find_t" selected>Solve for Period (T) & Frequency (f)</option>
                <option value="find_l">Solve for Pendulum Length (L)</option>
                <option value="find_g">Solve for Local Gravity (g)</option>
              </select>
            </div>

            <div class="form-group col-half">
              <label for="gravEnv">Gravity Preset Environment</label>
              <select id="gravEnv" class="form-control">
                <option value="9.80665" selected>Earth Sea-Level (g = 9.81 m/s²)</option>
                <option value="1.62">Moon Surface (g = 1.62 m/s²)</option>
                <option value="3.72">Mars Surface (g = 3.72 m/s²)</option>
                <option value="24.79">Jupiter Cloudtops (g = 24.79 m/s²)</option>
                <option value="custom">Custom Gravity</option>
              </select>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-half" id="grpL">
              <label for="valLength">Pendulum Rod / String Length (L)</label>
              <div class="input-with-unit">
                <input type="number" id="valLength" class="form-control" value="0.9936" step="any" min="0.001">
                <select id="unitLength" class="unit-select">
                  <option value="m" selected>Meters (m)</option>
                  <option value="cm">Centimeters (cm)</option>
                  <option value="ft">Feet (ft)</option>
                  <option value="in">Inches (in)</option>
                </select>
              </div>
            </div>

            <div class="form-group col-half" id="grpT" style="display:none;">
              <label for="valPeriod">Desired Oscillation Period (T)</label>
              <div class="input-with-unit">
                <input type="number" id="valPeriod" class="form-control" value="2.0" step="any" min="0.001">
                <span style="font-size:12px; padding:6px 12px; background:#fff; border:1px solid #cbd5e1; border-left:none; border-radius:0 4px 4px 0; display:flex; align-items:center;">Seconds</span>
              </div>
            </div>

            <div class="form-group col-half">
              <label for="valAngle">Initial Release Angle (&theta;₀)</label>
              <div class="input-with-unit">
                <input type="number" id="valAngle" class="form-control" value="5" step="1" min="0.1" max="89.9">
                <span style="font-size:12px; padding:6px 12px; background:#fff; border:1px solid #cbd5e1; border-left:none; border-radius:0 4px 4px 0; display:flex; align-items:center;">Degrees (°)</span>
              </div>
            </div>
          </div>

          <div class="btn-group">
            <button type="button" id="calcBtn" class="btn btn-primary">Calculate Pendulum</button>
            <button type="button" id="resetBtn" class="btn btn-secondary">Reset to Seconds Pendulum (L ≈ 1m)</button>
          </div>

          <div id="resultsPanel" class="results-panel">
            <div class="result-box primary-result">
              <div class="result-label" id="resPrimaryLabel">Oscillation Period (T)</div>
              <div class="result-value" id="resPrimaryVal">2.000 s</div>
              <div class="result-sub" id="resPrimarySub">Frequency: 0.500 Hz (30.0 cycles/min) • Small-angle: 1.999 s</div>
            </div>

            <div class="result-grid">
              <div class="result-item">
                <span class="sub-label">Pendulum Length (L)</span>
                <span class="sub-value" id="resLength">0.994 m (39.12 in)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Angular Frequency (&omega;)</span>
                <span class="sub-value" id="resOmega">3.142 rad/s</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Max Speed at Lowest Point (v_max)</span>
                <span class="sub-value" id="resVmax">0.275 m/s (0.99 km/h)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Large Angle Period Increase</span>
                <span class="sub-value" id="resAmpCorr">+0.05% (Borda Series Correction)</span>
              </div>
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Classical Physics of the Simple Gravitational Pendulum</h2>
          <p>A simple pendulum consists of an idealized point mass \(m\) (the bob) suspended from a frictionless pivot by a light, inextensible, unstretchable string or rod of length \(L\). When displaced laterally by an angle \(\theta\) from its vertical downward equilibrium and released, the tangential component of gravity exerts a restoring torque that accelerates the bob back toward the central vertical axis.</p>
          <p>According to Newton's Second Law for rotational motion (\(\tau = I \alpha\)), the differential equation governing the angular position \(\theta(t)\) is:</p>
          <div class="math-block">
            $$-m g L \sin\theta = (m L^2) \frac{d^2\theta}{dt^2} \implies \frac{d^2\theta}{dt^2} + \frac{g}{L} \sin\theta = 0$$
          </div>
          <p>This is a non-linear second-order differential equation. Notice that the mass \(m\) cancels out entirely: the motion of an ideal pendulum is completely independent of the bob's mass, volume, or material density—a fact first observed by Galileo Galilei in 1582 while watching a swinging bronze chandelier in the Cathedral of Pisa.</p>

          <h2>2. Small-Angle Approximation & The Harmonic Period Equation</h2>
          <p>For modest displacement angles (\(\theta < 15^\circ \approx 0.26\text{ radians}\)), the Maclaurin series expansion for sine (\(\sin\theta = \theta - \frac{\theta^3}{6} + \frac{\theta^5}{120} - \dots\)) allows the approximation \(\sin\theta \approx \theta\). Substituting this linear approximation transforms the equation into the canonical <strong>Simple Harmonic Motion (SHM)</strong> differential equation:</p>
          <div class="math-block">
            $$\frac{d^2\theta}{dt^2} + \left(\frac{g}{L}\right) \theta = 0$$
          </div>
          <p>The natural angular frequency of oscillation is \(\omega = \sqrt{g / L}\). Because period \(T = 2\pi / \omega\), the celebrated small-angle period formulation is:</p>
          <div class="math-block">
            $$T_0 = 2\pi \sqrt{\frac{L}{g}}$$
          </div>
          <p>And the corresponding temporal cycle frequency \(f\) in Hertz (\(\text{cycles/sec}\)) is:</p>
          <div class="math-block">
            $$f = \frac{1}{T_0} = \frac{1}{2\pi} \sqrt{\frac{g}{L}}$$
          </div>

          <h2>3. Large-Angle Amplitude Correction (Borda's Series)</h2>
          <p>When the initial release amplitude \(\theta_0\) exceeds \(15^\circ\), the small-angle approximation introduces measurable timing error. The exact period requires evaluating a complete elliptic integral of the first kind \(K(\sin(\theta_0 / 2))\). Expanding this integral via the <strong>Borda series</strong> yields:</p>
          <div class="math-block">
            $$T = T_0 \left[ 1 + \frac{1}{16}\theta_0^2 + \frac{11}{3072}\theta_0^4 + \frac{173}{737280}\theta_0^6 + \dots \right]$$
          </div>
          <p>Where \(\theta_0\) is expressed in radians. For example, at an amplitude of \(\theta_0 = 30^\circ\) (\(0.5236\text{ rad}\)), the first correction term adds \(\frac{1}{16}(0.5236)^2 \approx 0.0171\), increasing the oscillation period by \(1.71\%\) (a clock error of roughly \(24\text{ minutes per day}\)).</p>

          <h2>4. Historical and Engineering Benchmark Reference Table</h2>
          <p>To assist horologists, structural dynamics engineers, and science educators, the table below documents representative pendulums across history and modern engineering:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Pendulum System</th>
                <th>Effective Length (\(L\))</th>
                <th>Local Gravity (\(g\))</th>
                <th>Period (\(T\))</th>
                <th>Engineering Purpose</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Standard Seconds Pendulum (Earth)</td>
                <td>0.9936 m (39.12 in)</td>
                <td>9.807 m/s²</td>
                <td>2.000 seconds (1-sec tick)</td>
                <td>Horological benchmark for precision longcase grandfather clocks</td>
              </tr>
              <tr>
                <td>Mantle / Shelf Clock Pendulum</td>
                <td>0.248 m (9.76 in)</td>
                <td>9.807 m/s²</td>
                <td>1.000 second (0.5-sec tick)</td>
                <td>Compact domestic mechanical clock escapement</td>
              </tr>
              <tr>
                <td>Original Foucault Pendulum (Panthéon, Paris)</td>
                <td>67.0 meters</td>
                <td>9.81 m/s²</td>
                <td>16.42 seconds</td>
                <td>Demonstrating Earth's daily planetary rotation (1851)</td>
              </tr>
              <tr>
                <td>Taipei 101 Tuned Mass Damper (TMD)</td>
                <td>42.0 meters (Cables)</td>
                <td>9.79 m/s²</td>
                <td>13.02 seconds</td>
                <td>660-tonne steel sphere mitigating typhoon & earthquake sway</td>
              </tr>
              <tr>
                <td>Apollo 15 Lunar Surface Pendulum</td>
                <td>0.9936 m</td>
                <td>1.62 m/s² (Moon)</td>
                <td>4.922 seconds</td>
                <td>Measuring local lunar gravitational acceleration anomalies</td>
              </tr>
              <tr>
                <td>Industrial Crane Hoist Cable Load</td>
                <td>25.0 meters</td>
                <td>9.81 m/s²</td>
                <td>10.03 seconds</td>
                <td>Anti-sway automation algorithm calibration for container ports</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Worked Engineering Case Study: Gravity Measurement via Precision Pendulum</h2>
          <div class="worked-example-card">
            <h3>Problem Statement</h3>
            <p>A geophysics survey team is determining local gravitational acceleration \(g\) atop a mountain observatory using a calibrated invar-rod simple pendulum. The distance from the suspension pivot knife-edge to the center of mass of the spherical bob is measured as \(L = 1.2500\text{ meters}\). The pendulum is released from a small amplitude of \(\theta_0 = 4.0^\circ\) (\(0.06981\text{ rad}\)). An optical photogate measures the elapsed time for 100 complete oscillations as \(t_{\text{total}} = 224.62\text{ seconds}\).</p>
            <p><strong>Required:</strong></p>
            <ol>
              <li>Compute the experimental oscillation period \(T\).</li>
              <li>Evaluate the small-angle amplitude correction factor.</li>
              <li>Calculate the exact local gravitational acceleration \(g\) to four decimal places.</li>
            </ol>

            <h3>Step-by-Step Mathematical Solution</h3>
            <p><strong>Step 1: Calculate measured period \(T\):</strong></p>
            <div class="math-block">
              $$T = \frac{t_{\text{total}}}{100} = \frac{224.62\text{ s}}{100} = 2.24620\text{ seconds}$$
            </div>

            <p><strong>Step 2: Apply Borda's amplitude correction to isolate small-angle period \(T_0\):</strong></p>
            <div class="math-block">
              $$T = T_0 \left(1 + \frac{\theta_0^2}{16}\right) \implies T_0 = \frac{T}{1 + \frac{(0.06981)^2}{16}} = \frac{2.24620}{1 + 0.0003046} \approx 2.24552\text{ seconds}$$
            </div>

            <p><strong>Step 3: Solve for gravitational acceleration \(g\):</strong></p>
            <div class="math-block">
              $$T_0 = 2\pi \sqrt{\frac{L}{g}} \implies T_0^2 = \frac{4\pi^2 L}{g} \implies g = \frac{4\pi^2 L}{T_0^2}$$
            </div>
            <div class="math-block">
              $$g = \frac{4 \times (3.14159265)^2 \times 1.2500}{(2.24552)^2} = \frac{49.34802}{5.04236} \approx 9.7867\text{ m/s}^2$$
            </div>
            <p><strong>Geophysical Interpretation:</strong> The calculated value of \(g = 9.7867\text{ m/s}^2\) is noticeably lower than standard sea-level gravity (\(9.80665\text{ m/s}^2\)), reflecting the Free-Air Gravity Anomaly caused by the mountain observatory's high altitude (\(\approx 2,100\text{ meters}\) above sea level).</p>
          </div>

          <h2>6. Physical Pendulums vs. Simple Pendulums</h2>
          <p>Real physical objects (such as a swinging baseball bat or a solid metal pendulum rod) are <strong>compound (physical) pendulums</strong> with distributed mass rather than an idealized point mass. By applying the parallel axis theorem (\(I = I_{\text{cm}} + md^2\)), the period of a physical pendulum is:</p>
          <div class="math-block">
            $$T = 2\pi \sqrt{\frac{I}{m g d}}$$
          </div>
          <p>Where \(I\) is total moment of inertia about the pivot, and \(d\) is distance from the pivot to the center of mass. Every physical pendulum possesses an equivalent simple pendulum length \(L_{\text{eq}} = I / (md)\), identifying the <strong>center of oscillation</strong> (the "sweet spot" where impact forces generate zero reaction kick at the pivot).</p>

          <h2>7. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-item">
            <h3>Why did historical pendulum clocks lose time during hot summer months?</h3>
            <p>Thermal expansion causes the metal pendulum rod to lengthen as ambient temperature rises (\(\Delta L = \alpha L \Delta T\)). Because period scales with \(\sqrt{L}\), a longer rod swings slower, causing uncompensated clocks to lose several seconds per day. Horologists solved this by inventing temperature-compensated "gridiron" pendulums (combining alternating brass and steel rods) and mercury-filled pendulum bobs.</p>
          </div>
          <div class="faq-item">
            <h3>How does the Foucault Pendulum prove Earth's rotation?</h3>
            <p>A Foucault pendulum swings freely in an invariant inertial plane of oscillation. As Earth rotates beneath the pendulum, the floor appears to turn relative to the plane of the swing. The rate of apparent plane precession depends on latitude: \(\omega = 360^\circ \sin(\text{latitude})\) per day. At the North Pole, it completes a full \(360^\circ\) clockwise circle every 24 hours.</p>
          </div>
          <div class="faq-item">
            <h3>What is the maximum velocity of a pendulum bob during its swing?</h3>
            <p>By conservation of mechanical energy (\(mgh = \frac{1}{2}mv^2\)), the maximum velocity occurs at the lowest point of the swing where potential energy is completely converted into kinetic energy: \(v_{\max} = \sqrt{2gL(1 - \cos\theta_0)}\).</p>
          </div>
          <div class="faq-item">
            <h3>What is the maximum string tension experienced during a pendulum swing?</h3>
            <p>At the bottom of the swing, the string must support both gravitational weight (\(mg\)) and supply centripetal acceleration (\(m v^2 / L\)). The peak tension is \(T_{\text{max}} = mg + \frac{mv^2}{L} = mg(3 - 2\cos\theta_0)\). When released from \(90^\circ\) (\(\cos 90^\circ = 0\)), the maximum string tension is exactly three times the bob's resting weight (\(3mg\)).</p>
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
    // Simple Pendulum Engine
    const toMeters = (l, unit) => {
      switch(unit) {
        case 'cm': return l / 100;
        case 'ft': return l * 0.3048;
        case 'in': return l * 0.0254;
        default: return l;
      }
    };

    function updateTarget() {
      const mode = document.getElementById('solveTarget').value;
      document.getElementById('grpL').style.display = mode === 'find_l' ? 'none' : 'block';
      document.getElementById('grpT').style.display = mode === 'find_l' ? 'block' : 'none';
      calculate();
    }

    function calculate() {
      const mode = document.getElementById('solveTarget').value;
      const g = parseFloat(document.getElementById('gravEnv').value) || 9.80665;
      const angleDeg = parseFloat(document.getElementById('valAngle').value) || 5;
      const theta0 = angleDeg * (Math.PI / 180);

      // Borda expansion factor: 1 + theta^2/16 + 11*theta^4/3072
      const bordaFactor = 1 + (theta0 * theta0) / 16 + (11 * Math.pow(theta0, 4)) / 3072;
      const pctIncrease = (bordaFactor - 1) * 100;

      let L = 0, T = 0, T0 = 0;

      if (mode === 'find_t') {
        L = toMeters(parseFloat(document.getElementById('valLength').value) || 1, document.getElementById('unitLength').value);
        if (L <= 0 || g <= 0) return;
        T0 = 2 * Math.PI * Math.sqrt(L / g);
        T = T0 * bordaFactor;
      } else if (mode === 'find_l') {
        T = parseFloat(document.getElementById('valPeriod').value) || 2.0;
        T0 = T / bordaFactor;
        L = (g * T0 * T0) / (4 * Math.PI * Math.PI);
      } else if (mode === 'find_g') {
        L = toMeters(parseFloat(document.getElementById('valLength').value) || 1, document.getElementById('unitLength').value);
        T = parseFloat(document.getElementById('valPeriod').value) || 2.0;
        T0 = T / bordaFactor;
        const calc_g = (4 * Math.PI * Math.PI * L) / (T0 * T0);

        document.getElementById('resPrimaryLabel').textContent = "Calculated Local Gravity (g)";
        document.getElementById('resPrimaryVal').textContent = calc_g.toFixed(4) + " m/s²";
        document.getElementById('resPrimarySub').textContent = 
          "Equivalent to " + (calc_g / 9.80665).toFixed(4) + " Earth g (" + (calc_g * 3.28084).toFixed(3) + " ft/s²)";

        document.getElementById('resLength').textContent = L.toFixed(4) + " m";
        document.getElementById('resOmega').textContent = (2 * Math.PI / T).toFixed(3) + " rad/s";
        document.getElementById('resVmax').textContent = "N/A";
        document.getElementById('resAmpCorr').textContent = "+" + pctIncrease.toFixed(3) + "% Borda correction";
        return;
      }

      const f = 1 / T;
      const omega = Math.sqrt(g / L);
      // Max velocity at bottom v_max = sqrt(2*g*L*(1 - cos(theta)))
      const v_max = Math.sqrt(2 * g * L * (1 - Math.cos(theta0)));

      // Render Primary Box
      if (mode === 'find_t') {
        document.getElementById('resPrimaryLabel').textContent = "Oscillation Period (T)";
        document.getElementById('resPrimaryVal').textContent = T.toFixed(3) + " s";
        document.getElementById('resPrimarySub').textContent = 
          "Frequency: " + f.toFixed(3) + " Hz (" + (f * 60).toFixed(1) + " cycles/min) • Small-angle T₀: " + T0.toFixed(3) + " s";
      } else if (mode === 'find_l') {
        document.getElementById('resPrimaryLabel').textContent = "Required Pendulum Length (L)";
        document.getElementById('resPrimaryVal').textContent = L.toFixed(4) + " m (" + (L * 100).toFixed(2) + " cm)";
        document.getElementById('resPrimarySub').textContent = 
          "Equivalent to " + (L * 39.3701).toFixed(2) + " inches (" + (L * 3.28084).toFixed(3) + " ft)";
      }

      // Render Grid Items
      document.getElementById('resLength').textContent = 
        L.toFixed(3) + " m (" + (L * 39.3701).toFixed(2) + " in)";

      document.getElementById('resOmega').textContent = omega.toFixed(3) + " rad/s";
      document.getElementById('resVmax').textContent = 
        v_max.toFixed(3) + " m/s (" + (v_max * 3.6).toFixed(2) + " km/h)";

      document.getElementById('resAmpCorr').textContent = 
        "+" + pctIncrease.toFixed(3) + "% (Borda Series Expansion)";
    }

    document.getElementById('solveTarget').addEventListener('change', updateTarget);
    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculate);
      el.addEventListener('change', calculate);
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('solveTarget').value = 'find_t';
      document.getElementById('gravEnv').value = '9.80665';
      document.getElementById('valLength').value = '0.9936';
      document.getElementById('unitLength').value = 'm';
      document.getElementById('valAngle').value = '5';
      updateTarget();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p1 = os.path.join(base_dir, "photon-energy-calculator.html")
    p2 = os.path.join(base_dir, "simple-pendulum-calculator.html")

    with open(p1, "w", encoding="utf-8") as f:
        f.write(TOOL_1_HTML)
    print(f"Generated {p1}")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(TOOL_2_HTML)
    print(f"Generated {p2}")

if __name__ == "__main__":
    main()
