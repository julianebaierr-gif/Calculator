"""
Data definition for Solar and Mechanical Engineering calculators.
"""

SOLAR_MECHANICAL_TOOLS = [
    # 1. Solar Battery Bank
    {
        "slug": "solar-battery-bank-calculator.html",
        "title": "Solar Battery Bank Sizing Calculator",
        "category": "Solar & Renewable Energy",
        "cat_slug": "solar-energy.html",
        "icon": "🔋",
        "badge": "IEC 61427 & IEEE 1013",
        "meta_desc": "Calculate solar battery bank capacity in Amp-hours (Ah) and kilowatt-hours (kWh) based on daily energy consumption, days of autonomy, system voltage, and battery Depth of Discharge (DoD).",
        "keywords": "solar battery bank calculator, battery capacity ah calculator, solar storage sizing, lifepo4 battery sizing, days of autonomy calculator",
        "formula_preview": "Ah = (Daily Wh × Days) / (V_sys × DoD × η)",
        "inputs": [
            {"id": "daily_wh", "label": "Daily Energy Consumption", "type": "number", "unit": "Wh / day", "default": "4500", "min": "100", "max": "100000", "step": "50"},
            {"id": "autonomy_days", "label": "Days of Autonomy (Backup Days)", "type": "number", "unit": "days", "default": "2", "min": "1", "max": "10", "step": "0.5"},
            {"id": "sys_voltage", "label": "System Voltage", "type": "select", "options": [("12", "12 V (Small Off-Grid / RV)"), ("24", "24 V (Medium Cabin / Marine)"), ("48", "48 V (Standard Residential ESS)")], "default": "48"},
            {"id": "dod", "label": "Battery Chemistry & Max DoD", "type": "select", "options": [("0.50", "Lead-Acid / AGM / Gel (50% DoD)"), ("0.80", "Lithium LiFePO4 (80% DoD)"), ("0.90", "Premium LiFePO4 (90% DoD)")], "default": "0.80"},
            {"id": "temp_derating", "label": "Ambient Temperature Derating", "type": "select", "options": [("1.0", "Warm / Room Temp (25°C / 77°F) — 1.0"), ("0.85", "Moderate Cold (10°C / 50°F) — 0.85"), ("0.70", "Freezing (0°C / 32°F) — 0.70")], "default": "1.0"}
        ],
        "calc_js": """
            const wh = parseFloat(document.getElementById('daily_wh').value) || 0;
            const days = parseFloat(document.getElementById('autonomy_days').value) || 1;
            const v = parseFloat(document.getElementById('sys_voltage').value) || 48;
            const dod = parseFloat(document.getElementById('dod').value) || 0.8;
            const temp = parseFloat(document.getElementById('temp_derating').value) || 1.0;
            const inverterEff = 0.90; // Standard 90% inverter efficiency

            const requiredWh = (wh * days) / (inverterEff * dod * temp);
            const totalAh = requiredWh / v;
            const totalKwh = requiredWh / 1000;
            const usableKwh = (wh * days) / 1000;

            document.getElementById('prim-val').textContent = Math.round(totalAh) + ' Ah';
            document.getElementById('prim-unit').textContent = '@ ' + v + 'V System';
            document.getElementById('m-kwh').textContent = totalKwh.toFixed(2) + ' kWh';
            document.getElementById('m-usable').textContent = usableKwh.toFixed(2) + ' kWh';
            document.getElementById('m-dod').textContent = (dod * 100).toFixed(0) + '%';
            document.getElementById('m-cells100').textContent = Math.ceil(totalAh / 100) + ' units (100Ah)';
        """,
        "metrics": [
            ("m-kwh", "Total Nameplate Capacity", "kWh"),
            ("m-usable", "Usable Energy Required", "kWh"),
            ("m-dod", "Assumed DoD Limit", "%"),
            ("m-cells100", "Parallel 100Ah Batteries", "Count")
        ],
        "article": {
            "summary": "Sizing an off-grid or hybrid energy storage system requires balancing usable energy requirements, battery chemistry discharge kinetics, and ambient temperature degradation.",
            "principles": "<p>Unlike grid-tied PV systems where surplus energy is net-metered to the utility grid, off-grid and battery backup installations rely exclusively on stored chemical energy during periods of zero irradiance or grid outages. Sizing the battery bank improperly leads to two fatal failure modes: undersizing causes deep cycle depletion that destroys lead-acid or lithium battery cycle life; oversizing introduces excessive capital cost and prevents the array from reaching full absorption charge.</p>",
            "formulas": "<p>The required nominal battery bank capacity in Amp-hours (Ah) is derived from daily energy demand, days of autonomy, depth of discharge limit, and system DC voltage:</p>\\[ C_{Ah} = \\frac{E_{daily} \\times N_{autonomy}}{V_{system} \\times \\text{DoD} \\times \\eta_{inverter} \\times C_{temp}} \\]",
            "table_title": "Battery Chemistry Comparison (IEC 61427 Standards)",
            "table_headers": ["Chemistry Type", "Recommended DoD", "Cycle Life (80% EoL)", "Round-Trip Efficiency", "Self-Discharge Rate"],
            "table_rows": [
                ["Lithium Iron Phosphate (LiFePO4)", "80% – 90%", "3,500 – 6,000 cycles", "95% – 98%", "< 2% / month"],
                ["Absorbent Glass Mat (AGM Lead-Acid)", "50%", "500 – 800 cycles", "80% – 85%", "3% – 5% / month"],
                ["Flooded Lead-Acid (Deep Cycle)", "50%", "1,000 – 1,500 cycles", "75% – 80%", "5% – 10% / month"],
                ["Lithium Nickel Manganese Cobalt (NMC)", "80%", "2,000 – 3,000 cycles", "92% – 95%", "< 3% / month"]
            ],
            "example": "A remote telecom shelter consumes 4,500 Wh per day. The designer specifies 2 days of autonomy on a 48V DC bus utilizing Lithium Iron Phosphate batteries (80% max DoD) at 25°C. Total required gross storage = (4,500 × 2) / (0.90 × 0.80 × 1.0) = 12,500 Wh (12.5 kWh). Dividing by 48V yields 260.4 Ah. Specifying three parallel 48V 100Ah server rack batteries (300 Ah total) satisfies the requirement with safety margin.",
            "faqs": [
                ("What are Days of Autonomy?", "Days of autonomy represent the number of consecutive days a battery bank can supply full load without any solar photovoltaic recharging during heavily overcast or stormy conditions."),
                ("Why is 48V preferred over 12V for residential systems?", "A 48V system reduces current by 75% compared to a 12V system for the same power (P = V × I). Lower current drastically reduces conductor I²R heat losses, cable cross-sectional thickness, and fuse sizing requirements."),
                ("How does cold weather affect battery capacity?", "Cold temperatures increase internal electrolyte resistance. At 0°C (32°F), usable lead-acid capacity drops by approximately 30%, requiring a 0.70 derating factor.")
            ]
        }
    },

    # 2. Solar Inverter Sizing
    {
        "slug": "solar-inverter-sizing-calculator.html",
        "title": "Solar Inverter Sizing Calculator",
        "category": "Solar & Renewable Energy",
        "cat_slug": "solar-energy.html",
        "icon": "⚡",
        "badge": "NEC 690 & IEC 62109",
        "meta_desc": "Calculate continuous inverter capacity (kW/kVA) and surge rating based on total appliance wattage, inductive motor surge multipliers, and power factor.",
        "keywords": "solar inverter sizing calculator, inverter kva calculator, solar inverter capacity, off grid inverter sizing, motor surge wattage",
        "formula_preview": "kVA = (Continuous Watts × Surge Factor) / (1000 × PF)",
        "inputs": [
            {"id": "continuous_watts", "label": "Total Continuous Operating Load", "type": "number", "unit": "Watts (W)", "default": "3200", "min": "100", "max": "50000", "step": "50"},
            {"id": "largest_motor", "label": "Largest Inductive Motor / Compressor", "type": "number", "unit": "Watts (W)", "default": "1000", "min": "0", "max": "10000", "step": "50"},
            {"id": "surge_type", "label": "Motor Starting Surge Multiplier", "type": "select", "options": [("1.25", "Resistive Loads / Electronic (1.25x)"), ("2.0", "Refrigerators & Variable Speed AC (2.0x)"), ("3.0", "Pumps, Well Motors & Compressors (3.0x)")], "default": "3.0"},
            {"id": "power_factor", "label": "System Power Factor (cos φ)", "type": "select", "options": [("0.80", "Industrial / Mixed Inductive (0.80)"), ("0.85", "Standard Residential (0.85)"), ("0.95", "High Efficiency Inverter (0.95)"), ("1.0", "Pure Resistive (1.0)")], "default": "0.85"}
        ],
        "calc_js": """
            const contW = parseFloat(document.getElementById('continuous_watts').value) || 0;
            const motorW = parseFloat(document.getElementById('largest_motor').value) || 0;
            const surgeMult = parseFloat(document.getElementById('surge_type').value) || 2.0;
            const pf = parseFloat(document.getElementById('power_factor').value) || 0.85;

            const nonMotorW = Math.max(0, contW - motorW);
            const peakSurgeW = nonMotorW + (motorW * surgeMult);
            const continuousKva = (contW * 1.25) / (1000 * pf); // 125% continuous duty rule NEC
            const surgeKva = peakSurgeW / (1000 * pf);
            const recommendedKw = Math.ceil(continuousKva * pf * 1.1);

            document.getElementById('prim-val').textContent = continuousKva.toFixed(2) + ' kVA';
            document.getElementById('prim-unit').textContent = '(' + recommendedKw + ' kW Continuous Inverter)';
            document.getElementById('m-surge-w').textContent = Math.round(peakSurgeW) + ' W';
            document.getElementById('m-surge-kva').textContent = surgeKva.toFixed(2) + ' kVA';
            document.getElementById('m-nec-rule').textContent = '+25% Continuous';
            document.getElementById('m-dc-input').textContent = Math.round(contW / 0.92) + ' W DC';
        """,
        "metrics": [
            ("m-surge-w", "Peak Startup Surge Load", "Watts"),
            ("m-surge-kva", "Surge Apparent Power", "kVA"),
            ("m-nec-rule", "NEC Safety Headroom", "Rule 690.8"),
            ("m-dc-input", "Required PV/Battery Input", "Watts")
        ],
        "article": {
            "summary": "Inverter sizing establishes the power bridge between direct current (DC) photovoltaic generation and alternating current (AC) domestic and industrial consumer circuits.",
            "principles": "<p>Inverters convert DC voltage from solar arrays or battery banks into single-phase (120V/230V) or three-phase (400V/480V) AC power. The inverter must satisfy two distinct electrical criteria simultaneously: it must support the maximum continuous steady-state wattage of running appliances without overheating (NEC Article 690 requires a 125% safety continuous duty rating), and it must provide instantaneous Locked Rotor Amperage (LRA) surge capability to start inductive motors and compressors.</p>",
            "formulas": "<p>The continuous apparent power rating in kVA and peak surge demands are evaluated as follows:</p>\\[ S_{continuous} = \\frac{P_{continuous} \\times 1.25}{1000 \\times \\text{PF}} \\]\\[ P_{surge} = P_{base} + (P_{motor} \\times K_{surge}) \\]",
            "table_title": "Appliance Surge Multiplier Factors",
            "table_headers": ["Appliance / Equipment", "Running Watts", "Starting Surge Multiplier", "Typical Power Factor"],
            "table_rows": [
                ["Submersible Water Well Pump", "1,500 W", "3.0x – 4.0x", "0.75 – 0.85"],
                ["Central Air Conditioner (Scroll)", "3,500 W", "2.5x – 3.5x", "0.85"],
                ["Refrigerator / Freezer", "200 W", "2.5x – 3.0x", "0.80"],
                ["Microwave Oven", "1,200 W", "1.25x – 1.5x", "0.90"],
                ["LED Lighting & Electronics", "300 W", "1.0x – 1.1x", "0.95 – 1.0"]
            ],
            "example": "A household operates 2,200W of lighting, refrigeration, and electronics, plus a 1,000W well pump (3x starting surge). Continuous load = 3,200W. Applying NEC 125% continuous margin gives 4,000W. At 0.85 power factor, minimum continuous inverter rating = 4,000 / (1,000 × 0.85) = 4.7 kVA (a standard 5.0 kVA / 5 kW pure sine wave inverter). Peak surge requirement = 2,200W + (1,000 × 3) = 5,200W, which a quality 5kW inverter (providing 200% surge for 5 seconds) comfortably satisfies.",
            "faqs": [
                ("What is the difference between pure sine wave and modified sine wave?", "Pure sine wave inverters replicate utility grid electricity with total harmonic distortion (THD) under 3%, essential for motors, medical devices, and compressors. Modified sine wave square waves cause motor hum, overheating, and electronics failure."),
                ("What is the DC-to-AC Inverter Loading Ratio (ILR)?", "The Inverter Loading Ratio (or DC oversizing ratio) is the total DC solar array capacity divided by the AC inverter rating. Modern arrays commonly utilize an ILR of 1.15 to 1.30 to maximize energy capture during early morning and late afternoon without clipping peak noon power."),
                ("Why does power factor affect inverter sizing?", "Inverters are limited by thermal current capacity. Inductive loads introduce reactive current (VARs) that increases apparent power (kVA) without producing useful work, requiring a larger kVA-rated inverter.")
            ]
        }
    },

    # 3. EV Charging Time Calculator
    {
        "slug": "ev-charging-time-calculator.html",
        "title": "EV Charging Time & Power Calculator",
        "category": "Solar & Renewable Energy",
        "cat_slug": "solar-energy.html",
        "icon": "🔌",
        "badge": "SAE J1772 & IEC 61851",
        "meta_desc": "Calculate electric vehicle charging duration in hours and minutes across Level 1, Level 2, and DC Fast charging stations based on battery usable capacity and charging efficiency.",
        "keywords": "ev charging time calculator, electric car charge time, level 2 ev charger speed, kwh charging calculator, battery charge duration",
        "formula_preview": "Time (hrs) = [Capacity × (Target% - Current%)] / (Power × η)",
        "inputs": [
            {"id": "battery_kwh", "label": "EV Battery Usable Capacity", "type": "number", "unit": "kWh", "default": "75", "min": "10", "max": "200", "step": "1"},
            {"id": "start_soc", "label": "Starting State of Charge (SoC)", "type": "number", "unit": "%", "default": "20", "min": "0", "max": "99", "step": "1"},
            {"id": "target_soc", "label": "Target State of Charge (SoC)", "type": "number", "unit": "%", "default": "80", "min": "1", "max": "100", "step": "1"},
            {"id": "charger_power", "label": "Charging Power & Speed Level", "type": "select", "options": [
                ("1.4", "Level 1 AC (120V, 12A) — 1.4 kW"),
                ("3.6", "Level 2 AC Slow (230V, 16A) — 3.6 kW"),
                ("7.2", "Level 2 AC Home Standard (240V, 30A) — 7.2 kW"),
                ("11.0", "Level 2 AC 3-Phase (400V, 16A) — 11.0 kW"),
                ("22.0", "Level 2 AC Commercial (400V, 32A) — 22.0 kW"),
                ("50.0", "DC Fast Charger Level 3 — 50 kW"),
                ("150.0", "Ultra-Fast DC HPC — 150 kW")
            ], "default": "7.2"},
            {"id": "efficiency", "label": "Charging Efficiency", "type": "select", "options": [("0.90", "Typical AC Level 2 (90%)"), ("0.85", "Level 1 Slow AC (85%)"), ("0.94", "High-Voltage DC Fast (94%)")], "default": "0.90"}
        ],
        "calc_js": """
            const cap = parseFloat(document.getElementById('battery_kwh').value) || 75;
            const start = parseFloat(document.getElementById('start_soc').value) || 0;
            const end = parseFloat(document.getElementById('target_soc').value) || 80;
            const power = parseFloat(document.getElementById('charger_power').value) || 7.2;
            const eff = parseFloat(document.getElementById('efficiency').value) || 0.90;

            const deltaPercent = Math.max(0, (end - start) / 100);
            const energyNeeded = cap * deltaPercent;
            const effectivePower = power * eff;
            const hoursDecimal = energyNeeded / effectivePower;

            const hrs = Math.floor(hoursDecimal);
            const mins = Math.round((hoursDecimal - hrs) * 60);

            document.getElementById('prim-val').textContent = hrs + 'h ' + mins + 'm';
            document.getElementById('prim-unit').textContent = 'to reach ' + end + '% SoC';
            document.getElementById('m-energy').textContent = energyNeeded.toFixed(1) + ' kWh';
            document.getElementById('m-drawn').textContent = (energyNeeded / eff).toFixed(1) + ' kWh';
            document.getElementById('m-miles').textContent = '+' + Math.round(energyNeeded * 3.5) + ' mi';
            document.getElementById('m-rate').textContent = (effectivePower / cap * 100).toFixed(1) + '% / hr';
        """,
        "metrics": [
            ("m-energy", "Net Battery Energy Added", "kWh"),
            ("m-drawn", "Total Grid Energy Drawn", "kWh"),
            ("m-miles", "Estimated Range Added (~3.5mi/kWh)", "Miles"),
            ("m-rate", "Charging Speed Rate", "% SoC / hr")
        ],
        "article": {
            "summary": "Electric vehicle charging duration depends directly on battery pack capacity, state-of-charge delta, on-board charger (OBC) throughput, and grid conversion efficiency.",
            "principles": "<p>When charging an electric vehicle with alternating current (AC Level 1 or Level 2), the electrical grid supplies AC power to the vehicle's internal On-Board Charger (OBC), which rectifies AC into DC power to charge the battery cells. In DC fast charging (Level 3), high-voltage direct current bypasses the OBC and flows directly into the traction battery pack under BMS thermal surveillance.</p>",
            "formulas": "<p>Charging duration is calculated from the energy differential divided by the effective charging power:</p>\\[ \\Delta E = C_{battery} \\times \\left(\\frac{\\text{SoC}_{target} - \\text{SoC}_{current}}{100}\\right) \\]\\[ t_{charge} = \\frac{\\Delta E}{P_{charger} \\times \\eta_{charging}} \\]",
            "table_title": "EV Charging Standard Specifications (SAE J1772 & IEC)",
            "table_headers": ["Charging Level", "Voltage / Phase", "Max Current", "Typical Power", "Range Added / Hour"],
            "table_rows": [
                ["Level 1 AC", "120V Single-Phase", "12A – 16A", "1.4 kW – 1.9 kW", "3 – 5 miles (5 – 8 km)"],
                ["Level 2 AC (Home)", "240V Split-Phase", "32A – 48A", "7.2 kW – 11.5 kW", "25 – 40 miles (40 – 65 km)"],
                ["Level 2 AC (3-Phase)", "400V 3-Phase", "16A – 32A", "11.0 kW – 22.0 kW", "40 – 75 miles (65 – 120 km)"],
                ["DC Fast Charging (CCS/NACS)", "400V – 800V DC", "125A – 350A", "50 kW – 250 kW", "150 – 250 miles in 20 min"]
            ],
            "example": "A Tesla Model 3 Long Range with a 75 kWh battery charges from 20% to 80% State of Charge (60% delta = 45 kWh added). Connected to a standard 240V 30A Level 2 home wall connector delivering 7.2 kW at 90% AC-to-DC conversion efficiency (effective power = 6.48 kW). Total charging time = 45 kWh / 6.48 kW = 6.94 hours (6 hours and 56 minutes).",
            "faqs": [
                ("Why does DC fast charging slow down after 80% SoC?", "Lithium-ion cells cannot absorb high current at high voltages without lithium plating on the anode, which causes permanent cell degradation and fire hazards. The Battery Management System (BMS) automatically tapers current significantly once SoC reaches 80%."),
                ("What is charging efficiency loss?", "Between 10% and 15% of grid electrical energy is lost as heat in the charging cable, on-board rectifier, and battery electrochemical conversion."),
                ("Can any EV charge at 22 kW AC?", "No. Most North American EVs feature an on-board charger limited to 7.7 kW to 11.5 kW single-phase. European 3-phase vehicles can charge at 11 kW or 22 kW if equipped with optional dual OBCs.")
            ]
        }
    },

    # 4. Cooling Load HVAC
    {
        "slug": "cooling-load-calculator.html",
        "title": "Cooling Load (HVAC) Calculator",
        "category": "Mechanical & HVAC",
        "cat_slug": "mechanical.html",
        "icon": "❄️",
        "badge": "ASHRAE Standard 183",
        "meta_desc": "Calculate total HVAC cooling load capacity in BTU/hr and Refrigeration Tonnage (TR) based on room dimensions, occupant density, window solar gain, and equipment heat.",
        "keywords": "cooling load calculator, hvac tonnage calculator, btu per hour cooling, air conditioner sizing, room cooling load ashrae",
        "formula_preview": "BTU/hr = V × 6 + (Occupants × 400) + (Window m² × 500) + Watts",
        "inputs": [
            {"id": "room_length", "label": "Room Length", "type": "number", "unit": "meters (m)", "default": "6", "min": "2", "max": "50", "step": "0.5"},
            {"id": "room_width", "label": "Room Width", "type": "number", "unit": "meters (m)", "default": "5", "min": "2", "max": "50", "step": "0.5"},
            {"id": "room_height", "label": "Ceiling Height", "type": "number", "unit": "meters (m)", "default": "3", "min": "2", "max": "10", "step": "0.1"},
            {"id": "occupants", "label": "Typical Number of Occupants", "type": "number", "unit": "people", "default": "3", "min": "1", "max": "50", "step": "1"},
            {"id": "window_area", "label": "Total Window Glass Area (Sun-Facing)", "type": "number", "unit": "m²", "default": "4", "min": "0", "max": "50", "step": "0.5"},
            {"id": "equipment_watts", "label": "Electronic Equipment & Lights", "type": "number", "unit": "Watts (W)", "default": "600", "min": "0", "max": "20000", "step": "50"},
            {"id": "insulation", "label": "Building Insulation Quality", "type": "select", "options": [("0.85", "Superior (Double Glazed & Insulated Cavity)"), ("1.0", "Standard Residential (Normal Brick/Concrete)"), ("1.25", "Poor Insulation (Single Glazed / Top Floor Roof)")], "default": "1.0"}
        ],
        "calc_js": """
            const l = parseFloat(document.getElementById('room_length').value) || 0;
            const w = parseFloat(document.getElementById('room_width').value) || 0;
            const h = parseFloat(document.getElementById('room_height').value) || 0;
            const occ = parseFloat(document.getElementById('occupants').value) || 0;
            const win = parseFloat(document.getElementById('window_area').value) || 0;
            const equipW = parseFloat(document.getElementById('equipment_watts').value) || 0;
            const insul = parseFloat(document.getElementById('insulation').value) || 1.0;

            const volume = l * w * h;
            const baseEnvelopeBtu = volume * 200 * insul; // ~200 BTU per m3
            const occupantBtu = occ * 400; // ~400 BTU sensible + latent per seated person
            const windowBtu = win * 800; // ~800 BTU per m2 sunlit glass
            const equipBtu = equipW * 3.412; // 1 Watt = 3.412 BTU/hr

            const totalBtu = baseEnvelopeBtu + occupantBtu + windowBtu + equipBtu;
            const tons = totalBtu / 12000;
            const kw = totalBtu / 3412.14;

            document.getElementById('prim-val').textContent = tons.toFixed(2) + ' TR';
            document.getElementById('prim-unit').textContent = '(' + Math.round(totalBtu).toLocaleString() + ' BTU/hr)';
            document.getElementById('m-kw').textContent = kw.toFixed(2) + ' kW';
            document.getElementById('m-area').textContent = (l * w).toFixed(1) + ' m²';
            document.getElementById('m-vol').textContent = volume.toFixed(1) + ' m³';
            document.getElementById('m-rec').textContent = (Math.ceil(tons * 2) / 2).toFixed(1) + ' Ton Split AC';
        """,
        "metrics": [
            ("m-kw", "Thermal Cooling Power", "kW"),
            ("m-area", "Floor Area", "m²"),
            ("m-vol", "Room Enclosed Volume", "m³"),
            ("m-rec", "Commercial Split Sizing", "Recommended")
        ],
        "article": {
            "summary": "HVAC cooling load calculation determines the required sensible and latent heat extraction capacity necessary to maintain comfortable indoor temperature and relative humidity.",
            "principles": "<p>Cooling loads consist of two thermodynamic components: <strong>Sensible Heat</strong>, which raises dry-bulb temperature from building envelope conduction, solar window radiation, lighting, and electronics; and <strong>Latent Heat</strong>, which introduces water vapor moisture from occupant respiration and infiltration air that must be condensed by the evaporator coil.</p>",
            "formulas": "<p>Total thermal heat gain is aggregated from structural transmission, solar radiation, and internal metabolic releases:</p>\\[ q_{total} = q_{envelope} + q_{solar} + q_{occupants} + q_{equipment} \\]\\[ \\text{Tons of Refrigeration (TR)} = \\frac{q_{total} \\text{ (BTU/hr)}}{12,000} \\]",
            "table_title": "Typical Internal Heat Gain Coefficients (ASHRAE Fundamentals)",
            "table_headers": ["Heat Source", "Sensible Heat (W)", "Latent Heat (W)", "Total Heat Release"],
            "table_rows": [
                ["Seated Adult at Rest (Office)", "70 W (240 BTU/hr)", "45 W (155 BTU/hr)", "115 W (395 BTU/hr)"],
                ["Moderate Physical Activity (Retail)", "85 W (290 BTU/hr)", "90 W (310 BTU/hr)", "175 W (600 BTU/hr)"],
                ["Desktop Computer + Monitor", "150 W (512 BTU/hr)", "0 W", "150 W (512 BTU/hr)"],
                ["LED Lighting (per m²)", "8 – 12 W/m²", "0 W", "27 – 41 BTU/hr per m²"]
            ],
            "example": "A 30 m² master bedroom (6m × 5m × 3m = 90 m³ volume) with 3 occupants, 4 m² of sun-facing glass, and 600W of electronics. Envelope base load = 90 × 200 = 18,000 BTU/hr. Occupants = 3 × 400 = 1,200 BTU/hr. Windows = 4 × 800 = 3,200 BTU/hr. Equipment = 600 × 3.412 = 2,047 BTU/hr. Total heat load = 24,447 BTU/hr. Dividing by 12,000 gives 2.04 Tons of Refrigeration. A standard 2.0 or 2.5 Ton inverter mini-split satisfies the room.",
            "faqs": [
                ("What does 1 Ton of Refrigeration mean?", "One Ton of Refrigeration (1 TR) is defined as the rate of heat extraction required to freeze 1 short ton (2,000 lbs) of water at 0°C into ice in 24 hours. It equals exactly 12,000 BTU/hr (3.517 kW)."),
                ("What happens if an air conditioner is oversized?", "An oversized air conditioner cools the room too quickly without running long enough to dehumidify the air. This results in a cold, clammy, humid indoor environment and frequent compressor short-cycling that wastes electricity and causes early equipment failure."),
                ("How does ceiling height impact HVAC sizing?", "Traditional 'square foot' rules of thumb assume a standard 2.4m to 2.7m (8–9 ft) ceiling. Rooms with high cathedral or vaulted ceilings hold significantly more air volume and require volume-based BTU calculations.")
            ]
        }
    },

    # 5. Pipe Sizing
    {
        "slug": "pipe-sizing-calculator.html",
        "title": "Pipe Sizing & Water Flow Calculator",
        "category": "Mechanical & HVAC",
        "cat_slug": "mechanical.html",
        "icon": "🚰",
        "badge": "ASME B31 & Darcy-Weisbach",
        "meta_desc": "Calculate minimum pipe inner diameter, fluid velocity, and pressure drop per 100 meters based on volumetric flow rate and recommended velocity standards.",
        "keywords": "pipe sizing calculator, water pipe diameter calculator, flow velocity pipe, darcy weisbach pressure drop, pipe friction loss",
        "formula_preview": "Diameter (mm) = √[(4 × Q) / (π × v)] × 1000",
        "inputs": [
            {"id": "flow_rate", "label": "Volumetric Flow Rate", "type": "number", "unit": "m³ / hour", "default": "12", "min": "0.1", "max": "5000", "step": "0.5"},
            {"id": "target_velocity", "label": "Design Flow Velocity", "type": "number", "unit": "m / s", "default": "1.8", "min": "0.5", "max": "5.0", "step": "0.1"},
            {"id": "pipe_material", "label": "Pipe Material & Roughness (ε)", "type": "select", "options": [
                ("0.0015", "Copper / PEX / PVC / Smooth Plastic (ε = 0.0015 mm)"),
                ("0.045", "Commercial Carbon Steel (ε = 0.045 mm)"),
                ("0.15", "Galvanized Iron / Cast Iron (ε = 0.15 mm)")
            ], "default": "0.0015"}
        ],
        "calc_js": """
            const qM3h = parseFloat(document.getElementById('flow_rate').value) || 0;
            const v = parseFloat(document.getElementById('target_velocity').value) || 1.8;
            const roughness = parseFloat(document.getElementById('pipe_material').value) || 0.0015;

            const qM3s = qM3h / 3600;
            // Area = Q / v => pi * d^2 / 4 = Q / v => d = sqrt(4*Q / (pi * v))
            const dMeters = Math.sqrt((4 * qM3s) / (Math.PI * v));
            const dMm = dMeters * 1000;
            const dInches = dMm / 25.4;

            // Simplified Darcy-Weisbach head loss per 100m (f ~ 0.02 average for water)
            const f = 0.02;
            const hLoss100m = f * (100 / dMeters) * (v * v) / (2 * 9.81);
            const deltaP_bar = (hLoss100m * 9.81 * 1000) / 100000;

            document.getElementById('prim-val').textContent = dMm.toFixed(1) + ' mm';
            document.getElementById('prim-unit').textContent = '(' + dInches.toFixed(2) + ' inch ID)';
            document.getElementById('m-velocity').textContent = v.toFixed(2) + ' m/s';
            document.getElementById('m-headloss').textContent = hLoss100m.toFixed(2) + ' m / 100m';
            document.getElementById('m-pressloss').textContent = deltaP_bar.toFixed(3) + ' bar / 100m';
            document.getElementById('m-gpm').textContent = (qM3h * 4.403).toFixed(1) + ' GPM';
        """,
        "metrics": [
            ("m-velocity", "Actual Water Velocity", "m/s"),
            ("m-headloss", "Friction Head Loss", "m / 100m"),
            ("m-pressloss", "Friction Pressure Drop", "bar / 100m"),
            ("m-gpm", "Flow in US Gallons/Min", "GPM")
        ],
        "article": {
            "summary": "Fluid conveyance pipe sizing coordinates volumetric flow with velocity boundaries to prevent erosive pipe wall wear, water hammer surges, and excessive pumping pressure losses.",
            "principles": "<p>Sizing piping systems involves a thermodynamic trade-off between capital expenditure and operational pumping energy. Specifying small-diameter pipes reduces initial material cost but increases fluid velocity and friction losses exponentially (friction loss scales with velocity squared: \\(h_f \\propto v^2\\)). Excessive velocity exceeding 2.5 m/s causes abrasive erosion, noise, and cavitation. Conversely, oversized pipes maintain low friction but risk sediment accumulation.</p>",
            "formulas": "<p>From the continuity equation for incompressible steady flow, cross-sectional area and internal diameter are calculated as:</p>\\[ Q = A \\times v = \\frac{\\pi D^2}{4} \\times v \\implies D = \\sqrt{\\frac{4Q}{\\pi v}} \\]\\[ h_f = f \\times \\frac{L}{D} \\times \\frac{v^2}{2g} \\quad \\text{(Darcy-Weisbach Friction Loss)} \\]",
            "table_title": "Recommended Maximum Fluid Velocities (CIBSE & ASHRAE)",
            "table_headers": ["Service Application", "Recommended Velocity (m/s)", "Velocity (ft/s)", "Noise / Erosion Risk Threshold"],
            "table_rows": [
                ["Domestic Water Supply (Mains)", "1.2 – 2.0 m/s", "4.0 – 6.5 ft/s", "> 2.4 m/s (Erosion risk)"],
                ["Pump Suction Header", "0.8 – 1.2 m/s", "2.5 – 4.0 ft/s", "> 1.5 m/s (Pump cavitation)"],
                ["Pump Discharge Header", "1.5 – 2.5 m/s", "5.0 – 8.0 ft/s", "> 3.0 m/s (Excessive head loss)"],
                ["Hydronic Chilled Water Lines", "1.2 – 2.4 m/s", "4.0 – 8.0 ft/s", "> 2.5 m/s (Pipe wall erosion)"],
                ["General Gravity Drainage", "0.75 – 1.5 m/s", "2.5 – 5.0 ft/s", "< 0.6 m/s (Sediment settling)"]
            ],
            "example": "A commercial HVAC circulation pump circulates 12 m³/hr of chilled water. The mechanical design specification dictates a target velocity of 1.8 m/s in copper pipe. Volumetric flow Q = 12 / 3600 = 0.00333 m³/s. Required inner diameter D = √[(4 × 0.00333) / (π × 1.8)] = 0.0485 m = 48.5 mm (1.91 inches). Specifying standard nominal 50 mm (2-inch DN50) pipe satisfies velocity criteria with friction loss of approximately 3.4 meters head loss per 100m of pipe run.",
            "faqs": [
                ("Why is pump suction velocity kept lower than discharge velocity?", "Pump suction lines must avoid low-pressure localized vapor pockets. High velocities cause pressure drops below the fluid's vapor pressure, triggering destructive vapor bubble cavitation that erodes pump impellers."),
                ("How does pipe roughness influence head loss?", "Rougher materials (such as weathered galvanized iron) increase the Darcy friction factor f, doubling or tripling friction head losses compared to smooth PEX or copper pipes."),
                ("What is Water Hammer?", "Water hammer is a hydraulic pressure surge created when fluid in motion is forced to stop or change direction suddenly (such as rapid valve closure). Limiting pipe velocity reduces the kinetic momentum available to generate pressure spikes.")
            ]
        }
    }
]
