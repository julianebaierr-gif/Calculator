import glob
import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORIES = {
    "health": {
        "name": "Health & Fitness",
        "icon": "⚖️",
        "hub": "health.html",
        "tools": [
            ("bmr-calculator.html", "BMR Calculator", "🧬", "Mifflin-St Jeor & Katch-McArdle resting calories"),
            ("macro-calculator.html", "Macro Split Calculator", "🥗", "Daily protein, carbs & fats for IIFYM"),
            ("calorie-calculator.html", "Calorie Calculator (TDEE)", "🔥", "BMR & daily caloric maintenance"),
            ("bmi-calculator.html", "BMI Calculator", "⚖️", "Body mass index & classification"),
            ("body-fat-calculator.html", "Body Fat Calculator", "📐", "Navy tape body fat & lean mass"),
            ("ideal-weight-calculator.html", "Ideal Body Weight", "🎯", "Devine & Robinson target weight"),
            ("water-intake-calculator.html", "Daily Water Intake", "💧", "Baseline & active hydration needs"),
        ]
    },
    "finance": {
        "name": "Finance & Investment",
        "icon": "🏦",
        "hub": "finance.html",
        "tools": [
            ("rule-of-72-calculator.html", "Rule of 72 Doubling Time", "📈", "Investment doubling & tripling horizon"),
            ("car-loan-calculator.html", "Car Loan Financing", "🚗", "Auto loan payments & trade-in tax"),
            ("roi-calculator.html", "ROI & Annualized CAGR", "📊", "Net capital gain & geometric CAGR"),
            ("loan-emi-calculator.html", "Loan EMI Calculator", "💳", "Monthly payment & interest split"),
            ("mortgage-calculator.html", "Mortgage & PITI", "🏡", "Monthly payment, escrow & amortization"),
            ("compound-interest-calculator.html", "Compound Interest", "📈", "Wealth growth with deposits"),
            ("simple-interest-calculator.html", "Simple Interest", "💵", "Linear interest & maturity sum"),
            ("salary-calculator.html", "Salary & Paycheck", "💼", "Hourly, monthly & annual pay"),
            ("discount-calculator.html", "Discount & Sale", "🏷️", "Net savings, coupons & sales tax"),
            ("tip-calculator.html", "Tip & Bill Splitter", "🍽️", "Dining gratuity & party bill split"),
        ]
    },
    "math": {
        "name": "Mathematics & Utilities",
        "icon": "🔢",
        "hub": "math.html",
        "tools": [
            ("standard-deviation-calculator.html", "Standard Deviation & Variance", "📊", "Sample (n-1) & population (N) stats"),
            ("percentage-calculator.html", "Percentage Calculator", "％", "Portions, discounts & % change"),
            ("fraction-calculator.html", "Fraction Calculator", "➗", "Add, multiply & simplify fractions"),
            ("ratio-calculator.html", "Ratio Simplifier", "⚖️", "Euclid's GCD ratio reduction"),
            ("gpa-calculator.html", "College GPA Calculator", "🎓", "4.0 scale cumulative GPA"),
        ]
    },
    "engineering": {
        "name": "Electrical & Power Systems",
        "icon": "⚡",
        "hub": "engineering.html",
        "tools": [
            ("wire-ampacity-calculator.html", "Wire Ampacity (NEC 310.16)", "🔌", "Allowable conductor current & derating"),
            ("conduit-fill-calculator.html", "Conduit Fill (NEC Ch. 9)", "🪢", "40% fill rule & wire jam ratio"),
            ("motor-starting-current-calculator.html", "Motor Starting Current", "⚙️", "NEMA locked rotor inrush amps"),
            ("short-circuit-calculator.html", "Short-Circuit (IEC 60909)", "💥", "Symmetrical fault kA & breaking"),
            ("transformer-sizing-calculator.html", "Transformer Sizing (NEC 450)", "⚡", "kVA rating & full-load amps"),
            ("cable-sizing-calculator.html", "Cable Sizing (IEC/NEC)", "🔌", "IEC/NEC ampacity & derating"),
            ("voltage-drop-calculator.html", "Voltage Drop Calculator", "📉", "NEC 3% & 5% copper/aluminum run"),
            ("ohms-law-calculator.html", "Ohm's Law Calculator", "⚡", "Voltage, current, power & ohms"),
            ("power-factor-calculator.html", "Power Factor (kW to kVAR)", "⚡", "Capacitor bank rating & line current savings"),
            ("parallel-resistor-calculator.html", "Parallel Resistor (Req)", "⚡", "Equivalent resistance & branch current divider"),
            ("battery-life-calculator.html", "Battery Life & Runtime", "🔋", "Peukert's law discharge & C-rate runtime"),
            ("resistor-color-code-calculator.html", "Resistor Color Code", "🎨", "4 & 5-band axial resistance"),
            ("555-timer-calculator.html", "555 Timer Astable & Monostable", "⏱️", "Frequency, duty cycle & pulse width"),
            ("led-resistor-calculator.html", "LED Series Resistor Calculator", "💡", "Current limiting & wattage rating"),
            ("capacitive-reactance-calculator.html", "Capacitive Reactance (Xc)", "⚡", "AC capacitor impedance & phase shift"),
            ("inductive-reactance-calculator.html", "Inductive Reactance (Xl)", "⚡", "AC inductor reactance & back-EMF"),
            ("op-amp-gain-calculator.html", "Op-Amp Gain & Inverting/Non-Inv", "📈", "Closed loop gain, bandwidth & dB"),
            ("three-phase-power-calculator.html", "Three-Phase AC Power (kVA/kW)", "⚡", "Real, reactive & apparent 3-phase power"),
            ("adc-dac-calculator.html", "ADC & DAC Converter Resolution", "🎛️", "Quantization LSB, SQNR & ENOB"),
            ("antenna-length-calculator.html", "Antenna Length & Resonant Dipole", "📡", "Half-wave & quarter-wave velocity factor"),
            ("battery-short-circuit-current-calculator.html", "Battery Short Circuit (IEC 60896)", "🔋", "DC prospective fault current & arc flash"),
            ("bjt-transistor-calculator.html", "BJT Transistor Bias & Q-Point", "⚡", "Voltage divider bias & saturation limit"),
            ("breaker-size-calculator.html", "Breaker Size (NEC 125% Rule)", "🛡️", "Continuous load sizing & trip curves"),
            ("decibel-calculator.html", "Decibel Calculator (dB, dBm, SPL)", "🔊", "Power, voltage, dBm to Watts & dB SPL"),
            ("earth-pit-resistance-calculator.html", "Earth Pit Resistance (IEEE 80)", "🌍", "Grounding rod dissipation & soil resistivity"),
            ("electrical-power-calculator.html", "Electrical Power & Energy Cost", "⚡", "Real, reactive, apparent & kWh cost"),
            ("microstrip-impedance-calculator.html", "Microstrip Impedance (IPC-2141)", "📡", "Single-ended & differential Z0"),
            ("resistor-network-calculator.html", "Resistor Network (Delta-Wye & Ladder)", "⚡", "Δ-Y Kennelly transform & R-2R ladder"),
            ("transformer-turns-ratio-calculator.html", "Transformer Turns Ratio (a)", "⚡", "Voltage, current & impedance matching"),
            ("aluminium-cable-sizing-calculator.html", "Aluminium Cable Sizing (NEC/IEC)", "🔌", "AA-8000 ampacity, lugs & AL/CU area"),
            ("busbar-sizing-calculator.html", "Busbar Sizing (DIN 43671 / IEC)", "⚡", "Continuous ampacity & short-circuit force"),
            ("cable-sizing-calculator-bs-7671.html", "Cable Sizing (BS 7671 18th Ed)", "🔌", "UK wiring regulations & mV/A/m drop"),
            ("cable-sizing-calculator-iec-60364.html", "Cable Sizing (IEC 60364-5-52)", "🔌", "International LV dimensioning & adiabatic"),
            ("cable-sizing-installation-method-a.html", "Cable Sizing Method A (Insulated Wall)", "🔌", "A1 & A2 conduit in cavity derating"),
            ("fault-current-calculator.html", "Fault Current (IEEE 141 / IEC)", "💥", "Transformer secondary & point-to-point kA"),
            ("filter-calculator.html", "Analog Filter (RC, RL, LC)", "🎛️", "Cutoff frequency, dB gain & phase angle"),
            ("generator-sizing-calculator.html", "Generator Sizing (ISO 8528)", "⚡", "Standby kVA, motor inrush & altitude derate"),
            ("heatsink-calculator.html", "Heatsink Sizing & Thermal", "❄️", "Thermal resistance θ_sa & junction temp"),
            ("cable-sizing-installation-method-c.html", "Cable Sizing Method C (Clipped Direct)", "🔌", "Surface clipped to masonry ampacity"),
            ("cable-sizing-installation-method-e.html", "Cable Sizing Method E (Cable Tray)", "🔌", "Perforated tray & ladder rack in free air"),
            ("cable-sizing-calculator-nec.html", "Cable Sizing (NEC Table 310.16)", "🔌", "125% continuous load & conduit fill derate"),
            ("copper-cable-sizing-calculator.html", "Copper Cable Sizing (100% IACS)", "🔌", "Pure ETP Cu ampacity & I²R loss cost"),
            ("earthing-cable-size-calculator.html", "Earthing Cable Size (IEC 60364-5-54)", "⚡", "Adiabatic S = √(I²·t)/k & k-factor"),
            ("kw-to-cable-size-calculator.html", "kW to Cable Size (1-Phase & 3-Phase)", "🔌", "Active kW to full-load current & mV/A/m"),
            ("single-phase-cable-sizing-calculator.html", "Single Phase Cable Sizing (230V/120V)", "🔌", "2-wire loop drop & radial/ring circuit"),
            ("three-phase-cable-sizing-calculator.html", "Three Phase Cable Sizing (400V/480V)", "⚡", "Line-to-line balanced vector drop & method E"),
            ("wire-gauge-calculator.html", "Wire Gauge (AWG to mm² Metric)", "📏", "ASTM B258 logarithmic AWG scale & circular mils"),
        ]
    },
    "solar": {
        "name": "Solar & Renewable Energy",
        "icon": "☀️",
        "hub": "solar-energy.html",
        "tools": [
            ("solar-panel-sizing-calculator.html", "Solar Panel & Array Sizing", "☀️", "Array watts & peak sun hours"),
            ("solar-battery-bank-calculator.html", "Solar Battery Bank Sizing", "🔋", "Storage Ah & kWh for autonomy"),
            ("solar-inverter-sizing-calculator.html", "Solar Inverter Sizing", "⚡", "Continuous kVA & surge capacity"),
            ("pv-string-sizing-calculator.html", "PV String Sizing (NEC 690)", "☀️", "MPPT voltage limits & module temperature"),
            ("ev-charging-time-calculator.html", "EV Charging Time & Power", "🔌", "Levels 1, 2 & DC Fast charge time"),
            ("ev-charging-circuit-calculator.html", "EV Charging Circuit (NEC 625)", "🔌", "Continuous load 125%, breaker & AWG wire"),
        ]
    },
    "mechanical": {
        "name": "Mechanical & HVAC",
        "icon": "⚙️",
        "hub": "mechanical.html",
        "tools": [
            ("bolt-torque-calculator.html", "Bolt Torque & Preload", "🔩", "Tightening torque & clamp load preload"),
            ("bearing-life-calculator.html", "Bearing Life (ISO 281)", "⚙️", "L10 & L10h rating life in revs & hours"),
            ("pump-head-calculator.html", "Pump Head (TDH & Flow)", "🌊", "Total dynamic head & motor BHP"),
            ("gear-ratio-calculator.html", "Gear Ratio & Speed", "⚙️", "Velocity reduction & torque ratio"),
            ("cooling-load-calculator.html", "Cooling Load (HVAC) Sizing", "❄️", "Sensible & latent heat in BTU/hr"),
            ("pipe-sizing-calculator.html", "Pipe Sizing & Water Flow", "🚰", "Internal diameter & friction loss"),
            ("torque-calculator.html", "Torque & Shaft Power", "⚙️", "Rotational torque N·m & kW/HP"),
            ("belt-length-calculator.html", "Belt Length (Open & Crossed Pulley)", "⚙️", "Pitch length, center distance & wrap angle"),
            ("conveyor-belt-speed-calculator.html", "Conveyor Belt Speed & Tonnage", "🏭", "Linear velocity, drum RPM & CEMA capacity"),
            ("cutting-speed-calculator.html", "Cutting Speed & Spindle RPM", "⚙️", "Linear surface speed Vc & Taylor tool life"),
            ("feed-rate-calculator.html", "CNC Feed Rate & Chip Load", "⚙️", "Table feed vf, radial chip thinning & MRR"),
            ("flywheel-energy-calculator.html", "Flywheel Kinetic Energy & Stress", "🔄", "Stored energy, moment of inertia & hoop stress"),
            ("gear-module-calculator.html", "Gear Module & Pitch Geometry", "⚙️", "Metric module m, diametral pitch DP & tip dia"),
            ("heat-exchanger-calculator.html", "Heat Exchanger (LMTD & NTU Area)", "🌡️", "Thermal duty, counter-flow LMTD & TEMA area"),
            ("hvac-calculator.html", "HVAC Sizing & Cooling Tonnage", "❄️", "Sensible, latent dehumidification & supply CFM"),
            ("hydraulic-cylinder-calculator.html", "Hydraulic Cylinder Sizing (ISO 6020)", "🚜", "Push/pull force, fluid velocity & Euler buckling"),
            ("hydraulic-cylinder-force-calculator.html", "Hydraulic Cylinder Net Force (ISO 3320)", "🚜", "Net thrust, backpressure & seal friction drag"),
            ("hydraulic-cylinder-speed-calculator.html", "Hydraulic Cylinder Speed & Flow", "🚜", "Piston velocity, cycle time & regenerative boost"),
            ("hydraulic-pump-power-calculator.html", "Hydraulic Pump Power (ISO 4409)", "⚙️", "Motor drive power, displacement & shaft torque"),
            ("power-to-torque-calculator.html", "Power to Torque & Shaft Sizing", "⚙️", "Rotary torque, gear ratio & shaft shear stress"),
            ("psychrometric-calculator.html", "Psychrometric & Moist Air (ASHRAE)", "🌡️", "Dew point, humidity ratio W, wet bulb & enthalpy"),
            ("pulley-mechanical-advantage-calculator.html", "Pulley Mechanical Advantage (CMAA 70)", "🏗️", "Block & tackle IMA, AMA & reeving friction"),
            ("pulley-rpm-calculator.html", "Pulley RPM & Belt Speed (ISO 5296)", "⚙️", "Rotational speed, ratio, belt velocity & slip"),
            ("pump-flow-calculator.html", "Pump Flow Rate & Velocity", "🌊", "Pipe bore velocity, m³/h, GPM & VFD scaling"),
            ("reynolds-number-calculator.html", "Reynolds Number (Moody & Swamee-Jain)", "🧪", "Laminar, transition & turbulent flow regime"),
            ("shaft-diameter-calculator.html", "Shaft Diameter (ASME B106.1M)", "⚙️", "Combined torsion, bending moment & keyway de-rate"),
            ("spring-rate-calculator.html", "Helical Spring Rate (SMI / ASTM A228)", "🌀", "Spring constant k, Wahl stress factor & solid height"),
            ("thermal-expansion-calculator.html", "Thermal Expansion & Pipe Stress", "🌡️", "Linear growth ΔL, volumetric ΔV & ASME loop leg"),
            ("torque-converter.html", "Torque Converter Sizing (SAE J643)", "🚗", "Stall torque ratio, speed ratio & K-factor"),
            ("torque-to-hp-calculator.html", "Torque to HP & BMEP Converter", "🏎️", "Brake horsepower, kilowatts & 4-stroke BMEP"),
            ("projectile-motion-calculator.html", "Projectile Motion Trajectory", "🚀", "Apex height, time of flight, range & impact velocity"),
        ]
    },
    "civil": {
        "name": "Civil & Construction",
        "icon": "🏗️",
        "hub": "civil.html",
        "tools": [
            ("brick-calculator.html", "Brick & Masonry Calculator", "🧱", "ASTM modular brick & mortar bags"),
            ("asphalt-calculator.html", "Asphalt Paving & Tonnage", "🛣️", "HMA road tonnage & base course"),
            ("beam-deflection-calculator.html", "Beam Deflection & Moments", "📐", "AISC 360 deflection & moment"),
            ("retaining-wall-calculator.html", "Retaining Wall Stability", "🧱", "Rankine earth pressure & overturning"),
            ("concrete-calculator.html", "Concrete Slab, Footing & Column", "🏗️", "Wet concrete m³ & cement bags"),
            ("rebar-calculator.html", "Rebar Weight & Grid Spacing", "🔩", "Cut bar counts & linear mass kg/lbs"),
            ("rainwater-downpipe-calculator.html", "Rainwater Downpipe Sizing", "🌧️", "BS EN 12056 roof catchment & leader sizing"),
            ("beam-calculator.html", "Beam Bending Moment & Shear", "📐", "AISC 360 simply supported & cantilever SFD/BMD"),
            ("block-calculator.html", "Block Masonry Estimator", "🧱", "CMU block counts, Type S mortar & core grout"),
            ("concrete-block-calculator.html", "Concrete Block Calculator", "🧱", "ASTM C90 CMU counts, mortar & ASTM C476 grout"),
            ("concrete-mix-ratio-calculator.html", "Concrete Mix Ratio", "🏗️", "ACI 211.1 1.54 factor, cement bags & aggregate"),
            ("drywall-calculator.html", "Drywall Sheets, Mud & Tape", "🏠", "ASTM C840 gypsum sheets 4x8 to 4x12 & compound"),
            ("excavation-calculator.html", "Excavation & Earthwork Haul", "🚜", "OSHA 1926 bank vs loose cubic yards & haul fleet"),
            ("excavation-volume-calculator.html", "Excavation Volume Calculator", "📐", "Prismoidal formula & trapezoidal trench slopes"),
            ("flooring-calculator.html", "Flooring Area & Box Estimator", "🪵", "NWFA hardwood, LVP & tile carton boxes & underlay"),
            ("footing-size-calculator.html", "Footing Size & Soil Bearing", "🏛️", "Pad width B, contact pressure & two-way punching shear"),
            ("gravel-calculator.html", "Gravel & Aggregate Estimator", "🪨", "Tonnage, cubic meters/yards & compaction allowance"),
            ("paint-calculator.html", "Paint Gallon & Coverage", "🎨", "Wall & ceiling gallons, liters, primer & fenestrations"),
            ("rebar-weight-calculator.html", "Rebar Weight & Tonnage", "🔩", "Metric kg/m d²/162, US lb/ft #²/24 & BBS bundles"),
            ("roof-pitch-calculator.html", "Roof Pitch & Rafter Length", "🏠", "Pitch X:12, slope angle, area multiplier & rafter length"),
            ("slab-concrete-calculator.html", "Slab Concrete Volume", "🏗️", "Slab-on-grade, thickened edge footings & saw-cut joints"),
            ("slope-calculator.html", "Slope & Grade Calculator", "📐", "Rise/run gradient, % grade, angle & ADA ramp 1:12 compliance"),
        ]
    },
    "chemical": {
        "name": "Chemical & Water Treatment",
        "icon": "🧪",
        "hub": "chemical.html",
        "tools": [
            ("chlorine-dosing-calculator.html", "Chlorine Dosing Calculator", "💧", "AWWA C651 water disinfection & bleach"),
            ("chemical-dosing-calculator.html", "Chemical Dosing Rate Calculator", "🧪", "Pump flow LPH & mg/L ppm feed"),
            ("pipe-sizing-calculator.html", "Pipe Sizing & Water Flow", "🚰", "Internal diameter & friction loss"),
            ("cooling-load-calculator.html", "Cooling Load (HVAC) Sizing", "❄️", "Sensible & latent heat in BTU/hr"),
        ]
    },
    "fire": {
        "name": "Fire & Life Safety",
        "icon": "🚨",
        "hub": "fire-safety.html",
        "tools": [
            ("fire-alarm-battery-calculator.html", "Fire Alarm Battery (NFPA 72)", "🚨", "24h standby + evacuation alarm Ah sizing"),
            ("hydrant-fire-flow-calculator.html", "Hydrant Fire Flow (NFPA 291)", "🚒", "Pitot discharge flow & rated 20 psi capacity"),
            ("fire-sprinkler-calculator.html", "Fire Sprinkler Hydraulics", "💦", "NFPA 13 head flow Q=K√P & demand"),
            ("smoke-detector-spacing-calculator.html", "Smoke Detector Spacing & Layout", "🚨", "NFPA 72 ceiling height derating"),
            ("cable-sizing-calculator.html", "Cable Sizing (IEC/NEC)", "🔌", "Fire alarm circuit conductor gauge"),
            ("voltage-drop-calculator.html", "Voltage Drop Calculator", "📉", "Alarm notification appliance circuit"),
            ("fire-pump-sizing-calculator.html", "Fire Pump Sizing (NFPA 20)", "🚒", "Rated flow, net head, churn & motor BHP"),
            ("nac-voltage-drop-calculator.html", "NAC Voltage Drop (NFPA 72 & UL 864)", "🚨", "Point-to-point & lump-sum 16V EOL limit"),
            ("fire-sprinkler-hydraulic-calculator.html", "Fire Sprinkler Hydraulic (NFPA 13)", "💦", "Hazen-Williams friction & head Q=K√P"),
            ("strobe-candela-calculator.html", "Strobe Candela (NFPA 72 Chapter 18)", "🚨", "Wall & ceiling candela sizing & UL 1971"),
        ]
    },
    "programmer": {
        "name": "Programmer & Networking",
        "icon": "👨‍💻",
        "hub": "programmer.html",
        "tools": [
            ("subnet-calculator.html", "IPv4 Subnet & CIDR IP Calculator", "🌐", "Network ID, mask & usable hosts"),
            ("unit-converter.html", "Universal Multi-Unit Converter", "🔄", "Data, bytes & physical unit converter"),
            ("date-difference-calculator.html", "Date Difference & Workdays", "📅", "Epoch timestamp & elapsed time"),
            ("percentage-calculator.html", "Percentage Calculator", "％", "Ratio, portion & growth rate"),
        ]
    },
    "datetime": {
        "name": "Date & Time Utility",
        "icon": "📅",
        "hub": "datetime.html",
        "tools": [
            ("date-difference-calculator.html", "Date Difference & Business Days", "📅", "Exact calendar days & work weeks"),
            ("age-calculator.html", "Exact Age Calculator", "🎂", "Chronological age & day of week"),
            ("salary-calculator.html", "Salary & Paycheck Calculator", "💼", "Hourly to annual pay rates"),
            ("unit-converter.html", "Universal Multi-Unit Converter", "🔄", "Time, speed, temperature & length"),
        ]
    },
    "converter": {
        "name": "Universal Unit Converters",
        "icon": "🔄",
        "hub": "converter.html",
        "tools": [
            ("unit-converter.html", "Universal Multi-Unit Converter", "🔄", "Length, mass, temp, pressure & vol"),
            ("percentage-calculator.html", "Percentage Calculator", "％", "Proportions, discounts & % change"),
            ("fraction-calculator.html", "Fraction Calculator", "➗", "Arithmetic & fraction conversion"),
            ("ratio-calculator.html", "Ratio Simplifier", "⚖️", "Irreducible integer proportions"),
        ]
    }
}

