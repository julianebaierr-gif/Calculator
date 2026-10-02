"""
Updates index.html with the 40 calculators, updated chips, category cards, directory cards, and FAQs.
"""
import re

def update_index():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Meta description & schema
    content = content.replace("Explore 30+ specialized calculators across 12 core disciplines.", "Explore 40+ specialized calculators across 12 core disciplines.")
    content = content.replace("All 33 calculators across all 12 disciplines are 100% free", "All 40 calculators across all 12 disciplines are 100% free")
    content = content.replace("The platform provides <strong>33 specialized precision calculators</strong>", "The platform provides <strong>40 specialized precision calculators</strong>")
    content = content.replace("Explore all 33 certified calculators organized across 12 specialized disciplines.", "Explore all 40 certified calculators organized across 12 specialized disciplines.")

    # 2. Chips
    content = content.replace('🏦 Finance (5)</a>', '🏦 Finance (7)</a>')
    content = content.replace('⚡ Electrical (5)</a>', '⚡ Electrical (6)</a>')
    content = content.replace('🏗️ Civil (2)</a>', '🏗️ Civil (4)</a>')
    content = content.replace('🚨 Fire (1)</a>', '🚨 Fire (2)</a>')

    # 3. Category Overview Cards (Top 12 Cards Grid)
    # Finance card
    finance_old = """      <!-- 2. Finance & Investment -->
      <div class="category-overview-card cat-finance">
        <div class="cat-card-header">
          <div class="cat-icon-box" style="background:#EFF6FF;border-color:#BFDBFE;">🏦</div>
          <span class="cat-count-badge" style="background:#EFF6FF;color:#2563EB;border-color:#BFDBFE;">5 Tools</span>
        </div>
        <div class="cat-card-title">Finance & Investment</div>
        <div class="cat-card-desc">Transparent financial mathematics for reducing-balance mortgages, compound interest wealth, and sales taxes.</div>
        <div class="cat-tool-preview-list">
          <a href="loan-emi-calculator.html" class="cat-tool-item"><span>🏦 Loan EMI Calculator</span><span class="arr">&rarr;</span></a>
          <a href="compound-interest-calculator.html" class="cat-tool-item"><span>📈 Compound Interest</span><span class="arr">&rarr;</span></a>
          <a href="simple-interest-calculator.html" class="cat-tool-item"><span>💰 Simple Interest</span><span class="arr">&rarr;</span></a>
          <a href="discount-calculator.html" class="cat-tool-item"><span>🏷️ Discount & Sale</span><span class="arr">&rarr;</span></a>
          <a href="salary-calculator.html" class="cat-tool-item"><span>💼 Salary / Paycheck</span><span class="arr">&rarr;</span></a>
        </div>
        <a href="finance.html" class="cat-explore-btn">Explore Finance Hub &rarr;</a>
      </div>"""

    finance_new = """      <!-- 2. Finance & Investment -->
      <div class="category-overview-card cat-finance">
        <div class="cat-card-header">
          <div class="cat-icon-box" style="background:#EFF6FF;border-color:#BFDBFE;">🏦</div>
          <span class="cat-count-badge" style="background:#EFF6FF;color:#2563EB;border-color:#BFDBFE;">7 Tools</span>
        </div>
        <div class="cat-card-title">Finance & Investment</div>
        <div class="cat-card-desc">Transparent financial mathematics for reducing-balance mortgages, compound interest wealth, and sales taxes.</div>
        <div class="cat-tool-preview-list">
          <a href="loan-emi-calculator.html" class="cat-tool-item"><span>🏦 Loan EMI Calculator</span><span class="arr">&rarr;</span></a>
          <a href="mortgage-calculator.html" class="cat-tool-item"><span>🏡 Mortgage &amp; PITI</span><span class="arr">&rarr;</span></a>
          <a href="compound-interest-calculator.html" class="cat-tool-item"><span>📈 Compound Interest</span><span class="arr">&rarr;</span></a>
          <a href="tip-calculator.html" class="cat-tool-item"><span>🍽️ Tip &amp; Bill Split</span><span class="arr">&rarr;</span></a>
          <a href="simple-interest-calculator.html" class="cat-tool-item"><span>💰 Simple Interest</span><span class="arr">&rarr;</span></a>
          <a href="discount-calculator.html" class="cat-tool-item"><span>🏷️ Discount &amp; Sale</span><span class="arr">&rarr;</span></a>
          <a href="salary-calculator.html" class="cat-tool-item"><span>💼 Salary / Paycheck</span><span class="arr">&rarr;</span></a>
        </div>
        <a href="finance.html" class="cat-explore-btn">Explore Finance Hub &rarr;</a>
      </div>"""

    content = content.replace(finance_old, finance_new)

    # Electrical card
    electrical_old = """      <!-- 4. Electrical & Engineering -->
      <div class="category-overview-card cat-engineering">
        <div class="cat-card-header">
          <div class="cat-icon-box" style="background:#FFFBEB;border-color:#FDE68A;">⚡</div>
          <span class="cat-count-badge" style="background:#FFFBEB;color:#D97706;border-color:#FDE68A;">5 Tools</span>
        </div>
        <div class="cat-card-title">Electrical Engineering</div>
        <div class="cat-card-desc">Verified electrical engineering calculators compliant with IEC 60364-5-52, NEC NFPA 70, and EIA resistor standards.</div>
        <div class="cat-tool-preview-list">
          <a href="ohms-law-calculator.html" class="cat-tool-item"><span>⚡ Ohm's Law Wheel</span><span class="arr">&rarr;</span></a>
          <a href="voltage-drop-calculator.html" class="cat-tool-item"><span>📉 Voltage Drop (NEC)</span><span class="arr">&rarr;</span></a>
          <a href="cable-sizing-calculator.html" class="cat-tool-item"><span>🔌 Cable Sizing (IEC)</span><span class="arr">&rarr;</span></a>
          <a href="resistor-color-code-calculator.html" class="cat-tool-item"><span>🎨 Resistor Color Code</span><span class="arr">&rarr;</span></a>
          <a href="solar-panel-sizing-calculator.html" class="cat-tool-item"><span>☀️ Solar PV Array Sizing</span><span class="arr">&rarr;</span></a>
        </div>
        <a href="engineering.html" class="cat-explore-btn">Explore Electrical Hub &rarr;</a>
      </div>"""

    electrical_new = """      <!-- 4. Electrical & Engineering -->
      <div class="category-overview-card cat-engineering">
        <div class="cat-card-header">
          <div class="cat-icon-box" style="background:#FFFBEB;border-color:#FDE68A;">⚡</div>
          <span class="cat-count-badge" style="background:#FFFBEB;color:#D97706;border-color:#FDE68A;">6 Tools</span>
        </div>
        <div class="cat-card-title">Electrical Engineering</div>
        <div class="cat-card-desc">Verified electrical engineering calculators compliant with IEC 60364-5-52, NEC NFPA 70, and EIA resistor standards.</div>
        <div class="cat-tool-preview-list">
          <a href="ohms-law-calculator.html" class="cat-tool-item"><span>⚡ Ohm's Law Wheel</span><span class="arr">&rarr;</span></a>
          <a href="voltage-drop-calculator.html" class="cat-tool-item"><span>📉 Voltage Drop (NEC)</span><span class="arr">&rarr;</span></a>
          <a href="cable-sizing-calculator.html" class="cat-tool-item"><span>🔌 Cable Sizing (IEC)</span><span class="arr">&rarr;</span></a>
          <a href="short-circuit-calculator.html" class="cat-tool-item"><span>💥 Short-Circuit (IEC 60909)</span><span class="arr">&rarr;</span></a>
          <a href="transformer-sizing-calculator.html" class="cat-tool-item"><span>🔄 Transformer Sizing</span><span class="arr">&rarr;</span></a>
          <a href="resistor-color-code-calculator.html" class="cat-tool-item"><span>🎨 Resistor Color Code</span><span class="arr">&rarr;</span></a>
        </div>
        <a href="engineering.html" class="cat-explore-btn">Explore Electrical Hub &rarr;</a>
      </div>"""

    content = content.replace(electrical_old, electrical_new)

    # Civil card
    civil_old = """      <!-- 7. Civil & Construction -->
      <div class="category-overview-card cat-civil">
        <div class="cat-card-header">
          <div class="cat-icon-box" style="background:#FEFCE8;border-color:#FEF08A;">🏗️</div>
          <span class="cat-count-badge" style="background:#FEFCE8;color:#B45309;border-color:#FEF08A;">2 Tools</span>
        </div>
        <div class="cat-card-title">Civil & Construction</div>
        <div class="cat-card-desc">Concrete slab volume in m³/yd³, cement batching bags, and reinforcing steel rebar weight estimations.</div>
        <div class="cat-tool-preview-list">
          <a href="concrete-calculator.html" class="cat-tool-item"><span>🏗️ Concrete Volume Sizing</span><span class="arr">&rarr;</span></a>
          <a href="rebar-calculator.html" class="cat-tool-item"><span>🔩 Rebar Weight & Spacing</span><span class="arr">&rarr;</span></a>
        </div>
        <a href="civil.html" class="cat-explore-btn">Explore Civil Hub &rarr;</a>
      </div>"""

    civil_new = """      <!-- 7. Civil & Construction -->
      <div class="category-overview-card cat-civil">
        <div class="cat-card-header">
          <div class="cat-icon-box" style="background:#FEFCE8;border-color:#FEF08A;">🏗️</div>
          <span class="cat-count-badge" style="background:#FEFCE8;color:#B45309;border-color:#FEF08A;">4 Tools</span>
        </div>
        <div class="cat-card-title">Civil & Construction</div>
        <div class="cat-card-desc">Concrete slab volume in m³/yd³, cement batching bags, beam deflection, and retaining wall stability estimations.</div>
        <div class="cat-tool-preview-list">
          <a href="concrete-calculator.html" class="cat-tool-item"><span>🏗️ Concrete Volume Sizing</span><span class="arr">&rarr;</span></a>
          <a href="rebar-calculator.html" class="cat-tool-item"><span>🔩 Rebar Weight &amp; Spacing</span><span class="arr">&rarr;</span></a>
          <a href="beam-deflection-calculator.html" class="cat-tool-item"><span>📏 Beam Deflection &amp; Stress</span><span class="arr">&rarr;</span></a>
          <a href="retaining-wall-calculator.html" class="cat-tool-item"><span>🧱 Retaining Wall Stability</span><span class="arr">&rarr;</span></a>
        </div>
        <a href="civil.html" class="cat-explore-btn">Explore Civil Hub &rarr;</a>
      </div>"""

    content = content.replace(civil_old, civil_new)

    # Fire card
    fire_old = """      <!-- 9. Fire & Safety -->
      <div class="category-overview-card cat-fire">
        <div class="cat-card-header">
          <div class="cat-icon-box" style="background:#FEF2F2;border-color:#FECACA;">🚨</div>
          <span class="cat-count-badge" style="background:#FEF2F2;color:#DC2626;border-color:#FECACA;">1 Tool</span>
        </div>
        <div class="cat-card-title">Fire & Life Safety</div>
        <div class="cat-card-desc">NFPA 72 smoke detector spacing with ceiling height derating factors and layout coverage analysis.</div>
        <div class="cat-tool-preview-list">
          <a href="smoke-detector-spacing-calculator.html" class="cat-tool-item"><span>🚨 Smoke Detector Spacing</span><span class="arr">&rarr;</span></a>
        </div>
        <a href="fire-safety.html" class="cat-explore-btn">Explore Fire Hub &rarr;</a>
      </div>"""

    fire_new = """      <!-- 9. Fire & Safety -->
      <div class="category-overview-card cat-fire">
        <div class="cat-card-header">
          <div class="cat-icon-box" style="background:#FEF2F2;border-color:#FECACA;">🚨</div>
          <span class="cat-count-badge" style="background:#FEF2F2;color:#DC2626;border-color:#FECACA;">2 Tools</span>
        </div>
        <div class="cat-card-title">Fire & Life Safety</div>
        <div class="cat-card-desc">NFPA 72 smoke detector spacing with ceiling height derating and NFPA 13 sprinkler hydraulic flow sizing.</div>
        <div class="cat-tool-preview-list">
          <a href="smoke-detector-spacing-calculator.html" class="cat-tool-item"><span>🚨 Smoke Detector Spacing</span><span class="arr">&rarr;</span></a>
          <a href="fire-sprinkler-calculator.html" class="cat-tool-item"><span>💦 Sprinkler Flow &amp; Pressure</span><span class="arr">&rarr;</span></a>
        </div>
        <a href="fire-safety.html" class="cat-explore-btn">Explore Fire Hub &rarr;</a>
      </div>"""

    content = content.replace(fire_old, fire_new)

    # 4. Directory Grid Cards
    # Electrical directory card
    dir_elec_old = """        <!-- 1. Electrical Engineering -->
        <div class="directory-card" style="border-top: 3px solid #D97706;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>⚡</span> <a href="engineering.html">Electrical Engineering</a>
            </h3>
            <span class="directory-card-badge" style="background:#FFFBEB;color:#D97706;border:1px solid #FDE68A;">IEC &amp; NEC</span>
          </div>
          <p class="directory-card-desc">
            Industrial low-voltage and medium-voltage electrical design suite. Calculate conductor ampacity via our <a href="cable-sizing-calculator.html">Cable Sizing Calculator (IEC 60364-5-52)</a>, analyze feeder impedance with the <a href="voltage-drop-calculator.html">Voltage Drop Calculator</a>, verify DC/AC power circuits using <a href="ohms-law-calculator.html">Ohm's Law Calculator</a>, and decode 4/5/6-band resistors with the <a href="resistor-color-code-calculator.html">Resistor Color Code Decoder</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="cable-sizing-calculator.html"><span>🔌 Cable Sizing &amp; Current Capacity</span><span class="tool-meta">IEC 60364 / NEC</span></a>
            </li>
            <li class="directory-link-item">
              <a href="voltage-drop-calculator.html"><span>📉 Voltage Drop &amp; Feeder Length</span><span class="tool-meta">NEC 3% / 5% Limit</span></a>
            </li>
            <li class="directory-link-item">
              <a href="ohms-law-calculator.html"><span>⚡ Ohm's Law &amp; Power Wheel</span><span class="tool-meta">V = IR &amp; P = VI</span></a>
            </li>
            <li class="directory-link-item">
              <a href="resistor-color-code-calculator.html"><span>🎨 Resistor Color Code Decoder</span><span class="tool-meta">EIA 4/5/6-Band</span></a>
            </li>
          </ul>
        </div>"""

    dir_elec_new = """        <!-- 1. Electrical Engineering -->
        <div class="directory-card" style="border-top: 3px solid #D97706;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>⚡</span> <a href="engineering.html">Electrical Engineering</a>
            </h3>
            <span class="directory-card-badge" style="background:#FFFBEB;color:#D97706;border:1px solid #FDE68A;">IEC &amp; NEC</span>
          </div>
          <p class="directory-card-desc">
            Industrial low-voltage and medium-voltage electrical design suite. Calculate conductor ampacity via our <a href="cable-sizing-calculator.html">Cable Sizing Calculator (IEC 60364-5-52)</a>, evaluate fault levels with the <a href="short-circuit-calculator.html">Short-Circuit Calculator (IEC 60909)</a>, size substations via the <a href="transformer-sizing-calculator.html">Transformer Sizing Calculator</a>, analyze feeder impedance with the <a href="voltage-drop-calculator.html">Voltage Drop Calculator</a>, verify DC/AC circuits using <a href="ohms-law-calculator.html">Ohm's Law</a>, and decode resistors with the <a href="resistor-color-code-calculator.html">Resistor Color Code Decoder</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="cable-sizing-calculator.html"><span>🔌 Cable Sizing &amp; Current Capacity</span><span class="tool-meta">IEC 60364 / NEC</span></a>
            </li>
            <li class="directory-link-item">
              <a href="short-circuit-calculator.html"><span>💥 Short-Circuit Current (Ik'' &amp; Ip)</span><span class="tool-meta">IEC 60909 Symmetrical</span></a>
            </li>
            <li class="directory-link-item">
              <a href="transformer-sizing-calculator.html"><span>🔄 Transformer Capacity &amp; FLC</span><span class="tool-meta">NEC 450 / IEC 60076</span></a>
            </li>
            <li class="directory-link-item">
              <a href="voltage-drop-calculator.html"><span>📉 Voltage Drop &amp; Feeder Length</span><span class="tool-meta">NEC 3% / 5% Limit</span></a>
            </li>
            <li class="directory-link-item">
              <a href="ohms-law-calculator.html"><span>⚡ Ohm's Law &amp; Power Wheel</span><span class="tool-meta">V = IR &amp; P = VI</span></a>
            </li>
            <li class="directory-link-item">
              <a href="resistor-color-code-calculator.html"><span>🎨 Resistor Color Code Decoder</span><span class="tool-meta">EIA 4/5/6-Band</span></a>
            </li>
          </ul>
        </div>"""

    content = content.replace(dir_elec_old, dir_elec_new)

    # Civil directory card
    dir_civil_old = """        <!-- 4. Civil & Construction Engineering -->
        <div class="directory-card" style="border-top: 3px solid #B45309;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🏗️</span> <a href="civil.html">Civil &amp; Construction</a>
            </h3>
            <span class="directory-card-badge" style="background:#FEFCE8;color:#B45309;border:1px solid #FEF08A;">ACI 318 &amp; ASTM</span>
          </div>
          <p class="directory-card-desc">
            Structural material estimation, batching ratios, and reinforcement takeoffs. Estimate wet concrete volume in m³ and yards³ plus cement bag counts via the <a href="concrete-calculator.html">Concrete Slab &amp; Column Calculator (ACI 318)</a>, and determine linear rebar lengths, cutting schedules, and total reinforcement weight in kg and lbs using the <a href="rebar-calculator.html">Rebar Weight &amp; Grid Spacing Calculator (ASTM A615)</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="concrete-calculator.html"><span>🏗️ Concrete Volume &amp; Batching</span><span class="tool-meta">ACI 318 / Cement Bags</span></a>
            </li>
            <li class="directory-link-item">
              <a href="rebar-calculator.html"><span>🔩 Rebar Weight &amp; Grid Spacing</span><span class="tool-meta">ASTM A615 (kg/lbs)</span></a>
            </li>
          </ul>
        </div>"""

    dir_civil_new = """        <!-- 4. Civil & Construction Engineering -->
        <div class="directory-card" style="border-top: 3px solid #B45309;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🏗️</span> <a href="civil.html">Civil &amp; Construction</a>
            </h3>
            <span class="directory-card-badge" style="background:#FEFCE8;color:#B45309;border:1px solid #FEF08A;">ACI 318 &amp; ASTM</span>
          </div>
          <p class="directory-card-desc">
            Structural material estimation, batching ratios, and reinforcement takeoffs. Estimate wet concrete volume in m³ and yards³ plus cement bag counts via the <a href="concrete-calculator.html">Concrete Slab &amp; Column Calculator (ACI 318)</a>, analyze beam moments and deflections via the <a href="beam-deflection-calculator.html">Beam Deflection Calculator (AISC 360)</a>, verify lateral earth pressures and overturning stability with the <a href="retaining-wall-calculator.html">Retaining Wall Calculator</a>, and determine linear rebar lengths and weight using the <a href="rebar-calculator.html">Rebar Weight &amp; Grid Spacing Calculator (ASTM A615)</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="concrete-calculator.html"><span>🏗️ Concrete Volume &amp; Batching</span><span class="tool-meta">ACI 318 / Cement Bags</span></a>
            </li>
            <li class="directory-link-item">
              <a href="rebar-calculator.html"><span>🔩 Rebar Weight &amp; Grid Spacing</span><span class="tool-meta">ASTM A615 (kg/lbs)</span></a>
            </li>
            <li class="directory-link-item">
              <a href="beam-deflection-calculator.html"><span>📏 Beam Deflection &amp; Bending Stress</span><span class="tool-meta">Euler-Bernoulli / AISC</span></a>
            </li>
            <li class="directory-link-item">
              <a href="retaining-wall-calculator.html"><span>🧱 Cantilever Retaining Wall Stability</span><span class="tool-meta">Rankine Earth Pressure</span></a>
            </li>
          </ul>
        </div>"""

    content = content.replace(dir_civil_old, dir_civil_new)

    # Fire directory card
    dir_fire_old = """        <!-- 6. Fire & Life Safety -->
        <div class="directory-card" style="border-top: 3px solid #DC2626;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🚨</span> <a href="fire-safety.html">Fire &amp; Life Safety</a>
            </h3>
            <span class="directory-card-badge" style="background:#FEF2F2;color:#DC2626;border:1px solid #FECACA;">NFPA 72 &amp; EN 54</span>
          </div>
          <p class="directory-card-desc">
            Certified life safety and architectural fire alarm design tools. Determine detector layout spacing, maximum square coverage grids, and ceiling height derating reduction factors adhering to the National Fire Alarm and Signaling Code using the <a href="smoke-detector-spacing-calculator.html">Smoke Detector Spacing Calculator (NFPA 72)</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="smoke-detector-spacing-calculator.html"><span>🚨 Smoke Detector Layout &amp; Spacing</span><span class="tool-meta">NFPA 72 Grid (9.1m)</span></a>
            </li>
          </ul>
        </div>"""

    dir_fire_new = """        <!-- 6. Fire & Life Safety -->
        <div class="directory-card" style="border-top: 3px solid #DC2626;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🚨</span> <a href="fire-safety.html">Fire &amp; Life Safety</a>
            </h3>
            <span class="directory-card-badge" style="background:#FEF2F2;color:#DC2626;border:1px solid #FECACA;">NFPA 72 &amp; EN 54</span>
          </div>
          <p class="directory-card-desc">
            Certified life safety, hydraulic suppression, and architectural fire alarm design tools. Determine detector layout spacing and ceiling height derating factors using the <a href="smoke-detector-spacing-calculator.html">Smoke Detector Spacing Calculator (NFPA 72)</a>, and calculate sprinkler discharge density, K-factor nozzle flow, and water demand with the <a href="fire-sprinkler-calculator.html">Fire Sprinkler Flow Calculator (NFPA 13)</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="smoke-detector-spacing-calculator.html"><span>🚨 Smoke Detector Layout &amp; Spacing</span><span class="tool-meta">NFPA 72 Grid (9.1m)</span></a>
            </li>
            <li class="directory-link-item">
              <a href="fire-sprinkler-calculator.html"><span>💦 Sprinkler Flow &amp; Pressure Sizing</span><span class="tool-meta">NFPA 13 (Q = K√P)</span></a>
            </li>
          </ul>
        </div>"""

    content = content.replace(dir_fire_old, dir_fire_new)

    # Finance directory card
    dir_fin_old = """        <!-- 8. Finance & Investment -->
        <div class="directory-card" style="border-top: 3px solid #2563EB;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🏦</span> <a href="finance.html">Finance &amp; Investment</a>
            </h3>
            <span class="directory-card-badge" style="background:#EFF6FF;color:#2563EB;border:1px solid #BFDBFE;">Actuarial Math</span>
          </div>
          <p class="directory-card-desc">
            Actuarial loan mechanics, wealth compounding, and retail economics. Plan debt amortization with the <a href="loan-emi-calculator.html">Loan EMI Calculator</a>, project CAGR portfolio growth with periodic deposits via the <a href="compound-interest-calculator.html">Compound Interest Calculator</a>, compute linear promissory returns using <a href="simple-interest-calculator.html">Simple Interest</a>, optimize markdown deals with the <a href="discount-calculator.html">Discount &amp; Tax Calculator</a>, and convert hourly wages to net take-home earnings with the <a href="salary-calculator.html">Salary Paycheck Calculator</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="loan-emi-calculator.html"><span>🏦 Loan EMI &amp; Amortization</span><span class="tool-meta">Monthly Reducing Balance</span></a>
            </li>
            <li class="directory-link-item">
              <a href="compound-interest-calculator.html"><span>📈 Compound Interest &amp; Wealth</span><span class="tool-meta">Periodic Contributions</span></a>
            </li>
            <li class="directory-link-item">
              <a href="salary-calculator.html"><span>💼 Salary / Paycheck Converter</span><span class="tool-meta">Hourly to Annual</span></a>
            </li>
            <li class="directory-link-item">
              <a href="discount-calculator.html"><span>🏷️ Discount &amp; Retail Sales Tax</span><span class="tool-meta">Stacked Markdown Savings</span></a>
            </li>
            <li class="directory-link-item">
              <a href="simple-interest-calculator.html"><span>💰 Simple Interest Calculator</span><span class="tool-meta">I = P × R × T / 100</span></a>
            </li>
          </ul>
        </div>"""

    dir_fin_new = """        <!-- 8. Finance & Investment -->
        <div class="directory-card" style="border-top: 3px solid #2563EB;">
          <div class="directory-card-header">
            <h3 class="directory-card-title">
              <span>🏦</span> <a href="finance.html">Finance &amp; Investment</a>
            </h3>
            <span class="directory-card-badge" style="background:#EFF6FF;color:#2563EB;border:1px solid #BFDBFE;">Actuarial Math</span>
          </div>
          <p class="directory-card-desc">
            Actuarial loan mechanics, wealth compounding, mortgage amortization, and retail economics. Model 30-year home loans with PITI and PMI via the <a href="mortgage-calculator.html">Mortgage Calculator</a>, plan general debt amortization with the <a href="loan-emi-calculator.html">Loan EMI Calculator</a>, compute restaurant gratuity and bill splitting with the <a href="tip-calculator.html">Tip Calculator</a>, project CAGR portfolio growth with periodic deposits via the <a href="compound-interest-calculator.html">Compound Interest Calculator</a>, compute linear promissory returns using <a href="simple-interest-calculator.html">Simple Interest</a>, optimize markdown deals with the <a href="discount-calculator.html">Discount &amp; Tax Calculator</a>, and convert hourly wages to net take-home earnings with the <a href="salary-calculator.html">Salary Paycheck Calculator</a>.
          </p>
          <ul class="directory-links-list">
            <li class="directory-link-item">
              <a href="mortgage-calculator.html"><span>🏡 Mortgage &amp; Amortization (PITI)</span><span class="tool-meta">Principal, Interest &amp; Taxes</span></a>
            </li>
            <li class="directory-link-item">
              <a href="loan-emi-calculator.html"><span>🏦 Loan EMI &amp; Amortization</span><span class="tool-meta">Monthly Reducing Balance</span></a>
            </li>
            <li class="directory-link-item">
              <a href="tip-calculator.html"><span>🍽️ Tip &amp; Bill Split Calculator</span><span class="tool-meta">Pre-Tax Gratuity &amp; Splitting</span></a>
            </li>
            <li class="directory-link-item">
              <a href="compound-interest-calculator.html"><span>📈 Compound Interest &amp; Wealth</span><span class="tool-meta">Periodic Contributions</span></a>
            </li>
            <li class="directory-link-item">
              <a href="salary-calculator.html"><span>💼 Salary / Paycheck Converter</span><span class="tool-meta">Hourly to Annual</span></a>
            </li>
            <li class="directory-link-item">
              <a href="discount-calculator.html"><span>🏷️ Discount &amp; Retail Sales Tax</span><span class="tool-meta">Stacked Markdown Savings</span></a>
            </li>
            <li class="directory-link-item">
              <a href="simple-interest-calculator.html"><span>💰 Simple Interest Calculator</span><span class="tool-meta">I = P × R × T / 100</span></a>
            </li>
          </ul>
        </div>"""

    content = content.replace(dir_fin_old, dir_fin_new)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("index.html updated successfully!")

if __name__ == "__main__":
    update_index()
