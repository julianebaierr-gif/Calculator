"""
Generates bolt-torque-calculator.html and bearing-life-calculator.html
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
# 1. BOLT TORQUE CALCULATOR
# ==========================================
TOOL_BOLT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bolt Torque Calculator — Preload Tension &amp; Tightening Torque (VDI 2230 / ISO 898)</title>
  <meta name="description" content="Calculate bolt tightening torque, clamp load preload tension, and thread friction for metric and imperial fasteners using VDI 2230 and standard torque coefficient nut factor formulas.">
  <meta name="keywords" content="bolt torque calculator, tightening torque calculator, bolt preload calculator, torque tension relationship, bolt clamp load, metric bolt torque 8.8 10.9 12.9, vdi 2230 tightening torque">
  <link rel="canonical" href="https://calchub.org/bolt-torque-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Bolt Torque & Preload Tension Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates required tightening torque, axial bolt preload force, proof load stress, and friction head loss per ISO 898-1 and VDI 2230 standards."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "How is bolt tightening torque calculated from desired clamp load?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Bolt tightening torque is standardly calculated using the short-form friction equation: T = K × D × F, where T is the tightening torque (N·m or lbf·ft), K is the dimensionless torque coefficient (nut factor), D is the nominal bolt diameter (meters or feet), and F is the target axial clamp preload force (Newtons or pounds-force). For detailed engineering under VDI 2230, the formula separates pitch lead angle torque, thread flank friction, and under-head washer face bearing friction."
            }
          },
          {
            "@type": "Question",
            "name": "What is the K-factor (Nut Factor) and how does lubrication change bolt torque?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The K-factor represents total friction resistance during tightening. For dry, unlubricated zinc-plated steel bolts, K typically ranges between 0.20 and 0.22. Applying light machine oil reduces K to 0.15, while high-temperature anti-seize paste (molybdenum disulfide / copper paste) drops K to between 0.10 and 0.12. Because torque is directly proportional to K, applying anti-seize to a dry-torque specification increases clamp tension by over 70%, easily snapping the fastener or yielding joint threads."
            }
          },
          {
            "@type": "Question",
            "name": "What percentage of yield strength is recommended for bolt preload?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard industrial practice recommends preloading static bolted joints to between 70% and 75% of proof strength (or approximately 65% to 70% of minimum yield strength). For critical dynamically loaded, fatigue-sensitive joints (such as connecting rod cap bolts or structural steel per AISC/RCSC), preloads of 90% of proof load or torque-to-yield (TTY) angle methods are specified to maximize clamping stiffness and eliminate joint separation."
            }
          },
          {
            "@type": "Question",
            "name": "What are the proof strength and tensile ratings for ISO metric grades 8.8, 10.9, and 12.9?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under ISO 898-1: Grade 8.8 has a nominal tensile strength of 800 MPa, yield strength of 640 MPa, and proof stress of 580 MPa. Grade 10.9 has 1000 MPa tensile, 900 MPa yield, and 830 MPa proof stress. Grade 12.9 has 1200 MPa tensile, 1080 MPa yield, and 970 MPa proof stress. Selecting the correct grade is vital because a Grade 10.9 bolt requires 43% more torque than a Grade 8.8 bolt of the same diameter to achieve its rated clamp force."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body class="cat-theme-mechanical">

  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="engineering.html" class="nav-link">⚡ Electrical</a>
          <a href="mechanical.html" class="nav-link active">⚙️ Mechanical</a>
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
      <span class="category-tag">⚙️ Mechanical Machine Design &amp; VDI 2230</span>
      <h1 class="calc-page-title">Bolt Torque Calculator</h1>
      <p class="calc-page-desc">Calculate required tightening torque, axial preload clamp force, and proof stress percentage for standard metric and imperial bolted connections across various lubrication conditions.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>🔩</span> Fastener &amp; Tightening Parameters</h2>
            <span class="status-info">ISO 898-1 / SAE J429</span>
          </div>
          <form id="bolt-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="bolt-standard">Thread Standard &amp; Sizing</label>
                <select id="bolt-standard" class="form-control" onchange="updateBoltSpecs()">
                  <option value="M6" data-d="6" data-p="1.0" data-as="20.1">M6 × 1.0 mm (Coarse)</option>
                  <option value="M8" data-d="8" data-p="1.25" data-as="36.6">M8 × 1.25 mm (Coarse)</option>
                  <option value="M10" data-d="10" data-p="1.5" data-as="58.0">M10 × 1.5 mm (Coarse)</option>
                  <option value="M12" data-d="12" data-p="1.75" data-as="84.3" selected>M12 × 1.75 mm (Coarse)</option>
                  <option value="M14" data-d="14" data-p="2.0" data-as="115.0">M14 × 2.0 mm (Coarse)</option>
                  <option value="M16" data-d="16" data-p="2.0" data-as="157.0">M16 × 2.0 mm (Coarse)</option>
                  <option value="M20" data-d="20" data-p="2.5" data-as="245.0">M20 × 2.5 mm (Coarse)</option>
                  <option value="M24" data-d="24" data-p="3.0" data-as="353.0">M24 × 3.0 mm (Coarse)</option>
                  <option value="M30" data-d="30" data-p="3.5" data-as="561.0">M30 × 3.5 mm (Coarse)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="bolt-grade">Steel Material Property Class</label>
                <select id="bolt-grade" class="form-control" onchange="runBoltCalc()">
                  <option value="4.8" data-proof="310" data-yield="340" data-tensile="400">Class 4.8 (Low Carbon Steel)</option>
                  <option value="8.8" data-proof="580" data-yield="640" data-tensile="800" selected>Class 8.8 (Standard High Tensile)</option>
                  <option value="10.9" data-proof="830" data-yield="900" data-tensile="1000">Class 10.9 (Automotive Structural)</option>
                  <option value="12.9" data-proof="970" data-yield="1080" data-tensile="1200">Class 12.9 (Heavy Machinery Alloy)</option>
                  <option value="A2-70" data-proof="450" data-yield="450" data-tensile="700">Stainless Steel A2-70 / 304</option>
                  <option value="A4-80" data-proof="600" data-yield="600" data-tensile="800">Stainless Steel A4-80 / 316</option>
                </select>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="lubrication-condition">Surface Condition &amp; Nut Factor (K)</label>
                <select id="lubrication-condition" class="form-control" onchange="runBoltCalc()">
                  <option value="0.20" selected>Dry / As Received (Zinc Plated / K = 0.20)</option>
                  <option value="0.15">Light Machine Oil / Clean Steel (K = 0.15)</option>
                  <option value="0.12">Moly Anti-Seize / Extreme Pressure Paste (K = 0.12)</option>
                  <option value="0.18">Cadmium Plated / Phosphated (K = 0.18)</option>
                  <option value="0.28">Dry Stainless Steel on Stainless (Galling Risk / K = 0.28)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="target-preload-pct">Target Preload Percentage of Proof Load</label>
                <select id="target-preload-pct" class="form-control" onchange="runBoltCalc()">
                  <option value="0.65">65% of Proof Load (Gasketed / Low Fatigue)</option>
                  <option value="0.75" selected>75% of Proof Load (Standard Industrial Practice)</option>
                  <option value="0.85">85% of Proof Load (Rigid Dynamic Joints)</option>
                  <option value="0.90">90% of Proof Load (Structural Steel High-Slip)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runBoltCalc()">Calculate Bolt Torque &amp; Preload</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Bolted Joint Report</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Bolted Connection Engineering Analysis</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Recommended Tightening Torque</div>
            <div id="res-torque-nm" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">88.1 N·m</div>
            <div id="res-torque-imperial" style="font-size:1.05rem;color:#2563EB;font-weight:700;">64.9 lbf·ft (779.6 lbf·in)</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Axial Clamp Force (Preload Tension)</span>
              <span id="res-clamp-force" class="result-val" style="font-size:1.1rem;font-weight:700;color:#059669;">36.67 kN (8,244 lbf)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Fastener Tensile Stress Area (As)</span>
              <span id="res-stress-area" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">84.3 mm²</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Preload Tensile Stress</span>
              <span id="res-tensile-stress" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">435.0 MPa</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Material Proof Strength</span>
              <span id="res-proof-strength" class="result-val" style="font-size:1.1rem;font-weight:700;color:#475569;">580.0 MPa</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Torque Distribution: Thread Friction</span>
              <span id="res-thread-loss" class="result-val" style="font-size:1.1rem;font-weight:700;color:#DC2626;">~40% - 45%</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Torque Distribution: Head Friction</span>
              <span id="res-head-loss" class="result-val" style="font-size:1.1rem;font-weight:700;color:#DC2626;">~45% - 50%</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#EFF6FF;border:1px solid #BFDBFE;font-size:0.85rem;color:#1E40AF;">
            <strong>⚙️ Related Mechanical Tools:</strong> Verify rotational drive capacity with our <a href="torque-calculator.html" style="color:#1E40AF;font-weight:700;">Torque &amp; Power Calculator</a> or check machine drive ratio with the <a href="gear-ratio-calculator.html" style="color:#1E40AF;font-weight:700;">Gear Ratio Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Physics of Bolted Joints: Clamp Force vs Tightening Torque</h2>
        <p>A threaded fastener functions primarily as an ultra-stiff tension spring. When a technician turns a wrench to apply torque, the helical inclined plane of the thread converts rotational movement into axial elongation. This elongation stretches the bolt shank while compressing the clamped mating flanges together. The resulting compressive force—termed the <strong>clamp load</strong> or <strong>preload tension ($F_p$)</strong>—is the single parameter that holds mechanical assemblies together, prevents cyclic fatigue failure, seals pressurized gaskets, and prevents frictional joint slip under transverse shear loads.</p>

        <p>However, torque wrenches do not measure tension directly; they measure rotational resistance. In an unlubricated bolted connection, approximately <strong>90% of the input torque</strong> is lost overcoming frictional resistance at the mating interfaces (under-head bearing face friction and thread flank friction), leaving only about <strong>10% of torque</strong> to actually stretch the fastener shank and generate clamping force. Understanding the mathematical mechanics of bolt friction is essential to prevent both under-tightening (which leads to fatigue failure and vibration loosening) and over-tightening (which causes thread stripping or bolt fracture).</p>

        <h2>Mathematical Preload &amp; Tightening Torque Formulas</h2>
        <p>In standard engineering design, tightening torque is governed by two formal models: the simplified nut factor relationship and the rigorous VDI 2230 thread friction model.</p>

        <h3>1. The Standard Torque Coefficient (Nut Factor) Equation</h3>
        <p>Widely adopted by the Society of Automotive Engineers (SAE), American Institute of Steel Construction (AISC), and machinery guidelines:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$T = K \cdot D \cdot F_p$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$T$</strong> = Required tightening torque in Newton-meters ($\text{N}\cdot\text{m}$) or pound-feet ($\text{lbf}\cdot\text{ft}$).</li>
          <li><strong>$K$</strong> = Dimensionless nut factor (torque coefficient), encompassing thread friction, bearing face friction, and thread lead angle geometry.</li>
          <li><strong>$D$</strong> = Nominal major bolt diameter (e.g., $0.012\text{ m}$ for an M12 fastener).</li>
          <li><strong>$F_p$</strong> = Desired axial clamp preload force in Newtons ($\text{N}$) or pounds-force ($\text{lbf}$).</li>
        </ul>

        <h3>2. Fastener Proof Load &amp; Tensile Stress Area</h3>
        <p>The maximum safe clamp force depends on the fastener's nominal cross-sectional tensile stress area ($A_s$), defined under ISO 898-1 as:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$A_s = \frac{\pi}{4} \left( D - 0.9382 \cdot P \right)^2$$
        </div>
        <p>Where $D$ is the nominal major diameter and $P$ is the thread pitch in millimeters. The target axial preload force is then calculated based on the specified percentage of material proof strength ($\sigma_{proof}$):</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$F_p = A_s \cdot \sigma_{proof} \cdot \eta_{preload}$$
        </div>
        <p>Where $\eta_{preload}$ is the engineering preload fraction (typically $0.75$ for general engineering and up to $0.90$ for slip-critical structural connections).</p>

        <h2>Friction Coefficient Nut Factor (K) Reference Table</h2>
        <p>The nut factor $K$ is heavily dependent on surface treatments, coatings, and lubrication. The following table highlights empirical $K$ values under controlled tightening conditions:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Fastener Surface &amp; Lubricant Condition</th>
                <th style="padding:0.75rem;">Nut Factor (K) Range</th>
                <th style="padding:0.75rem;">Typical Value</th>
                <th style="padding:0.75rem;">Risk Assessment &amp; Application</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Zinc-Plated (Dry, as-received)</strong></td>
                <td style="padding:0.75rem;">0.19 – 0.25</td>
                <td style="padding:0.75rem;">0.20</td>
                <td style="padding:0.75rem;">Standard commercial fasteners; wide scatter in friction.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Light Machine Oil / Clean Steel</strong></td>
                <td style="padding:0.75rem;">0.14 – 0.17</td>
                <td style="padding:0.75rem;">0.15</td>
                <td style="padding:0.75rem;">Automotive and machinery shop assembly standard.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Moly Anti-Seize Paste ($\text{MoS}_2$)</strong></td>
                <td style="padding:0.75rem;">0.10 – 0.13</td>
                <td style="padding:0.75rem;">0.12</td>
                <td style="padding:0.75rem;">High temperature flanges; must reduce wrench torque by ~40%!</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Phosphate &amp; Oil (Black Oxide)</strong></td>
                <td style="padding:0.75rem;">0.15 – 0.19</td>
                <td style="padding:0.75rem;">0.17</td>
                <td style="padding:0.75rem;">Consistent friction profile; preferred for structural steel.</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>Dry Stainless Steel (A2 / A4 on 304/316)</strong></td>
                <td style="padding:0.75rem;">0.24 – 0.35</td>
                <td style="padding:0.75rem;">0.28</td>
                <td style="padding:0.75rem;">High galling risk; always use anti-seize paste on stainless threads.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: M16 Flange Bolting
          </h3>
          <p><strong>Scenario:</strong> A piping engineer is specifying the tightening torque for a high-pressure pump discharge flange secured with metric <strong>M16 × 2.0 mm Class 8.8</strong> high-tensile steel bolts. The threads are lubricated with light machine oil ($K = 0.15$), and the target clamp tension is $75\%$ of proof load.</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Determine Tensile Stress Area ($A_s$):</strong>
              $$A_s = \frac{\pi}{4}(16 - 0.9382 \times 2.0)^2 = 157.0\text{ mm}^2 = 157.0 \times 10^{-6}\text{ m}^2$$
            </li>
            <li><strong>Look up Proof Strength ($\sigma_{proof}$):</strong> Under ISO 898-1, Class 8.8 steel has a proof strength of $580\text{ MPa}$ ($580\times 10^6\text{ N/m}^2$).</li>
            <li><strong>Calculate Required Preload Tension ($F_p$):</strong>
              $$F_p = 157.0 \times 10^{-6}\text{ m}^2 \times 580 \times 10^6\text{ N/m}^2 \times 0.75 = 68,295\text{ N} = 68.30\text{ kN}$$
            </li>
            <li><strong>Compute Tightening Torque ($T$):</strong>
              $$T = K \cdot D \cdot F_p = 0.15 \times 0.016\text{ m} \times 68,295\text{ N} = 163.9\text{ N}\cdot\text{m}$$
            </li>
            <li><strong>Comparison Note:</strong> If the bolts were assembled dry with zinc plating ($K = 0.20$), achieving the exact same $68.30\text{ kN}$ clamp force would require $T = 0.20 \times 0.016 \times 68,295 = 218.5\text{ N}\cdot\text{m}$. Applying dry torque to oiled threads would overload the fastener to $100\%$ of yield strength!</li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why do bolted joints loosen under vibration even when torqued properly?</h4>
            <p style="margin:0;color:#64748B;">Dynamic transverse shear loads cause microscopic slip between mating threads. When transversal forces overcome the frictional locking angle, the screw unwinds by fractions of a degree per cycle (the Junker effect). Preventing vibration loosening requires sufficient initial preload tension, Nord-Lock wedge washers, prevailing torque locknuts, or liquid threadlocker.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is the difference between Torque-to-Yield (TTY) bolts and reusable standard bolts?</h4>
            <p style="margin:0;color:#64748B;">Standard fasteners operate entirely within their elastic range (below proof stress), meaning they return to their original length when loosened and can be reused. Torque-to-Yield (TTY) fasteners (common in engine cylinder heads) are intentionally stretched past their plastic yield point. TTY bolts provide highly consistent clamp force across variations in friction, but undergo permanent plastic deformation and must never be reused.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">How accurate is a calibrated click-type torque wrench?</h4>
            <p style="margin:0;color:#64748B;">While a calibrated torque wrench has an instrument accuracy of &plusmn;3% to &plusmn;5%, the resulting clamp force variation in the fastener can be as high as &plusmn;25% to &plusmn;30% due to unmeasured variations in surface roughness, thread burrs, and lubricant distribution. For critical aerospace and structural connections, ultrasonic elongation measurement or turn-of-nut angle tightening is required.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why does stainless steel gall during tightening and how can it be avoided?</h4>
            <p style="margin:0;color:#64748B;">Austenitic stainless steels (304, 316) self-passivate with an ultra-thin chromium oxide layer. Under thread contact pressure, friction strips this protective layer, causing microscopic bare metal asperities to cold-weld (gall) together. Galling can seize a bolt instantly before target torque is reached. It is prevented by applying specialized nickel or PTFE anti-seize paste and keeping wrench RPM low.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚙️ Mechanical Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="bolt-torque-calculator.html" style="font-weight:700;color:#2563EB;">🔩 Bolt Torque &amp; Preload</a></li>
          <li><a href="bearing-life-calculator.html" style="color:#475569;">⚙️ Bearing Life (ISO 281)</a></li>
          <li><a href="torque-calculator.html" style="color:#475569;">🔄 Torque &amp; Shaft Power</a></li>
          <li><a href="gear-ratio-calculator.html" style="color:#475569;">⚙️ Gear Ratio &amp; Speed</a></li>
          <li><a href="pipe-sizing-calculator.html" style="color:#475569;">🚰 Pipe Sizing &amp; Flow</a></li>
          <li><a href="pump-head-calculator.html" style="color:#475569;">🌊 Pump Head (TDH)</a></li>
          <li><a href="cooling-load-calculator.html" style="color:#475569;">❄️ HVAC Cooling Load</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Engineering Design Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="beam-deflection-calculator.html" style="color:#475569;">📐 Beam Deflection &amp; Moments</a></li>
          <li><a href="rebar-calculator.html" style="color:#475569;">🔩 Rebar Weight &amp; Spacing</a></li>
          <li><a href="concrete-calculator.html" style="color:#475569;">🏗️ Concrete Volume &amp; Mix</a></li>
          <li><a href="unit-converter.html" style="color:#475569;">🔄 Universal Unit Converter</a></li>
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
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">Fastener Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          ISO 898-1 Metric Bolts<br>
          VDI 2230 Systematic Calculation<br>
          SAE J429 Mechanical Requirements
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Mechanical Engineering Computational Suite.
    </div>
  </footer>

  <script>
    function updateBoltSpecs() {
      runBoltCalc();
    }

    function runBoltCalc() {
      const boltSel = document.getElementById('bolt-standard');
      const opt = boltSel.options[boltSel.selectedIndex];
      const dMm = parseFloat(opt.dataset.d) || 12;
      const asMm2 = parseFloat(opt.dataset.as) || 84.3;

      const gradeSel = document.getElementById('bolt-grade');
      const gradeOpt = gradeSel.options[gradeSel.selectedIndex];
      const proofMpa = parseFloat(gradeOpt.dataset.proof) || 580;

      const K = parseFloat(document.getElementById('lubrication-condition').value) || 0.20;
      const preloadPct = parseFloat(document.getElementById('target-preload-pct').value) || 0.75;

      // Axial Preload Force: F_p = As * proofMpa * preloadPct (in Newtons)
      const preloadN = asMm2 * proofMpa * preloadPct;
      const preloadKn = preloadN / 1000.0;
      const preloadLbf = preloadN * 0.224809;

      // Tightening Torque: T = K * D * F_p
      const dMeters = dMm / 1000.0;
      const torqueNm = K * dMeters * preloadN;
      const torqueLbft = torqueNm * 0.737562;
      const torqueLbin = torqueNm * 8.85075;

      // Tensile Stress
      const tensileStressMpa = proofMpa * preloadPct;

      document.getElementById('res-torque-nm').textContent = torqueNm.toFixed(1) + ' N·m';
      document.getElementById('res-torque-imperial').textContent = torqueLbft.toFixed(1) + ' lbf·ft (' + torqueLbin.toFixed(1) + ' lbf·in)';
      document.getElementById('res-clamp-force').textContent = preloadKn.toFixed(2) + ' kN (' + Math.round(preloadLbf).toLocaleString() + ' lbf)';
      document.getElementById('res-stress-area').textContent = asMm2.toFixed(1) + ' mm²';
      document.getElementById('res-tensile-stress').textContent = tensileStressMpa.toFixed(1) + ' MPa';
      document.getElementById('res-proof-strength').textContent = proofMpa.toFixed(0) + ' MPa';
    }

    window.addEventListener('DOMContentLoaded', runBoltCalc);
  </script>
</body>
</html>
"""