def determine_tool_cat(filename):
    f = filename.lower()
    if any(k in f for k in ["bmi", "calorie", "body-fat", "ideal-weight", "water-intake", "bmr", "macro"]):
        return "health"
    if any(k in f for k in ["mortgage", "tip", "loan", "compound", "simple-interest", "discount", "salary", "roi", "rule-of-72"]):
        return "finance"
    if any(k in f for k in ["short-circuit", "transformer", "ohms", "voltage-drop", "resistor", "cable-sizing", "conduit-fill", "motor-starting", "wire-ampacity", "power-factor", "parallel-resistor", "battery-life", "555-timer", "led-resistor", "capacitive-reactance", "inductive-reactance", "op-amp-gain", "three-phase-power", "adc-dac", "antenna-length", "battery-short-circuit", "bjt-transistor", "breaker-size", "decibel", "earth-pit", "electrical-power", "microstrip", "busbar", "fault-current", "filter", "generator", "heatsink", "copper-cable", "earthing", "kw-to-cable", "single-phase", "three-phase", "wire-gauge"]):
        return "engineering"
    if any(k in f for k in ["solar", "charging", "pv-string", "ev-charging"]):
        return "solar"
    if any(k in f for k in ["cooling", "pipe", "torque", "pump-head", "gear-ratio", "bolt-torque", "bearing-life", "belt-length", "conveyor-belt", "cutting-speed", "feed-rate", "flywheel", "gear-module", "heat-exchanger", "hvac", "hydraulic-cylinder", "hydraulic-pump", "power-to-torque", "psychrometric", "pulley", "pump-flow", "reynolds-number", "shaft-diameter", "spring-rate", "thermal-expansion", "torque-converter", "torque-to-hp", "projectile"]):
        return "mechanical"
    if any(k in f for k in ["beam", "retaining", "concrete", "rebar", "brick", "asphalt", "rainwater-downpipe", "block", "drywall", "excavation", "flooring", "footing", "gravel", "paint", "roof-pitch", "slab", "slope"]):
        return "civil"
    if any(k in f for k in ["chemical", "chlorine"]):
        return "chemical"
    if any(k in f for k in ["sprinkler", "smoke", "fire-alarm", "hydrant", "fire-pump", "nac", "strobe"]):
        return "fire"
    if "subnet" in f:
        return "programmer"
    if any(k in f for k in ["date-difference", "age"]):
        return "datetime"
    if "unit" in f:
        return "converter"
    if any(k in f for k in ["percentage", "fraction", "ratio", "gpa", "standard-deviation"]):
        return "math"
    return "math"

