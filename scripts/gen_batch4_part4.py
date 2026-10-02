"""
Generates fire-pump-sizing-calculator.html and ev-charging-circuit-calculator.html
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
# 1. FIRE PUMP SIZING CALCULATOR
# ==========================================
TOOL_FIRE_PUMP = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fire Pump Sizing Calculator — NFPA 20 Head, GPM &amp; Driver Horsepower</title>
  <meta name="description" content="Calculate stationary fire pump capacity (GPM), total dynamic head (PSI), churn pressure, and electric motor driver brake horsepower (BHP) per NFPA 20 standards.">
  <meta name="keywords" content="fire pump sizing calculator, nfpa 20 fire pump, fire pump horsepower calculator, fire pump head calculation, churn pressure fire pump, fire pump curve 150 percent, centrifugal fire pump sizing">
  <link rel="canonical" href="https://calchub.org/fire-pump-sizing-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "NFPA 20 Stationary Fire Pump Sizing Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates required fire pump flow capacity, net pressure head, motor driver brake horsepower, and NFPA 20 curve compliance points."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What are the three mandatory performance curve test points mandated by NFPA 20?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under NFPA 20 (Standard for the Installation of Stationary Pumps for Fire Protection), a centrifugal fire pump must produce a characteristic head-flow curve meeting three strict criteria: 1) Churn (Shutoff): Zero-flow pressure must not exceed 140% of rated net head; 2) Rated Capacity (100% Flow): Must produce at least 100% of rated pressure head; 3) Peak Overload (150% Flow): Must produce at least 65% of rated net pressure head at 150% of rated volumetric flow capacity."
            }
          },
          {
            "@type": "Question",
            "name": "How is fire pump driver Brake Horsepower (BHP) calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Fire pump driver power is calculated using hydraulic water horsepower divided by mechanical pump efficiency: BHP = (Q × H) / (3960 × η), where Q is pump flow rate in gallons per minute (GPM), H is total dynamic head in feet of water (Head in ft = Net PSI × 2.31), and η is pump hydraulic efficiency (typically 0.70 to 0.82 for split-case centrifugal pumps). Per NFPA 20, electric motors must be sized to handle maximum horsepower at any point along the pump curve without exceeding service factor."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between a horizontal split-case pump and an end-suction fire pump?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Horizontal split-case (HSC) fire pumps are the industry standard for high-flow installations (500 to 5,000+ GPM). The casing divides along the horizontal shaft axis, allowing internal inspection and impeller servicing without disconnecting suction/discharge piping or moving the driver. End-suction pumps are more compact and economical for smaller demands (250 to 750 GPM), but require disconnecting piping or motor during major overhauls."
            }
          },
          {
            "@type": "Question",
            "name": "What is net fire pump pressure head versus discharge pressure?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Net pump head is the actual pressure energy added to the water by the pump impeller alone: P_net = P_discharge - P_suction. If a municipal water main delivers 40 PSI residual suction pressure to the pump inlet flange and the required system demand at the discharge riser is 140 PSI, the fire pump must be rated for a net pressure of: 140 - 40 = 100 PSI."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body class="cat-theme-fire">

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
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
        </div>
        <div class="nav-row">
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="fire-safety.html" class="nav-link active">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>

  <div class="calc-page-header">
    <div class="calc-page-header-inner">
      <span class="category-tag">🚨 Hydraulic Life Safety &amp; NFPA 20</span>
      <h1 class="calc-page-title">Fire Pump Sizing Calculator</h1>
      <p class="calc-page-desc">Calculate stationary fire pump rated flow (GPM), total dynamic head, churn pressure limits, and driver motor horsepower (BHP) per NFPA 20 stationary fire pump standards.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>🚒</span> System Hydraulic Demand Inputs</h2>
            <span class="status-info">NFPA 20 Criteria</span>
          </div>
          <form id="firepump-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="system-demand-gpm">Required Fire Flow Demand (GPM)</label>
                <div style="display:flex;gap:0.5rem;">
                  <input type="number" id="system-demand-gpm" class="form-control" value="1000" min="50" max="10000" step="50" oninput="runFirePumpCalc()">
                  <select id="preset-gpm" class="form-control" style="width:140px;" onchange="applyPumpGpmPreset()">
                    <option value="custom">Standard GPM</option>
                    <option value="500">500 GPM</option>
                    <option value="750">750 GPM</option>
                    <option value="1000" selected>1,000 GPM</option>
                    <option value="1500">1,500 GPM</option>
                    <option value="2000">2,000 GPM</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label class="form-label" for="system-demand-psi">Required System Discharge Pressure (PSI)</label>
                <input type="number" id="system-demand-psi" class="form-control" value="145" min="20" max="400" step="5" oninput="runFirePumpCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="suction-supply-psi">Available City Residual Suction (PSI)</label>
                <input type="number" id="suction-supply-psi" class="form-control" value="45" min="0" max="250" step="5" oninput="runFirePumpCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="pump-efficiency">Estimated Pump Hydraulic Efficiency (%)</label>
                <input type="number" id="pump-efficiency" class="form-control" value="75" min="40" max="95" step="1" oninput="runFirePumpCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="pump-type">Fire Pump Mechanical Construction</label>
                <select id="pump-type" class="form-control" onchange="runFirePumpCalc()">
                  <option value="hsc" selected>Horizontal Split-Case (HSC — Standard Commercial)</option>
                  <option value="end-suction">End-Suction Centrifugal (Compact &lt; 750 GPM)</option>
                  <option value="vertical-turbine">Vertical Turbine (Deep Well / Suction Below Grade)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="driver-type">Primary Driver Selection</label>
                <select id="driver-type" class="form-control" onchange="runFirePumpCalc()">
                  <option value="electric" selected>Electric Motor (NFPA 20 Article 9)</option>
                  <option value="diesel">Diesel Engine (NFPA 20 Article 11 / Listed)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runFirePumpCalc()">Size Fire Pump &amp; Driver</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Submittal Schedule</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Pump Rating &amp; NFPA 20 Performance</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Recommended Driver Motor Rating</div>
            <div id="res-hp-primary" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">100 HP</div>
            <div id="res-bhp-calculated" style="font-size:1.05rem;color:#059669;font-weight:700;">Calculated Brake Horsepower: 77.8 BHP</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Net Pump Pressure Boost Head</span>
              <span id="res-net-head-psi" class="result-val" style="font-size:1.1rem;font-weight:700;color:#2563EB;">100.0 PSI (231.0 ft Head)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Max Churn Pressure (140% Limit)</span>
              <span id="res-churn-pressure" class="result-val" style="font-size:1.1rem;font-weight:700;color:#DC2626;">140.0 PSI Net (&le; 185 PSI Gross)</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">150% Overload Capacity Point</span>
              <span id="res-overload-point" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">1,500 GPM at &ge; 65.0 PSI Net</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Hydraulic Water Horsepower (WHP)</span>
              <span id="res-whp-val" class="result-val" style="font-size:1.1rem;font-weight:700;color:#7C3AED;">58.3 WHP</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#FEF2F2;border:1px solid #FECACA;font-size:0.85rem;color:#991B1B;">
            <strong>🚨 Hydraulic System Design:</strong> Verify sprinkler head demand with our <a href="fire-sprinkler-calculator.html" style="color:#991B1B;font-weight:700;">Fire Sprinkler Hydraulic Calculator</a>, evaluate municipal supply with the <a href="hydrant-fire-flow-calculator.html" style="color:#991B1B;font-weight:700;">Hydrant Fire Flow Calculator</a>, and size standby power with the <a href="fire-alarm-battery-calculator.html" style="color:#991B1B;font-weight:700;">Fire Alarm Battery Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Engineering Behind Stationary Fire Pumps &amp; NFPA 20 Standards</h2>
        <p>In life safety building design, fire sprinkler systems and standpipe risers require dedicated water pressure and volumetric flow to deliver effective fire suppression streams. When municipal water distribution mains cannot guarantee adequate pressure—especially during peak daytime domestic usage or in high-rise buildings where static elevation head robs pressure at $0.433\text{ PSI per foot}$—a stationary fire pump must be installed under the strict legal mandates of <strong>NFPA 20: Standard for the Installation of Stationary Pumps for Fire Protection</strong>.</p>

        <p>Unlike commercial HVAC hydronic pumps designed to run continuously at a single peak-efficiency operating point, a fire pump is an emergency life safety device engineered to deliver massive volumes of water across extreme operating excursions. Centrifugal fire pumps must operate continuously without stalling, cavitating, or tripping overcurrent protective devices, even when supplying flows up to $150\%$ of their nameplate rating.</p>

        <h2>Mathematical Sizing Formulations</h2>

        <h3>1. Net Pump Pressure Head Calculation</h3>
        <p>A fire pump boosts the existing residual pressure supplied by the city water connection or suction reservoir:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$P_{\text{net, PSI}} = P_{\text{system demand, PSI}} - P_{\text{suction residual, PSI}}$$
        </div>
        <p>In hydraulic calculations, pressure in pounds per square inch (PSI) is converted to feet of water head ($H$ in feet) using the specific weight of water ($\gamma = 62.4\text{ lb/ft}^3$, where $1\text{ PSI} = 2.3066\text{ ft}$ of water):</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$H = P_{\text{net, PSI}} \times 2.31 \quad [\text{Feet of Total Dynamic Head}]$$
        </div>

        <h3>2. Hydraulic Water Horsepower (WHP) and Driver Brake Horsepower (BHP)</h3>
        <p>The theoretical power imparted directly into the discharging water stream is the <strong>Water Horsepower (WHP)</strong>:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$\text{WHP} = \frac{Q \times H}{3,960} = \frac{Q \times (P_{\text{net}} \times 2.31)}{3,960} = \frac{Q \times P_{\text{net}}}{1,714}$$
        </div>
        <p>Where $Q$ is volumetric flow rate in gallons per minute (GPM) and $P_{\text{net}}$ is in PSI. Accounting for mechanical impeller friction and hydraulic slip losses ($\eta$, typically $0.70$ to $0.80$ for centrifugal fire pumps), the actual shaft power demanded from the driver is the <strong>Brake Horsepower (BHP)</strong>:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #DC2626;">
          $$\text{BHP} = \frac{\text{WHP}}{\eta} = \frac{Q \times H}{3,960 \times \eta}$$
        </div>

        <h3>3. NFPA 20 Three-Point Characteristic Performance Curve</h3>
        <p>NFPA 20 Section 6.2 mandates that certified fire pumps must satisfy three critical coordinates on their factory certified test curve:</p>
        <ol>
          <li><strong>Churn (Zero Flow / Shutoff):</strong> The net pressure head at zero flow must not exceed $140\%$ of rated net head ($H_{\text{churn}} \le 1.40 \times H_{\text{rated}}$). This prevents excessive over-pressurization from bursting downstream pipe fittings.</li>
          <li><strong>Rated Capacity (100% Flow):</strong> The pump must produce at least $100\%$ of its nameplate rated pressure head ($H_{100\%} \ge 1.00 \times H_{\text{rated}}$) at $100\%$ rated GPM.</li>
          <li><strong>Peak Overload Capacity (150% Flow):</strong> The pump must be capable of discharging $150\%$ of its rated volumetric capacity at a net head of no less than $65\%$ of its rated net head ($H_{150\%} \ge 0.65 \times H_{\text{rated}}$).</li>
        </ol>

        <h2>Standard NFPA 20 Pump Ratings &amp; Motor Horsepower Schedule</h2>
        <p>Standardized commercial fire pump selections based on hydraulic demand:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Rated Capacity (GPM)</th>
                <th style="padding:0.75rem;">Typical Net Pressure (PSI)</th>
                <th style="padding:0.75rem;">Calculated BHP (at 75% η)</th>
                <th style="padding:0.75rem;">Standard Motor Rating (HP)</th>
                <th style="padding:0.75rem;">150% Flow Point</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>500 GPM</strong></td>
                <td style="padding:0.75rem;">80 PSI</td>
                <td style="padding:0.75rem;">31.1 BHP</td>
                <td style="padding:0.75rem;">40 HP</td>
                <td style="padding:0.75rem;">750 GPM at &ge; 52 PSI</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>750 GPM</strong></td>
                <td style="padding:0.75rem;">100 PSI</td>
                <td style="padding:0.75rem;">58.3 BHP</td>
                <td style="padding:0.75rem;">75 HP</td>
                <td style="padding:0.75rem;">1,125 GPM at &ge; 65 PSI</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>1,000 GPM</strong></td>
                <td style="padding:0.75rem;">100 PSI</td>
                <td style="padding:0.75rem;">77.8 BHP</td>
                <td style="padding:0.75rem;">100 HP</td>
                <td style="padding:0.75rem;">1,500 GPM at &ge; 65 PSI</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>1,500 GPM</strong></td>
                <td style="padding:0.75rem;">125 PSI</td>
                <td style="padding:0.75rem;">145.9 BHP</td>
                <td style="padding:0.75rem;">150 HP / 200 HP</td>
                <td style="padding:0.75rem;">2,250 GPM at &ge; 81 PSI</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>2,000 GPM</strong></td>
                <td style="padding:0.75rem;">140 PSI</td>
                <td style="padding:0.75rem;">217.8 BHP</td>
                <td style="padding:0.75rem;">250 HP</td>
                <td style="padding:0.75rem;">3,000 GPM at &ge; 91 PSI</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: High-Bay Warehouse Pump
          </h3>
          <p><strong>Scenario:</strong> A fire protection engineer is designing an automatic wet sprinkler and standpipe system for a logistics warehouse. Hydraulic calculations show the most remote design area requires $Q = 1,000\text{ GPM}$ at $135\text{ PSI}$ residual pressure at the riser. The municipal water main provides $45\text{ PSI}$ residual suction pressure while flowing $1,000\text{ GPM}$.</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Calculate Required Net Pump Pressure ($P_{\text{net}}$):</strong>
              $$P_{\text{net}} = 135\text{ PSI (Demand)} - 45\text{ PSI (City Suction)} = 90.0\text{ PSI}$$
            </li>
            <li><strong>Select Standard Fire Pump Rating:</strong>
              The engineer specifies a listed horizontal split-case pump rated at <strong>1,000 GPM at 95 PSI net head</strong> to provide a $5\text{ PSI}$ design safety cushion.
            </li>
            <li><strong>Convert Net Head to Feet of Water:</strong>
              $$H = 95\text{ PSI} \times 2.31 = 219.45\text{ Feet}$$
            </li>
            <li><strong>Calculate Brake Horsepower (assuming $\eta = 0.74$):</strong>
              $$\text{BHP} = \frac{1,000\text{ GPM} \times 219.45\text{ ft}}{3,960 \times 0.74} = \frac{219,450}{2,930.4} \approx 74.89\text{ BHP}$$
            </li>
            <li><strong>Determine Electric Motor Rating:</strong>
              The next standard NEMA motor frame size above $74.89\text{ BHP}$ is <strong>75 HP</strong>. However, NFPA 20 mandates that the electric motor must not exceed its nameplate rating at the pump's peak horsepower point (which typically occurs at $140\%$ to $150\%$ flow). Because a $1,000\text{ GPM}$ pump flowing at $1,500\text{ GPM}$ demands approximately $88\text{ BHP}$, the engineer specifies a <strong>100 HP electric motor</strong> to ensure non-overloading operation across the entire curve.
            </li>
            <li><strong>Verify NFPA 20 Churn &amp; Overload Points:</strong>
              $$\text{Max Churn Pressure} = 95\text{ PSI} \times 1.40 = 133\text{ PSI Net } (+ 45\text{ city} = 178\text{ PSI Gross})$$
              $$\text{150% Overload Pressure} \ge 95\text{ PSI} \times 0.65 = 61.75\text{ PSI Net at } 1,500\text{ GPM}$$
            </li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is a Jockey Pump (Pressure Maintenance Pump) and how is it sized?</h4>
            <p style="margin:0;color:#64748B;">A jockey pump is a small auxiliary centrifugal pump (typically 1 to 5 GPM, 1/4 to 2 HP) installed in parallel with the main fire pump. Its sole function is to maintain constant supervisory pressure in the sprinkler piping to compensate for minor valve packing drips or thermal temperature fluctuations. Sizing the jockey pump prevents the massive main fire pump from short-cycling on and off for nuisance pressure drops.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why does NFPA 20 require a casing relief valve on electric fire pumps?</h4>
            <p style="margin:0;color:#64748B;">When an electric fire pump runs at churn (zero flow during weekly test churn runs or during initial fire alarm standby), the churning impeller transfers all mechanical shaft energy into the trapped water body as thermal friction heat. Without water movement, the casing water will boil in minutes, destroying mechanical shaft seals and warping impellers. A 3/4-inch or 1-inch automatic casing relief valve bleeds a small continuous stream of cold water to drain, keeping the casing cool.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">When is a main pressure relief valve required on a fire pump?</h4>
            <p style="margin:0;color:#64748B;">Per NFPA 20, a full-size main pressure relief valve (typically 3 to 6 inches) is mandatory on all diesel engine fire pumps because an engine governor failure could cause engine overspeed, generating catastrophic discharge pressures. On electric motor pumps, a main relief valve is required only if the total churn pressure (net churn head + maximum static municipal suction pressure) exceeds the pressure rating of system piping (typically 175 PSI for standard Class 125/150 fittings).</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is Net Positive Suction Head (NPSH) in fire pump installations?</h4>
            <p style="margin:0;color:#64748B;">NPSH is the minimum absolute pressure required at the pump suction eye to prevent water from vaporizing into steam bubbles (cavitation). NFPA 20 strictly regulates suction piping sizing (limiting suction velocity to under 15 ft/sec at 150% flow) to ensure that Net Positive Suction Head Available (NPSHA) exceeds Net Positive Suction Head Required (NPSHR) by at least 5 feet at all operating points.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">🚨 Fire Protection Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="fire-pump-sizing-calculator.html" style="font-weight:700;color:#DC2626;">🚒 Fire Pump Sizing (NFPA 20)</a></li>
          <li><a href="hydrant-fire-flow-calculator.html" style="color:#475569;">🚒 Hydrant Fire Flow (NFPA 291)</a></li>
          <li><a href="fire-alarm-battery-calculator.html" style="color:#475569;">🚨 Fire Alarm Battery (NFPA 72)</a></li>
          <li><a href="smoke-detector-spacing-calculator.html" style="color:#475569;">🚨 Smoke Detector Spacing</a></li>
          <li><a href="fire-sprinkler-calculator.html" style="color:#475569;">💦 Fire Sprinkler Hydraulics</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚙️ Mechanical Hydraulics</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="pump-head-calculator.html" style="color:#475569;">🌊 Pump Head (TDH)</a></li>
          <li><a href="pipe-sizing-calculator.html" style="color:#475569;">🚰 Pipe Sizing &amp; Flow</a></li>
          <li><a href="motor-starting-current-calculator.html" style="color:#475569;">⚙️ Motor Starting Current</a></li>
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
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">NFPA Hydraulic Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          NFPA 20 Installation of Stationary Pumps for Fire Protection<br>
          UL 448 Pumps for Fire-Protection Service<br>
          FM Global Data Sheet 3-7 Fire Pumps
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Fire Protection Hydraulics Suite.
    </div>
  </footer>

  <script>
    function applyPumpGpmPreset() {
      const val = document.getElementById('preset-gpm').value;
      if (val !== 'custom') {
        document.getElementById('system-demand-gpm').value = val;
      }
      runFirePumpCalc();
    }

    // Standard NEMA motor ratings HP
    const NEMA_HP = [15, 20, 25, 30, 40, 50, 60, 75, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500];

    function runFirePumpCalc() {
      const q = Math.max(10, parseFloat(document.getElementById('system-demand-gpm').value) || 1000);
      const pDemand = Math.max(10, parseFloat(document.getElementById('system-demand-psi').value) || 145);
      const pSuction = Math.max(0, parseFloat(document.getElementById('suction-supply-psi').value) || 45);
      const effPct = Math.min(95, Math.max(40, parseFloat(document.getElementById('pump-efficiency').value) || 75));
      const eff = effPct / 100.0;

      const pNetPsi = Math.max(10, pDemand - pSuction);
      const headFeet = pNetPsi * 2.30665;

      // WHP = (Q * HeadFt) / 3960 = (Q * P_net) / 1714
      const whp = (q * headFeet) / 3960.0;
      const bhp = whp / eff;

      // Peak BHP at 150% flow point (typically ~1.15 to 1.25 of rated BHP)
      const peakBhp = bhp * 1.18;

      // Select NEMA motor frame
      let recHp = NEMA_HP[NEMA_HP.length - 1];
      for (let i = 0; i < NEMA_HP.length; i++) {
        if (NEMA_HP[i] >= peakBhp) {
          recHp = NEMA_HP[i];
          break;
        }
      }

      const churnNetPsi = pNetPsi * 1.40;
      const churnGrossPsi = churnNetPsi + pSuction;
      const overloadQ = q * 1.50;
      const overloadNetPsi = pNetPsi * 0.65;

      document.getElementById('res-hp-primary').textContent = recHp + ' HP Motor';
      document.getElementById('res-bhp-calculated').textContent = 'Calculated Brake Horsepower: ' + bhp.toFixed(1) + ' BHP (Peak: ' + peakBhp.toFixed(1) + ' BHP)';
      document.getElementById('res-net-head-psi').textContent = pNetPsi.toFixed(1) + ' PSI Net (' + headFeet.toFixed(1) + ' ft Head)';
      document.getElementById('res-churn-pressure').textContent = churnNetPsi.toFixed(1) + ' PSI Net (\u2264 ' + churnGrossPsi.toFixed(1) + ' PSI Gross)';
      document.getElementById('res-overload-point').textContent = Math.round(overloadQ).toLocaleString() + ' GPM at \u2265 ' + overloadNetPsi.toFixed(1) + ' PSI Net';
      document.getElementById('res-whp-val').textContent = whp.toFixed(1) + ' WHP';
    }

    window.addEventListener('DOMContentLoaded', runFirePumpCalc);
  </script>
</body>
</html>
"""

