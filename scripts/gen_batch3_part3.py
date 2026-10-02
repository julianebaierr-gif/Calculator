"""
Generates fire-alarm-battery-calculator.html and hydrant-fire-flow-calculator.html
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
# 1. FIRE ALARM BATTERY CALCULATOR
# ==========================================
TOOL_FA_BATTERY = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fire Alarm Battery Calculator — NFPA 72 Standby &amp; Alarm Ah Sizing</title>
  <meta name="description" content="Calculate required secondary battery backup capacity (Ampere-hours Ah) for fire alarm control panels per NFPA 72 standards with 24-hour standby and 1.20 safety factor.">
  <meta name="keywords" content="fire alarm battery calculator, nfpa 72 battery calculation, fire alarm battery sizing, standby alarm current ah, fire panel battery calculation, secondary power supply nfpa 72, 24 hour standby battery">
  <link rel="canonical" href="https://calchub.org/fire-alarm-battery-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "NFPA 72 Fire Alarm Secondary Battery Sizing Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates required secondary power supply sealed lead-acid (SLA) battery storage capacity in Ampere-hours per NFPA 72 Chapter 10 requirements."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What are the NFPA 72 battery standby and alarm duration requirements?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Per NFPA 72 (National Fire Alarm and Signaling Code), standard protected premises fire alarm systems require secondary battery storage capable of operating the system under quiescent non-alarm standby load for at least 24 hours, followed by at least 5 minutes of full evacuation notification alarm load at maximum rated output. For emergency voice/alarm communication systems (EVACS) or high-rise mass notification systems, the alarm evacuation duration requirement increases to 15 minutes."
            }
          },
          {
            "@type": "Question",
            "name": "Why does NFPA 72 mandate a 1.20 (20%) battery aging de-rating safety factor?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "NFPA 72 Section 10.6.7.2 mandates a minimum 20% safety factor (multiplier of 1.20) because rechargeable sealed lead-acid (SLA/VRLA) batteries suffer irreversible chemical degradation, sulfation, and internal resistance increases over time. Battery manufacturers define end-of-life as the point when capacity drops to 80% of rated nameplate capacity. The 1.20 multiplier guarantees that even when an aged battery reaches 80% capacity at year 3 or 4, it can still reliably satisfy the full 24-hour standby plus evacuation alarm requirement."
            }
          },
          {
            "@type": "Question",
            "name": "What is the formula for calculating fire alarm battery Ampere-hours?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The required minimum battery capacity is: C_min = 1.20 × [ (I_standby × T_standby) + (I_alarm × T_alarm) ], where I_standby is quiescent supervisor current in Amperes, T_standby is standby duration in hours (typically 24.0 or 60.0 hours), I_alarm is peak total alarm current in Amperes, and T_alarm is evacuation duration in hours (5 minutes = 0.0833 hours, or 15 minutes = 0.250 hours)."
            }
          },
          {
            "@type": "Question",
            "name": "How does temperature affect fire alarm sealed lead-acid battery capacity?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Standard SLA batteries are rated at an optimal ambient temperature of 25°C (77°F). At freezing temperatures (0°C / 32°F), available electrochemical capacity drops by approximately 15% to 20%, requiring larger batteries or climate-controlled enclosures. Conversely, operating in unconditioned boiler rooms above 35°C (95°F) accelerates grid corrosion and halves battery operational lifespan."
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
      <span class="category-tag">🚨 Life Safety Systems &amp; NFPA 72</span>
      <h1 class="calc-page-title">Fire Alarm Battery Calculator</h1>
      <p class="calc-page-desc">Calculate required secondary standby battery capacity (Ampere-hours Ah) for Fire Alarm Control Panels (FACP) and Notification Appliance Circuit (NAC) power supplies per NFPA 72 Chapter 10.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>🚨</span> Panel Supervisory &amp; Alarm Loads</h2>
            <span class="status-info">NFPA 72 Table 10.6.7.2</span>
          </div>
          <form id="fa-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="standby-current">Quiescent Standby Current (Amps)</label>
                <input type="number" id="standby-current" class="form-control" value="0.450" min="0.01" max="50.0" step="0.005" oninput="runFaCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="standby-hours">Standby Duration (Hours)</label>
                <select id="standby-hours" class="form-control" onchange="runFaCalc()">
                  <option value="24" selected>24 Hours (NFPA 72 Standard Premises)</option>
                  <option value="48">48 Hours (Remote Supervised Station)</option>
                  <option value="60">60 Hours (Central Station / High Reliability)</option>
                  <option value="4">4 Hours (Emergency Generator Equipped)</option>
                </select>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="alarm-current">Full Notification Alarm Current (Amps)</label>
                <input type="number" id="alarm-current" class="form-control" value="3.850" min="0.1" max="100.0" step="0.05" oninput="runFaCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="alarm-minutes">Evacuation Alarm Duration (Minutes)</label>
                <select id="alarm-minutes" class="form-control" onchange="runFaCalc()">
                  <option value="5" selected>5 Minutes (Standard Horn/Strobe Notification)</option>
                  <option value="15">15 Minutes (Emergency Voice Evacuation - EVACS)</option>
                  <option value="30">30 Minutes (Special Industrial / High Occupancy)</option>
                </select>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="safety-factor">NFPA 72 Battery De-Rating Factor</label>
                <select id="safety-factor" class="form-control" onchange="runFaCalc()">
                  <option value="1.20" selected>1.20 (NFPA 72 Mandatory 20% Aging Reserve)</option>
                  <option value="1.25">1.25 (Cold Temperature Environment / Enhanced Margin)</option>
                  <option value="1.00">1.00 (Unadjusted Theoretical Minimum)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="battery-voltage">System Nominal DC Voltage</label>
                <select id="battery-voltage" class="form-control" onchange="runFaCalc()">
                  <option value="24" selected>24V DC (Two 12V SLA Batteries in Series)</option>
                  <option value="12">12V DC (Single 12V SLA Battery)</option>
                </select>
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runFaCalc()">Calculate Battery Capacity</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print NFPA 72 Submittal</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Secondary Power Sizing Summary</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Minimum Required Battery Capacity</div>
            <div id="res-min-ah" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">13.34 Ah</div>
            <div id="res-rec-battery" style="font-size:1.05rem;color:#DC2626;font-weight:700;">Standard Recommendation: 18 Ah (Two 12V 18Ah SLA in Series)</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Standby Ah Load (24h)</span>
              <span id="res-standby-ah" class="result-val" style="font-size:1.1rem;font-weight:700;color:#2563EB;">10.80 Ah</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Alarm Ah Load</span>
              <span id="res-alarm-ah" class="result-val" style="font-size:1.1rem;font-weight:700;color:#DC2626;">0.32 Ah</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Raw Calculated Capacity</span>
              <span id="res-raw-ah" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">11.12 Ah</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">20% Aging Safety Margin</span>
              <span id="res-margin-ah" class="result-val" style="font-size:1.1rem;font-weight:700;color:#059669;">+ 2.22 Ah</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#FEF2F2;border:1px solid #FECACA;font-size:0.85rem;color:#991B1B;">
            <strong>🚨 Notification Circuit Design:</strong> Check strobe candela spacing with our <a href="smoke-detector-spacing-calculator.html" style="color:#991B1B;font-weight:700;">Smoke Detector Spacing Calculator</a> and verify water supply hydraulically with the <a href="fire-sprinkler-calculator.html" style="color:#991B1B;font-weight:700;">Fire Sprinkler Hydraulic Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>NFPA 72 Secondary Power Supply Compliance Mandates</h2>
        <p>In life safety building engineering, fire detection and alarm systems are fundamentally categorized as life safety systems that must remain fully operational when municipal AC utility mains power is severed—a common occurrence during building fires, structural collapses, and severe electrical storms. Under <strong>NFPA 72 (National Fire Alarm and Signaling Code) Section 10.6.7</strong>, all protected premises fire alarm systems are required to feature a reliable secondary (standby) power supply, almost universally implemented via dedicated valve-regulated sealed lead-acid (VRLA/SLA) rechargeable batteries housed inside the Fire Alarm Control Panel (FACP) or external battery cabinets.</p>

        <p>A compliant secondary power calculation must account for two completely distinct operating modes: <strong>quiescent supervisory standby</strong> (continuous baseline current drawn by microprocessors, smoke detector loops, addressable polling modules, and LED indicators) and <strong>alarm notification</strong> (heavy instantaneous current drawn by horn/strobes, chime-strobes, voice evacuation amplifiers, and door holder releases).</p>

        <h2>The Governing NFPA 72 Calculation Formula</h2>
        <p>The total Ampere-hour ($C$) battery requirement is computed using the standard algebraic summation defined in fire protection engineering submittals:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #DC2626;">
          $$C_{\text{required}} = 1.20 \cdot \left[ \left( I_{\text{standby}} \cdot T_{\text{standby}} \right) + \left( I_{\text{alarm}} \cdot \frac{T_{\text{alarm, min}}}{60} \right) \right]$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$I_{\text{standby}}$</strong> = Total supervisory standby current drawn by all connected modules and initiating circuits in Amperes ($A$).</li>
          <li><strong>$T_{\text{standby}}$</strong> = Mandated standby operational duration in hours ($24.0\text{ hours}$ for standard facilities; $60.0\text{ hours}$ for central stations).</li>
          <li><strong>$I_{\text{alarm}}$</strong> = Peak total alarm current drawn during active evacuation notification in Amperes ($A$).</li>
          <li><strong>$T_{\text{alarm, min}}$</strong> = Required evacuation duration in minutes ($5\text{ minutes} = \frac{5}{60} = 0.0833\text{ hrs}$; or $15\text{ minutes} = 0.250\text{ hrs}$ for voice systems).</li>
          <li><strong>$1.20$</strong> = Mandatory $20\%$ battery aging safety factor per NFPA 72 Section 10.6.7.2.</li>
        </ul>

        <h2>Standard Commercial SLA Battery Sizes &amp; Enclosure Fit</h2>
        <p>Engineers cannot specify fractional battery ratings (such as $13.34\text{ Ah}$). Instead, you must specify the next larger standard commercial battery size. Standard 12V SLA battery capacities and dimensions include:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">Nominal Ah Rating (at 20-hr rate)</th>
                <th style="padding:0.75rem;">Standard Voltage</th>
                <th style="padding:0.75rem;">Typical Enclosure Location</th>
                <th style="padding:0.75rem;">Terminal Type</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>7.0 Ah – 8.0 Ah</strong></td>
                <td style="padding:0.75rem;">12V (2x for 24V)</td>
                <td style="padding:0.75rem;">Internal to standard FACP cabinet bottom</td>
                <td style="padding:0.75rem;">F1 / F2 Faston tab</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>12.0 Ah</strong></td>
                <td style="padding:0.75rem;">12V (2x for 24V)</td>
                <td style="padding:0.75rem;">Internal to large FACP cabinets</td>
                <td style="padding:0.75rem;">F2 Faston tab</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>18.0 Ah</strong></td>
                <td style="padding:0.75rem;">12V (2x for 24V)</td>
                <td style="padding:0.75rem;">Internal large cabinets or external BB-17 box</td>
                <td style="padding:0.75rem;">M5 / M6 threaded nut &amp; bolt</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>26.0 Ah – 33.0 Ah</strong></td>
                <td style="padding:0.75rem;">12V (2x for 24V)</td>
                <td style="padding:0.75rem;">Dedicated external locked red battery cabinet</td>
                <td style="padding:0.75rem;">M6 threaded terminal post</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>55.0 Ah</strong></td>
                <td style="padding:0.75rem;">12V (2x for 24V)</td>
                <td style="padding:0.75rem;">Heavy-duty floor-mounted battery rack / enclosure</td>
                <td style="padding:0.75rem;">M8 insert threaded post</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: High-Rise Voice System
          </h3>
          <p><strong>Scenario:</strong> A life safety engineer is designing an addressable Emergency Voice/Alarm Communication System (EVACS) for an 8-story commercial office building. The panel equipment schedule shows:</p>
          <ul>
            <li>Quiescent supervisory standby current: $I_{\text{standby}} = 0.620\text{ A}$</li>
            <li>Standby requirement: $24\text{ hours}$</li>
            <li>Active alarm evacuation current (audio amplifiers + strobes): $I_{\text{alarm}} = 6.450\text{ A}$</li>
            <li>Voice alarm evacuation duration: $15\text{ minutes}$ per NFPA 72</li>
          </ul>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Calculate Standby Capacity Load:</strong>
              $$\text{Standby Ah} = 0.620\text{ A} \times 24.0\text{ hrs} = 14.88\text{ Ah}$$
            </li>
            <li><strong>Convert Alarm Minutes to Hours:</strong>
              $$T_{\text{alarm}} = \frac{15\text{ min}}{60\text{ min/hr}} = 0.250\text{ hrs}$$
            </li>
            <li><strong>Calculate Alarm Capacity Load:</strong>
              $$\text{Alarm Ah} = 6.450\text{ A} \times 0.250\text{ hrs} = 1.6125\text{ Ah}$$
            </li>
            <li><strong>Sum Raw Required Ah:</strong>
              $$\text{Raw Total} = 14.88 + 1.6125 = 16.4925\text{ Ah}$$
            </li>
            <li><strong>Apply Mandatory 1.20 NFPA 72 Aging Factor:</strong>
              $$C_{\text{min}} = 1.20 \times 16.4925\text{ Ah} = 19.791\text{ Ah}$$
            </li>
            <li><strong>Commercial Battery Selection:</strong> Because $19.79\text{ Ah}$ exceeds standard $18\text{ Ah}$ batteries, the engineer must specify a pair of <strong>12V 26 Ah (or 33 Ah)</strong> batteries housed in an external red battery cabinet.</li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">When is a 60-hour standby battery capacity mandatory instead of 24 hours?</h4>
            <p style="margin:0;color:#64748B;">Under NFPA 72, a 60-hour secondary supply is required for systems that do not transmit supervisory signals to a constantly attended location (such as a 24/7 central monitoring station or proprietary supervising station) or where local facilities remain unattended over long holiday weekends without automatic trouble reporting.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Can a dedicated emergency backup diesel generator replace fire alarm batteries?</h4>
            <p style="margin:0;color:#64748B;">No, but it can reduce the battery standby duration requirement. When an NFPA 110 Type 10, Class 24 Level 1 emergency standby generator is installed with automatic transfer switch (ATS), NFPA 72 allows reducing the battery standby requirement from 24 hours down to 4 hours, which covers the interval during generator startup or transient maintenance refueling.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">How frequently must sealed lead-acid fire alarm batteries be replaced?</h4>
            <p style="margin:0;color:#64748B;">NFPA 72 Chapter 14 mandates that SLA batteries must undergo annual load voltage testing and be replaced no later than 3 to 5 years from their manufacturing date code, or whenever an impedance/conductance test reveals capacity below 80% of rating.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why do fire alarm control panels use 24V DC rather than 12V DC?</h4>
            <p style="margin:0;color:#64748B;">Doubling the system voltage from 12V to 24V halves the required circuit current for equivalent wattage, which reduces conductor I²R voltage drop across long notification appliance circuits (NACs) by 75%. This allows fire alarm horns and strobes to operate reliably at wire run distances exceeding 500 to 1,000 feet.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">🚨 Fire Protection Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="fire-alarm-battery-calculator.html" style="font-weight:700;color:#DC2626;">🚨 Fire Alarm Battery (NFPA 72)</a></li>
          <li><a href="hydrant-fire-flow-calculator.html" style="color:#475569;">🚒 Hydrant Fire Flow (NFPA 291)</a></li>
          <li><a href="smoke-detector-spacing-calculator.html" style="color:#475569;">🚨 Smoke Detector Spacing</a></li>
          <li><a href="fire-sprinkler-calculator.html" style="color:#475569;">💦 Fire Sprinkler Hydraulics</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Electrical Engineering Suite</h3>
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
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">NFPA Life Safety Codes</div>
        <div style="font-size:0.85rem;line-height:2;">
          NFPA 72 National Fire Alarm &amp; Signaling Code<br>
          NFPA 101 Life Safety Code<br>
          UL 864 Control Units &amp; Accessories
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Fire &amp; Life Safety Engineering Suite.
    </div>
  </footer>

  <script>
    function runFaCalc() {
      const iStandby = Math.max(0.001, parseFloat(document.getElementById('standby-current').value) || 0.450);
      const tStandby = parseFloat(document.getElementById('standby-hours').value) || 24;
      const iAlarm = Math.max(0.01, parseFloat(document.getElementById('alarm-current').value) || 3.850);
      const tAlarmMin = parseFloat(document.getElementById('alarm-minutes').value) || 5;
      const safetyFactor = parseFloat(document.getElementById('safety-factor').value) || 1.20;
      const vSys = document.getElementById('battery-voltage').value;

      const standbyAh = iStandby * tStandby;
      const alarmAh = iAlarm * (tAlarmMin / 60.0);
      const rawAh = standbyAh + alarmAh;
      const totalMinAh = rawAh * safetyFactor;
      const marginAh = totalMinAh - rawAh;

      let recAh = 7;
      if (totalMinAh <= 7.0) recAh = 7.0;
      else if (totalMinAh <= 8.0) recAh = 8.0;
      else if (totalMinAh <= 12.0) recAh = 12.0;
      else if (totalMinAh <= 18.0) recAh = 18.0;
      else if (totalMinAh <= 26.0) recAh = 26.0;
      else if (totalMinAh <= 33.0) recAh = 33.0;
      else if (totalMinAh <= 55.0) recAh = 55.0;
      else recAh = Math.ceil(totalMinAh / 10) * 10;

      const battConfig = vSys === '24' ? 'Two 12V ' + recAh + 'Ah SLA in Series' : 'Single 12V ' + recAh + 'Ah SLA';

      document.getElementById('res-min-ah').textContent = totalMinAh.toFixed(2) + ' Ah';
      document.getElementById('res-rec-battery').textContent = 'Commercial Selection: ' + recAh + ' Ah (' + battConfig + ')';
      document.getElementById('res-standby-ah').textContent = standbyAh.toFixed(2) + ' Ah (' + tStandby + 'h)';
      document.getElementById('res-alarm-ah').textContent = alarmAh.toFixed(3) + ' Ah (' + tAlarmMin + 'm)';
      document.getElementById('res-raw-ah').textContent = rawAh.toFixed(2) + ' Ah';
      document.getElementById('res-margin-ah').textContent = '+ ' + marginAh.toFixed(2) + ' Ah (' + Math.round((safetyFactor - 1)*100) + '%)';
    }

    window.addEventListener('DOMContentLoaded', runFaCalc);
  </script>
</body>
</html>
"""