def build_sidebar_html(current_file, cat_key):
    cat_data = CATEGORIES[cat_key]
    items_html = []
    for slug, title, icon, desc in cat_data["tools"]:
        is_active = (slug == current_file)
        active_class = " active" if is_active else ""
        items_html.append(f'''            <li><a href="{slug}" class="sidebar-link-item{active_class}"><span class="link-bullet">›</span> {title}</a></li>''')

    tools_list = "\n".join(items_html)

    return f'''      <!-- Related Category Sidebar -->
      <aside class="post-sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <span class="widget-icon">{cat_data["icon"]}</span>
            <h3 class="widget-title">Related {cat_data["name"]}</h3>
          </div>
          <p class="sidebar-widget-subtitle">Specialized calculation tools in this discipline:</p>
          <ul class="sidebar-links-list">
{tools_list}
          </ul>
          <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border-light);">
            <a href="{cat_data["hub"]}" class="sidebar-category-link">View All {cat_data["name"]} Calculators &rarr;</a>
          </div>
        </div>
      </aside>'''

def update_all_sidebars():
    category_pages = set([
        "index.html", "404.html", "health.html", "finance.html", "math.html",
        "engineering.html", "solar-energy.html", "mechanical.html", "civil.html",
        "chemical.html", "fire-safety.html", "programmer.html", "datetime.html", "converter.html"
    ])

    all_html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    tool_files = [f for f in all_html_files if os.path.basename(f) not in category_pages]

    print(f"Applying updated sidebars across {len(tool_files)} tool pages...")
    updated_count = 0

    # Pattern for existing sidebar
    sidebar_regex = re.compile(r'<!--\s*(?:Related Category Sidebar|Post Sidebar)\s*-->\s*<aside class="post-sidebar"[^>]*>.*?</aside>', re.DOTALL | re.IGNORECASE)

    for file_path in tool_files:
        filename = os.path.basename(file_path)
        cat_key = determine_tool_cat(filename)
        new_sidebar = build_sidebar_html(filename, cat_key)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if sidebar_regex.search(content):
            content = sidebar_regex.sub(lambda m: new_sidebar, content)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            updated_count += 1
        elif '<aside class="post-sidebar"' in content:
            alt_regex = re.compile(r'<aside class="post-sidebar"[^>]*>.*?</aside>', re.DOTALL | re.IGNORECASE)
            content = alt_regex.sub(lambda m: new_sidebar, content)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            updated_count += 1
        elif '<aside class="calc-sidebar"' in content:
            calc_regex = re.compile(r'<aside class="calc-sidebar"[^>]*>.*?</aside>', re.DOTALL | re.IGNORECASE)
            content = calc_regex.sub(lambda m: new_sidebar, content)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            updated_count += 1

    print(f"Successfully updated sidebars across {updated_count} tool pages!")

if __name__ == "__main__":
    update_all_sidebars()
