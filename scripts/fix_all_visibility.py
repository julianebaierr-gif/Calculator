"""
Comprehensive fix for 100% visibility of all 54 tools on index.html and category hubs.
"""

import os
import re
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define all 54 tools categorized accurately
CAT_MAP = {
    "health.html": {
        "title": "Health & Fitness",
        "tools": [
            ("bmi-calculator.html", "BMI Calculator", "⚖️", "Body mass index, WHO classification & prime ratio", "BMI = kg / (m)²"),
            ("calorie-calculator.html", "Calorie Calculator (TDEE)", "🔥", "Basal metabolic rate & daily expenditure", "TDEE = BMR × Activity"),
            ("bmr-calculator.html", "BMR Calculator", "🧬", "Mifflin-St Jeor & Katch-McArdle resting calories", "BMR = 10W + 6.25H - 5A + s"),
            ("macro-calculator.html", "Macro Split Calculator", "🥗", "Daily protein, carbs & fats for IIFYM", "Atwater: 4C - 4P - 9F kcal/g"),
            ("body-fat-calculator.html", "Body Fat Calculator", "📐", "Navy tape body fat & lean mass", "US Navy Circumference Model"),
            ("ideal-weight-calculator.html", "Ideal Body Weight", "🎯", "Devine & Robinson target weight", "IBW = 50kg + 2.3kg/inch"),
            ("water-intake-calculator.html", "Daily Water Intake", "💧", "Baseline & active hydration needs", "Base (35ml/kg) + Exercise"),
        ]
    },
    "finance.html": {
        "title": "Finance & Investment",
        "tools": [
            ("loan-emi-calculator.html", "Loan EMI Calculator", "💳", "Monthly payment & interest split", "EMI = [P·r·(1+r)ⁿ] / [(1+r)ⁿ - 1]"),
            ("car-loan-calculator.html", "Car Loan Financing", "🚗", "Auto loan payments & trade-in tax", "Auto EMI & Sales Tax Credit"),
            ("mortgage-calculator.html", "Mortgage & PITI", "🏡", "Monthly payment, escrow & amortization", "PITI = P&I + Tax + Ins + PMI"),
            ("roi-calculator.html", "ROI & Annualized CAGR", "📊", "Net capital gain & geometric CAGR", "ROI = (Gain - Cost) ÷ Cost"),
            ("rule-of-72-calculator.html", "Rule of 72 Doubling Time", "📈", "Investment doubling & tripling horizon", "Doubling Years ≈ 72 ÷ Return%"),
            ("compound-interest-calculator.html", "Compound Interest", "📈", "Wealth growth with deposits", "A = P(1 + r/n)ⁿᵗ + PMT···"),
            ("simple-interest-calculator.html", "Simple Interest", "💵", "Linear interest & maturity sum", "I = P × R × T / 100"),
            ("salary-calculator.html", "Salary & Paycheck", "💼", "Hourly, monthly & annual pay", "Annual = Hourly × Hours × 52"),
            ("discount-calculator.html", "Discount & Sale", "🏷️", "Net savings, coupons & sales tax", "Price × (1 - d₁) × (1 + tax)"),
            ("tip-calculator.html", "Tip & Bill Splitter", "🍽️", "Dining gratuity & party bill split", "Tip = Subtotal × Tip%"),
        ]
    },
    "math.html": {
        "title": "Mathematics & Utilities",
        "tools": [
            ("percentage-calculator.html", "Percentage Calculator", "％", "Portions, discounts & % change", "P = (Value / Total) × 100"),
            ("standard-deviation-calculator.html", "Standard Deviation & Variance", "📊", "Sample (n-1) & population stats", "s = √[ ∑(x - x̄)² ÷ (n - 1) ]"),
            ("fraction-calculator.html", "Fraction Calculator", "➗", "Add, multiply & simplify fractions", "a/b ± c/d = (ad ± bc) / bd"),
            ("ratio-calculator.html", "Ratio Simplifier", "⚖️", "Euclid's GCD ratio reduction", "X = (B × C) / A"),
            ("age-calculator.html", "Exact Age Calculator", "🎂", "Chronological age & day of week", "Gregorian Leap Calendar"),
            ("gpa-calculator.html", "College GPA Calculator", "🎓", "4.0 scale cumulative GPA", "GPA = ∑(Points × Cr) ÷ ∑Cr"),
        ]
    },
    "engineering.html": {
        "title": "Electrical & Power Systems",
        "tools": [
            ("ohms-law-calculator.html", "Ohm's Law Calculator", "⚡", "Voltage, current, power & ohms", "V = I·R | P = V·I = I²R"),
            ("voltage-drop-calculator.html", "Voltage Drop Calculator", "📉", "NEC 3% & 5% copper/aluminum run", "ΔV = (2 or √3) · I · L · ρ / A"),
            ("cable-sizing-calculator.html", "Cable Sizing (IEC/NEC)", "🔌", "IEC/NEC ampacity & derating", "I_tabulated ≥ I_load / (Ca × Cg)"),
            ("wire-ampacity-calculator.html", "Wire Ampacity (NEC 310.16)", "🔌", "Allowable conductor current & derating", "I_adj = I_base × K_temp × K_bundle"),
            ("conduit-fill-calculator.html", "Conduit Fill (NEC Ch. 9)", "🪢", "40% fill rule & wire jam ratio", "Fill % = ∑(A_cond) ÷ A_conduit ≤ 40%"),
            ("motor-starting-current-calculator.html", "Motor Starting Current", "⚙️", "NEMA locked rotor inrush amps", "LRA = (HP × kVA/HP × 1000) ÷ (√3 × V)"),
            ("short-circuit-calculator.html", "Short-Circuit (IEC 60909)", "💥", "Symmetrical fault kA & breaking", "Ik'' = c·Un / (√3·|Zk|)"),
            ("transformer-sizing-calculator.html", "Transformer Sizing (NEC 450)", "⚡", "kVA rating & full-load amps", "FLC = (kVA × 1000) / (√3 × V)"),
            ("power-factor-calculator.html", "Power Factor (kW to kVAR)", "⚡", "Capacitor bank rating & line current savings", "Qc = P × [tan(θ1) - tan(θ2)]"),
            ("parallel-resistor-calculator.html", "Parallel Resistor (Req)", "⚡", "Equivalent resistance & branch current divider", "1/Req = ∑(1/Ri) | Conductance G"),
            ("battery-life-calculator.html", "Battery Life & Runtime", "🔋", "Peukert's law discharge & C-rate runtime", "t = H × (C / IH)^k × DoD"),
            ("resistor-color-code-calculator.html", "Resistor Color Code", "🎨", "4 & 5-band axial resistance", "R = (Digits) × 10ⁿ ± Tol%"),
            ("555-timer-calculator.html", "555 Timer Astable & Monostable", "⏱️", "Frequency, duty cycle & pulse width", "f = 1.44 / ((R1 + 2R2) × C)"),
            ("led-resistor-calculator.html", "LED Series Resistor Calculator", "💡", "Current limiting & wattage rating", "R = (Vs - Vf) / If | P = I²R"),
            ("capacitive-reactance-calculator.html", "Capacitive Reactance (Xc)", "⚡", "AC capacitor impedance & phase shift", "Xc = 1 / (2π · f · C)"),
            ("inductive-reactance-calculator.html", "Inductive Reactance (Xl)", "⚡", "AC inductor reactance & back-EMF", "Xl = 2π · f · L"),
            ("op-amp-gain-calculator.html", "Op-Amp Gain & Inverting/Non-Inv", "📈", "Closed loop gain, bandwidth & dB", "Av = -Rf/Rin | 1 + Rf/Rin"),
            ("three-phase-power-calculator.html", "Three-Phase AC Power (kVA/kW)", "⚡", "Real, reactive & apparent 3-phase power", "P = √3 × V_LL × I_L × cos(θ)"),
            ("adc-dac-calculator.html", "ADC & DAC Converter Resolution", "🎛️", "Quantization LSB, SQNR & ENOB", "LSB = V_ref / 2^N | SQNR = 6.02N + 1.76"),
            ("antenna-length-calculator.html", "Antenna Length & Resonant Dipole", "📡", "Half-wave & quarter-wave velocity factor", "L = 142.65·k / f (MHz) | 468/f"),
            ("battery-short-circuit-current-calculator.html", "Battery Short Circuit (IEC 60896)", "🔋", "DC prospective fault current & arc flash", "I_sc = U_n / R_total | Doan Arc Flash"),
            ("bjt-transistor-calculator.html", "BJT Transistor Bias & Q-Point", "⚡", "Voltage divider bias & saturation limit", "I_B = (V_TH - V_BE) / [R_TH + (β+1)R_E]"),
            ("breaker-size-calculator.html", "Breaker Size (NEC 125% Rule)", "🛡️", "Continuous load sizing & trip curves", "I_min = 1.25·I_cont + I_noncont | NEC 240.6"),
            ("decibel-calculator.html", "Decibel Calculator (dB, dBm, SPL)", "🔊", "Power, voltage, dBm to Watts & dB SPL", "dB = 10·log(P1/P0) | 20·log(V1/V0)"),
            ("earth-pit-resistance-calculator.html", "Earth Pit Resistance (IEEE 80)", "🌍", "Grounding rod dissipation & soil resistivity", "R = (ρ/2πL)·[ln(8L/d) - 1]"),
            ("electrical-power-calculator.html", "Electrical Power & Energy Cost", "⚡", "Real, reactive, apparent & kWh cost", "P = VI·cos(θ) | P_3φ = √3·V_LL·I_L·PF"),
            ("microstrip-impedance-calculator.html", "Microstrip Impedance (IPC-2141)", "📡", "Single-ended & differential Z0", "Z0 = [87 / √(εr + 1.41)] · ln[5.98h / (0.8w + t)]"),
            ("resistor-network-calculator.html", "Resistor Network (Delta-Wye & Ladder)", "⚡", "Δ-Y Kennelly transform & R-2R ladder", "R_A = (R1·R2) / (R1+R2+R3) | V_out = V_ref·(D/2^N)"),
            ("transformer-turns-ratio-calculator.html", "Transformer Turns Ratio (a)", "⚡", "Voltage, current & impedance matching", "a = Np/Ns = Vp/Vs = Is/Ip = √(Zp/Zs)"),
            ("aluminium-cable-sizing-calculator.html", "Aluminium Cable Sizing (NEC/IEC)", "🔌", "AA-8000 ampacity, lugs & AL/CU area", "A_Al = 1.64 × A_Cu | Dual Rated AL9CU"),
            ("busbar-sizing-calculator.html", "Busbar Sizing (DIN 43671 / IEC)", "⚡", "Continuous ampacity & short-circuit force", "I = C · A^0.61 · √ΔT | F = (μ0/2π)·(i_p²/s)·L"),
            ("cable-sizing-calculator-bs-7671.html", "Cable Sizing (BS 7671 18th Ed)", "🔌", "UK wiring regulations & mV/A/m drop", "Ib ≤ In ≤ Iz | It ≥ In / (Ca·Cg·Cc·Ci)"),
            ("cable-sizing-calculator-iec-60364.html", "Cable Sizing (IEC 60364-5-52)", "🔌", "International LV dimensioning & adiabatic", "Ib ≤ In ≤ Iz | S ≥ √(Isc²·t) / k"),
            ("cable-sizing-installation-method-a.html", "Cable Sizing Method A (Insulated Wall)", "🔌", "A1 & A2 conduit in cavity derating", "Iz = I0 · Ca · Cg · Ci | High thermal penalty"),
        ]
    },
    "solar-energy.html": {
        "title": "Solar & Renewable Energy",
        "tools": [
            ("solar-panel-sizing-calculator.html", "Solar Panel & Array Sizing", "☀️", "Array watts & peak sun hours", "PV (W) = Daily Wh / (PSH × η)"),
            ("solar-battery-bank-calculator.html", "Solar Battery Bank Sizing", "🔋", "Storage Ah & kWh for autonomy", "Storage Ah = Wh ÷ (V × DoD × η)"),
            ("solar-inverter-sizing-calculator.html", "Solar Inverter Sizing", "⚡", "Continuous kVA & surge capacity", "Inverter VA = Peak Continuous Load × 1.25"),
            ("pv-string-sizing-calculator.html", "PV String Sizing (NEC 690)", "☀️", "MPPT voltage limits & module temperature", "N_max = ⌊V_max / Voc_cold⌋"),
            ("ev-charging-time-calculator.html", "EV Charging Time & Power", "🔌", "Levels 1, 2 & DC Fast charge time", "Time (hrs) = Battery (kWh) ÷ Net kW"),
            ("ev-charging-circuit-calculator.html", "EV Charging Circuit (NEC 625)", "🔌", "Continuous load 125%, breaker & AWG wire", "I_min = 1.25 × I_EVSE | NEC 625.42"),
        ]
    },
    "mechanical.html": {
        "title": "Mechanical & HVAC",
        "tools": [
            ("bolt-torque-calculator.html", "Bolt Torque & Preload", "🔩", "Tightening torque & clamp load preload", "T = K · D · Fp (VDI 2230)"),
            ("bearing-life-calculator.html", "Bearing Life (ISO 281)", "⚙️", "L10 & L10h rating life in revs & hours", "L10 = (C / P)^p × 10⁶ revs"),
            ("cooling-load-calculator.html", "Cooling Load (HVAC) Sizing", "❄️", "Sensible & latent heat in BTU/hr", "Q = 1.08 × CFM × ΔT"),
            ("pipe-sizing-calculator.html", "Pipe Sizing & Water Flow", "🚰", "Internal diameter & friction loss", "Q = A × V | Darcy-Weisbach"),
            ("pump-head-calculator.html", "Pump Head (TDH & Flow)", "🌊", "Total dynamic head & motor BHP", "TDH = Static Head + Friction Head"),
            ("gear-ratio-calculator.html", "Gear Ratio & Speed", "⚙️", "Velocity reduction & torque ratio", "Ratio = Driven Teeth ÷ Driving Teeth"),
            ("torque-calculator.html", "Torque & Shaft Power", "⚙️", "Rotational torque N·m & kW/HP", "P = (2π × N × T) ÷ 60000"),
        ]
    },
    "civil.html": {
        "title": "Civil & Construction",
        "tools": [
            ("concrete-calculator.html", "Concrete Slab, Footing & Column", "🏗️", "Wet concrete m³ & cement bags", "Volume = L × W × H (1.54 Bulking)"),
            ("rebar-calculator.html", "Rebar Weight & Grid Spacing", "🔩", "Cut bar counts & linear mass kg/lbs", "Mass = (d² ÷ 162) × L"),
            ("brick-calculator.html", "Brick & Masonry Calculator", "🧱", "ASTM modular brick & mortar bags", "Bricks = Area × Multiplier × (1 + Waste)"),
            ("asphalt-calculator.html", "Asphalt Paving & Tonnage", "🛣️", "HMA road tonnage & base course", "Tons = Volume × Density ÷ 2,000 lbs"),
            ("beam-deflection-calculator.html", "Beam Deflection & Moments", "📐", "AISC 360 deflection & moment", "δmax = 5wL⁴ / 384EI"),
            ("retaining-wall-calculator.html", "Retaining Wall Stability", "🧱", "Rankine earth pressure & overturning", "Pa = 0.5 × γ × H² × Ka"),
        ]
    },
    "chemical.html": {
        "title": "Chemical & Water Treatment",
        "tools": [
            ("chlorine-dosing-calculator.html", "Chlorine Dosing Calculator", "💧", "AWWA C651 water disinfection & bleach", "Feed (lbs) = Vol (MGal) × Dose (mg/L) × 8.34"),
            ("chemical-dosing-calculator.html", "Chemical Dosing Rate Calculator", "🧪", "Pump flow LPH & mg/L ppm feed", "Feed Rate (LPH) = (Q × D) ÷ (S × SG × 10000)"),
        ]
    },
    "fire-safety.html": {
        "title": "Fire & Life Safety",
        "tools": [
            ("fire-alarm-battery-calculator.html", "Fire Alarm Battery (NFPA 72)", "🚨", "24h standby + evacuation alarm Ah sizing", "C = 1.20 × (I_sb·T_sb + I_al·T_al)"),
            ("hydrant-fire-flow-calculator.html", "Hydrant Fire Flow (NFPA 291)", "🚒", "Pitot discharge flow & rated 20 psi capacity", "Q = 29.83·cd·d²√P | Q_R at 20 psi"),
            ("smoke-detector-spacing-calculator.html", "Smoke Detector Spacing & Layout", "🚨", "NFPA 72 ceiling height derating", "S = 30ft Baseline with Derating Factor"),
            ("fire-sprinkler-calculator.html", "Fire Sprinkler Hydraulics", "💦", "NFPA 13 head flow Q=K√P & demand", "Q = K × √P (K-Factor 5.6 & 8.0)"),
            ("fire-pump-sizing-calculator.html", "Fire Pump Sizing (NFPA 20)", "🚒", "Rated flow, net head, churn & motor BHP", "BHP = (Q × H × SG) / (3960 × η)"),
        ]
    },
    "programmer.html": {
        "title": "Programmer & Networking",
        "tools": [
            ("subnet-calculator.html", "IPv4 Subnet & CIDR IP Calculator", "🌐", "Network ID, mask & usable hosts", "Usable Hosts = 2^(32 - CIDR) - 2"),
        ]
    },
    "datetime.html": {
        "title": "Date & Time Utility",
        "tools": [
            ("date-difference-calculator.html", "Date Difference & Business Days", "📅", "Exact calendar days & work weeks", "Elapsed Days & Mon-Fri Working Days"),
        ]
    },
    "converter.html": {
        "title": "Universal Unit Converters",
        "tools": [
            ("unit-converter.html", "Universal Multi-Unit Converter", "🔄", "Length, mass, temp, pressure & vol", "100% Client-Side Direct Exact Multipliers"),
        ]
    }
}