# ==========================================
# 2. EV CHARGING CIRCUIT CALCULATOR
# ==========================================
TOOL_EV_CIRCUIT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EV Charging Circuit Calculator — NEC 625 Breaker &amp; Wire Sizing (125% Rule)</title>
  <meta name="description" content="Calculate EV charging branch circuit breaker size, copper wire gauge (AWG), charging power in kW, and miles of range added per hour per NEC Article 625.">
  <meta name="keywords" content="ev charging circuit calculator, nec 625 breaker sizing, ev wire size calculator, 125 percent continuous load ev, level 2 ev circuit, 48 amp ev charger breaker, ev charging range per hour">
  <link rel="canonical" href="https://calchub.org/ev-charging-circuit-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "NEC 625 EV Charging Circuit Sizing Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates branch circuit breaker ratings, conductor gauge, charging power in kW, and hourly range addition for electric vehicle supply equipment per NEC 625."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Why does NEC Article 625 mandate the 125% continuous load rule for EV chargers?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under National Electrical Code (NEC) Article 625.41 and Article 210.20(A), electric vehicle supply equipment (EVSE) is classified as a 'continuous load' because charging sessions routinely draw full maximum current for 3 hours or longer. Circuit breakers and conductors generate steady I²R thermal heating. To prevent thermal nuisance tripping and avoid degrading conductor insulation, the branch circuit overcurrent protection device (breaker) and conductors must be sized for at least 125% of the continuous charging load current."
            }
          },
          {
            "@type": "Question",
            "name": "What circuit breaker and wire size are required for a 48-Amp Level 2 EV charger?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A 48-Amp continuous EV charger requires a minimum breaker rating of: 48A × 1.25 = 60 Amperes. Under NEC 310.16 (75°C terminal rating for copper conductors), a 60A circuit requires minimum #6 AWG THHN copper wire or #4 AWG aluminum wire. If using nonmetallic sheathed cable (Romex / NM-B), it is restricted to the 60°C column (55A ampacity), requiring an upgrade to #4 AWG NM-B copper."
            }
          },
          {
            "@type": "Question",
            "name": "What is the charging speed difference between Level 1, Level 2, and DC Fast Charging?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Level 1 operates on standard 120V household outlets (12A continuous = 1.44 kW), providing approximately 3 to 5 miles of range per hour. Level 2 operates on 240V split-phase circuits (16A to 48A = 3.8 kW to 11.5 kW), providing 15 to 45 miles of range per hour, fully replenishing a depleted battery overnight in 6 to 9 hours. DC Fast Charging (Level 3) operates on 400V to 800V three-phase commercial feeds (50 kW to 350 kW), adding 150 to 250+ miles in 15 to 30 minutes."
            }
          },
          {
            "@type": "Question",
            "name": "Why is hardwiring recommended over a NEMA 14-50 receptacle for high-power Level 2 charging?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard consumer-grade NEMA 14-50 outlets are limited to 40A continuous charging (on a 50A breaker) and are prone to thermal degradation and melting under sustained multi-hour 40A heating cycles. Hardwiring allows full 48A continuous charging on a 60A breaker (delivering 11.5 kW vs 9.6 kW), eliminates plug contact resistance, and exempts the installation from requiring a costly GFCI breaker (which often nuisance-trips against the EVSE's internal GFCI test circuit per NEC 625.54)."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body class="cat-theme-solar">

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
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
        </div>
        <div class="nav-row">
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="solar-energy.html" class="nav-link active">☀️ Solar</a>
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
      <span class="category-tag">☀️ Electric Vehicle Infrastructure &amp; NEC 625</span>
      <h1 class="calc-page-title">EV Charging Circuit Calculator</h1>
      <p class="calc-page-desc">Calculate required overcurrent breaker rating (125% rule), copper conductor gauge (AWG), charging power in kW, and range recovery rate per NEC Article 625.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>🔌</span> EVSE Charger &amp; Electrical Supply</h2>
            <span class="status-info">NEC 625.41 Continuous Rule</span>
          </div>
          <form id="evcircuit-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="evse-rating-preset">Popular EV Charger Configurations</label>
                <select id="evse-rating-preset" class="form-control" onchange="applyEvsePreset()">
                  <option value="48-240" selected>48A @ 240V (Hardwired Wall Connector / 11.5 kW)</option>
                  <option value="40-240">40A @ 240V (NEMA 14-50 Plug-In Station / 9.6 kW)</option>
                  <option value="32-240">32A @ 240V (Standard Level 2 Mobile Cable / 7.7 kW)</option>
                  <option value="16-240">16A @ 240V (Low-Power Level 2 / 3.8 kW)</option>
                  <option value="12-120">12A @ 120V (Standard Level 1 Convenience / 1.4 kW)</option>
                  <option value="80-240">80A @ 240V (High-Power Dual Inverter / 19.2 kW)</option>
                  <option value="custom">Custom Load Specification</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="continuous-amps">EVSE Continuous Current ($I_{\text{load}}$ in Amps)</label>
                <input type="number" id="continuous-amps" class="form-control" value="48" min="1" max="200" step="1" oninput="runEvCircuitCalc()">
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="circuit-voltage">Circuit Nominal AC Voltage</label>
                <select id="circuit-voltage" class="form-control" onchange="runEvCircuitCalc()">
                  <option value="240" selected>240 V (US Residential Split-Phase)</option>
                  <option value="208">208 V (US Commercial 3-Phase 2-Leg)</option>
                  <option value="120">120 V (Level 1 Household Standard)</option>
                  <option value="230">230 V (European Single-Phase)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="wire-type">Conductor Insulation &amp; Wiring Method</label>
                <select id="wire-type" class="form-control" onchange="runEvCircuitCalc()">
                  <option value="thhn-conduit" selected>THHN Copper in Conduit (75°C / 90°C Terminal)</option>
                  <option value="romex-nmb">Romex NM-B Cable (Limited to 60°C NEC 334.80)</option>
                  <option value="aluminum-ser">Aluminum SER Cable (75°C Terminal)</option>
                </select>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="run-length-ft">One-Way Circuit Run Distance (Feet)</label>
                <input type="number" id="run-length-ft" class="form-control" value="50" min="5" max="500" step="5" oninput="runEvCircuitCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="ev-efficiency">Vehicle Efficiency (miles / kWh)</label>
                <input type="number" id="ev-efficiency" class="form-control" value="3.5" min="1.0" max="6.0" step="0.1" oninput="runEvCircuitCalc()">
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runEvCircuitCalc()">Size EV Branch Circuit</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Electrical Permit Plan</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Circuit Sizing &amp; Charging Performance</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Required Dedicated Circuit Breaker</div>
            <div id="res-breaker-primary" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">60 Amp Breaker</div>
            <div id="res-wire-gauge" style="font-size:1.05rem;color:#059669;font-weight:700;">Conductor: #6 AWG Copper THHN (75°C Rated)</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Delivered Charging Power</span>
              <span id="res-charging-power" class="result-val" style="font-size:1.1rem;font-weight:700;color:#2563EB;">11.52 kW</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Range Added Per Hour</span>
              <span id="res-range-hourly" class="result-val" style="font-size:1.1rem;font-weight:700;color:#059669;">+ 40.3 Miles / Hour</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Continuous Current Sizing (125%)</span>
              <span id="res-continuous-125" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">60.00 Amperes</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">One-Way Voltage Drop (50 ft)</span>
              <span id="res-circuit-vdrop" class="result-val" style="font-size:1.1rem;font-weight:700;color:#7C3AED;">1.18% (2.83 V Drop — NEC &le; 3%)</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:0.85rem;color:#166534;">
            <strong>🔌 Complete EV Infrastructure:</strong> Check feeder run capacity with our <a href="voltage-drop-calculator.html" style="color:#166534;font-weight:700;">Voltage Drop Calculator</a>, verify conduit fill with the <a href="conduit-fill-calculator.html" style="color:#166534;font-weight:700;">Conduit Fill Calculator</a>, and calculate full vehicle charge time with the <a href="ev-charging-time-calculator.html" style="color:#166534;font-weight:700;">EV Charging Time Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The National Electrical Code (NEC Article 625) &amp; EV Charging Safety</h2>
        <p>Electric Vehicle Supply Equipment (EVSE) represents one of the largest continuous electrical loads installed in modern residential homes and commercial parking facilities. Unlike intermittent household appliances (such as a microwave that runs for 3 minutes or a toaster that runs for 90 seconds), an electric vehicle will continuously draw maximum nameplate amperage from the circuit breaker panel for 6 to 10 consecutive hours every night.</p>

        <p>Because electrical conductors and circuit breaker thermal bimetallic trip mechanisms generate continuous resistive heat ($P = I^2 R$), operating at $100\%$ capacity for multiple hours causes cumulative thermal expansion, terminal screw loosening, insulation degradation, and catastrophic panel fires. For this reason, <strong>NEC Article 625.41 (Overcurrent Protection)</strong> and <strong>NEC Article 210.20(A)</strong> explicitly mandate that EV charging circuits must be treated as <strong>continuous loads</strong>, requiring overcurrent protection and branch conductors to be sized at no less than <strong>$125\%$ of the continuous load current</strong>.</p>

        <h2>Mathematical Sizing Formulations</h2>

        <h3>1. The 125% Overcurrent Protection Rule</h3>
        <p>The minimum required circuit breaker ampacity ($I_{\text{breaker}}$) is calculated using the standard continuous load multiplier:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$I_{\text{breaker, min}} = I_{\text{continuous}} \times 1.25$$
        </div>
        <p>If the calculated value does not correspond to a standard commercial circuit breaker rating, the designer must select the next higher standard rating specified in <strong>NEC Article 240.6(A)</strong> (15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100 Amps).</p>

        <h3>2. Delivered Electric Vehicle Charging Power ($P_{\text{charging}}$)</h3>
        <p>Delivered electrical power transferred to the vehicle's onboard charger in kilowatts (kW) is:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$P_{\text{charging}} = \frac{V_{\text{circuit}} \times I_{\text{continuous}}}{1,000} \quad [\text{kW}]$$
        </div>

        <h3>3. Estimated Range Recovery Rate (Miles per Hour)</h3>
        <p>The vehicle range added per hour of continuous charging ($\text{RPH}$) is modeled using vehicle drivetrain efficiency ($\mu_{\text{efficiency}}$, typically $3.0$ to $4.0\text{ miles/kWh}$ for sedans and $2.0$ to $2.5\text{ miles/kWh}$ for electric trucks) and charging conversion efficiency ($\eta \approx 90\%$):</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #7C3AED;">
          $$\text{RPH} = P_{\text{charging}} \times \mu_{\text{efficiency}} \times \eta \quad [\text{Miles of Range / Hour}]$$
        </div>

        <h2>Standard EVSE Circuit Sizing, Breaker &amp; Conductor Gauge Table</h2>
        <p>Sizing matrix for standard commercial and residential Level 2 EVSE installations:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Continuous Charging Current</th>
                <th style="padding:0.75rem;">Minimum Breaker Size (125%)</th>
                <th style="padding:0.75rem;">Copper THHN in Conduit (75°C)</th>
                <th style="padding:0.75rem;">Romex NM-B Cable (60°C Limit)</th>
                <th style="padding:0.75rem;">Power at 240V</th>
                <th style="padding:0.75rem;">Typical Range Added</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>16 Amperes</strong></td>
                <td style="padding:0.75rem;">20 Amp</td>
                <td style="padding:0.75rem;">#12 AWG Cu</td>
                <td style="padding:0.75rem;">#12 AWG Cu</td>
                <td style="padding:0.75rem;">3.84 kW</td>
                <td style="padding:0.75rem;">12 – 15 miles/hr</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>24 Amperes</strong></td>
                <td style="padding:0.75rem;">30 Amp</td>
                <td style="padding:0.75rem;">#10 AWG Cu</td>
                <td style="padding:0.75rem;">#10 AWG Cu</td>
                <td style="padding:0.75rem;">5.76 kW</td>
                <td style="padding:0.75rem;">18 – 22 miles/hr</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>32 Amperes</strong></td>
                <td style="padding:0.75rem;">40 Amp</td>
                <td style="padding:0.75rem;">#8 AWG Cu</td>
                <td style="padding:0.75rem;">#8 AWG Cu</td>
                <td style="padding:0.75rem;">7.68 kW</td>
                <td style="padding:0.75rem;">25 – 30 miles/hr</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>40 Amperes</strong></td>
                <td style="padding:0.75rem;">50 Amp</td>
                <td style="padding:0.75rem;">#8 AWG Cu</td>
                <td style="padding:0.75rem;">#6 AWG Cu</td>
                <td style="padding:0.75rem;">9.60 kW</td>
                <td style="padding:0.75rem;">30 – 35 miles/hr</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>48 Amperes</strong></td>
                <td style="padding:0.75rem;">60 Amp</td>
                <td style="padding:0.75rem;">#6 AWG Cu</td>
                <td style="padding:0.75rem;">#4 AWG Cu</td>
                <td style="padding:0.75rem;">11.52 kW</td>
                <td style="padding:0.75rem;">38 – 45 miles/hr</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>80 Amperes</strong></td>
                <td style="padding:0.75rem;">100 Amp</td>
                <td style="padding:0.75rem;">#3 AWG Cu</td>
                <td style="padding:0.75rem;">#1 AWG Cu</td>
                <td style="padding:0.75rem;">19.20 kW</td>
                <td style="padding:0.75rem;">60 – 75 miles/hr</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: Residential 48A Wall Connector
          </h3>
          <p><strong>Scenario:</strong> A homeowner purchases a Tesla Universal Wall Connector capable of charging at $48\text{A}$ on a $240\text{V}$ split-phase supply. The main electrical service panel is located $65\text{ feet}$ away in the basement. The installer runs conductors inside EMT conduit to the garage wall.</p>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Apply the NEC 125% Continuous Rule:</strong>
              $$I_{\text{breaker}} = 48\text{ A} \times 1.25 = 60.0\text{ Amperes}$$
              The electrician specifies a dedicated two-pole <strong>60 Amp circuit breaker</strong>.
            </li>
            <li><strong>Select Conductor Gauge per NEC 310.16:</strong>
              Under the $75^\circ\text{C}$ terminal column, #6 AWG copper conductor has an allowable ampacity of $65\text{ Amperes}$, which exceeds the $60\text{A}$ breaker rating. The installer pulls two insulated #6 AWG THHN copper phase conductors (black and red) and one bare #10 AWG copper equipment grounding conductor (EGC) through $3/4\text{-inch}$ EMT conduit.
            </li>
            <li><strong>Check Voltage Drop at 65 Feet:</strong>
              Using copper conductor resistance ($R \approx 0.491\text{ }\Omega / 1,000\text{ ft}$ for #6 AWG):
              $$R_{\text{loop}} = 2 \times 65\text{ ft} \times \frac{0.491}{1,000} \approx 0.0638\text{ }\Omega$$
              $$\Delta V = I \times R_{\text{loop}} = 48\text{ A} \times 0.0638\text{ }\Omega \approx 3.06\text{ Volts}$$
              $$\% \Delta V = \frac{3.06\text{ V}}{240\text{ V}} \times 100\% \approx 1.28\%$$
              This is well below the NEC recommended maximum feeder voltage drop limit of $3.0\%$.
            </li>
            <li><strong>Calculate Delivered Charging Power &amp; Hourly Range:</strong>
              $$P = \frac{240\text{ V} \times 48\text{ A}}{1,000} = 11.52\text{ kW}$$
              At $3.5\text{ miles/kWh}$ vehicle efficiency:
              $$\text{Range Added} = 11.52\text{ kW} \times 3.5\text{ mi/kWh} \approx 40.3\text{ Miles per Hour of Charging}$$
            </li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why is Romex (NM-B) wire restricted to a lower ampacity than THHN in conduit?</h4>
            <p style="margin:0;color:#64748B;">Per NEC Article 334.80, nonmetallic sheathed cable (Romex / NM-B) must be sized using the 60°C thermal column of Table 310.16 regardless of conductor insulation rating because Romex bundles conductors tightly inside a PVC jacket surrounded by building thermal insulation. For example, #6 AWG Romex is rated for only 55A at 60°C (insufficient for a 60A breaker!), whereas #6 AWG THHN in conduit is rated for 65A at 75°C.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Does NEC 625 require GFCI protection for EV charger branch circuits?</h4>
            <p style="margin:0;color:#64748B;">Under NEC 2020/2023 Article 625.54, all EVSE receptacles (such as NEMA 14-50 and 6-50 outlets) require Class A 5mA GFCI breaker protection in the panel. However, virtually all modern EV chargers incorporate internal CCID (Charge Circuit Interrupting Device) ground-fault protection. Dual GFCI devices in series often nuisance trip. Hardwiring the charger directly exempts the circuit from NEC 625.54 GFCI breaker requirements, saving $120+ and preventing nuisance shutdowns.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Can a 200-Amp residential electrical service handle an EV charger installation?</h4>
            <p style="margin:0;color:#64748B;">Most modern 200A panels can accommodate a 40A or 48A Level 2 charger unless the home has massive existing electrical loads (all-electric heat pump, electric tankless water heater, hot tub, and electric range). An electrician must perform an NEC Article 220 Service Load Calculation. If calculated demand exceeds 160A (80% of 200A), the installer can install an automatic EV Energy Management System (EMS / load-shedding device) to avoid a costly $3,000+ utility service upgrade.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is the difference between charging on 208V commercial vs 240V residential?</h4>
            <p style="margin:0;color:#64748B;">Commercial buildings and apartment complexes supply three-phase 208Y/120V power, giving a line-to-line voltage of 208V instead of residential 240V split-phase. At 48 Amps, charging on 208V delivers 208V × 48A = 9.98 kW, which is approximately 13.4% slower than 240V (which delivers 11.52 kW). The car charges normally, but range addition per hour is slightly reduced.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">☀️ Solar &amp; EV Infrastructure</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="ev-charging-circuit-calculator.html" style="font-weight:700;color:#059669;">🔌 EV Charging Circuit (NEC 625)</a></li>
          <li><a href="ev-charging-time-calculator.html" style="color:#475569;">🔌 EV Charging Time &amp; Power</a></li>
          <li><a href="pv-string-sizing-calculator.html" style="color:#475569;">☀️ PV String Sizing</a></li>
          <li><a href="solar-panel-sizing-calculator.html" style="color:#475569;">☀️ Solar Panel Sizing</a></li>
          <li><a href="solar-battery-bank-calculator.html" style="color:#475569;">🔋 Solar Battery Bank Sizing</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Electrical Wiring Suite</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="wire-ampacity-calculator.html" style="color:#475569;">🔌 Wire Ampacity (NEC)</a></li>
          <li><a href="conduit-fill-calculator.html" style="color:#475569;">🪢 Conduit Fill Calculator</a></li>
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
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">EV Electrical Codes</div>
        <div style="font-size:0.85rem;line-height:2;">
          NFPA 70 NEC Article 625 Electric Vehicle Power Transfer<br>
          UL 2594 Standard for EVSE Safety<br>
          SAE J1772 Electric Vehicle Conductive Charge Coupler
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional EV Infrastructure &amp; Electrical Sizing Suite.
    </div>
  </footer>

  <script>
    function applyEvsePreset() {
      const val = document.getElementById('evse-rating-preset').value;
      if (val !== 'custom') {
        const parts = val.split('-');
        document.getElementById('continuous-amps').value = parts[0];
        document.getElementById('circuit-voltage').value = parts[1];
      }
      runEvCircuitCalc();
    }

    // Standard NEC 240.6 breaker sizes
    const STANDARD_BREAKERS = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125];

    function runEvCircuitCalc() {
      const iLoad = Math.max(1, parseFloat(document.getElementById('continuous-amps').value) || 48);
      const vCircuit = parseFloat(document.getElementById('circuit-voltage').value) || 240;
      const wireMethod = document.getElementById('wire-type').value;
      const distFt = Math.max(1, parseFloat(document.getElementById('run-length-ft').value) || 50);
      const effMilesKwh = Math.max(0.5, parseFloat(document.getElementById('ev-efficiency').value) || 3.5);

      // Continuous load 125% rule
      const iMinBreaker = iLoad * 1.25;

      let recBreaker = STANDARD_BREAKERS[STANDARD_BREAKERS.length - 1];
      for (let i = 0; i < STANDARD_BREAKERS.length; i++) {
        if (STANDARD_BREAKERS[i] >= iMinBreaker) {
          recBreaker = STANDARD_BREAKERS[i];
          break;
        }
      }

      // Conductor sizing
      let gaugeStr = '';
      let rOhmsPer1000 = 0.491; // default #6 AWG Cu

      if (wireMethod === 'thhn-conduit') {
        // 75C column
        if (recBreaker <= 15) { gaugeStr = '#14 AWG Copper THHN (15A max)'; rOhmsPer1000 = 3.07; }
        else if (recBreaker <= 20) { gaugeStr = '#12 AWG Copper THHN (20A)'; rOhmsPer1000 = 1.93; }
        else if (recBreaker <= 30) { gaugeStr = '#10 AWG Copper THHN (30A)'; rOhmsPer1000 = 1.21; }
        else if (recBreaker <= 50) { gaugeStr = '#8 AWG Copper THHN (50A)'; rOhmsPer1000 = 0.764; }
        else if (recBreaker <= 65) { gaugeStr = '#6 AWG Copper THHN (65A)'; rOhmsPer1000 = 0.491; }
        else if (recBreaker <= 85) { gaugeStr = '#4 AWG Copper THHN (85A)'; rOhmsPer1000 = 0.308; }
        else if (recBreaker <= 100) { gaugeStr = '#3 AWG Copper THHN (100A)'; rOhmsPer1000 = 0.245; }
        else { gaugeStr = '#2 AWG Copper THHN (115A)'; rOhmsPer1000 = 0.194; }
      } else if (wireMethod === 'romex-nmb') {
        // 60C column limit per NEC 334.80
        if (recBreaker <= 15) { gaugeStr = '#14 AWG Romex NM-B (15A max)'; rOhmsPer1000 = 3.07; }
        else if (recBreaker <= 20) { gaugeStr = '#12 AWG Romex NM-B (20A)'; rOhmsPer1000 = 1.93; }
        else if (recBreaker <= 30) { gaugeStr = '#10 AWG Romex NM-B (30A)'; rOhmsPer1000 = 1.21; }
        else if (recBreaker <= 40) { gaugeStr = '#8 AWG Romex NM-B (40A)'; rOhmsPer1000 = 0.764; }
        else if (recBreaker <= 55) { gaugeStr = '#6 AWG Romex NM-B (55A)'; rOhmsPer1000 = 0.491; }
        else if (recBreaker <= 70) { gaugeStr = '#4 AWG Romex NM-B (70A)'; rOhmsPer1000 = 0.308; }
        else { gaugeStr = '#2 AWG Romex NM-B (95A)'; rOhmsPer1000 = 0.194; }
      } else {
        // Aluminum SER 75C
        if (recBreaker <= 40) { gaugeStr = '#6 AWG Aluminum SER (40A)'; rOhmsPer1000 = 0.808; }
        else if (recBreaker <= 50) { gaugeStr = '#4 AWG Aluminum SER (50A)'; rOhmsPer1000 = 0.508; }
        else if (recBreaker <= 65) { gaugeStr = '#3 AWG Aluminum SER (65A)'; rOhmsPer1000 = 0.403; }
        else if (recBreaker <= 75) { gaugeStr = '#2 AWG Aluminum SER (75A)'; rOhmsPer1000 = 0.319; }
        else if (recBreaker <= 90) { gaugeStr = '#1 AWG Aluminum SER (90A)'; rOhmsPer1000 = 0.253; }
        else { gaugeStr = '#1/0 AWG Aluminum SER (100A)'; rOhmsPer1000 = 0.201; }
      }

      // Charging power kW
      const kwPower = (vCircuit * iLoad) / 1000.0;
      const hourlyMiles = kwPower * effMilesKwh * 0.90; // ~90% charger efficiency

      // Voltage drop: 2 * L * R * I / 1000
      const loopR = (2 * distFt * rOhmsPer1000) / 1000.0;
      const vDrop = iLoad * loopR;
      const vDropPct = (vDrop / vCircuit) * 100.0;

      document.getElementById('res-breaker-primary').textContent = recBreaker + ' Amp Breaker';
      document.getElementById('res-wire-gauge').textContent = 'Conductor: ' + gaugeStr;
      document.getElementById('res-charging-power').textContent = kwPower.toFixed(2) + ' kW';
      document.getElementById('res-range-hourly').textContent = '+ ' + hourlyMiles.toFixed(1) + ' Miles / Hour';
      document.getElementById('res-continuous-125').textContent = iMinBreaker.toFixed(2) + ' Amperes';
      document.getElementById('res-circuit-vdrop').textContent = vDropPct.toFixed(2) + '% (' + vDrop.toFixed(2) + ' V Drop \u2014 ' + (vDropPct <= 3.0 ? 'NEC Compliant \u2264 3%' : 'Exceeds 3% Rec') + ')';
    }

    window.addEventListener('DOMContentLoaded', runEvCircuitCalc);
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "fire-pump-sizing-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_FIRE_PUMP)
print("[PASS] fire-pump-sizing-calculator.html generated successfully!")

with open(os.path.join(BASE_DIR, "ev-charging-circuit-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_EV_CIRCUIT)
print("[PASS] ev-charging-circuit-calculator.html generated successfully!")