# ==========================================
# 2. HYDRANT FIRE FLOW CALCULATOR
# ==========================================
TOOL_HYDRANT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hydrant Fire Flow Calculator — NFPA 291 Pitot Flow &amp; Rated 20 PSI Capacity</title>
  <meta name="description" content="Calculate fire hydrant water discharge flow (GPM) using pitot tube pressure and determine rated available fire flow at 20 psi residual pressure per NFPA 291 color coding standards.">
  <meta name="keywords" content="hydrant fire flow calculator, nfpa 291 fire flow, pitot fire flow calculator, rated flow at 20 psi, fire hydrant gpm calculation, coefficient of discharge cd, hydrant color code nfpa">
  <link rel="canonical" href="https://calchub.org/hydrant-fire-flow-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "NFPA 291 Fire Hydrant Flow & Rating Calculator",
        "operatingSystem": "All",
        "applicationCategory": "EngineeringApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates Pitot discharge flow, rated available fire flow at 20 psi residual pressure, and NFPA 291 color classification."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "How is fire hydrant discharge flow calculated from pitot tube pressure?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Hydrant discharge flow rate is calculated per NFPA 291 using the orifice equation: Q = 29.83 × c_d × d² × √P, where Q is discharge flow in gallons per minute (GPM), c_d is the dimensionless coefficient of discharge (0.90 for smooth rounded outlets, 0.80 for square outlets, 0.70 for projecting inside), d is the internal diameter of the hydrant butt in inches, and P is the velocity Pitot pressure measured at the center of the water stream in pounds per square inch (PSI)."
            }
          },
          {
            "@type": "Question",
            "name": "What is the NFPA 291 formula for rated fire flow at 20 PSI residual pressure?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The available flow at 20 psi residual pressure is determined using the Hazen-Williams pressure extrapolation formula: Q_R = Q_F × [ (P_S - 20) / (P_S - P_R) ]^0.54, where Q_R is rated fire flow at 20 psi (GPM), Q_F is actual total flow measured during the flow test (GPM), P_S is the static pressure before opening hydrants (PSI), and P_R is residual pressure measured at the test gauge while flowing (PSI)."
            }
          },
          {
            "@type": "Question",
            "name": "What are the NFPA 291 hydrant bonnet color code classifications?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "NFPA 291 establishes four standardized color classifications based on rated flow at 20 psi: Class AA (Light Blue): 1,500 GPM or greater; Class A (Green): 1,000 to 1,499 GPM; Class B (Orange): 500 to 999 GPM; Class C (Red): Less than 500 GPM. This enables fire attack crews to instantly gauge water supply capacity upon arrival."
            }
          },
          {
            "@type": "Question",
            "name": "Why is 20 PSI universally considered the minimum residual pressure in municipal water mains?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Water utilities and fire departments enforce 20 psi residual pressure to prevent cavitation in fire department pumper suction impellers and, crucially, to maintain positive pressure against groundwater infiltration. If pressure drops below 20 psi (or approaches negative pressure), contaminated groundwater can siphon through pipe joints into the municipal drinking water supply (back-siphonage)."
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
      <span class="category-tag">🚒 Water Supply Hydraulics &amp; NFPA 291</span>
      <h1 class="calc-page-title">Hydrant Fire Flow Calculator</h1>
      <p class="calc-page-desc">Calculate actual discharge flow from fire hydrant nozzles using pitot pressure and extrapolate available fire flow at 20 psi residual pressure per NFPA 291 flow testing standards.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>🚒</span> Hydrant Flow Test Field Data</h2>
            <span class="status-info">NFPA 291 Standards</span>
          </div>
          <form id="hydrant-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="nozzle-diam">Flowing Nozzle Diameter</label>
                <select id="nozzle-diam" class="form-control" onchange="runHydrantCalc()">
                  <option value="2.5" selected>2.5 Inch (Standard Hose Butt / 2.50")</option>
                  <option value="4.5">4.5 Inch (Pumper Steamer Nozzle / 4.50")</option>
                  <option value="4.0">4.0 Inch (Storz Connection / 4.00")</option>
                  <option value="5.0">5.0 Inch (Large Pumper Outlet / 5.00")</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="discharge-coeff">Outlet Nozzle Discharge Coeff ($c_d$)</label>
                <select id="discharge-coeff" class="form-control" onchange="runHydrantCalc()">
                  <option value="0.90" selected>0.90 — Smooth, Well-Rounded Outlet</option>
                  <option value="0.80">0.80 — Square, Sharp-Edged Outlet</option>
                  <option value="0.70">0.70 — Projecting Inwards (Rough Barrel)</option>
                </select>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="pitot-pressure">Flowing Pitot Gauge Pressure (PSI)</label>
                <input type="number" id="pitot-pressure" class="form-control" value="28" min="1" max="150" step="1" oninput="runHydrantCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="num-outlets">Number of Outlets Flowing</label>
                <select id="num-outlets" class="form-control" onchange="runHydrantCalc()">
                  <option value="1" selected>1 Nozzle Flowing</option>
                  <option value="2">2 Nozzles Flowing Simultaneously</option>
                  <option value="3">3 Nozzles Flowing Simultaneously</option>
                </select>
              </div>
            </div>

            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="static-pressure">Static Pressure at Test Hydrant (PSI)</label>
                <input type="number" id="static-pressure" class="form-control" value="65" min="25" max="250" step="1" oninput="runHydrantCalc()">
              </div>
              <div class="form-group">
                <label class="form-label" for="residual-pressure">Residual Pressure at Test Hydrant (PSI)</label>
                <input type="number" id="residual-pressure" class="form-control" value="48" min="21" max="249" step="1" oninput="runHydrantCalc()">
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runHydrantCalc()">Calculate Fire Flow &amp; Rating</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Flow Test Certificate</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Hydrant Rating &amp; Capacity Classification</h2>
          
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Rated Fire Flow at 20 PSI Residual</div>
            <div id="res-rated-flow" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#0F172A;margin:0.25rem 0;">1,478 GPM</div>
            <div id="res-color-class" style="font-size:1.1rem;color:#16A34A;font-weight:700;">🟢 Class A (Green Bonnet) — 1,000 to 1,499 GPM</div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Actual Flow During Test (Qf)</span>
              <span id="res-test-flow" class="result-val" style="font-size:1.1rem;font-weight:700;color:#2563EB;">887 GPM</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Flow Rate in Liters / Min</span>
              <span id="res-test-lpm" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">3,358 LPM</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Test Pressure Drop (Ps - Pr)</span>
              <span id="res-press-drop" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">17 PSI Drop</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Hazen-Williams Exponent Factor</span>
              <span id="res-hw-factor" class="result-val" style="font-size:1.1rem;font-weight:700;color:#7C3AED;">1.666</span>
            </div>
          </div>

          <div style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:0.85rem;color:#166534;">
            <strong>💦 Water Supply Analysis:</strong> Verify that available water flow meets building fire demand with our <a href="fire-sprinkler-calculator.html" style="color:#166534;font-weight:700;">Fire Sprinkler Hydraulic Calculator</a> and size distribution mains with our <a href="pipe-sizing-calculator.html" style="color:#166534;font-weight:700;">Pipe Sizing Calculator</a>.
          </div>
        </section>
      </div>

      <article class="educational-content" style="margin-top:3rem;line-height:1.7;color:#334155;">
        <h2>The Science of Fire Hydrant Testing &amp; Water Supply Evaluation</h2>
        <p>Municipal water distribution grids must provide sufficient volume and pressure for both domestic consumption and emergency structural fire suppression. Evaluating a water main's fire-fighting capacity requires a dual-hydrant field test conducted under the standardized protocols of <strong>NFPA 291: Recommended Practice for Water Flow Testing and Marking of Hydrants</strong> and the <strong>American Water Works Association (AWWA M17)</strong> manual.</p>

        <p>A standardized test utilizes at least two adjacent hydrants: a <strong>Test Hydrant</strong> (where static pressure $P_s$ and residual pressure $P_r$ are measured using an unflowing pressure cap) and one or more <strong>Flow Hydrants</strong> located downstream (where nozzles are opened and stream velocity is measured using a handheld Pitot tube gauge).</p>

        <h2>NFPA 291 Mathematical Formulation</h2>

        <h3>1. Pitot Discharge Flow Rate ($Q_F$)</h3>
        <p>The flow velocity of water discharging from a hydrant butt is converted to volumetric discharge using Torricelli's orifice velocity law, adjusted for empirical units:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #2563EB;">
          $$Q = 29.83 \cdot c_d \cdot d^2 \cdot \sqrt{P}$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$Q$</strong> = Discharging flow rate in gallons per minute (GPM).</li>
          <li><strong>$c_d$</strong> = Dimensionless coefficient of discharge based on internal nozzle butt geometry (typically $0.90$ for modern hydrants with smooth rounded transitions).</li>
          <li><strong>$d$</strong> = Measured inside diameter of the flowing nozzle outlet in inches (e.g., $2.50\text{ in}$ or $4.50\text{ in}$).</li>
          <li><strong>$P$</strong> = Pitot velocity pressure measured in the center of the discharging stream in pounds per square inch (PSI).</li>
        </ul>

        <h3>2. Rated Fire Flow at 20 PSI Residual ($Q_R$)</h3>
        <p>Because opening hydrants causes a pressure drop in the distribution network due to pipe friction, municipal fire flow capacity is universally standardized to the flow available at a minimum residual pressure of <strong>20 PSI</strong>. This is extrapolated using the Hazen-Williams friction loss relationship:</p>
        <div class="formula-box" style="background:#F1F5F9;padding:1.25rem;border-radius:8px;margin:1.5rem 0;font-family:monospace;border-left:4px solid #059669;">
          $$Q_R = Q_F \cdot \left( \frac{P_S - 20}{P_S - P_R} \right)^{0.54}$$
        </div>
        <p>Where:</p>
        <ul>
          <li><strong>$Q_R$</strong> = Rated available fire flow at $20\text{ PSI}$ residual pressure (GPM).</li>
          <li><strong>$Q_F$</strong> = Total actual flow measured across all discharging outlets during the field test (GPM).</li>
          <li><strong>$P_S$</strong> = Static pressure recorded at the test hydrant with no hydrants flowing (PSI).</li>
          <li><strong>$P_R$</strong> = Residual pressure recorded at the test hydrant with all test hydrants flowing (PSI).</li>
          <li><strong>$0.54$</strong> = Empirical exponent derived from the Hazen-Williams friction loss formula ($h_f \propto Q^{1.852}$, where $\frac{1}{1.852} \approx 0.54$).</li>
        </ul>

        <h2>NFPA 291 Hydrant Color Coding Classification</h2>
        <p>To assist responding fire company commanders in making split-second tactical decisions regarding apparatus positioning and hose line deployments, NFPA 291 establishes a standardized color code for hydrant bonnets and nozzle caps:</p>

        <div class="table-responsive" style="overflow-x:auto;margin:1.5rem 0;">
          <table class="table-custom" style="width:100%;border-collapse:collapse;border:1px solid #E2E8F0;">
            <thead style="background:#F8FAFC;">
              <tr style="border-bottom:2px solid #CBD5E1;text-align:left;">
                <th style="padding:0.75rem;">NFPA Class</th>
                <th style="padding:0.75rem;">Bonnet &amp; Cap Color</th>
                <th style="padding:0.75rem;">Rated Capacity (at 20 PSI)</th>
                <th style="padding:0.75rem;">Fireground Tactical Capability</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Class AA</strong></td>
                <td style="padding:0.75rem;"><span style="color:#0284C7;font-weight:700;">🔵 Light Blue</span></td>
                <td style="padding:0.75rem;">1,500 GPM or greater</td>
                <td style="padding:0.75rem;">Can supply master streams, multiple pumpers, and large commercial fires.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;background:#F8FAFC;">
                <td style="padding:0.75rem;"><strong>Class A</strong></td>
                <td style="padding:0.75rem;"><span style="color:#16A34A;font-weight:700;">🟢 Green</span></td>
                <td style="padding:0.75rem;">1,000 – 1,499 GPM</td>
                <td style="padding:0.75rem;">Standard commercial and residential structural fire attack supply.</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:0.75rem;"><strong>Class B</strong></td>
                <td style="padding:0.75rem;"><span style="color:#EA580C;font-weight:700;">🟠 Orange</span></td>
                <td style="padding:0.75rem;">500 – 999 GPM</td>
                <td style="padding:0.75rem;">Single pumper supply; moderate residential occupancy protection.</td>
              </tr>
              <tr>
                <td style="padding:0.75rem;"><strong>Class C</strong></td>
                <td style="padding:0.75rem;"><span style="color:#DC2626;font-weight:700;">🔴 Red</span></td>
                <td style="padding:0.75rem;">Less than 500 GPM</td>
                <td style="padding:0.75rem;">Deficient water supply; risk of pulling pumper into cavitation or pulling vacuum.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="worked-example-card" style="background:#F8FAFC;border:2px solid #E2E8F0;border-radius:12px;padding:1.5rem;margin:2rem 0;">
          <h3 style="margin-top:0;color:#0F172A;display:flex;align-items:center;gap:0.5rem;">
            <span>📋</span> Real-World Engineering Worked Example: Warehouse Fire Flow Test
          </h3>
          <p><strong>Scenario:</strong> A fire protection engineer conducts a flow test for a proposed warehouse sprinkler system connection. Field gauge observations:</p>
          <ul>
            <li>Static pressure before flow: $P_S = 72\text{ PSI}$</li>
            <li>Residual pressure while flowing: $P_R = 54\text{ PSI}$</li>
            <li>Flow hydrant outlet: One $2.5\text{ inch}$ butt with rounded inlet ($c_d = 0.90$)</li>
            <li>Measured pitot velocity pressure: $P = 32\text{ PSI}$</li>
          </ul>

          <ol style="padding-left:1.25rem;line-height:1.8;">
            <li><strong>Calculate Test Discharge Flow ($Q_F$):</strong>
              $$Q_F = 29.83 \times 0.90 \times (2.5)^2 \times \sqrt{32} = 29.83 \times 0.90 \times 6.25 \times 5.6569 \approx 949\text{ GPM}$$
            </li>
            <li><strong>Calculate Pressure Terms:</strong>
              $$P_S - 20 = 72 - 20 = 52\text{ PSI}$$
              $$P_S - P_R = 72 - 54 = 18\text{ PSI}$$
            </li>
            <li><strong>Compute Extrapolation Ratio:</strong>
              $$\left( \frac{52}{18} \right)^{0.54} = (2.8889)^{0.54} \approx 1.767$$
            </li>
            <li><strong>Calculate Rated Fire Flow at 20 PSI ($Q_R$):</strong>
              $$Q_R = 949\text{ GPM} \times 1.767 \approx 1,677\text{ GPM}$$
            </li>
            <li><strong>NFPA 291 Classification:</strong> Since $Q_R = 1,677\text{ GPM} \ge 1,500\text{ GPM}$, the hydrant is classified as <strong>Class AA</strong> and painted with a <strong>Light Blue</strong> bonnet.</li>
          </ol>
        </div>

        <h2>Frequently Asked Technical Questions</h2>
        <div class="faq-accordion" style="margin-top:1.5rem;">
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">How far should the Pitot blade tip be held from the hydrant orifice?</h4>
            <p style="margin:0;color:#64748B;">Per NFPA 291 Section 4.3.2, the opening of the Pitot tube orifice should be held exactly in the center of the discharging stream, at a distance of one-half the nozzle diameter (approximately 1.25 inches for a 2.5-inch nozzle) away from the face of the outlet butt.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">What is the minimum pressure drop required for an accurate flow test?</h4>
            <p style="margin:0;color:#64748B;">NFPA 291 recommends inducing a residual pressure drop of at least 25% of static pressure (or at least 10 to 15 PSI drop). If the pressure drop is too small (&lt; 5 PSI), minor gauge reading errors become magnified exponentially when extrapolated down to 20 PSI, producing inaccurate capacity ratings.</p>
          </div>
          <div class="faq-item" style="border-bottom:1px solid #E2E8F0;padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Can multiple nozzles or multiple hydrants be flowed at once?</h4>
            <p style="margin:0;color:#64748B;">Yes. In strong municipal grids with large mains (12-inch or larger), opening a single 2.5-inch nozzle may not produce an adequate pressure drop. In such cases, test crews open the 4.5-inch pumper steamer nozzle or flow two hydrants simultaneously. The test flow Q_F is simply the mathematical sum of the individual nozzle discharges.</p>
          </div>
          <div class="faq-item" style="padding:1rem 0;">
            <h4 style="margin:0 0 0.5rem 0;color:#0F172A;font-size:1.05rem;">Why is a diffuser used during hydrant flow tests?</h4>
            <p style="margin:0;color:#64748B;">Unrestricted water discharge at 1,000+ GPM has tremendous kinetic energy capable of tearing up asphalt, washing out landscaping, and propelling dangerous gravel projectiles. Hose monsters and stream diffusers disperse the high-velocity jet into an aerated spray while incorporating built-in Pitot gauges for accurate measurement.</p>
          </div>
        </div>
      </article>
    </main>

    <aside class="sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;margin-bottom:1.5rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">🚒 Water &amp; Fire Safety Tools</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="hydrant-fire-flow-calculator.html" style="font-weight:700;color:#DC2626;">🚒 Hydrant Fire Flow (NFPA 291)</a></li>
          <li><a href="fire-alarm-battery-calculator.html" style="color:#475569;">🚨 Fire Alarm Battery (NFPA 72)</a></li>
          <li><a href="fire-sprinkler-calculator.html" style="color:#475569;">💦 Fire Sprinkler Hydraulics</a></li>
          <li><a href="pipe-sizing-calculator.html" style="color:#475569;">🚰 Pipe Sizing &amp; Flow</a></li>
          <li><a href="pump-head-calculator.html" style="color:#475569;">🌊 Pump Head (TDH)</a></li>
        </ul>
      </div>

      <div class="sidebar-card" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <h3 style="font-size:1rem;margin-top:0;color:#0F172A;">⚡ Civil &amp; Fluid Engineering</h3>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.88rem;line-height:2;">
          <li><a href="chlorine-dosing-calculator.html" style="color:#475569;">💧 Chlorine Dosing Calculator</a></li>
          <li><a href="chemical-dosing-calculator.html" style="color:#475569;">🧪 Chemical Dosing Rate</a></li>
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
        <div style="font-weight:700;color:#FFFFFF;margin-bottom:0.75rem;">Hydraulic Testing Standards</div>
        <div style="font-size:0.85rem;line-height:2;">
          NFPA 291 Fire Flow Testing &amp; Marking<br>
          AWWA M17 Installation, Field Testing &amp; Maintenance<br>
          NFPA 13 Installation of Sprinkler Systems
        </div>
      </div>
    </div>
    <div style="max-width:1200px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid #1E293B;text-align:center;font-size:0.82rem;">
      &copy; 2026 CalcHub. Professional Municipal &amp; Fire Hydraulics Suite.
    </div>
  </footer>

  <script>
    function runHydrantCalc() {
      const d = parseFloat(document.getElementById('nozzle-diam').value) || 2.5;
      const cd = parseFloat(document.getElementById('discharge-coeff').value) || 0.90;
      const pitotP = Math.max(1, parseFloat(document.getElementById('pitot-pressure').value) || 28);
      const numOutlets = parseInt(document.getElementById('num-outlets').value) || 1;
      const ps = Math.max(25, parseFloat(document.getElementById('static-pressure').value) || 65);
      const pr = Math.max(21, Math.min(ps - 1, parseFloat(document.getElementById('residual-pressure').value) || 48));

      // Single outlet flow: Q = 29.83 * cd * d^2 * sqrt(P)
      const qSingle = 29.83 * cd * (d * d) * Math.sqrt(pitotP);
      const qTotalFlow = qSingle * numOutlets;
      const qTotalLpm = qTotalFlow * 3.78541;

      // Pressure drop
      const deltaP = ps - pr;
      const targetDeltaP = ps - 20;

      // Hazen-Williams rating: Q_R = Q_F * ( (Ps - 20) / (Ps - Pr) )^0.54
      let ratedFlow = 0;
      let hwFactor = 1.0;
      if (deltaP > 0) {
        hwFactor = Math.pow(targetDeltaP / deltaP, 0.54);
        ratedFlow = qTotalFlow * hwFactor;
      }

      // Color classification
      let colorClass = '';
      if (ratedFlow >= 1500) {
        colorClass = '\uD83D\uDD35 Class AA (Light Blue Bonnet) \u2014 \u2265 1,500 GPM';
      } else if (ratedFlow >= 1000) {
        colorClass = '\uD83D\uDFE2 Class A (Green Bonnet) \u2014 1,000 to 1,499 GPM';
      } else if (ratedFlow >= 500) {
        colorClass = '\uD83D\uDFE0 Class B (Orange Bonnet) \u2014 500 to 999 GPM';
      } else {
        colorClass = '\uD83D\uDD34 Class C (Red Bonnet) \u2014 < 500 GPM (Deficient)';
      }

      document.getElementById('res-rated-flow').textContent = Math.round(ratedFlow).toLocaleString() + ' GPM';
      document.getElementById('res-color-class').textContent = colorClass;
      document.getElementById('res-test-flow').textContent = Math.round(qTotalFlow).toLocaleString() + ' GPM (' + numOutlets + ' outlet' + (numOutlets > 1 ? 's' : '') + ')';
      document.getElementById('res-test-lpm').textContent = Math.round(qTotalLpm).toLocaleString() + ' LPM';
      document.getElementById('res-press-drop').textContent = deltaP.toFixed(0) + ' PSI Drop';
      document.getElementById('res-hw-factor').textContent = hwFactor.toFixed(3);
    }

    window.addEventListener('DOMContentLoaded', runHydrantCalc);
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "fire-alarm-battery-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_FA_BATTERY)
print("[PASS] fire-alarm-battery-calculator.html generated successfully!")

with open(os.path.join(BASE_DIR, "hydrant-fire-flow-calculator.html"), "w", encoding="utf-8") as f:
    f.write(TOOL_HYDRANT)
print("[PASS] hydrant-fire-flow-calculator.html generated successfully!")