def update_category_pages():
    for cat_file, data in CAT_MAP.items():
        file_path = os.path.join(BASE_DIR, cat_file)
        if not os.path.exists(file_path):
            continue
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        cards_html = []
        for slug, title, icon, desc, formula in data["tools"]:
            cards_html.append(f"""        <a href="{slug}" class="silo-card">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="silo-card-icon">{icon}</div>
            <span class="silo-card-badge">Certified Tool</span>
          </div>
          <div class="silo-card-title">{title}</div>
          <div class="silo-card-desc">{desc}</div>
          <div class="formula-badge-pill">{formula}</div>
          <span style="display:inline-flex;align-items:center;gap:4px;font-weight:700;font-size:0.85rem;color:var(--brand-primary);margin-top:1rem;">
            Launch Calculator &rarr;
          </span>
        </a>""")

        grid_inner = "\n\n".join(cards_html)
        num_tools = len(data["tools"])

        # Replace cards grid
        grid_pattern = re.compile(r'<div class="silo-card-grid"[^>]*>.*?</div>(?=\s*(?:<!--.*?-->\s*)*<article)', re.DOTALL)
        new_grid = f'<div class="silo-card-grid" style="margin-top:0;margin-bottom:3.5rem;">\n{grid_inner}\n    </div>'
        
        content = grid_pattern.sub(new_grid, content)

        # Update counter labels
        content = re.sub(r'<strong>\d+</strong>\s*(?:Certified Calculators|Precision Tools|Engineering Tools)', f'<strong>{num_tools}</strong> Certified Calculators', content)
        content = re.sub(r'Available (?:Tools|Health Calculators|Engineering Calculators|Finance Calculators|Mathematics Calculators)\s*\(\d+\)', f'Available Tools ({num_tools})', content)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {cat_file} with all {num_tools} cards!")

