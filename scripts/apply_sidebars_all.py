import glob
import re

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
            ("compound-interest-calculator.html", "Compound Interest", "📈", "Wealth growth with deposits"),
            ("simple-interest-calculator.html", "Simple Interest", "💵", "Linear interest & maturity sum"),
            ("discount-calculator.html", "Discount & Sale", "🏷️", "Net savings, coupons & sales tax"),
            ("salary-calculator.html", "Salary & Paycheck", "💼", "Hourly, monthly & annual pay"),
        ]
    },
    "math": {
        "name": "Mathematics & Utilities",
        "icon": "🔢",
        "hub": "math.html",
        "tools": [
            ("percentage-calculator.html", "Percentage Calculator", "％", "Portions, discounts & % change"),
            ("age-calculator.html", "Exact Age Calculator", "🎂", "Chronological age & milestones"),
            ("gpa-calculator.html", "College GPA Calculator", "🎓", "4.0 scale cumulative GPA"),
            ("fraction-calculator.html", "Fraction Calculator", "➗", "Add, multiply & simplify fractions"),
            ("ratio-calculator.html", "Ratio Simplifier", "⚖️", "Euclid's GCD ratio reduction"),
        ]
    },
    "engineering": {
        "name": "Electrical & Power Systems",
        "icon": "⚡",
        "hub": "engineering.html",
        "tools": [
            ("ohms-law-calculator.html", "Ohm's Law Calculator", "⚡", "Voltage, current, power & ohms"),
            ("voltage-drop-calculator.html", "Voltage Drop Calculator", "📉", "NEC 3% & 5% copper/aluminum run"),
            ("cable-sizing-calculator.html", "Cable Sizing (IEC/NEC)", "🔌", "IEC/NEC ampacity & derating"),
            ("resistor-color-code-calculator.html", "Resistor Color Code", "🎨", "4 & 5-band axial resistance"),
            ("solar-panel-sizing-calculator.html", "Solar Panel & Array", "☀️", "Array watts & peak sun hours"),
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
            ("concrete-calculator.html", "Concrete Slab, Footing & Column", "🏗️", "Wet concrete m³ & cement bags"),
            ("rebar-calculator.html", "Rebar Weight & Grid Spacing", "🔩", "Cut bar counts & linear mass kg/lbs"),
            ("pipe-sizing-calculator.html", "Pipe Sizing & Water Flow", "🚰", "Internal diameter & friction loss"),
            ("cable-sizing-calculator.html", "Cable Sizing (IEC/NEC)", "🔌", "Underground utility conductor run"),
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
            ("concrete-calculator.html", "Concrete Basin & Slab Volume", "🏗️", "Wet concrete m³ & cement bags"),
        ]
    },
    "fire": {
        "name": "Fire & Life Safety",
        "icon": "🚨",
        "hub": "fire-safety.html",
        "tools": [
            ("smoke-detector-spacing-calculator.html", "Smoke Detector Spacing & Layout", "🚨", "NFPA 72 ceiling height derating"),
            ("cable-sizing-calculator.html", "Cable Sizing (IEC/NEC)", "🔌", "Fire alarm circuit conductor gauge"),
            ("voltage-drop-calculator.html", "Voltage Drop Calculator", "📉", "Alarm notification appliance circuit"),
            ("subnet-calculator.html", "IPv4 Subnet & CIDR IP", "🌐", "Building management network IP"),
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
    if "health" in f or "bmi" in f or "calorie" in f or "body-fat" in f or "ideal-weight" in f or "water-intake" in f:
        return "health"
    if "finance" in f or "loan" in f or "compound" in f or "interest" in f or "discount" in f or "salary" in f:
        return "finance"
    if "solar" in f or "charging" in f:
        return "solar"
    if "mechanical" in f or "cooling" in f or "pipe" in f or "torque" in f:
        return "mechanical"
    if "civil" in f or "concrete" in f or "rebar" in f or "brick" in f or "beam" in f:
        return "civil"
    if "chemical" in f:
        return "chemical"
    if "fire" in f or "smoke" in f:
        return "fire"
    if "programmer" in f or "subnet" in f:
        return "programmer"
    if "date" in f or "time" in f:
        return "datetime"
    if "converter" in f or "unit" in f:
        return "converter"
    if "engineering" in f or "ohms" in f or "voltage" in f or "cable" in f or "resistor" in f:
        return "engineering"
    if "math" in f or "percentage" in f or "age" in f or "gpa" in f or "fraction" in f or "ratio" in f:
        return "math"
    return "math"

def build_sidebar_html(current_file, cat_key):
    cat = CATEGORIES[cat_key]
    items_html = []
    for href, title, icon, desc in cat["tools"]:
        if href == current_file:
            items_html.append(f"""          <div class="sidebar-tool-item active">
            <span class="st-icon">{icon}</span>
            <div class="st-info">
              <span class="st-title">{title}</span>
              <span class="st-tag">Current Tool</span>
            </div>
          </div>""")
        else:
            items_html.append(f"""          <a href="{href}" class="sidebar-tool-item">
            <span class="st-icon">{icon}</span>
            <div class="st-info">
              <span class="st-title">{title}</span>
              <span class="st-desc">{desc}</span>
            </div>
          </a>""")
    
    tools_str = "\n".join(items_html)

    return f"""      <!-- Related Category Sidebar -->
      <aside class="post-sidebar">
        <div class="sidebar-widget">
          <div class="sidebar-widget-header">
            <span class="widget-icon">{cat['icon']}</span>
            <h3 class="widget-title">Related {cat['name']}</h3>
          </div>
          <p class="sidebar-widget-subtitle">Specialized calculation tools in this discipline:</p>
          <div class="sidebar-tools-list">
{tools_str}
          </div>
          <div class="sidebar-widget-footer">
            <a href="{cat['hub']}" class="sidebar-cat-link">
              Explore All {cat['name']} &rarr;
            </a>
          </div>
        </div>

        <div class="sidebar-widget sidebar-trust-widget">
          <div class="trust-badge-row">
            <span class="trust-icon">🛡️</span>
            <div>
              <div class="trust-title">Verified Standards</div>
              <div class="trust-desc">Client-side precision execution · Zero tracking · Standards verified.</div>
            </div>
          </div>
        </div>
      </aside>"""

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    cat_key = determine_tool_cat(filepath)
    sidebar_html = build_sidebar_html(filepath, cat_key)

    # 1. Find the end of calculator-workspace
    m_start = re.search(r'<([a-z0-9]+)[^>]*class=["\'][^"\']*calculator-workspace[^"\']*["\'][^>]*>', content, re.IGNORECASE)
    if not m_start:
        print(f"Skipping {filepath}: no calculator-workspace")
        return False
    start_pos = m_start.start()
    tag_name = m_start.group(1)

    open_count = 0
    end_pos = -1
    tag_regex = re.compile(rf'</?{tag_name}\b[^>]*>', re.IGNORECASE)
    for tm in tag_regex.finditer(content, start_pos):
        tag_str = tm.group(0)
        if tag_str.startswith('</'):
            open_count -= 1
            if open_count == 0:
                end_pos = tm.end()
                break
        else:
            open_count += 1

    if end_pos == -1:
        print(f"Error finding end of workspace in {filepath}")
        return False

    prefix = content[:end_pos]
    suffix_start = content[end_pos:]
    main_end_rel = suffix_start.find('</main>')
    if main_end_rel == -1:
        print(f"Error finding </main> in {filepath}")
        return False

    between = suffix_start[:main_end_rel]
    rest_of_file = suffix_start[main_end_rel:]

    # 2. Remove any old related section at the bottom
    old_related_pattern = re.compile(r'(?:<!--\s*Related Topic Silos\s*-->\s*)?<section>\s*<h2[^>]*>Related[^<]*</h2>\s*<div class="silo-card-grid">.*?</div>\s*</section>', re.DOTALL | re.IGNORECASE)
    clean_between = old_related_pattern.sub('', between).strip()

    # If it was already wrapped in post-layout-grid, clean it
    if 'post-layout-grid' in clean_between:
        # Extract main content and sidebar
        m_main = re.search(r'<div class="post-main-content">(.*?)</div>\s*<!-- Related Category Sidebar -->', clean_between, re.DOTALL)
        if m_main:
            clean_between = m_main.group(1).strip()

    # 3. Assemble new content
    new_middle = f"""

    <!-- Post Body with Dedicated Related Sidebar -->
    <div class="post-layout-grid">
      <div class="post-main-content">
        {clean_between}
      </div>

{sidebar_html}
    </div>
  """

    new_content = prefix + new_middle + rest_of_file

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True

def main():
    tools = [f for f in glob.glob('*.html') if f not in [
        'index.html', '404.html', 'health.html', 'finance.html', 'math.html',
        'engineering.html', 'solar-energy.html', 'mechanical.html', 'civil.html',
        'chemical.html', 'fire-safety.html', 'programmer.html', 'datetime.html',
        'converter.html'
    ]]

    print(f"Processing sidebars across {len(tools)} calculator tools...")
    success_count = 0
    for t in tools:
        if process_file(t):
            success_count += 1
            print(f"  [OK] {t} ({determine_tool_cat(t)})")
        else:
            print(f"  [FAIL] {t}")

    print(f"\nSuccessfully updated sidebars in {success_count}/{len(tools)} tools!")

if __name__ == "__main__":
    main()
