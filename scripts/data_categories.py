"""
Data definitions for the 8 new Category Hub pages.
"""

NEW_CATEGORIES = [
    {
        "slug": "solar-energy.html",
        "title": "Solar & Renewable Energy Calculators",
        "icon": "☀️",
        "accent_color": "#D97706",
        "badge": "IEC 61215 & NEC 690",
        "meta_desc": "Free industrial solar and renewable energy calculators. Size solar photovoltaic arrays, calculate battery storage Ah/kWh, size inverters, and estimate EV charging duration.",
        "overview": "Clean energy system engineering requires precise matching of solar photovoltaic generation, battery storage kinetics, and inverter duty ratings to prevent blackout brownouts.",
        "tools": [
            ("solar-panel-sizing-calculator.html", "Solar Panel & Battery Sizing", "☀️", "PV & Battery Bank", "Calculate array wattage, panel counts, and battery bank storage based on peak sun hours."),
            ("solar-battery-bank-calculator.html", "Solar Battery Bank Sizing", "🔋", "IEC 61427 & IEEE 1013", "Size battery storage in Ah and kWh for off-grid autonomy and cycle life protection."),
            ("solar-inverter-sizing-calculator.html", "Solar Inverter Sizing", "⚡", "NEC 690 & IEC 62109", "Calculate continuous inverter kVA and inductive motor starting surge capacity."),
            ("ev-charging-time-calculator.html", "EV Charging Time & Power", "🔌", "SAE J1772 & IEC 61851", "Estimate exact hours and minutes to charge electric vehicles across Levels 1, 2, and DC Fast.")
        ]
    },
    {
        "slug": "mechanical.html",
        "title": "Mechanical & HVAC Calculators",
        "icon": "⚙️",
        "badge": "ASHRAE & ASME Standards",
        "meta_desc": "Free precision mechanical engineering and HVAC calculators. Calculate room cooling loads (BTU/hr & TR), water pipe sizing, total dynamic pump head, and rotational shaft torque.",
        "overview": "Thermodynamics and fluid dynamics govern modern building environmental control and industrial powertrain machinery.",
        "tools": [
            ("cooling-load-calculator.html", "Cooling Load (HVAC) Sizing", "❄️", "ASHRAE Standard 183", "Calculate sensible and latent heat gains in BTU/hr and Refrigeration Tons (TR)."),
            ("pipe-sizing-calculator.html", "Pipe Sizing & Water Flow", "🚰", "ASME B31 & Darcy", "Determine internal pipe diameter, fluid velocity, and pressure drop per 100 meters."),
            ("torque-calculator.html", "Torque & Shaft Power", "⚙️", "ISO 80000 & DIN 743", "Convert force, radius, and RPM into rotational torque (N·m / lbf·ft) and mechanical power (kW / HP).")
        ]
    },
    {
        "slug": "civil.html",
        "title": "Civil & Construction Calculators",
        "icon": "🏗️",
        "badge": "ACI 318 & Eurocode Standards",
        "meta_desc": "Free civil engineering and structural construction calculators. Estimate concrete slab volume (m³ & yd³), cement bags, rebar grid weight, and structural loads.",
        "overview": "Structural safety and cost efficiency depend upon accurate material takeoff estimation and mechanical load distribution.",
        "tools": [
            ("concrete-calculator.html", "Concrete Slab, Footing & Column", "🏗️", "ACI 318 & BS EN 206", "Calculate wet concrete volume in m³ and yards³, plus 50kg cement bags, sand, and gravel quantities."),
            ("rebar-calculator.html", "Rebar Weight & Grid Spacing", "🔩", "ASTM A615 & Eurocode 2", "Calculate reinforcing steel linear length, cut bar counts, and total mass in kg and lbs.")
        ]
    },
    {
        "slug": "chemical.html",
        "title": "Chemical & Water Treatment Calculators",
        "icon": "🧪",
        "badge": "AWWA & EPA Standards",
        "meta_desc": "Free chemical engineering and water treatment calculators. Calculate chemical dosing pump feed rates in LPH, solution ppm, and reaction molarity.",
        "overview": "Safe municipal potable water disinfection and industrial effluent remediation require rigorous stoichiometric and mass balance calculations.",
        "tools": [
            ("chemical-dosing-calculator.html", "Chemical Dosing Rate Calculator", "🧪", "AWWA & EPA Standards", "Calculate chemical feed rate in kg/day and positive displacement pump stroke flow in L/hr.")
        ]
    },
    {
        "slug": "fire-safety.html",
        "title": "Fire & Life Safety Calculators",
        "icon": "🚨",
        "badge": "NFPA 72 & Life Safety Codes",
        "meta_desc": "Free fire protection and life safety engineering calculators. Calculate smoke detector spacing with ceiling height derating factors according to NFPA 72.",
        "overview": "Life safety systems provide early detection and egress notification during hazardous smoldering and flaming fire events.",
        "tools": [
            ("smoke-detector-spacing-calculator.html", "Smoke Detector Spacing & Layout", "🚨", "NFPA 72 & EN 54-7", "Calculate required smoke detector unit counts and grid spacing with ceiling height derating.")
        ]
    },
    {
        "slug": "programmer.html",
        "title": "Programmer & Networking Calculators",
        "icon": "👨‍💻",
        "badge": "RFC 1878 & IEEE Standards",
        "meta_desc": "Free computer science and network engineering calculators. Calculate IPv4 subnets, CIDR prefix masks, network/broadcast IDs, and usable host address ranges.",
        "overview": "Binary mathematics and discrete network address partitioning form the technical foundation of the global internet protocol architecture.",
        "tools": [
            ("subnet-calculator.html", "IPv4 Subnet & CIDR IP Calculator", "🌐", "RFC 1878 & IEEE 802.3", "Calculate network ID, broadcast address, dotted subnet mask, and usable host count from CIDR prefix.")
        ]
    },
    {
        "slug": "datetime.html",
        "title": "Date & Time Utility Calculators",
        "icon": "📅",
        "badge": "ISO 8601 Calendar Standard",
        "meta_desc": "Free Gregorian calendar and date duration calculators. Calculate exact days between dates, working business days (excluding weekends), weeks, and months.",
        "overview": "Calendar mathematics calculates precise elapsed intervals across quadrennial leap years and irregular month lengths for project management and legal contracts.",
        "tools": [
            ("date-difference-calculator.html", "Date Difference & Business Days", "📅", "ISO 8601 Calendar", "Calculate exact days, working business days (excluding weekends), full weeks, and percentage of year.")
        ]
    },
    {
        "slug": "converter.html",
        "title": "Universal Unit Converters",
        "icon": "🔄",
        "badge": "BIPM & NIST SI Metric",
        "meta_desc": "Free universal engineering and physical unit converter. Convert length, mass/weight, temperature, pressure, area, and volume across SI metric and imperial units.",
        "overview": "Accurate dimensional analysis translates physical quantities between metric SI standards and US Customary engineering measurements.",
        "tools": [
            ("unit-converter.html", "Universal Multi-Unit Converter", "🔄", "NIST & BIPM SI Units", "Convert length, mass, temperature, pressure, and volume with international precision coefficients.")
        ]
    }
]