def update_index_page():
    index_path = os.path.join(BASE_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Category Overview Cards with ALL tools
    cat_cards_html = []
    total_tools_count = 0

    for cat_file, data in CAT_MAP.items():
        num_tools = len(data["tools"])
        total_tools_count += num_tools
        tool_links = []
        for slug, title, icon, desc, formula in data["tools"]:
            tool_links.append(f"""          <a href="{slug}" class="cat-tool-item"><span>{icon} {title}</span><span class="arr">&rarr;</span></a>""")
        
        links_block = "\n".join(tool_links)
        cat_cards_html.append(f"""      <!-- {data["title"]} -->
      <div class="category-overview-card">
        <div class="cat-card-header">
          <div class="cat-icon-box">{data["tools"][0][2]}</div>
          <span class="cat-count-badge">{num_tools} Tools</span>
        </div>
        <div class="cat-card-title">{data["title"]}</div>
        <div class="cat-card-desc">Certified industrial & academic calculations verified against international standards.</div>
        <div class="cat-tool-preview-list">
{links_block}
        </div>
        <a href="{cat_file}" class="cat-explore-btn">Explore {data["title"]} Hub &rarr;</a>
      </div>""")

    new_cat_grid = '<div class="category-overview-grid">\n' + "\n\n".join(cat_cards_html) + '\n    </div>'

    # Replace category grid on index.html
    cat_grid_pattern = re.compile(r'<div class="category-overview-grid">.*?</div>\s*(?=<!-- Comprehensive Platform Authority|<!-- Full Interactive Tool Directory|\s*<section)', re.DOTALL)
    if cat_grid_pattern.search(content):
        content = cat_grid_pattern.sub(new_cat_grid + '\n\n    ', content)
    else:
        # Fallback search
        cat_grid_pattern2 = re.compile(r'<div class="category-overview-grid">.*?</div>', re.DOTALL)
        content = cat_grid_pattern2.sub(new_cat_grid, content, count=1)

    # 2. Add Complete Interactive 54-Tool Directory Section if not present
    all_tools_items = []
    for cat_file, data in CAT_MAP.items():
        for slug, title, icon, desc, formula in data["tools"]:
            all_tools_items.append(f"""        <div class="directory-tool-card" data-cat="{data['title'].lower()}" data-search="{title.lower()} {slug.lower()} {desc.lower()}" style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:1rem;display:flex;flex-direction:column;justify-content:space-between;transition:transform 0.2s,box-shadow 0.2s;">
          <div>
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
              <span style="font-size:1.5rem;">{icon}</span>
              <span style="font-size:0.72rem;background:#F1F5F9;color:#475569;padding:2px 8px;border-radius:12px;font-weight:600;">{data['title']}</span>
            </div>
            <h3 style="margin:0 0 0.35rem;font-size:1rem;color:#0F172A;"><a href="{slug}" style="color:#0F172A;text-decoration:none;">{title}</a></h3>
            <p style="margin:0 0 0.75rem;font-size:0.82rem;color:#64748B;line-height:1.4;">{desc}</p>
          </div>
          <div style="display:flex;align-items:center;justify-content:space-between;border-top:1px solid #F1F5F9;padding-top:0.65rem;margin-top:0.5rem;">
            <code style="font-size:0.75rem;color:#2563EB;background:#EFF6FF;padding:2px 6px;border-radius:4px;">{formula[:28]}</code>
            <a href="{slug}" style="font-size:0.82rem;font-weight:700;color:#2563EB;text-decoration:none;">Launch &rarr;</a>
          </div>
        </div>""")

    directory_block = f"""    <!-- Full Interactive Tool Directory (All {total_tools_count} Calculators Live) -->
    <section id="all-calculators-directory" style="margin-top:4rem;padding-top:2.5rem;border-top:1px solid #E2E8F0;">
      <div style="text-align:center;margin-bottom:2rem;">
        <span class="category-tag" style="background:#F0FDF4;color:#166534;border-color:#BBF7D0;margin-bottom:0.75rem;">
          ⚡ Complete Live Directory · {total_tools_count} High-Precision Tools Live
        </span>
        <h2 style="font-size:2rem;color:#0F172A;margin:0 0 0.5rem;">All {total_tools_count} Online Calculators</h2>
        <p style="color:#64748B;font-size:1rem;max-width:700px;margin:0 auto 1.5rem;">
          Instant access to all verified tools across Health, Finance, Engineering, Civil, Mechanical, Math, Chemical, and Solar energy.
        </p>

        <!-- Live Instant Search Bar -->
        <div style="max-width:600px;margin:0 auto;position:relative;">
          <input type="text" id="directory-search-input" placeholder="🔍 Search any calculator (e.g., bmr, wire, brick, roi, pump, asphalt)..." 
                 oninput="filterDirectoryTools()"
                 style="width:100%;padding:0.85rem 1.25rem;border-radius:12px;border:2px solid #CBD5E1;font-size:1rem;outline:none;transition:border-color 0.2s;"
                 onfocus="this.style.borderColor='#2563EB'" onblur="this.style.borderColor='#CBD5E1'">
        </div>
      </div>

      <div id="directory-tools-grid" style="display:grid;grid-template-columns:repeat(auto-fill, minmax(260px, 1fr));gap:1rem;">
{chr(10).join(all_tools_items)}
      </div>
      <div id="no-search-results" style="display:none;text-align:center;padding:3rem;color:#64748B;">
        <p style="font-size:1.1rem;margin-bottom:0.5rem;">No calculators match your search.</p>
        <button type="button" class="btn btn-secondary" onclick="document.getElementById('directory-search-input').value='';filterDirectoryTools();">Clear Search</button>
      </div>

      <script>
        function filterDirectoryTools() {{
          const q = document.getElementById('directory-search-input').value.toLowerCase().trim();
          const cards = document.querySelectorAll('.directory-tool-card');
          let visibleCount = 0;
          cards.forEach(card => {{
            const searchData = card.getAttribute('data-search') || '';
            const match = !q || searchData.includes(q);
            card.style.display = match ? 'flex' : 'none';
            if (match) visibleCount++;
          }});
          document.getElementById('no-search-results').style.display = visibleCount === 0 ? 'block' : 'none';
        }}
      </script>
    </section>"""

    # Check if section already exists, replace or insert before closing </main>
    if '<section id="all-calculators-directory"' in content:
        content = re.sub(r'<section id="all-calculators-directory".*?</section>', directory_block, content, flags=re.DOTALL)
    else:
        content = content.replace('</main>', directory_block + '\n  </main>')

    # Update hero quick category chips
    chips_html = f"""      <div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-bottom:1.5rem;">
        <a href="health.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">⚖️ Health ({len(CAT_MAP['health.html']['tools'])})</a>
        <a href="finance.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🏦 Finance ({len(CAT_MAP['finance.html']['tools'])})</a>
        <a href="math.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🔢 Math ({len(CAT_MAP['math.html']['tools'])})</a>
        <a href="engineering.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">⚡ Electrical ({len(CAT_MAP['engineering.html']['tools'])})</a>
        <a href="solar-energy.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">☀️ Solar ({len(CAT_MAP['solar-energy.html']['tools'])})</a>
        <a href="mechanical.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">⚙️ Mechanical ({len(CAT_MAP['mechanical.html']['tools'])})</a>
        <a href="civil.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🏗️ Civil ({len(CAT_MAP['civil.html']['tools'])})</a>
        <a href="chemical.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🧪 Chemical ({len(CAT_MAP['chemical.html']['tools'])})</a>
        <a href="fire-safety.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🚨 Fire ({len(CAT_MAP['fire-safety.html']['tools'])})</a>
        <a href="programmer.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">👨‍💻 Tech ({len(CAT_MAP['programmer.html']['tools'])})</a>
        <a href="datetime.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">📅 Date ({len(CAT_MAP['datetime.html']['tools'])})</a>
        <a href="converter.html" class="btn btn-secondary" style="font-size:0.85rem;padding:0.4rem 0.85rem;">🔄 Converter ({len(CAT_MAP['converter.html']['tools'])})</a>
      </div>"""

    content = re.sub(r'<!-- Quick Category Jump Chips -->\s*<div[^>]*>.*?</div>', f'<!-- Quick Category Jump Chips -->\n{chips_html}', content, flags=re.DOTALL)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"index.html updated! All {total_tools_count} calculators are now listed in category previews AND directory!")

if __name__ == "__main__":
    update_category_pages()
    update_index_page()
