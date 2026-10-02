"""
Generates conduit-fill-calculator.html and motor-starting-current-calculator.html
"""
import os

TOOL_CONDUIT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Conduit Fill Calculator (NEC Table 1 &amp; 4) — Raceway Capacity &amp; Jam Ratio</title>
  <meta name="description" content="Calculate electrical conduit fill percentage according to NEC Chapter 9 Tables 1, 4 &amp; 5. Supports EMT, PVC Sch 40/80, RMC with THHN/THWN conductors and jam ratio alerts.">
  <meta name="keywords" content="conduit fill calculator, nec conduit fill, emt conduit fill, pvc schedule 40 fill, raceway capacity calculator, nec chapter 9 table 1, 40 percent fill rule, wire pulling jam ratio">
  <link rel="canonical" href="https://calchub.org/conduit-fill-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Conduit Fill Calculator (NEC Standard)",
        "operatingSystem": "All",
        "applicationCategory": "UtilitiesApplication",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
        "description": "Calculates raceway fill percentage and conductor capacity per National Electrical Code Chapter 9 Table 1 guidelines."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is the maximum allowed conduit fill percentage according to the NEC?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "NEC Chapter 9 Table 1 mandates that a raceway containing 1 conductor may be filled up to 53% of its cross-sectional area, 2 conductors up to 31%, and 3 or more conductors up to a maximum of 40%."
            }
          },
          {
            "@type": "Question",
            "name": "Why is the 2-conductor fill limit 31% while 3 or more conductors allow 40%?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Two conductors pulled into a conduit tend to twist into an oval configuration with their axes side-by-side, creating severe diagonal friction against the cylindrical conduit wall. The lower 31% limit prevents excessive pulling tension and jacket tearing."
            }
          },
          {
            "@type": "Question",
            "name": "What is the wire pulling jam ratio and why does it cause cable lockup?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The jam ratio is the ratio of the conduit inside diameter (ID) to the conductor outside diameter (OD). When pulling three conductors around a bend, if the ID/OD ratio falls between 2.8 and 3.2, the cables can form a triangular wedge that jams permanently inside the conduit."
            }
          },
          {
            "@type": "Question",
            "name": "Does the conduit fill rule apply to short nipples under 24 inches?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "NEC Chapter 9 Note 4 grants an exception for conduit nipples not exceeding 24 inches (600 mm) installed between boxes or enclosures. Nipples are permitted to be filled up to 60% of their total cross-sectional area without applying ampacity derating factors."
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
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="engineering.html" class="nav-link active">⚡ Electrical</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
        </div>
        <div class="nav-row">
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
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
      <span class="category-tag">⚡ Electrical &amp; Power Engineering</span>
      <h1 class="calc-page-title">Conduit Fill Calculator</h1>
      <p class="calc-page-desc">Size electrical raceways compliant with NEC Chapter 9 Table 1, Table 4, and Table 5 standards. Verify 40% fill limits, total conductor displacement area, and wire pulling jam ratios.</p>
    </div>
  </div>

  <div class="layout-container" style="display:flex;gap:2rem;max-width:1200px;margin:2rem auto;padding:0 1.25rem;align-items:start;">
    
    <main style="flex:1;min-width:0;">
      <div class="calculator-workspace">
        <section class="calc-card">
          <div class="calc-card-header">
            <h2 class="calc-card-title"><span>🔌</span> Raceway &amp; Wire Selection</h2>
            <span class="status-info">NEC Chapter 9</span>
          </div>
          <form id="conduit-form" onsubmit="return false;">
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="conduit-type">Conduit Type</label>
                <select id="conduit-type" class="form-control" onchange="runConduitCalc()">
                  <option value="emt" selected>EMT (Electrical Metallic Tubing)</option>
                  <option value="pvc40">PVC Schedule 40 (Rigid Nonmetallic)</option>
                  <option value="pvc80">PVC Schedule 80 (Heavy Wall Nonmetallic)</option>
                  <option value="rmc">RMC (Rigid Metal Conduit - Steel)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="trade-size">Conduit Trade Size</label>
                <select id="trade-size" class="form-control" onchange="runConduitCalc()">
                  <option value="0.5">1/2 inch (Trade Size 16)</option>
                  <option value="0.75" selected>3/4 inch (Trade Size 21)</option>
                  <option value="1.0">1 inch (Trade Size 27)</option>
                  <option value="1.25">1-1/4 inch (Trade Size 35)</option>
                  <option value="1.5">1-1/2 inch (Trade Size 41)</option>
                  <option value="2.0">2 inch (Trade Size 53)</option>
                  <option value="2.5">2-1/2 inch (Trade Size 63)</option>
                  <option value="3.0">3 inch (Trade Size 78)</option>
                  <option value="4.0">4 inch (Trade Size 103)</option>
                </select>
              </div>
            </div>

            <h3 style="font-size:1rem;color:#0F172A;margin:1.25rem 0 0.5rem;padding-bottom:0.25rem;border-bottom:1px solid #E2E8F0;">Conductor Group 1 (Primary Feeder)</h3>
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="wire-type1">Insulation Material</label>
                <select id="wire-type1" class="form-control" onchange="runConduitCalc()">
                  <option value="thhn" selected>THHN / THWN-2 (Copper/Alum)</option>
                  <option value="xhhw">XHHW / XHHW-2 (Cross-linked PE)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="wire-size1">Conductor Gauge (AWG/kcmil)</label>
                <select id="wire-size1" class="form-control" onchange="runConduitCalc()">
                  <option value="14">14 AWG</option>
                  <option value="12">12 AWG</option>
                  <option value="10" selected>10 AWG</option>
                  <option value="8">8 AWG</option>
                  <option value="6">6 AWG</option>
                  <option value="4">4 AWG</option>
                  <option value="2">2 AWG</option>
                  <option value="1/0">1/0 AWG</option>
                  <option value="2/0">2/0 AWG</option>
                  <option value="3/0">3/0 AWG</option>
                  <option value="4/0">4/0 AWG</option>
                  <option value="250">250 kcmil</option>
                  <option value="500">500 kcmil</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="wire-qty1">Number of Conductors</label>
                <input type="number" id="wire-qty1" class="form-control" value="4" min="1" max="100" oninput="runConduitCalc()">
              </div>
            </div>

            <h3 style="font-size:1rem;color:#0F172A;margin:1.25rem 0 0.5rem;padding-bottom:0.25rem;border-bottom:1px solid #E2E8F0;">Conductor Group 2 (Grounding / Auxiliary)</h3>
            <div class="calc-fields-grid">
              <div class="form-group">
                <label class="form-label" for="wire-size2">Ground Wire Gauge</label>
                <select id="wire-size2" class="form-control" onchange="runConduitCalc()">
                  <option value="none">None (No auxiliary wires)</option>
                  <option value="14">14 AWG THHN</option>
                  <option value="12">12 AWG THHN</option>
                  <option value="10" selected>10 AWG THHN</option>
                  <option value="8">8 AWG THHN</option>
                  <option value="6">6 AWG THHN</option>
                  <option value="4">4 AWG THHN</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label" for="wire-qty2">Ground Wire Quantity</label>
                <input type="number" id="wire-qty2" class="form-control" value="1" min="0" max="20" oninput="runConduitCalc()">
              </div>
            </div>

            <div class="calc-actions" style="margin-top:1.5rem;display:flex;gap:1rem;">
              <button type="button" class="btn btn-primary" onclick="runConduitCalc()">Recalculate Fill</button>
              <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ Print Report</button>
            </div>
          </form>
        </section>

        <section class="results-card">
          <h2 class="results-title">Raceway Sizing Summary</h2>
          <div class="primary-result-box" style="margin-bottom:1.5rem;text-align:center;padding:1.5rem;border-radius:12px;background:#F8FAFC;border:2px solid #E2E8F0;">
            <div class="primary-result-label" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;">Total Raceway Fill</div>
            <div id="res-fill-pct" class="primary-result-value" style="font-size:2.5rem;font-weight:800;color:#2563EB;margin:0.25rem 0;">26.4%</div>
            <div id="res-compliance-badge" style="display:inline-block;padding:0.35rem 0.85rem;border-radius:9999px;font-weight:700;font-size:0.82rem;background:#ECFDF5;color:#059669;border:1px solid #A7F3D0;">
              ✓ COMPLIANT (Under 40% Max)
            </div>
          </div>

          <div class="result-details-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Conduit Inside Area</span>
              <span id="res-conduit-area" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">0.533 sq in</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Max Permissible Area (40%)</span>
              <span id="res-allowed-area" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">0.213 sq in</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Total Conductors Area</span>
              <span id="res-wires-area" class="result-val" style="font-size:1.1rem;font-weight:700;color:#0F172A;">0.106 sq in</span>
            </div>
            <div class="result-item" style="background:#FFFFFF;border:1px solid #E2E8F0;padding:0.75rem;border-radius:8px;">
              <span class="result-label" style="display:block;font-size:0.78rem;color:#64748B;">Remaining Usable Area</span>
              <span id="res-remain-area" class="result-val" style="font-size:1.1rem;font-weight:700;color:#059669;">0.107 sq in</span>
            </div>
          </div>

          <div id="res-jam-box" style="margin-top:1.25rem;padding:0.85rem;border-radius:8px;background:#FFFBEB;border:1px solid #FDE68A;font-size:0.85rem;color:#B45309;">
            <strong>ℹ️ Jam Ratio Check:</strong> Ratio is <span id="res-jam-ratio">4.92</span>. Safe from triangular cable jam lockup during bends (critical risk zone is 2.8 to 3.2).
          </div>
        </section>
      </div>

      <!-- In-Depth Technical Article (1,200+ words) -->
      <article class="article-section" style="margin-top:2.5rem;line-height:1.7;color:#334155;">
        <h2>Authoritative Guide to Electrical Conduit Fill &amp; Raceway Engineering</h2>
        <p>
          Proper raceway dimensioning is a cornerstone of safe industrial and commercial electrical installation design. In electrical contracting and power engineering, installing conductors inside metallic or nonmetallic conduits is not simply a matter of mechanical containment; it governs heat dissipation, pulling tension, insulation longevity, and structural safety during thermal expansion. When electric current flows through conductors, copper and aluminum experience resistive heating ($I^2 R$ Joule losses). If conductors are packed too tightly within an enclosed conduit, thermal convective air circulation is choked off, ambient temperatures skyrocket beyond insulation thresholds (such as 75°C or 90°C), and insulation degrades rapidly, creating catastrophic short circuits and phase-to-ground arc faults. To prevent this hazard, the <strong>National Electrical Code (NEC NFPA 70)</strong> prescribes rigid volumetric limitations in <strong>NEC Chapter 9, Table 1</strong>, cross-referenced with the internal dimensions of raceways in <strong>Table 4</strong> and conductor dimensional physical dimensions in <strong>Table 5</strong>.
        </p>

        <h3>The NEC Chapter 9 Table 1 Percent Fill Rules</h3>
        <p>
          The percentage of cross-sectional raceway area that may be occupied by insulated conductors is governed strictly by the number of individual cables being pulled through the conduit system. The NEC mandates the following statutory limits:
        </p>
        <div class="worked-example-card" style="background:#F8FAFC;border-left:4px solid #2563EB;padding:1.25rem;border-radius:0 8px 8px 0;margin:1.5rem 0;">
          <h4 style="margin:0 0 0.5rem;color:#1E293B;">Statutory NEC Fill Thresholds:</h4>
          <ul style="margin:0;padding-left:1.25rem;">
            <li><strong>1 Conductor (53% Maximum Fill):</strong> When pulling a single insulated cable or a multi-conductor jacketed assembly, the cable naturally rests along the bottom invert of the conduit, allowing ample peripheral air space above the cable jacket. The maximum permissible fill is 53%.</li>
            <li><strong>2 Conductors (31% Maximum Fill):</strong> Two separate conductors pulled into a conduit tend to twist into an oval cross-section. When bending around elbows and sweeps, the two conductors wedge tightly against each other and press laterally against the conduit walls, creating severe frictional drag. To prevent jacket tearing, the limit drops to 31%.</li>
            <li><strong>3 or More Conductors (40% Maximum Fill):</strong> For three or more conductors, geometric randomness allows air pockets to form between individual strands, allowing natural convection cooling while maintaining manageable pulling tension. Hence, the standard design threshold is <strong>40% fill</strong>.</li>
          </ul>
        </div>

        <h3>Mathematical Governing Equations</h3>
        <p>
          Calculating conduit fill requires converting conduit internal diameters ($ID$) and conductor external diameters ($OD$) into cross-sectional areas. For cylindrical conduits:
        </p>
        <p>$$\text{Total Internal Raceway Area } A_{conduit} = \frac{\pi \cdot d_{inner}^2}{4}$$</p>
        <p>
          The allowable cross-sectional area for conductors ($A_{allow}$) given a specified fill fraction ($F_{limit} = 0.40$ for 3+ wires) is:
        </p>
        <p>$$A_{allow} = A_{conduit} \times F_{limit}$$</p>
        <p>
          For a mix of $k$ different conductor sizes, the total aggregate displacement area of all pulled cables is the sum of their individual cross-sectional areas:
        </p>
        <p>$$A_{wires} = \sum_{i=1}^{k} N_i \cdot \left( \frac{\pi \cdot d_{wire, i}^2}{4} \right)$$</p>
        <p>
          Compliance is achieved when $A_{wires} \le A_{allow}$. The actual percentage fill is given by:
        </p>
        <p>$$\text{Fill Percentage } (\%) = \left( \frac{A_{wires}}{A_{conduit}} \right) \times 100\%$$</p>

        <h3>Raceway Types &amp; Internal Dimensional Variances</h3>
        <p>
          A frequent mistake in electrical estimating and field engineering is assuming that all conduits sharing the same nominal "trade size" possess identical internal cross-sectional areas. In reality, wall thicknesses differ drastically across materials:
        </p>
        <table class="reference-table" style="width:100%;border-collapse:collapse;margin:1.5rem 0;font-size:0.9rem;">
          <thead>
            <tr style="background:#F1F5F9;text-align:left;">
              <th style="padding:0.75rem;border:1px solid #CBD5E1;">Conduit Type</th>
              <th style="padding:0.75rem;border:1px solid #CBD5E1;">Wall Characteristic</th>
              <th style="padding:0.75rem;border:1px solid #CBD5E1;">Trade Size 1" Total Area</th>
              <th style="padding:0.75rem;border:1px solid #CBD5E1;">40% Allowed Area</th>
              <th style="padding:0.75rem;border:1px solid #CBD5E1;">Typical Application</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;"><strong>EMT (Tubing)</strong></td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">Thin-wall steel</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">0.864 sq in (557 mm²)</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">0.346 sq in (223 mm²)</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">Commercial indoor dry locations</td>
            </tr>
            <tr>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;"><strong>PVC Schedule 40</strong></td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">Standard nonmetallic</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">0.811 sq in (523 mm²)</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">0.324 sq in (209 mm²)</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">Direct underground burial / concrete encasement</td>
            </tr>
            <tr>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;"><strong>PVC Schedule 80</strong></td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">Extra-heavy wall</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">0.655 sq in (423 mm²)</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">0.262 sq in (169 mm²)</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">Areas subject to severe physical damage</td>
            </tr>
            <tr>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;"><strong>RMC (Rigid Steel)</strong></td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">Heavy threaded steel</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">0.863 sq in (557 mm²)</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">0.345 sq in (223 mm²)</td>
              <td style="padding:0.75rem;border:1px solid #CBD5E1;">Hazardous industrial plant floors &amp; service masts</td>
            </tr>
          </tbody>
        </table>
        <p>
          Notice that 1-inch Schedule 80 PVC provides only 0.262 sq in of permissible 40% area, compared to 0.346 sq in for 1-inch EMT—a massive 24.3% reduction in wire capacity! Always size raceways using the exact Schedule or tubing standard specified in project construction blueprints. For conductor current-carrying calculations, verify your run against our <a href="cable-sizing-calculator.html">Cable Sizing Calculator</a> and check line losses with the <a href="voltage-drop-calculator.html">Voltage Drop Calculator</a>.
        </p>

        <h3>The Cable Pulling Jam Ratio Phenomenon</h3>
        <p>
          Even when an installation complies perfectly with the 40% volumetric fill limit, pulling three conductors through conduit bends carries a hidden physical hazard: <strong>cable jamming</strong>. When three conductors are pulled simultaneously through a conduit elbow or sweep, they can slide from their typical triangular configuration into a flat planar configuration side-by-side. If the internal diameter of the conduit is approximately three times the outside diameter of a single conductor, the three cables can form a mechanical wedge that jams permanently against the walls, halting the pull and snapping the pulling rope. The mathematical jam ratio is defined as:
        </p>
        <p>$$\text{Jam Ratio } (J) = \frac{D_{conduit, inner}}{d_{conductor, outer}}$$</p>
        <p>
          The recognized critical jamming zone identified by the IEEE and the National Electrical Contractors Association (NECA) occurs when:
        </p>
        <p>$$2.8 \le J \le 3.2$$</p>
        <p>
          If your calculated jam ratio falls within this 2.8 to 3.2 window, pulling engineers strongly advise upsizing the conduit trade size by one increment or choosing conductors with slightly different outer jacket thicknesses to escape the wedge trap.
        </p>

        <h3>Worked Practical Example: 3-Phase 100A Subpanel Feeder</h3>
        <div class="worked-example-card" style="background:#F0FDF4;border-left:4px solid #16A34A;padding:1.25rem;border-radius:0 8px 8px 0;margin:1.5rem 0;">
          <h4 style="margin:0 0 0.5rem;color:#14532D;">Real-World Installation Takeoff:</h4>
          <p><strong>Design Scenario:</strong> An electrical contractor is installing a 100-ampere, 3-phase, 4-wire subpanel feeder plus an equipment grounding conductor inside Electrical Metallic Tubing (EMT). The bill of materials specifies:</p>
          <ul style="margin:0.5rem 0;padding-left:1.25rem;">
            <li>3 &times; 3 AWG THHN copper phase conductors (nominal cross-sectional area: 0.0973 sq in each)</li>
            <li>1 &times; 3 AWG THHN copper neutral conductor (area: 0.0973 sq in)</li>
            <li>1 &times; 8 AWG THHN copper equipment grounding conductor (area: 0.0366 sq in)</li>
          </ul>
          <p><strong>Step 1: Calculate Total Conductor Displacement Area:</strong></p>
          <p>$$A_{wires} = (4 \times 0.0973) + (1 \times 0.0366) = 0.3892 + 0.0366 = 0.4258 \text{ sq in}$$</p>
          <p><strong>Step 2: Evaluate 1-1/4 Inch EMT Capacity:</strong></p>
          <p>From NEC Chapter 9 Table 4, 1-1/4" EMT has an internal diameter of 1.380 in, giving a total internal area of 1.496 sq in. The allowed 40% fill limit is:</p>
          <p>$$A_{allow} = 1.496 \times 0.40 = 0.598 \text{ sq in}$$</p>
          <p><strong>Step 3: Verification &amp; Fill Percentage:</strong></p>
          <p>$$\text{Fill Percentage} = \frac{0.4258}{1.496} \times 100\% = 28.46\%$$</p>
          <p>Since 28.46% is well below the statutory 40% ceiling, 1-1/4" EMT is 100% code compliant with ample margin for smooth pulling around bends without excessive sidewall bearing pressure.</p>
        </div>

        <h3>Conduit Nipples &amp; Short Raceway Derating Exceptions</h3>
        <p>
          Under <strong>NEC Chapter 9, Note 4 to the Tables</strong>, where conduits or tubing do not exceed 24 inches (600 mm) in length—frequently referred to as conduit nipples installed between adjacent distribution panels, wireways, or switchboards—the maximum allowable fill percentage increases from 40% to a generous <strong>60%</strong>. Furthermore, under <strong>NEC 310.15(C)(1) Note 4</strong>, conductors installed within nipples 24 inches or less in length are completely exempt from ambient temperature ampacity derating adjustments, simplifying panelboard terminations. When planning transformers or substations, also refer to our <a href="transformer-sizing-calculator.html">Transformer Sizing Calculator</a> and verify interrupting duty with our <a href="short-circuit-calculator.html">Short-Circuit Current Calculator</a>.
        </p>

        <!-- Technical FAQs -->
        <div class="faq-container" style="margin-top:2.5rem;">
          <h3 style="margin-bottom:1rem;color:#0F172A;">Frequently Asked Questions About Conduit Fill</h3>
          
          <details class="faq-item" style="border:1px solid #E2E8F0;border-radius:8px;padding:1rem;margin-bottom:0.75rem;">
            <summary style="font-weight:700;cursor:pointer;color:#1E293B;">What is the maximum allowed conduit fill percentage according to the NEC?</summary>
            <div class="faq-content" style="margin-top:0.75rem;color:#475569;">
              NEC Chapter 9 Table 1 mandates that a raceway containing 1 conductor may be filled up to 53% of its cross-sectional area, 2 conductors up to 31%, and 3 or more conductors up to a maximum of 40%.
            </div>
          </details>

          <details class="faq-item" style="border:1px solid #E2E8F0;border-radius:8px;padding:1rem;margin-bottom:0.75rem;">
            <summary style="font-weight:700;cursor:pointer;color:#1E293B;">Why is the 2-conductor fill limit 31% while 3 or more conductors allow 40%?</summary>
            <div class="faq-content" style="margin-top:0.75rem;color:#475569;">
              Two conductors pulled into a conduit tend to twist into an oval configuration with their axes side-by-side, creating severe diagonal friction against the cylindrical conduit wall. The lower 31% limit prevents excessive pulling tension and jacket tearing.
            </div>
          </details>

          <details class="faq-item" style="border:1px solid #E2E8F0;border-radius:8px;padding:1rem;margin-bottom:0.75rem;">
            <summary style="font-weight:700;cursor:pointer;color:#1E293B;">What is the wire pulling jam ratio and why does it cause cable lockup?</summary>
            <div class="faq-content" style="margin-top:0.75rem;color:#475569;">
              The jam ratio is the ratio of the conduit inside diameter (ID) to the conductor outside diameter (OD). When pulling three conductors around a bend, if the ID/OD ratio falls between 2.8 and 3.2, the cables can form a triangular wedge that jams permanently inside the conduit.
            </div>
          </details>

          <details class="faq-item" style="border:1px solid #E2E8F0;border-radius:8px;padding:1rem;margin-bottom:0.75rem;">
            <summary style="font-weight:700;cursor:pointer;color:#1E293B;">Does the conduit fill rule apply to short nipples under 24 inches?</summary>
            <div class="faq-content" style="margin-top:0.75rem;color:#475569;">
              NEC Chapter 9 Note 4 grants an exception for conduit nipples not exceeding 24 inches (600 mm) installed between boxes or enclosures. Nipples are permitted to be filled up to 60% of their total cross-sectional area without applying ampacity derating factors.
            </div>
          </details>
        </div>
      </article>
    </main>

    <!-- Post Sidebar -->
    <aside class="post-sidebar" style="width:300px;flex-shrink:0;">
      <div class="sidebar-widget" style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:12px;padding:1.25rem;">
        <div class="sidebar-widget-header" style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.75rem;">
          <span class="widget-icon" style="font-size:1.25rem;">⚡</span>
          <h3 class="widget-title" style="margin:0;font-size:1.05rem;color:#0F172A;">Electrical Engineering Suite</h3>
        </div>
        <div class="sidebar-widget-subtitle" style="font-size:0.8rem;color:#64748B;margin-bottom:1rem;">Standards-compliant electrical calculation tools:</div>
        <ul class="sidebar-tools-list" style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.5rem;">
          <li><a href="conduit-fill-calculator.html" class="sidebar-tool-item active" style="display:block;padding:0.5rem 0.75rem;border-radius:6px;background:#EFF6FF;color:#2563EB;text-decoration:none;font-size:0.85rem;font-weight:600;">🔌 Conduit Fill (NEC Ch. 9)</a></li>
          <li><a href="motor-starting-current-calculator.html" class="sidebar-tool-item" style="display:block;padding:0.5rem 0.75rem;border-radius:6px;color:#475569;text-decoration:none;font-size:0.85rem;">⚙️ Motor Starting Current</a></li>
          <li><a href="cable-sizing-calculator.html" class="sidebar-tool-item" style="display:block;padding:0.5rem 0.75rem;border-radius:6px;color:#475569;text-decoration:none;font-size:0.85rem;">🔌 Cable Sizing (IEC 60364)</a></li>
          <li><a href="voltage-drop-calculator.html" class="sidebar-tool-item" style="display:block;padding:0.5rem 0.75rem;border-radius:6px;color:#475569;text-decoration:none;font-size:0.85rem;">📉 Voltage Drop (NEC)</a></li>
          <li><a href="short-circuit-calculator.html" class="sidebar-tool-item" style="display:block;padding:0.5rem 0.75rem;border-radius:6px;color:#475569;text-decoration:none;font-size:0.85rem;">💥 Short-Circuit (IEC 60909)</a></li>
          <li><a href="transformer-sizing-calculator.html" class="sidebar-tool-item" style="display:block;padding:0.5rem 0.75rem;border-radius:6px;color:#475569;text-decoration:none;font-size:0.85rem;">🔄 Transformer Sizing (NEC 450)</a></li>
          <li><a href="ohms-law-calculator.html" class="sidebar-tool-item" style="display:block;padding:0.5rem 0.75rem;border-radius:6px;color:#475569;text-decoration:none;font-size:0.85rem;">⚡ Ohm's Law Wheel</a></li>
          <li><a href="resistor-color-code-calculator.html" class="sidebar-tool-item" style="display:block;padding:0.5rem 0.75rem;border-radius:6px;color:#475569;text-decoration:none;font-size:0.85rem;">🎨 Resistor Color Code</a></li>
        </ul>
        <div class="sidebar-widget-footer" style="margin-top:1.25rem;padding-top:0.75rem;border-top:1px solid #E2E8F0;text-align:center;">
          <a href="engineering.html" class="sidebar-cat-link" style="color:#2563EB;font-weight:600;font-size:0.85rem;text-decoration:none;">Explore Electrical Hub &rarr;</a>
        </div>
      </div>
    </aside>

  </div>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand-logo">
            <span class="logo-badge">∑</span>
            <span>Calc<span class="accent">Hub</span></span>
          </a>
          <p>High-precision, free online calculators designed according to published mathematical, clinical, and industrial engineering standards. 100% free, browser-based, with zero tracking.</p>
        </div>
        <div class="footer-col">
          <h4>Electrical &amp; Power</h4>
          <ul class="footer-links">
            <li><a href="conduit-fill-calculator.html">Conduit Fill Calculator</a></li>
            <li><a href="motor-starting-current-calculator.html">Motor Starting Current</a></li>
            <li><a href="cable-sizing-calculator.html">Cable Sizing (IEC)</a></li>
            <li><a href="voltage-drop-calculator.html">Voltage Drop (NEC)</a></li>
            <li><a href="short-circuit-calculator.html">Short-Circuit Current</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Engineering Suites</h4>
          <ul class="footer-links">
            <li><a href="engineering.html">Electrical Engineering</a></li>
            <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
            <li><a href="civil.html">Civil &amp; Structural</a></li>
            <li><a href="solar-energy.html">Solar Energy</a></li>
            <li><a href="chemical.html">Chemical &amp; Water</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Engineering calculations are for guidance purposes.</p>
        <div>
          <a href="sitemap.xml" style="color:#64748B;margin-left:1rem;">Sitemap</a>
          <a href="index.html" style="color:#64748B;margin-left:1rem;">Privacy &amp; Terms</a>
        </div>
      </div>
    </div>
  </footer>

  <script>
    // NEC Chapter 9 Table 4 Internal Areas (sq in) and IDs (inches)
    const conduitDB = {
      emt: {
        '0.5': { id: 0.622, area: 0.304 },
        '0.75': { id: 0.824, area: 0.533 },
        '1.0': { id: 1.049, area: 0.864 },
        '1.25': { id: 1.380, area: 1.496 },
        '1.5': { id: 1.610, area: 2.036 },
        '2.0': { id: 2.067, area: 3.356 },
        '2.5': { id: 2.731, area: 5.858 },
        '3.0': { id: 3.356, area: 8.846 },
        '4.0': { id: 4.310, area: 14.59 }
      },
      pvc40: {
        '0.5': { id: 0.602, area: 0.285 },
        '0.75': { id: 0.804, area: 0.508 },
        '1.0': { id: 1.029, area: 0.811 },
        '1.25': { id: 1.360, area: 1.453 },
        '1.5': { id: 1.590, area: 1.986 },
        '2.0': { id: 2.047, area: 3.291 },
        '2.5': { id: 2.445, area: 4.695 },
        '3.0': { id: 3.042, area: 7.268 },
        '4.0': { id: 3.998, area: 12.55 }
      },
      pvc80: {
        '0.5': { id: 0.526, area: 0.217 },
        '0.75': { id: 0.722, area: 0.409 },
        '1.0': { id: 0.936, area: 0.655 },
        '1.25': { id: 1.255, area: 1.237 },
        '1.5': { id: 1.476, area: 1.711 },
        '2.0': { id: 1.913, area: 2.874 },
        '2.5': { id: 2.290, area: 4.119 },
        '3.0': { id: 2.864, area: 6.442 },
        '4.0': { id: 3.786, area: 11.26 }
      },
      rmc: {
        '0.5': { id: 0.632, area: 0.314 },
        '0.75': { id: 0.836, area: 0.549 },
        '1.0': { id: 1.063, area: 0.863 },
        '1.25': { id: 1.394, area: 1.526 },
        '1.5': { id: 1.624, area: 2.071 },
        '2.0': { id: 2.083, area: 3.408 },
        '2.5': { id: 2.489, area: 4.866 },
        '3.0': { id: 3.090, area: 7.499 },
        '4.0': { id: 4.050, area: 12.88 }
      }
    };

    // NEC Chapter 9 Table 5 Conductor Areas (sq in) and Outer Diameters (in)
    const wireDB = {
      thhn: {
        '14': { area: 0.0097, od: 0.111 },
        '12': { area: 0.0133, od: 0.130 },
        '10': { area: 0.0211, od: 0.164 },
        '8': { area: 0.0366, od: 0.216 },
        '6': { area: 0.0507, od: 0.254 },
        '4': { area: 0.0824, od: 0.324 },
        '2': { area: 0.1158, od: 0.384 },
        '1/0': { area: 0.1855, od: 0.486 },
        '2/0': { area: 0.2223, od: 0.532 },
        '3/0': { area: 0.2679, od: 0.584 },
        '4/0': { area: 0.3237, od: 0.642 },
        '250': { area: 0.3970, od: 0.711 },
        '500': { area: 0.7073, od: 0.949 }
      },
      xhhw: {
        '14': { area: 0.0139, od: 0.133 },
        '12': { area: 0.0181, od: 0.152 },
        '10': { area: 0.0243, od: 0.176 },
        '8': { area: 0.0437, od: 0.236 },
        '6': { area: 0.0590, od: 0.274 },
        '4': { area: 0.0814, od: 0.322 },
        '2': { area: 0.1146, od: 0.382 },
        '1/0': { area: 0.1825, od: 0.482 },
        '2/0': { area: 0.2190, od: 0.528 },
        '3/0': { area: 0.2642, od: 0.580 },
        '4/0': { area: 0.3197, od: 0.638 },
        '250': { area: 0.3904, od: 0.705 },
        '500': { area: 0.6940, od: 0.940 }
      }
    };

    function runConduitCalc() {
      const cType = document.getElementById('conduit-type').value;
      const cSize = document.getElementById('trade-size').value;
      const wType1 = document.getElementById('wire-type1').value;
      const wSize1 = document.getElementById('wire-size1').value;
      const wQty1 = parseInt(document.getElementById('wire-qty1').value) || 0;
      const wSize2 = document.getElementById('wire-size2').value;
      const wQty2 = parseInt(document.getElementById('wire-qty2').value) || 0;

      const conduitInfo = conduitDB[cType][cSize];
      const wire1Info = wireDB[wType1][wSize1];

      let totalWiresArea = wQty1 * wire1Info.area;
      let totalConductorsCount = wQty1;

      if (wSize2 !== 'none' && wQty2 > 0) {
        const wire2Info = wireDB['thhn'][wSize2];
        totalWiresArea += wQty2 * wire2Info.area;
        totalConductorsCount += wQty2;
      }

      // Max fill fraction
      let maxFillFrac = 0.40;
      if (totalConductorsCount === 1) maxFillFrac = 0.53;
      else if (totalConductorsCount === 2) maxFillFrac = 0.31;

      const allowedArea = conduitInfo.area * maxFillFrac;
      const fillPct = (totalWiresArea / conduitInfo.area) * 100;
      const remainArea = allowedArea - totalWiresArea;

      document.getElementById('res-fill-pct').textContent = fillPct.toFixed(1) + '%';
      document.getElementById('res-conduit-area').textContent = conduitInfo.area.toFixed(3) + ' sq in';
      document.getElementById('res-allowed-area').textContent = allowedArea.toFixed(3) + ' sq in (' + (maxFillFrac * 100) + '%)';
      document.getElementById('res-wires-area').textContent = totalWiresArea.toFixed(3) + ' sq in';

      const badge = document.getElementById('res-compliance-badge');
      if (fillPct <= (maxFillFrac * 100)) {
        badge.textContent = '✓ COMPLIANT (Under ' + (maxFillFrac * 100) + '% Max)';
        badge.style.background = '#ECFDF5';
        badge.style.color = '#059669';
        badge.style.borderColor = '#A7F3D0';
        document.getElementById('res-remain-area').textContent = remainArea.toFixed(3) + ' sq in';
        document.getElementById('res-remain-area').style.color = '#059669';
      } else {
        badge.textContent = '✕ EXCEEDS NEC LIMIT (' + (maxFillFrac * 100) + '% Max)';
        badge.style.background = '#FEF2F2';
        badge.style.color = '#DC2626';
        badge.style.borderColor = '#FECACA';
        document.getElementById('res-remain-area').textContent = 'Over by ' + Math.abs(remainArea).toFixed(3) + ' sq in';
        document.getElementById('res-remain-area').style.color = '#DC2626';
      }

      // Jam Ratio Check
      const jamRatio = conduitInfo.id / wire1Info.od;
      document.getElementById('res-jam-ratio').textContent = jamRatio.toFixed(2);
      const jamBox = document.getElementById('res-jam-box');
      if (totalConductorsCount >= 3 && jamRatio >= 2.8 && jamRatio <= 3.2) {
        jamBox.style.background = '#FEF2F2';
        jamBox.style.borderColor = '#FECACA';
        jamBox.style.color = '#B91C1C';
        jamBox.innerHTML = '<strong>⚠️ HIGH RISK OF CABLE JAMMING:</strong> Jam ratio is ' + jamRatio.toFixed(2) + ' (critical window: 2.8 to 3.2). Conductors are at high risk of wedging and lockup around bends. Upsize conduit trade size!';
      } else {
        jamBox.style.background = '#FFFBEB';
        jamBox.style.borderColor = '#FDE68A';
        jamBox.style.color = '#B45309';
        jamBox.innerHTML = '<strong>ℹ️ Jam Ratio Check:</strong> Ratio is ' + jamRatio.toFixed(2) + '. Safe from triangular cable jam lockup during bends (critical risk zone is 2.8 to 3.2).';
      }
    }

    window.addEventListener('DOMContentLoaded', runConduitCalc);
  </script>
</body>
</html>
"""

with open("conduit-fill-calculator.html", "w", encoding="utf-8") as f:
    f.write(TOOL_CONDUIT)

print("conduit-fill-calculator.html generated successfully!")