# ==========================================
# 2. BEARING LIFE CALCULATOR
# ==========================================
TOOL_BEARING = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bearing Life Calculator — ISO 281 L10 &amp; L10h Rating Life</title>
  <meta name="description" content="Calculate rolling element bearing rating life in millions of revolutions (L10) and operating service hours (L10h) based on ISO 281 dynamic load rating C and equivalent load P.">
  <meta name="keywords" content="bearing life calculator, l10 bearing life calculator, l10h bearing life, iso 281 bearing calculation, dynamic load rating c, equivalent bearing load p, ball bearing roller bearing life">
  <link rel="canonical" href="https://calchub.org/bearing-life-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "ISO 281 Rolling Bearing Life Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates basic rating life L10 in millions of revolutions and L10h service operating hours for ball and roller bearings per ISO 281."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is bearing L10 rating life?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The basic rating life L10 is the number of revolutions (or operating hours at constant speed) that 90% of a sufficiently large group of identical rolling element bearings will complete or exceed before the first evidence of material rolling contact fatigue (flaking or spalling) develops on either race ring or rolling element."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for calculating bearing rating life under ISO 281?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under ISO 281, basic rating life in millions of revolutions is: L10 = (C / P)^p, where C is the basic dynamic load rating (kN), P is the equivalent dynamic bearing load (kN), and p is the life exponent (p = 3 for ball bearings with point contact, and p = 10/3 ≈ 3.333 for roller bearings with line contact). To convert to service operating hours at constant shaft rotational speed n (RPM): L10h = (10^6 / (60 × n)) × (C / P)^p."
            }
          },
          {
            "@type": "Question",
            "name": "How is equivalent dynamic bearing load (P) calculated from radial and thrust loads?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Combined radial load (Fr) and axial thrust load (Fa) are combined into a single equivalent dynamic radial load using: P = X × Fr + Y × Fa, where X is the radial factor and Y is the thrust factor obtained from bearing manufacturer catalogs based on the axial load ratio Fa / (e × Fr)."
            }
          },
          {
            "@type": "Question",
            "name": "Why do roller bearings have a life exponent of 10/3 while ball bearings have 3?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ball bearings experience elliptical 'point contact' against the inner and outer raceways, where Hertzian contact stress scales with the cube root of the normal load, resulting in an empirical fatigue life exponent of p = 3. Roller bearings (cylindrical, tapered, and spherical) have modified line contact, spreading stress over a rectangular strip, which empirically correlates to a steeper life exponent of p = 10/3 (3.333)."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body class="cat-theme-mechanical">

  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="engineering.html" class="nav-link">⚡ Electrical</a>
          <a href="mechanical.html" class="nav-link active">⚙️ Mechanical</a>
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
      <span class="category-tag">⚙️ Rotating Machinery &amp; Tribology</span>
      <h1 class="calc-page-title">Bearing Life Calculator</h1>
      <p class="calc-page-desc">Calculate ISO 281 basic rating life (L10 in millions of revolutions and L10h in operating hours) for deep groove ball bearings, angular contact bearings, and roller bearings under radial and thrust loads.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>⚙️</span> Bearing Load &amp; Operating Conditions</h2>
            <span class="status-info">ISO 281 / ANSI ABMA</span>
          </div>
          <form id="bearing-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="bearing-type">Bearing Rolling Element Type</label>
                <select id="bearing-type" class="form-control" onchange="runBearingCalc()">
                  <option value="ball" selected>Ball Bearing (Deep Groove / Angular / p = 3.0)</option>
                  <option value="roller">Roller Bearing (Cylindrical / Tapered / Spherical / p = 3.333)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="shaft-rpm">Rotational Speed (RPM)</label>
                <input type="number" id="shaft-rpm" class="form-control" value="1750" min="1" max="100000" step="50" oninput="runBearingCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="dynamic-c">Basic Dynamic Load Rating C (kN)</label>
                <input type="number" id="dynamic-c" class="form-control" value="35.5" min="0.1" max="10000" step="0.5" oninput="runBearingCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="equiv-load-p">Equivalent Dynamic Load P (kN)</label>
                <input type="number" id="equiv-load-p" class="form-control" value="7.2" min="0.05" max="10000" step="0.1" oninput="runBearingCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="reliability-factor">Reliability Requirement (a₁ Factor)</label>
                <select id="reliability-factor" class="form-control" onchange="runBearingCalc()">
                  <option value="1.00" selected>90% Reliability (L10 Baseline / a₁ = 1.00)</option>
                  <option value="0.64">95% Reliability (L5 / a₁ = 0.64)</option>
                  <option value="0.55">96% Reliability (L4 / a₁ = 0.55)</option>
                  <option value="0.47">97% Reliability (L3 / a₁ = 0.47)</option>
                  <option value="0.37">98% Reliability (L2 / a₁ = 0.37)</option>
                  <option value="0.25">99% Reliability (Critical Turbomachinery / a₁ = 0.25)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="daily-hours">Operating Duty Cycle (Hours / Day)</label>
                <input type="number" id="daily-hours" class="form-control" value="16" min="1" max="24" step="1" oninput="runBearingCalc()">
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runBearingCalc()">Calculate Bearing Life</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Fatigue Life Report</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Bearing Reliability &amp; Service Life</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">L10h Rating Life in Service Hours</div>
            <div id="res-l10h" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">1,141 Operating Hours</div>
            <div id="res-years-service" style="font-size:1.05rem;color:#059669;font-weight:700;">≈ 71 Working Days at 16 hrs/day</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">L10 Life in Revolutions</span>
              <span id="res-l10-revs" class="result-val" style="font-size:1.1rem;font-weight:700;color:#2563EB;">119.8 Million Revs</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Dynamic Load Ratio (C / P)</span>
              <span id="res-c-p-ratio" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">4.93</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Contact Life Exponent (p)</span>
              <span id="res-exponent-p" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">3.0 (Ball Contact)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Reliability a₁ Factor</span>
              <span id="res-a1-val" class="result-val" style="font-size:1.1rem;font-weight:700;color:#475569;">1.00 (90%)</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:0.85rem;color:#166534;">
            <strong>⚙️ Machine Design Tip:</strong> For industrial gearboxes and continuous process blowers, target an $L_{10h}$ service life between 20,000 and 40,000 hours by either increasing bearing dynamic rating $C$ or optimizing gear pitch lines with our <a href="gear-ratio-calculator.html" style="color:#166534;font-weight:700;">Gear Ratio Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>Understanding Rolling Contact Fatigue &amp; ISO 281 Rating Life</h2>
        <p>In mechanical powertrain engineering, rolling bearings rarely fail from sudden yield stress or gross material breakage under normal operating parameters. Instead, they operate under cyclic contact stresses ranging from 1,000 to over 3,000 MPa at microscopic Hertzian contact ellipses. Over millions of stress cycles, subsurface shear stresses initiate micro-cracks that gradually propagate to the surface, resulting in catastrophic spalling and flaking of raceway metal. This degradation mechanism is termed <strong>rolling contact fatigue (RCF)</strong>.</p>

        <p>Because rolling contact fatigue is a statistical material phenomenon governed by Weibull distribution statistics, bearing life cannot be expressed as a single deterministic value for every individual unit. Under the international standard <strong>ISO 281</strong> (and ANSI/ABMA Standard 9 &amp; 11), bearing longevity is quantified as the <strong>$L_{10}$ basic rating life</strong>: the service life in millions of revolutions that <strong>90% of a large population</strong> of identical bearings will achieve or exceed before the inception of fatigue spalling.</p>

        <h2>ISO 281 Mathematical Formulation</h2>
        <p>The fundamental ISO 281 equations define bearing life as a power relationship between the manufacturer's catalog dynamic load rating and the applied mechanical operating load:</p>

        <h3>1. Basic Rating Life in Revolutions ($L_{10}$)</h3>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$L_{10} = \left( \frac{C}{P} \right)^p \quad \text{[Millions of Revolutions]}$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$C$</strong> = Basic dynamic load rating in kilonewtons ($\text{kN}$). This represents the constant radial (or axial) load that a bearing can theoretically endure for a basic rating life of exactly $10^6$ revolutions.</li>
          <li><strong>$P$</strong> = Equivalent dynamic bearing load in kilonewtons ($\text{kN}$).</li>
          <li><strong>$p$</strong> = Life exponent based on contact geometry:
            <ul>
              <li>$p = 3$ for ball bearings (elliptical point contact).</li>
              <li>$p = \frac{10}{3} \approx 3.333$ for roller bearings (modified line contact).</li>
            </ul>
          </li>
        </ul>

        <h3>2. Service Rating Life in Operating Hours ($L_{10h}$)</h3>
        <p>To convert millions of revolutions into practical operating hours at a constant rotational speed $n$ (RPM):</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$L_{10h} = \frac{10^6}{60 \cdot n} \cdot \left( \frac{C}{P} \right)^p = \frac{10^6 \cdot L_{10}}{60 \cdot n} \quad \text{[Hours]}$$
        </div>

        <h3>3. Equivalent Dynamic Load Calculation ($P$)</h3>
        <p>When a bearing experiences simultaneous radial force ($F_r$) and axial thrust force ($F_a$), the complex multi-axial stress field is reduced to an equivalent radial load using ISO radial and axial factors ($X$ and $Y$):</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$P = X \cdot F_r + Y \cdot F_a$$
        </div>
        <p>If the axial thrust load is negligible compared to radial load ($\frac{F_a}{F_r} \le e$, where $e$ is the limiting thrust factor), $X = 1$ and $Y = 0$, simplifying to $P = F_r$.</p>

        <h2>Typical Industry Required Design Life Guidelines</h2>
        <p>Different machinery applications demand vastly different minimum $L_{10h}$ service targets based on replacement accessibility, failure severity, and operating schedule:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Application Category</th>
                <th style="padding:0.75rem;">Operating Profile</th>
                <th style="padding:0.75rem;">Recommended Minimum $L_{10h}$</th>
                <th style="padding:0.75rem;">Required Reliability</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Household Appliances &amp; Handheld Power Tools</strong></td>
                <td style="padding:0.75rem;">Intermittent operation (1–2 hrs/day)</td>
                <td style="padding:0.75rem;">1,000 – 3,000 hours</td>
                <td style="padding:0.75rem;">90% ($a_1 = 1.00$)</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Automotive Hub Bearings &amp; Transmissions</strong></td>
                <td style="padding:0.75rem;">Intermittent driving (150,000 km)</td>
                <td style="padding:0.75rem;">3,000 – 5,000 hours</td>
                <td style="padding:0.75rem;">90% – 95%</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Industrial Motors, Blowers &amp; Pumps (8-hr shift)</strong></td>
                <td style="padding:0.75rem;">Regular industrial operation</td>
                <td style="padding:0.75rem;">15,000 – 25,000 hours</td>
                <td style="padding:0.75rem;">90% ($a_1 = 1.00$)</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>24/7 Continuous Process Plants &amp; Paper Mills</strong></td>
                <td style="padding:0.75rem;">Continuous non-stop operation</td>
                <td style="padding:0.75rem;">40,000 – 60,000 hours</td>
                <td style="padding:0.75rem;">95% – 98%</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>Critical Turbomachinery &amp; Mine Hoists</strong></td>
                <td style="padding:0.75rem;">Uninterruptible mission-critical</td>
                <td style="padding:0.75rem;">100,000+ hours</td>
                <td style="padding:0.75rem;">99% ($a_1 = 0.25$)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: Centrifugal Pump Drive
          </h3>
          <p><strong>Scenario:</strong> A chemical process facility installs a centrifugal slurry pump running at $n = 1,450\text{ RPM}$. The drive end uses a 6310 deep groove ball bearing with a basic dynamic rating $C = 62.0\text{ kN}$. Under full impeller hydraulic head, the equivalent dynamic load is $P = 8.5\text{ kN}$. The pump operates $24\text{ hours/day}$ and requires standard $90\%$ reliability ($a_1 = 1.0$).</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Determine the Load Ratio ($C / P$):</strong>
              $$\frac{C}{P} = \frac{62.0\text{ kN}}{8.5\text{ kN}} = 7.294$$
            </li>
            <li><strong>Calculate $L_{10}$ in Millions of Revolutions ($p = 3$ for ball bearing):</strong>
              $$L_{10} = (7.294)^3 = 388.1\text{ Million Revolutions}$$
            </li>
            <li><strong>Calculate $L_{10h}$ Service Life in Operating Hours:</strong>
              $$L_{10h} = \frac{10^6}{60 \cdot 1,450} \cdot 388.1 = \frac{10^6 \times 388.1}{87,000} \approx 4,461\text{ Hours}$$
            </li>
            <li><strong>Calculate Calendar Service Longevity:</strong>
              $$\text{Operating Days} = \frac{4,461\text{ hours}}{24\text{ hrs/day}} \approx 185.9\text{ Days} \approx 6.2\text{ Months}$$
            </li>
            <li><strong>Engineering Recommendation:</strong> A 6-month bearing replacement cycle is unacceptable for a continuous process plant. Upgrading to a spherical roller bearing with $C = 135\text{ kN}$ increases $(C/P)^{3.333} = (135/8.5)^{3.333} \approx 9,980\text{ Mrev}$, yielding $L_{10h} \approx 114,700\text{ hours}$ (over 13 years of maintenance-free continuous operation).</li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is the difference between static load rating (C0) and dynamic load rating (C)?</h4>
            <p style="margin:0;color:#64748B;">The dynamic load rating (C) is used for rotating bearings to calculate fatigue life under cyclic rolling contact stress. The static load rating (C0) applies when bearings rotate at very slow speeds (&lt; 10 RPM), oscillate slowly, or support stationary static shock loads. C0 is the load that produces a permanent plastic indentation of 0.0001 times the rolling element diameter at the most heavily stressed contact zone.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">How does lubrication contamination impact calculated bearing life?</h4>
            <p style="margin:0;color:#64748B;">ISO 281 introduced the modified rating life equation: Lnm = a1 × aISO × L10. The life modification factor aISO incorporates lubrication film thickness (viscosity ratio κ) and contamination factor (eC). If solid debris particles enter the bearing, stress concentrations around indents slash actual fatigue life by up to 80% to 90% compared to basic L10.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Can a bearing be underloaded and fail prematurely?</h4>
            <p style="margin:0;color:#64748B;">Yes! High-speed roller bearings require a minimum operating load (typically 1% to 2% of dynamic rating C). If equivalent load P is too light, the rolling elements fail to roll cleanly along raceways; instead, they slip and skid, generating intense frictional shear heat that strips lubricant and causes catastrophic smearing.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What are the early vibration indicators of bearing race fatigue?</h4>
            <p style="margin:0;color:#64748B;">Bearing fatigue generates distinct characteristic fault frequencies in vibration acceleration spectra: BPFO (Ball Pass Frequency Outer Race), BPFI (Ball Pass Frequency Inner Race), BSF (Ball Spin Frequency), and FTF (Fundamental Train Frequency of the cage). PeakVue and demodulation acceleration enveloping detect micro-impacts months before audible noise occurs.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚙️ Mechanical Machinery Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="bearing-life-calculator.html" style="font-weight:700;color:#2563EB;">⚙️ Bearing Life (ISO 281)</a></li>
          <li><a href="bolt-torque-calculator.html" style="color:#475569;">🔩 Bolt Torque &amp; Preload</a></li>
          <li><a href="torque-calculator.html" style="color:#475569;">🔄 Torque &amp; Shaft Power</a></li>
          <li><a href="gear-ratio-calculator.html" style="color:#475569;">⚙️ Gear Ratio &amp; Speed</a></li>
          <li><a href="pipe-sizing-calculator.html" style="color:#475569;">🚰 Pipe Sizing &amp; Flow</a></li>
          <li><a href="pump-head-calculator.html" style="color:#475569;">🌊 Pump Head (TDH)</a></li>
          <li><a href="cooling-load-calculator.html" style="color:#475569;">❄️ HVAC Cooling Load</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Engineering Design Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="motor-starting-current-calculator.html" style="color:#475569;">⚙️ Motor Starting Current</a></li>
          <li><a href="transformer-sizing-calculator.html" style="color:#475569;">⚡ Transformer Sizing</a></li>
          <li><a href="unit-converter.html" style="color:#475569;">🔄 Universal Unit Converter</a></li>
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
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">Tribology Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          ISO 281 Rolling Bearings — Dynamic Load Ratings<br>
          ANSI/ABMA Standard 9 &amp; 11<br>
          DIN ISO 76 Static Load Ratings
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Tribology &amp; Powertrain Computational Suite.
    </div>
  </footer>

  <script>
    function runBearingCalc() {
      const bType = document.getElementById('bearing-type').value;
      const rpm = Math.max(1, parseFloat(document.getElementById('shaft-rpm').value) || 1750);
      const C = Math.max(0.1, parseFloat(document.getElementById('dynamic-c').value) || 35.5);
      const P = Math.max(0.01, parseFloat(document.getElementById('equiv-load-p').value) || 7.2);
      const a1 = parseFloat(document.getElementById('reliability-factor').value) || 1.00;
      const dailyHours = Math.min(24, Math.max(1, parseFloat(document.getElementById('daily-hours').value) || 16));

      // Exponent: 3 for ball, 10/3 (3.333333) for roller
      const p = bType === 'ball' ? 3.0 : (10.0 / 3.0);

      const cpRatio = C / P;
      const l10RevsM = a1 * Math.pow(cpRatio, p); // in Millions of revs
      const l10hHours = (1e6 / (60 * rpm)) * l10RevsM;
      const workDays = l10hHours / dailyHours;
      const workYears = workDays / 365.25;

      document.getElementById('res-l10h').textContent = Math.round(l10hHours).toLocaleString() + ' Operating Hours';
      if (workDays < 365) {
        document.getElementById('res-years-service').textContent = '\u2248 ' + Math.round(workDays) + ' Working Days at ' + dailyHours + ' hrs/day';
      } else {
        document.getElementById('res-years-service').textContent = '\u2248 ' + workYears.toFixed(1) + ' Years at ' + dailyHours + ' hrs/day (' + Math.round(workDays).toLocaleString() + ' Days)';
      }

      document.getElementById('res-l10-revs').textContent = l10RevsM.toFixed(1) + ' Million Revs';
      document.getElementById('res-c-p-ratio').textContent = cpRatio.toFixed(2);
      document.getElementById('res-exponent-p').textContent = p.toFixed(3) + (bType === 'ball' ? ' (Ball Contact)' : ' (Roller Contact)');
      document.getElementById('res-a1-val').textContent = a1.toFixed(2) + ' (' + (a1 === 1.00 ? '90%' : (a1 === 0.25 ? '99%' : 'Adjusted')) + ')';
    }

    window.addEventListener('DOMContentLoaded', runBearingCalc);
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "bolt-torque-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_BOLT)
print("[PASS] bolt-torque-calculator.html generated successfully!")

with open(os.path.join(BASE_DIR, "bearing-life-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_BEARING)
print("[PASS] bearing-life-calculator.html generated successfully!")
