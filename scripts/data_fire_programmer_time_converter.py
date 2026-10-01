"""
Data definition for Fire & Safety, Programmer, DateTime, and Unit Converter calculators.
"""

FIRE_PROGRAMMER_TOOLS = [
    # 1. Smoke Detector Spacing
    {
        "slug": "smoke-detector-spacing-calculator.html",
        "title": "Smoke Detector Spacing & Coverage Calculator",
        "category": "Fire & Life Safety",
        "cat_slug": "fire-safety.html",
        "icon": "🚨",
        "badge": "NFPA 72 & EN 54-7",
        "meta_desc": "Calculate the required number and layout spacing of smoke detectors according to NFPA 72 National Fire Alarm Code based on room dimensions, ceiling height, and air changes.",
        "keywords": "smoke detector spacing calculator, nfpa 72 detector coverage, smoke alarm square feet, fire alarm layout calculator, ceiling height derating",
        "formula_preview": "Grid Spacing S = 30 ft (9.1m) baseline with ceiling height derating",
        "inputs": [
            {"id": "room_len", "label": "Room / Corridor Length", "type": "number", "unit": "meters (m)", "default": "24", "min": "2", "max": "200", "step": "0.5"},
            {"id": "room_wid", "label": "Room / Corridor Width", "type": "number", "unit": "meters (m)", "default": "15", "min": "2", "max": "200", "step": "0.5"},
            {"id": "ceiling_ht", "label": "Ceiling Height", "type": "select", "options": [
                ("1.0", "Up to 3.0 m (10 ft) — 1.0 (No derating)"),
                ("0.91", "3.0 to 3.6 m (10–12 ft) — 0.91 Multiplier"),
                ("0.84", "3.6 to 4.3 m (12–14 ft) — 0.84 Multiplier"),
                ("0.77", "4.3 to 4.9 m (14–16 ft) — 0.77 Multiplier"),
                ("0.71", "4.9 to 5.5 m (16–18 ft) — 0.71 Multiplier"),
                ("0.64", "5.5 to 6.1 m (18–20 ft) — 0.64 Multiplier")
            ], "default": "1.0"},
            {"id": "ceiling_type", "label": "Ceiling Construction Type", "type": "select", "options": [
                ("smooth", "Smooth Flat Ceiling"),
                ("beam", "Beamed / Joist Ceiling (Restricted airflow)")
            ], "default": "smooth"}
        ],
        "calc_js": """
            const l = parseFloat(document.getElementById('room_len').value) || 0;
            const w = parseFloat(document.getElementById('room_wid').value) || 0;
            const derate = parseFloat(document.getElementById('ceiling_ht').value) || 1.0;
            const cType = document.getElementById('ceiling_type').value;

            const baseSpacingM = 9.144; // 30 feet standard baseline NFPA 72
            let effectiveSpacing = baseSpacingM * derate;
            if (cType === 'beam') effectiveSpacing *= 0.85;

            // Spacing along length and width
            const countL = Math.ceil(l / effectiveSpacing);
            const countW = Math.ceil(w / effectiveSpacing);
            const totalDetectors = Math.max(1, countL * countW);

            const areaM2 = l * w;
            const coveragePerDetector = areaM2 / totalDetectors;
            const maxRadius = effectiveSpacing * 0.7; // 0.7 * S radius to corners

            document.getElementById('prim-val').textContent = totalDetectors + ' Detectors';
            document.getElementById('prim-unit').textContent = '(' + countL + ' × ' + countW + ' Grid Layout)';
            document.getElementById('m-eff-spacing').textContent = effectiveSpacing.toFixed(2) + ' m (' + (effectiveSpacing * 3.28084).toFixed(1) + ' ft)';
            document.getElementById('m-area').textContent = areaM2.toFixed(0) + ' m²';
            document.getElementById('m-cov-per').textContent = coveragePerDetector.toFixed(1) + ' m² / unit';
            document.getElementById('m-radius').textContent = maxRadius.toFixed(2) + ' m (Radius to corner)';
        """,
        "metrics": [
            ("m-eff-spacing", "Derated Linear Spacing", "Meters"),
            ("m-area", "Total Enclosed Room Area", "m²"),
            ("m-cov-per", "Average Area per Detector", "m² / unit"),
            ("m-radius", "Max Distance to Wall/Corner", "Meters")
        ],
        "article": {
            "summary": "Life safety design requires positioning spot-type smoke detectors within certified geometric radii to ensure early thermal and particulate detection during smoldering fires.",
            "principles": "<p>Under NFPA 72 (National Fire Alarm and Signaling Code Chapter 17), spot-type smoke detectors on smooth flat ceilings possess a standard baseline spacing of <strong>30 feet (9.14 meters)</strong> between centers, with a maximum allowable coverage area of 900 square feet (83.6 m²). Crucially, all points on the ceiling must fall within a circle of radius \\(R = 0.7 \\times S\\) (21 feet / 6.4 meters) centered on a detector. When ceilings exceed 10 feet (3.0 m), ascending smoke plumes entrain cold ambient air and lose thermal buoyancy (a phenomenon known as smoke stratification), requiring strict spacing derating factors.</p>",
            "formulas": "<p>Detector spacing and ceiling height compensation are dictated by NFPA Table 17.6.3.5.1:</p>\\[ S_{\\text{effective}} = S_{\\text{base}} \\times C_{\\text{height}} \\times C_{\\text{beam}} \\]\\[ N_{\\text{detectors}} = \\lceil\\frac{L}{S_{\\text{effective}}}\\rceil \\times \\lceil\\frac{W}{S_{\\text{effective}}}\\rceil \\]",
            "table_title": "NFPA 72 Ceiling Height Reduction Factors",
            "table_headers": ["Ceiling Height Range (m)", "Ceiling Height (ft)", "Spacing Multiplier Factor", "Effective Spacing (m / ft)"],
            "table_rows": [
                ["Up to 3.0 m", "Up to 10 ft", "1.00 (No reduction)", "9.1 m (30.0 ft)"],
                ["3.0 m to 3.6 m", "10 ft to 12 ft", "0.91", "8.3 m (27.3 ft)"],
                ["3.6 m to 4.3 m", "12 ft to 14 ft", "0.84", "7.7 m (25.2 ft)"],
                ["4.3 m to 4.9 m", "14 ft to 16 ft", "0.77", "7.0 m (23.1 ft)"],
                ["4.9 m to 5.5 m", "16 ft to 18 ft", "0.71", "6.5 m (21.3 ft)"],
                ["5.5 m to 6.1 m", "18 ft to 20 ft", "0.64", "5.8 m (19.2 ft)"]
            ],
            "example": "A commercial storage warehouse measures 24 meters long by 15 meters wide with a ceiling height of 3.8 meters (12.5 ft) and smooth ceilings. The height derating multiplier from NFPA 72 is 0.84, giving an effective linear spacing of 9.144 × 0.84 = 7.68 meters. Lengthwise detectors = ⌈24 / 7.68⌉ = 4. Widthwise detectors = ⌈15 / 7.68⌉ = 2. Total detectors required = 4 × 2 = 8 smoke detectors arranged on a uniform 4 × 2 rectangular grid.",
            "faqs": [
                ("How close to a wall can a smoke detector be placed?", "Detectors must not be positioned within 4 inches (100 mm) of any corner formed by the junction of ceiling and wall, where dead air pockets prevent smoke flow. Wall-mounted detectors must be positioned between 4 and 12 inches (100–300 mm) down from the ceiling."),
                ("What causes smoke stratification in high ceilings?", "In high ceilings, hot smoke rises buoyantly until heat transfers to surrounding cool air. If the smoke cools to ambient room temperature before reaching the roof, it stops rising and stratifies as a horizontal layer, bypassing ceiling-mounted detectors. Beam-type optical smoke detectors are often specified for high atriums."),
                ("How do HVAC air supply diffusers affect detectors?", "Detectors must maintain a minimum physical clearance of 3 feet (0.9 meters) from air supply diffusers to prevent incoming fresh air jets from blowing smoke away from the sensor chamber.")
            ]
        }
    },

    # 2. Subnet CIDR Calculator
    {
        "slug": "subnet-calculator.html",
        "title": "IPv4 Subnet & CIDR IP Calculator",
        "category": "Programmer & Networking",
        "cat_slug": "programmer.html",
        "icon": "🌐",
        "badge": "RFC 1878 & IEEE 802.3",
        "meta_desc": "Calculate IPv4 subnet masks, network address, broadcast address, usable host ranges, and wildcard masks instantly from CIDR notation prefix.",
        "keywords": "subnet calculator, cidr calculator, ipv4 subnet mask, usable host range, network address broadcast address, ip calculator",
        "formula_preview": "Usable Hosts = 2^(32 - Prefix) - 2",
        "inputs": [
            {"id": "ip_addr", "label": "IPv4 Address", "type": "text", "unit": "IP", "default": "192.168.1.55"},
            {"id": "cidr_prefix", "label": "Subnet Mask / CIDR Prefix", "type": "select", "options": [
                ("8", "/8 — 255.0.0.0 (16,777,214 Hosts)"),
                ("16", "/16 — 255.255.0.0 (65,534 Hosts)"),
                ("24", "/24 — 255.255.255.0 (254 Hosts)"),
                ("25", "/25 — 255.255.255.128 (126 Hosts)"),
                ("26", "/26 — 255.255.255.192 (62 Hosts)"),
                ("27", "/27 — 255.255.255.224 (30 Hosts)"),
                ("28", "/28 — 255.255.255.240 (14 Hosts)"),
                ("29", "/29 — 255.255.255.248 (6 Hosts)"),
                ("30", "/30 — 255.255.255.252 (2 Hosts — Point-to-Point)"),
                ("32", "/32 — 255.255.255.255 (Single Host Route)")
            ], "default": "24"}
        ],
        "calc_js": """
            const ipStr = document.getElementById('ip_addr').value.trim();
            const prefix = parseInt(document.getElementById('cidr_prefix').value) || 24;

            const parts = ipStr.split('.').map(Number);
            if (parts.length !== 4 || parts.some(p => isNaN(p) || p < 0 || p > 255)) {
                document.getElementById('prim-val').textContent = 'Invalid IP';
                return;
            }

            const ipNum = ((parts[0] << 24) >>> 0) + (parts[1] << 16) + (parts[2] << 8) + parts[3];
            const maskNum = prefix === 0 ? 0 : (~0 << (32 - prefix)) >>> 0;
            const netNum = (ipNum & maskNum) >>> 0;
            const wildNum = (~maskNum) >>> 0;
            const bcastNum = (netNum | wildNum) >>> 0;

            function numToIp(n) {
                return [(n >>> 24) & 255, (n >>> 16) & 255, (n >>> 8) & 255, n & 255].join('.');
            }

            const totalHosts = prefix === 32 ? 1 : Math.pow(2, 32 - prefix);
            const usableHosts = prefix >= 31 ? (prefix === 31 ? 2 : 1) : Math.max(0, totalHosts - 2);

            const firstHost = prefix >= 31 ? numToIp(netNum) : numToIp(netNum + 1);
            const lastHost = prefix >= 31 ? numToIp(bcastNum) : numToIp(bcastNum - 1);

            document.getElementById('prim-val').textContent = usableHosts.toLocaleString() + ' Usable Hosts';
            document.getElementById('prim-unit').textContent = 'Subnet: ' + numToIp(netNum) + '/' + prefix;
            document.getElementById('m-net').textContent = numToIp(netNum);
            document.getElementById('m-bcast').textContent = numToIp(bcastNum);
            document.getElementById('m-mask').textContent = numToIp(maskNum);
            document.getElementById('m-range').textContent = firstHost + ' – ' + lastHost;
        """,
        "metrics": [
            ("m-net", "Network Address (ID)", "IP"),
            ("m-bcast", "Broadcast Address", "IP"),
            ("m-mask", "Dotted Subnet Mask", "Mask"),
            ("m-range", "Usable Host Range", "IP Range")
        ],
        "article": {
            "summary": "Classless Inter-Domain Routing (CIDR) subnetting partitions large IPv4 address blocks into discrete, hierarchically structured local area networks (LANs).",
            "principles": "<p>An IPv4 address consists of 32 bits segmented into four 8-bit octets. A subnet mask divides these 32 bits into two functional portions: the <strong>Network Prefix</strong> (which identifies the network or broadcast domain) and the <strong>Host Identifier</strong> (which designates specific endpoints like servers, routers, and PCs). The all-zeros host address is reserved as the Network ID, while the all-ones host address is reserved for Layer-3 broadcast packets.</p>",
            "formulas": "<p>Total and usable host quantities for any prefix length \\(N\\) are determined exponentially by:</p>\\[ \\text{Total Addresses} = 2^{(32 - N)} \\]\\[ \\text{Usable Hosts} = 2^{(32 - N)} - 2 \\quad (\\text{for } N \\le 30) \\]",
            "table_title": "Standard IPv4 Subnet Mask Table (RFC 1878)",
            "table_headers": ["CIDR Prefix", "Subnet Mask", "Wildcard Mask", "Total Addresses", "Usable Host Count"],
            "table_rows": [
                ["/24", "255.255.255.0", "0.0.0.255", "256", "254 hosts (Standard office LAN)"],
                ["/25", "255.255.255.128", "0.0.0.127", "128", "126 hosts"],
                ["/26", "255.255.255.192", "0.0.0.63", "64", "62 hosts"],
                ["/27", "255.255.255.224", "0.0.0.31", "32", "30 hosts"],
                ["/28", "255.255.255.240", "0.0.0.15", "16", "14 hosts"],
                ["/30", "255.255.255.252", "0.0.0.3", "4", "2 hosts (Router-to-router link)"]
            ],
            "example": "Given the IP address 192.168.1.55 with CIDR prefix /24. The 24 network bits set to 1 yield a subnet mask of 255.255.255.0. Bitwise ANDing 192.168.1.55 with 255.255.255.0 produces the Network ID: 192.168.1.0. Inverting the mask yields wildcard 0.0.0.255, giving the Broadcast Address: 192.168.1.255. Usable hosts range from 192.168.1.1 through 192.168.1.254 (254 usable assignable IPs).",
            "faqs": [
                ("Why are 2 addresses subtracted from the total?", "In traditional IPv4 networking, the very first address represents the network identifier, and the final address is the directed broadcast address. Neither can be assigned to an individual host network interface card (NIC)."),
                ("What is a wildcard mask?", "A wildcard mask is the inverse of a subnet mask (0 bits indicate exact match, 1 bits indicate ignore). Wildcards are utilized extensively in Cisco Access Control Lists (ACLs) and OSPF routing configurations."),
                ("What is RFC 3021 /31 subnetting?", "RFC 3021 permits /31 subnets (which contain only 2 addresses total) specifically on dedicated point-to-point links between two routers, eliminating the requirement for separate network and broadcast addresses to conserve scarce IPv4 space.")
            ]
        }
    },

    # 3. Date Difference & Business Days
    {
        "slug": "date-difference-calculator.html",
        "title": "Date Difference & Business Days Calculator",
        "category": "Date & Time Utilities",
        "cat_slug": "datetime.html",
        "icon": "📅",
        "badge": "ISO 8601 Calendar",
        "meta_desc": "Calculate exact duration between two dates in total days, working business days (excluding weekends), full weeks, months, and years with include-end-day option.",
        "keywords": "date difference calculator, days between dates, business days calculator, working days between dates, date duration calculator",
        "formula_preview": "Duration = Date₂ - Date₁ (days, working days, weeks)",
        "inputs": [
            {"id": "start_date", "label": "Start Date", "type": "date", "unit": "", "default": "2026-01-01"},
            {"id": "end_date", "label": "End Date", "type": "date", "unit": "", "default": "2026-12-31"},
            {"id": "include_end", "label": "Include End Date?", "type": "select", "options": [
                ("0", "No (Standard span between dates)"),
                ("1", "Yes (Include both start and end days)")
            ], "default": "1"}
        ],
        "calc_js": """
            const sStr = document.getElementById('start_date').value;
            const eStr = document.getElementById('end_date').value;
            const incEnd = parseInt(document.getElementById('include_end').value) || 0;

            if (!sStr || !eStr) return;
            const d1 = new Date(sStr + 'T00:00:00');
            const d2 = new Date(eStr + 'T00:00:00');

            let diffMs = d2 - d1;
            if (diffMs < 0) {
                document.getElementById('prim-val').textContent = 'End date earlier';
                return;
            }

            let totalDays = Math.round(diffMs / (1000 * 60 * 60 * 24)) + incEnd;
            let businessDays = 0;
            let cur = new Date(d1);
            let loopLimit = incEnd ? totalDays : totalDays;

            for (let i = 0; i < loopLimit; i++) {
                const dayOfWeek = cur.getDay(); // 0 is Sunday, 6 is Saturday
                if (dayOfWeek !== 0 && dayOfWeek !== 6) {
                    businessDays++;
                }
                cur.setDate(cur.getDate() + 1);
            }

            const weeks = Math.floor(totalDays / 7);
            const remDays = totalDays % 7;
            const percentYear = ((totalDays / 365.25) * 100).toFixed(1);

            document.getElementById('prim-val').textContent = totalDays.toLocaleString() + ' Days';
            document.getElementById('prim-unit').textContent = '(' + businessDays.toLocaleString() + ' Working Days)';
            document.getElementById('m-weeks').textContent = weeks + ' wks, ' + remDays + ' days';
            document.getElementById('m-business').textContent = businessDays.toLocaleString() + ' days';
            document.getElementById('m-weekend').textContent = (totalDays - businessDays).toLocaleString() + ' days';
            document.getElementById('m-percent-yr').textContent = percentYear + '% of year';
        """,
        "metrics": [
            ("m-business", "Working Business Days", "Days"),
            ("m-weekend", "Weekend Days (Sat/Sun)", "Days"),
            ("m-weeks", "Full Weeks & Days", "Weeks"),
            ("m-percent-yr", "Percentage of Solar Year", "%")
        ],
        "article": {
            "summary": "Calendar date math calculates exact elapsed chronological intervals accounting for leap years, irregular Gregorian month lengths, and business day payroll schedules.",
            "principles": "<p>Calculating elapsed time between arbitrary dates is complicated by irregularities in the Gregorian calendar: variable month lengths (28, 29, 30, or 31 days) and quadrennial leap years. Furthermore, commercial, financial, and legal contracts frequently operate on <strong>Business Days</strong> (Monday through Friday), requiring systematic exclusion of weekend non-working days.</p>",
            "formulas": "<p>Calendar difference is computed by evaluating the absolute Unix epoch timestamp delta:</p>\\[ \\Delta t = \\frac{T_{end} - T_{start}}{86,400,000 \\text{ ms/day}} + K_{end} \\]\\[ \\text{Business Days} = \\sum_{d=T_{start}}^{T_{end}} [\\text{DayOfWeek}(d) \\notin \\{\\text{Sat}, \\text{Sun}\\}] \\]",
            "table_title": "Days in Gregorian Months Reference",
            "table_headers": ["Month", "Standard Days", "Leap Year Days", "Quarter"],
            "table_rows": [
                ["January", "31", "31", "Q1"],
                ["February", "28", "29 (Divisible by 4, not 100 unless 400)", "Q1"],
                ["March – April", "31 / 30", "31 / 30", "Q1 / Q2"],
                ["May – June", "31 / 30", "31 / 30", "Q2"],
                ["July – August", "31 / 31 (Consecutive 31-day months)", "31 / 31", "Q3"],
                ["September – December", "30 / 31 / 30 / 31", "30 / 31 / 30 / 31", "Q3 / Q4"]
            ],
            "example": "Between January 1, 2026 and December 31, 2026 inclusive: total elapsed duration = 365 calendar days (52 weeks and 1 day). Total weekend days = 104 days (52 Saturdays and 52 Sundays). Net business working days = 365 - 104 = 261 working business days.",
            "faqs": [
                ("What does 'Include End Date' mean?", "If you start on Monday and end on Tuesday, the elapsed span is 1 day. However, if counting calendar days worked on a project, both Monday and Tuesday were worked, totaling 2 days. The toggle allows selecting either methodology."),
                ("How are leap years determined?", "A leap year occurs in any year divisible by 4, except for century years (ending in 00), which are only leap years if they are also divisible by 400 (e.g., 2000 was a leap year, but 1900 was not)."),
                ("Does this calculator account for national statutory public holidays?", "Because statutory and bank holidays vary widely by country, state, and municipality, this tool strictly excludes weekends (Saturday and Sunday). Custom holiday subtraction can be done from the working day result.")
            ]
        }
    },

    # 4. Universal Unit Converter
    {
        "slug": "unit-converter.html",
        "title": "Universal Multi-Unit Converter",
        "category": "Universal Unit Converters",
        "cat_slug": "converter.html",
        "icon": "🔄",
        "badge": "NIST & BIPM SI Units",
        "meta_desc": "Convert units across length, mass/weight, temperature, pressure, area, and volume with high precision using international Bureau of Weights and Measures standards.",
        "keywords": "unit converter, length converter, weight converter kg to lbs, temperature converter c to f, pressure converter bar to psi",
        "formula_preview": "Standardized SI conversion coefficients",
        "inputs": [
            {"id": "conv_cat", "label": "Conversion Category", "type": "select", "options": [
                ("length", "Length (Meters, Feet, Inches, Kilometers, Miles)"),
                ("mass", "Mass / Weight (Kilograms, Pounds, Ounces, Grams, Tons)"),
                ("temperature", "Temperature (Celsius, Fahrenheit, Kelvin)"),
                ("pressure", "Pressure (Bar, PSI, Pascal, Atmosphere)"),
                ("volume", "Volume (Liters, Gallons, Cubic Meters, Cubic Feet)")
            ], "default": "length"},
            {"id": "input_val", "label": "Value to Convert", "type": "number", "unit": "", "default": "100", "min": "-1000", "max": "100000000", "step": "0.1"},
            {"id": "unit_from", "label": "Convert From Unit", "type": "select", "options": [
                ("m", "Meters (m)"),
                ("ft", "Feet (ft)"),
                ("in", "Inches (in)"),
                ("km", "Kilometers (km)"),
                ("mi", "Miles (mi)")
            ], "default": "m"},
            {"id": "unit_to", "label": "Convert To Unit", "type": "select", "options": [
                ("ft", "Feet (ft)"),
                ("m", "Meters (m)"),
                ("in", "Inches (in)"),
                ("km", "Kilometers (km)"),
                ("mi", "Miles (mi)")
            ], "default": "ft"}
        ],
        "calc_js": """
            const cat = document.getElementById('conv_cat').value;
            const val = parseFloat(document.getElementById('input_val').value) || 0;
            const uFrom = document.getElementById('unit_from').value;
            const uTo = document.getElementById('unit_to').value;

            // Length conversions relative to meter
            const L_RATES = { m: 1, km: 1000, ft: 0.3048, in: 0.0254, mi: 1609.344 };
            const M_RATES = { kg: 1, g: 0.001, lb: 0.453592, oz: 0.0283495, ton: 1000 };
            const P_RATES = { bar: 100000, psi: 6894.76, pa: 1, kpa: 1000, atm: 101325 };
            const V_RATES = { l: 0.001, m3: 1, gal: 0.00378541, ft3: 0.0283168 };

            let result = 0;
            if (cat === 'temperature') {
                if (uFrom === 'c' && uTo === 'f') result = (val * 9/5) + 32;
                else if (uFrom === 'f' && uTo === 'c') result = (val - 32) * 5/9;
                else if (uFrom === 'c' && uTo === 'k') result = val + 273.15;
                else if (uFrom === 'k' && uTo === 'c') result = val - 273.15;
                else result = val;
            } else if (cat === 'length') {
                const meters = val * (L_RATES[uFrom] || 1);
                result = meters / (L_RATES[uTo] || 1);
            } else if (cat === 'mass') {
                const kg = val * (M_RATES[uFrom] || 1);
                result = kg / (M_RATES[uTo] || 1);
            } else if (cat === 'pressure') {
                const pa = val * (P_RATES[uFrom] || 1);
                result = pa / (P_RATES[uTo] || 1);
            } else {
                const m3 = val * (V_RATES[uFrom] || 1);
                result = m3 / (V_RATES[uTo] || 1);
            }

            document.getElementById('prim-val').textContent = result.toLocaleString(undefined, {maximumFractionDigits: 4});
            document.getElementById('prim-unit').textContent = uTo.toUpperCase();
            document.getElementById('m-in').textContent = val + ' ' + uFrom.toUpperCase();
            document.getElementById('m-ratio').textContent = (result / (val || 1)).toFixed(6);
            document.getElementById('m-cat').textContent = cat.toUpperCase();
            document.getElementById('m-si').textContent = 'SI Compliant';
        """,
        "metrics": [
            ("m-in", "Input Value", "Original"),
            ("m-ratio", "Conversion Ratio Factor", "Multiplier"),
            ("m-cat", "Active Physical Dimension", "Dimension"),
            ("m-si", "Standard Classification", "SI System")
        ],
        "article": {
            "summary": "Dimensional analysis and unit conversion translate physical quantities between the International System of Units (SI) and US Customary / British Imperial measurement systems.",
            "principles": "<p>Scientific and engineering calculations require dimensional homogeneity. In 1959, the International Yard and Pound Agreement formally standardized the conversion ratio between imperial and metric systems: defining exactly <strong>1 inch = 25.4 millimeters</strong> and <strong>1 avoirdupois pound = 0.45359237 kilograms</strong>. Failure to convert units accurately has precipitated notorious engineering disasters, including the loss of NASA's Mars Climate Orbiter in 1999.</p>",
            "formulas": "<p>Linear conversions use fixed multiplication factors, while affine conversions (temperature) incorporate zero-point offsets:</p>\\[ \\text{Value}_{target} = \\text{Value}_{source} \\times \\left(\\frac{K_{source}}{K_{target}}\\right) \\]\\[ T_{^{\\circ}\\text{F}} = (T_{^{\\circ}\\text{C}} \\times 1.8) + 32 \\quad \\vert \\quad T_{\\text{K}} = T_{^{\\circ}\\text{C}} + 273.15 \\]",
            "table_title": "Primary SI Conversion Factors",
            "table_headers": ["Measurement Dimension", "Base SI Unit", "Common Imperial Unit", "Exact Conversion Equivalent"],
            "table_rows": [
                ["Length", "Meter (m)", "Foot (ft)", "1 ft = 0.3048 m exactly"],
                ["Mass", "Kilogram (kg)", "Pound (lb)", "1 lb = 0.45359237 kg"],
                ["Pressure", "Pascal (Pa)", "Pound per Square Inch (psi)", "1 psi = 6,894.757 Pa"],
                ["Energy", "Joule (J)", "British Thermal Unit (BTU)", "1 BTU = 1,055.056 J"],
                ["Volume", "Cubic Meter (m³)", "US Liquid Gallon", "1 gal = 0.00378541 m³"]
            ],
            "example": "Converting a vehicle tire pressure of 2.20 bar into US Customary pounds per square inch (psi). One bar equals 100,000 Pascals; one psi equals 6,894.76 Pascals. Therefore, 2.20 bar = 220,000 Pa. Dividing by 6,894.76 gives 31.91 psi.",
            "faqs": [
                ("What is the difference between mass and weight?", "Mass (measured in kilograms) is an intrinsic property representing the amount of matter in an object, remaining identical anywhere in the universe. Weight is the gravitational force acting on that mass (W = m × g), varying with local gravitational acceleration."),
                ("Why is -40° identical in Celsius and Fahrenheit?", "Because the two linear temperature scale formulas intersect at: -40 × 1.8 + 32 = -72 + 32 = -40°."),
                ("What is the difference between US liquid gallon and UK Imperial gallon?", "A US liquid gallon equals 231 cubic inches (3.785 liters), whereas an Imperial gallon equals 4.546 liters (approximately 20% larger).")
            ]
        }
    }
]
