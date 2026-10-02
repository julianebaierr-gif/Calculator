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
            ("bmi-calculator.html", "BMI Calculator", "⚖️", "Body mass index & classification"),
            ("calorie-calculator.html", "Calorie Calculator (TDEE)", "🔥", "BMR & daily caloric maintenance"),
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
            ("loan-emi-calculator.html", "Loan EMI Calculator", "💳", "Monthly payment & interest split"),
            ("car-loan-calculator.html", "Car Loan Financing", "🚗", "Auto loan payments & trade-in tax"),
            ("mortgage-calculator.html", "Mortgage & PITI", "🏡", "Monthly payment, escrow & amortization"),
            ("roi-calculator.html", "ROI & Annualized CAGR", "📈", "Net capital gain & geometric CAGR"),
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
            ("conduit-fill-calculator.html", "Conduit Fill (NEC Ch. 9)", "🔌", "40% fill rule & wire jam ratio"),
            ("motor-starting-current-calculator.html", "Motor Starting Current", "⚙️", "NEMA locked rotor inrush amps"),
            ("short-circuit-calculator.html", "Short-Circuit (IEC 60909)", "💥", "Symmetrical fault kA & breaking"),
            ("transformer-sizing-calculator.html", "Transformer Sizing (NEC 450)", "⚡", "kVA rating & full-load amps"),
            ("cable-sizing-calculator.html", "Cable Sizing (IEC/NEC)", "🔌", "IEC/NEC ampacity & derating"),
            ("voltage-drop-calculator.html", "Voltage Drop Calculator", "📉", "NEC 3% & 5% copper/aluminum run"),
            ("ohms-law-calculator.html", "Ohm's Law Calculator", "⚡", "Voltage, current, power & ohms"),
            ("resistor-color-code-calculator.html", "Resistor Color Code", "🎨", "4 & 5-band axial resistance"),
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
            ("ev-charging-time-calculator.html", "EV Charging Time & Power", "🔌", "Levels 1, 2 & DC Fast charge time"),
        ]
    },
    "mechanical": {
        "name": "Mechanical & HVAC",
        "icon": "⚙️",
        "hub": "mechanical.html",
        "tools": [
            ("pump-head-calculator.html", "Pump Head (TDH & Flow)", "🌊", "Total dynamic head & motor BHP"),
            ("gear-ratio-calculator.html", "Gear Ratio & Speed", "⚙️", "Velocity reduction & torque ratio"),
            ("cooling-load-calculator.html", "Cooling Load (HVAC) Sizing", "❄️", "Sensible & latent heat in BTU/hr"),
            ("pipe-sizing-calculator.html", "Pipe Sizing & Water Flow", "🚰", "Internal diameter & friction loss"),
            ("torque-calculator.html", "Torque & Shaft Power", "⚙️", "Rotational torque N·m & kW/HP"),
        ]
    },
    "civil": {
        "name": "Civil & Construction",
        "icon": "🏗️",
        "hub": "civil.html",
        "tools": [
            ("beam-deflection-calculator.html", "Beam Deflection & Moments", "📐", "AISC 360 deflection & moment"),
            ("retaining-wall-calculator.html", "Retaining Wall Stability", "🧱", "Rankine earth pressure & overturning"),
            ("concrete-calculator.html", "Concrete Slab, Footing & Column", "🏗️", "Wet concrete m³ & cement bags"),
            ("rebar-calculator.html", "Rebar Weight & Grid Spacing", "🔩", "Cut bar counts & linear mass kg/lbs"),
        ]
    },
    "chemical": {
        "name": "Chemical & Water Treatment",
        "icon": "🧪",
        "hub": "chemical.html",
        "tools": [
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
            ("fire-sprinkler-calculator.html", "Fire Sprinkler Hydraulics", "💦", "NFPA 13 head flow Q=K√P & demand"),
            ("smoke-detector-spacing-calculator.html", "Smoke Detector Spacing & Layout", "🚨", "NFPA 72 ceiling height derating"),
            ("cable-sizing-calculator.html", "Cable Sizing (IEC/NEC)", "🔌", "Fire alarm circuit conductor gauge"),
            ("voltage-drop-calculator.html", "Voltage Drop Calculator", "📉", "Alarm notification appliance circuit"),
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
    if any(k in f for k in ["bmi", "calorie", "body-fat", "ideal-weight", "water-intake"]):
        return "health"
    if any(k in f for k in ["mortgage", "tip", "loan", "compound", "simple-interest", "discount", "salary"]):
        return "finance"
    if any(k in f for k in ["short-circuit", "transformer", "ohms", "voltage-drop", "resistor", "cable-sizing"]):
        return "engineering"
    if any(k in f for k in ["solar", "charging"]):
        return "solar"
    if any(k in f for k in ["cooling", "pipe", "torque"]):
        return "mechanical"
    if any(k in f for k in ["beam", "retaining", "concrete", "rebar"]):
        return "civil"
    if "chemical" in f:
        return "chemical"
    if any(k in f for k in ["sprinkler", "smoke"]):
        return "fire"
    if "subnet" in f:
        return "programmer"
    if any(k in f for k in ["date-difference", "age"]):
        return "datetime"
    if "unit" in f:
        return "converter"
    if any(k in f for k in ["percentage", "fraction", "ratio", "gpa"]):
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

    sidebar_regex = re.compile(r'<!-- Related Category Sidebar -->\s*<aside class="post-sidebar">.*?</aside>', re.DOTALL)

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

    print(f"Successfully updated sidebars across {updated_count} tool pages!")

if __name__ == "__main__":
    update_all_sidebars()
