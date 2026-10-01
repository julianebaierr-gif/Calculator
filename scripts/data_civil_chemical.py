"""
Data definition for Civil, Mechanical (Torque), and Chemical Engineering calculators.
"""

CIVIL_CHEMICAL_TOOLS = [
    # 1. Torque & Power
    {
        "slug": "torque-calculator.html",
        "title": "Torque & Shaft Power Calculator",
        "category": "Mechanical & HVAC",
        "cat_slug": "mechanical.html",
        "icon": "⚙️",
        "badge": "ISO 80000 & DIN 743",
        "meta_desc": "Calculate mechanical rotational torque in Newton-meters (N·m) and foot-pounds (lbf·ft), lever force, and rotating shaft power in kilowatts (kW) and horsepower (HP).",
        "keywords": "torque calculator, rotational power calculator, nm to ft-lbs torque, shaft power kw to hp, torque force radius formula",
        "formula_preview": "Torque (N·m) = Force (N) × Lever Arm (m)",
        "inputs": [
            {"id": "calc_mode", "label": "Calculation Mode", "type": "select", "options": [
                ("force_arm", "Solve Torque from Force & Lever Arm"),
                ("power_rpm", "Solve Torque from Mechanical Power & RPM")
            ], "default": "force_arm"},
            {"id": "force_n", "label": "Applied Linear Force", "type": "number", "unit": "Newtons (N)", "default": "250", "min": "0.1", "max": "100000", "step": "1"},
            {"id": "lever_m", "label": "Lever Arm / Radius", "type": "number", "unit": "meters (m)", "default": "0.4", "min": "0.01", "max": "50", "step": "0.05"},
            {"id": "rpm", "label": "Rotational Speed (RPM)", "type": "number", "unit": "RPM", "default": "1800", "min": "1", "max": "50000", "step": "10"},
            {"id": "power_kw", "label": "Shaft Mechanical Power (if solving from Power)", "type": "number", "unit": "kW", "default": "15", "min": "0.1", "max": "5000", "step": "0.5"}
        ],
        "calc_js": """
            const mode = document.getElementById('calc_mode').value;
            const f = parseFloat(document.getElementById('force_n').value) || 0;
            const r = parseFloat(document.getElementById('lever_m').value) || 0;
            const rpm = parseFloat(document.getElementById('rpm').value) || 1;
            const kw = parseFloat(document.getElementById('power_kw').value) || 0;

            let torqueNm = 0;
            let powerWatts = 0;

            if (mode === 'force_arm') {
                torqueNm = f * r;
                // Power = Torque * angular velocity = Torque * (2 * pi * RPM / 60)
                const omega = (2 * Math.PI * rpm) / 60;
                powerWatts = torqueNm * omega;
            } else {
                powerWatts = kw * 1000;
                const omega = (2 * Math.PI * rpm) / 60;
                torqueNm = powerWatts / omega;
            }

            const torqueFtLbs = torqueNm * 0.737562;
            const finalKw = powerWatts / 1000;
            const hp = finalKw * 1.34102;

            document.getElementById('prim-val').textContent = torqueNm.toFixed(1) + ' N·m';
            document.getElementById('prim-unit').textContent = '(' + torqueFtLbs.toFixed(1) + ' lbf·ft)';
            document.getElementById('m-power-kw').textContent = finalKw.toFixed(2) + ' kW';
            document.getElementById('m-hp').textContent = hp.toFixed(2) + ' HP';
            document.getElementById('m-rad-sec').textContent = ((2 * Math.PI * rpm) / 60).toFixed(1) + ' rad/s';
            document.getElementById('m-f-lbs').textContent = (torqueNm / (r || 1) * 0.224809).toFixed(1) + ' lbf';
        """,
        "metrics": [
            ("m-power-kw", "Shaft Mechanical Power", "kW"),
            ("m-hp", "Mechanical Horsepower", "HP"),
            ("m-rad-sec", "Angular Velocity (ω)", "rad/s"),
            ("m-f-lbs", "Equivalent Force at Arm", "lbf")
        ],
        "article": {
            "summary": "Torque measures the rotational moment of force about an axis. Shaft power defines the time rate at which that rotational work is executed.",
            "principles": "<p>In mechanical powertrain engineering, torque represents the rotational analogue of linear force. When a force acts perpendicular to a lever arm distance from the center of rotation, torque is generated. Rotational power equals torque multiplied by angular velocity. For constant power transmission, torque is inversely proportional to rotational speed: high-speed motors produce low torque, while reduction gearboxes multiply torque while trading off shaft speed.</p>",
            "formulas": "<p>The fundamental relationships governing torque and rotational shaft power are formulated as:</p>\\[ \\tau = F \\times r \\sin(\\theta) \\]\\[ P = \\tau \\times \\omega = \\tau \\times \\left(\\frac{2\\pi \\times \\text{RPM}}{60}\\right) \\implies \\tau (\\text{N}\\cdot\\text{m}) = \\frac{9549 \\times P (\\text{kW})}{\\text{RPM}} \\]",
            "table_title": "Typical Electric Motor Torque Profiles (4-Pole 50Hz/60Hz)",
            "table_headers": ["Rated Motor Power", "Synchronous Speed", "Full-Load Torque (N·m)", "Breakdown Peak Torque Multiplier"],
            "table_rows": [
                ["1.1 kW (1.5 HP)", "1,500 RPM", "7.2 N·m", "2.4x – 2.8x rated"],
                ["5.5 kW (7.5 HP)", "1,500 RPM", "35.8 N·m", "2.5x – 3.0x rated"],
                ["15 kW (20 HP)", "1,500 RPM", "97.5 N·m", "2.6x – 3.2x rated"],
                ["45 kW (60 HP)", "1,500 RPM", "292 N·m", "2.7x – 3.2x rated"]
            ],
            "example": "A hydraulic pump requires 15 kW of mechanical power when driven by a 4-pole motor operating at 1,450 RPM. Applying the constant conversion factor gives: Torque = (9549 × 15) / 1,450 = 98.8 N·m (72.8 lbf·ft). A technician applying a 0.4-meter torque wrench would need to apply a linear perpendicular force of 98.8 / 0.4 = 247 Newtons (55.5 lbf) to generate the equivalent torque.",
            "faqs": [
                ("What is the difference between N·m and Joule?", "Both have identical SI units (kg·m²/s²), but Joule (J) is strictly reserved for scalar energy or work, while Newton-meter (N·m) denotes vector rotational torque."),
                ("Why do diesel engines produce higher torque than gasoline engines?", "Diesel engines feature higher compression ratios, longer stroke lengths (increasing the crankshaft lever arm radius r), and intense peak cylinder combustion pressures, generating significantly greater rotational moment at low RPM."),
                ("What does the number 9549 represent in the torque equation?", "9549 is the derived constant equal to 60,000 / (2 × π), which converts kilowatts and RPM directly into Newton-meters without intermediate angular velocity conversions.")
            ]
        }
    },

    # 2. Concrete Volume & Slabs
    {
        "slug": "concrete-calculator.html",
        "title": "Concrete Slab, Footing & Column Calculator",
        "category": "Civil & Construction",
        "cat_slug": "civil.html",
        "icon": "🏗️",
        "badge": "ACI 318 & BS EN 206",
        "meta_desc": "Calculate concrete volume in cubic meters (m³) and cubic yards (yd³), plus required 50kg cement bags, sand, and gravel quantities based on standard mix designs.",
        "keywords": "concrete calculator, concrete slab volume calculator, cubic yards concrete, cement bags calculator, concrete mix 1:2:4 ratio",
        "formula_preview": "Volume = Length × Width × Thickness (m³ or yd³)",
        "inputs": [
            {"id": "shape", "label": "Structural Element Shape", "type": "select", "options": [
                ("slab", "Rectangular Slab / Wall / Footing"),
                ("column", "Round Circular Column / Pier")
            ], "default": "slab"},
            {"id": "dim_length", "label": "Length (or Height for Column)", "type": "number", "unit": "meters (m)", "default": "8", "min": "0.1", "max": "200", "step": "0.1"},
            {"id": "dim_width", "label": "Width (or Diameter for Column)", "type": "number", "unit": "meters (m)", "default": "5", "min": "0.1", "max": "100", "step": "0.1"},
            {"id": "dim_thick", "label": "Slab Thickness / Depth", "type": "number", "unit": "centimeters (cm)", "default": "15", "min": "5", "max": "200", "step": "1"},
            {"id": "mix_ratio", "label": "Concrete Grade & Mix Ratio", "type": "select", "options": [
                ("m15", "M15 / 1:2:4 (General Foundation, Pathways)"),
                ("m20", "M20 / 1:1.5:3 (Standard Structural Slabs & Beams)"),
                ("m25", "M25 / 1:1:2 (High-Strength Columns & Footings)")
            ], "default": "m20"},
            {"id": "wastage", "label": "Wastage & Spillage Allowance", "type": "select", "options": [("1.05", "5% Extra (Typical)"), ("1.10", "10% Extra (Uneven ground)"), ("1.0", "Zero Extra (Exact Volume)")], "default": "1.05"}
        ],
        "calc_js": """
            const shape = document.getElementById('shape').value;
            const l = parseFloat(document.getElementById('dim_length').value) || 0;
            const w = parseFloat(document.getElementById('dim_width').value) || 0;
            const thickCm = parseFloat(document.getElementById('dim_thick').value) || 0;
            const mix = document.getElementById('mix_ratio').value;
            const waste = parseFloat(document.getElementById('wastage').value) || 1.05;

            let netVolM3 = 0;
            if (shape === 'slab') {
                netVolM3 = l * w * (thickCm / 100);
            } else {
                const radius = (w / 2);
                netVolM3 = Math.PI * radius * radius * l;
            }

            const grossVolM3 = netVolM3 * waste;
            const volYards3 = grossVolM3 * 1.30795;

            // Dry volume conversion factor for concrete is 1.54
            const dryVol = grossVolM3 * 1.54;
            let cementBags = 0, sandM3 = 0, gravelM3 = 0;

            if (mix === 'm15') { // 1:2:4 = 7 parts
                const cementM3 = (1 / 7) * dryVol;
                cementBags = (cementM3 * 1440) / 50; // Density 1440 kg/m3, 50kg bag
                sandM3 = (2 / 7) * dryVol;
                gravelM3 = (4 / 7) * dryVol;
            } else if (mix === 'm20') { // 1:1.5:3 = 5.5 parts
                const cementM3 = (1 / 5.5) * dryVol;
                cementBags = (cementM3 * 1440) / 50;
                sandM3 = (1.5 / 5.5) * dryVol;
                gravelM3 = (3 / 5.5) * dryVol;
            } else { // 1:1:2 = 4 parts
                const cementM3 = (1 / 4) * dryVol;
                cementBags = (cementM3 * 1440) / 50;
                sandM3 = (1 / 4) * dryVol;
                gravelM3 = (2 / 4) * dryVol;
            }

            document.getElementById('prim-val').textContent = grossVolM3.toFixed(2) + ' m³';
            document.getElementById('prim-unit').textContent = '(' + volYards3.toFixed(2) + ' cubic yards)';
            document.getElementById('m-cement-bags').textContent = Math.ceil(cementBags) + ' bags (50kg)';
            document.getElementById('m-sand').textContent = sandM3.toFixed(2) + ' m³';
            document.getElementById('m-gravel').textContent = gravelM3.toFixed(2) + ' m³';
            document.getElementById('m-weight').textContent = Math.round(grossVolM3 * 2400).toLocaleString() + ' kg';
        """,
        "metrics": [
            ("m-cement-bags", "Cement Bags Required", "50kg Bags"),
            ("m-sand", "Fine Aggregate (Sand)", "m³"),
            ("m-gravel", "Coarse Aggregate (Gravel)", "m³"),
            ("m-weight", "Total Wet Concrete Weight", "kg")
        ],
        "article": {
            "summary": "Concrete volume and mix estimation establishes precise aggregate batching quantities compliant with structural compressive strength specifications.",
            "principles": "<p>When raw dry components (cement, sand, and gravel aggregate) are mixed with water, the smaller sand grains fill the interstitial void spaces between gravel stones, and cement paste fills remaining micro-voids. Consequently, wet placed concrete shrinks by approximately 35% relative to loose dry material volume. Civil engineers apply a universal <strong>Dry Volume Factor of 1.54</strong> (meaning 1 m³ of wet concrete requires 1.54 m³ of dry ingredients) to calculate exact purchase orders.</p>",
            "formulas": "<p>Geometrical volume and dry material component batching are calculated as:</p>\\[ V_{wet} = L \\times W \\times T \\times (1 + \\text{Wastage}) \\]\\[ V_{dry} = V_{wet} \\times 1.54 \\]\\[ \\text{Cement Bags} = \\frac{\\frac{\\text{Cement Part}}{\\sum \\text{Parts}} \\times V_{dry} \\times 1,440 \\text{ kg/m}^3}{50 \\text{ kg/bag}} \\]",
            "table_title": "Standard Concrete Nominal Mix Designs (IS 456 & ACI 318)",
            "table_headers": ["Grade Designation", "Nominal Proportion (Cement : Sand : Coarse)", "28-Day Strength (f'c)", "Typical Civil Application"],
            "table_rows": [
                ["M10", "1 : 3 : 6", "10 MPa (1,450 psi)", "Plain cement concrete (PCC), non-structural base"],
                ["M15", "1 : 2 : 4", "15 MPa (2,175 psi)", "Bedding, pathway slabs, boundary walls"],
                ["M20", "1 : 1.5 : 3", "20 MPa (2,900 psi)", "Standard residential RCC slabs, beams, staircases"],
                ["M25", "1 : 1 : 2", "25 MPa (3,625 psi)", "Heavy load-bearing columns, rafts, water tanks"]
            ],
            "example": "A patio slab measures 8.0 meters long, 5.0 meters wide, and 15 cm (0.15 m) thick. Net volume = 8 × 5 × 0.15 = 6.0 m³. Adding a 5% wastage allowance gives 6.30 m³ of wet concrete (8.24 cubic yards). Multiplying by the 1.54 dry factor yields 9.70 m³ dry material. For an M20 structural mix (1:1.5:3, total 5.5 parts), cement volume = 9.70 / 5.5 = 1.764 m³. Multiplying by cement bulk density (1,440 kg/m³) yields 2,540 kg, requiring 51 bags of 50kg cement, 2.65 m³ of sand, and 5.29 m³ of gravel.",
            "faqs": [
                ("What does the 1.54 dry volume multiplier mean?", "Dry ingredients contain air pockets between particle grains. When water is added, the volume collapses by about 35%. Therefore, you must order 1.54 times the finished geometric volume in dry components."),
                ("How long does concrete take to cure to full strength?", "Concrete reaches approximately 65% to 70% compressive strength at 7 days, and achieves its certified design strength (f'c) at 28 days under moist curing."),
                ("What is the slump test?", "A slump test measures the workability and consistency of fresh concrete before placement. A standard cone is filled with concrete and inverted; the subsidence (slump in mm or inches) indicates moisture content and placement ease.")
            ]
        }
    },

    # 3. Rebar Weight & Spacing
    {
        "slug": "rebar-calculator.html",
        "title": "Rebar Weight & Grid Spacing Calculator",
        "category": "Civil & Construction",
        "cat_slug": "civil.html",
        "icon": "🔩",
        "badge": "ASTM A615 & Eurocode 2",
        "meta_desc": "Calculate total reinforcing steel (rebar) linear length, bar counts, and total weight in kilograms and pounds based on grid spacing, slab dimensions, and lap splices.",
        "keywords": "rebar calculator, rebar weight calculator, reinforcing steel weight, rebar spacing calculator, rebar weight per meter",
        "formula_preview": "Weight (kg/m) = D² / 162.2 (where D is bar diameter in mm)",
        "inputs": [
            {"id": "slab_length", "label": "Slab / Wall Length", "type": "number", "unit": "meters (m)", "default": "10", "min": "0.5", "max": "200", "step": "0.5"},
            {"id": "slab_width", "label": "Slab / Wall Width", "type": "number", "unit": "meters (m)", "default": "6", "min": "0.5", "max": "200", "step": "0.5"},
            {"id": "bar_diameter", "label": "Rebar Bar Diameter Size", "type": "select", "options": [
                ("8", "8 mm (#2.5) — 0.395 kg/m"),
                ("10", "10 mm (#3) — 0.617 kg/m"),
                ("12", "12 mm (#4) — 0.888 kg/m"),
                ("16", "16 mm (#5) — 1.578 kg/m"),
                ("20", "20 mm (#6) — 2.466 kg/m"),
                ("25", "25 mm (#8) — 3.853 kg/m")
            ], "default": "12"},
            {"id": "grid_spacing", "label": "Grid Center-to-Center Spacing", "type": "number", "unit": "mm (c/c)", "default": "150", "min": "50", "max": "500", "step": "25"},
            {"id": "layers", "label": "Reinforcement Layers (Mat)", "type": "select", "options": [
                ("1", "Single Mat Grid (Bottom Layer Only)"),
                ("2", "Double Mat Grid (Top & Bottom Meshes)")
            ], "default": "1"},
            {"id": "lap_splice", "label": "Lap Splice Allowance", "type": "select", "options": [
                ("1.10", "10% Extra (Standard Lapping)"),
                ("1.15", "15% Extra (Complex / High Lap Density)")
            ], "default": "1.10"}
        ],
        "calc_js": """
            const l = parseFloat(document.getElementById('slab_length').value) || 0;
            const w = parseFloat(document.getElementById('slab_width').value) || 0;
            const d = parseFloat(document.getElementById('bar_diameter').value) || 12;
            const s = (parseFloat(document.getElementById('grid_spacing').value) || 150) / 1000;
            const layers = parseFloat(document.getElementById('layers').value) || 1;
            const lap = parseFloat(document.getElementById('lap_splice').value) || 1.10;

            // Number of bars in each direction
            const numBarsLengthwise = Math.floor(w / s) + 1;
            const numBarsWidthwise = Math.floor(l / s) + 1;

            const totalLengthMeters = ((numBarsLengthwise * l) + (numBarsWidthwise * w)) * layers * lap;
            const unitWeightKgM = (d * d) / 162.2;
            const totalWeightKg = totalLengthMeters * unitWeightKgM;
            const totalWeightLbs = totalWeightKg * 2.20462;
            const numStandard12mBars = Math.ceil(totalLengthMeters / 12);

            document.getElementById('prim-val').textContent = Math.round(totalWeightKg).toLocaleString() + ' kg';
            document.getElementById('prim-unit').textContent = '(' + Math.round(totalWeightLbs).toLocaleString() + ' lbs)';
            document.getElementById('m-length').textContent = Math.round(totalLengthMeters) + ' m';
            document.getElementById('m-bars12m').textContent = numStandard12mBars + ' bars (12m standard)';
            document.getElementById('m-unit-wt').textContent = unitWeightKgM.toFixed(3) + ' kg/m';
            document.getElementById('m-total-bars').textContent = ((numBarsLengthwise + numBarsWidthwise) * layers) + ' cuts';
        """,
        "metrics": [
            ("m-length", "Total Running Length", "Meters"),
            ("m-bars12m", "Standard Commercial Bars (12m)", "Count"),
            ("m-unit-wt", "Unit Weight of Selected Bar", "kg / m"),
            ("m-total-bars", "Total Cut Bars Required", "Pieces")
        ],
        "article": {
            "summary": "Concrete possesses immense compressive strength but poor tensile capacity. Deformed steel reinforcement bars (rebar) absorb tensile and shearing stresses.",
            "principles": "<p>In structural elements such as reinforced concrete slabs, flexural loading generates compression on the top surface and intense tension along the bottom fibers. Concrete tensile strength is merely 8% to 12% of its compressive rating. Embedding high-yield deformed carbon steel rebar (typically ASTM Grade 60 or B500B with yield strength \\(f_y = 400\\text{--}500\\text{ MPa}\\)) resists tensile cracking and structural collapse.</p>",
            "formulas": "<p>Theoretical rebar weight per linear meter derives directly from the steel volumetric density of \\(7,850\\text{ kg/m}^3\\):</p>\\[ W_{\\text{linear}} = \\frac{\\pi D^2}{4} \\times 7,850 \\times 10^{-6} = \\frac{D^2}{162.28} \\text{ (kg/m)} \\]\\[ M_{\\text{total}} = L_{\\text{total}} \\times \\left(\\frac{D^2}{162.2}\\right) \\times K_{\\text{lap}} \\]",
            "table_title": "Standard Metric & Imperial Rebar Specifications",
            "table_headers": ["Metric Bar Size", "US Imperial Size", "Nominal Diameter (mm)", "Nominal Area (mm²)", "Unit Weight (kg/m)"],
            "table_rows": [
                ["8 mm", "#2.5", "8.0 mm", "50.3 mm²", "0.395 kg/m (0.265 lb/ft)"],
                ["10 mm", "#3", "9.5 mm", "71.0 mm²", "0.617 kg/m (0.414 lb/ft)"],
                ["12 mm", "#4", "12.7 mm", "113.1 mm²", "0.888 kg/m (0.596 lb/ft)"],
                ["16 mm", "#5", "15.9 mm", "201.1 mm²", "1.578 kg/m (1.060 lb/ft)"],
                ["20 mm", "#6", "19.1 mm", "314.2 mm²", "2.466 kg/m (1.657 lb/ft)"],
                ["25 mm", "#8", "25.4 mm", "490.9 mm²", "3.853 kg/m (2.590 lb/ft)"]
            ],
            "example": "A 10m × 6m foundation raft slab requires a 12mm rebar mesh at 150 mm center-to-center spacing in a single layer with a 10% lap splice allowance. Lengthwise bars = (6 / 0.15) + 1 = 41 bars of 10m length = 410m. Widthwise bars = (10 / 0.15) + 1 = 68 bars of 6m length = 408m. Total raw length = 818m. Factoring 10% lap gives 899.8m. For 12mm rebar, unit weight = 12² / 162.2 = 0.888 kg/m. Total steel weight = 899.8 × 0.888 = 799 kg (0.80 metric tons, or 75 standard 12-meter commercial stock bars).",
            "faqs": [
                ("Why does the formula use 162.2?", "Steel has a density of 7,850 kg/m³. When calculating mass for a circular cross-section per meter length, the algebra simplifies to: D² × (π/4) × 7,850 / 10⁶ = D² / 162.28."),
                ("What is concrete clear cover?", "Clear cover is the physical distance between the outer surface of the rebar and the nearest exterior concrete face. It protects the steel from environmental corrosion and fire exposure (typically 25mm for slabs, 40mm for beams/columns, and 50–75mm for soil-contact footings)."),
                ("What is a lap splice?", "Because commercial steel bars are manufactured in fixed lengths (usually 12 meters / 40 feet), continuous runs require overlapping parallel bars. Structural codes typically mandate a lap splice length of 40 to 50 times the bar diameter.")
            ]
        }
    },

    # 4. Chemical Dosing Rate
    {
        "slug": "chemical-dosing-calculator.html",
        "title": "Chemical Dosing Rate Calculator",
        "category": "Chemical & Water Treatment",
        "cat_slug": "chemical.html",
        "icon": "🧪",
        "badge": "AWWA & EPA Standards",
        "meta_desc": "Calculate chemical feed rate in kg/day, lbs/day, and dosing pump stroke volumetric flow in Liters/hr (LPH) based on water plant flow rate, target ppm dosage, and chemical solution purity.",
        "keywords": "chemical dosing calculator, water treatment chemical feed rate, ppm to kg per day, dosing pump lph calculator, coagulant dosing rate",
        "formula_preview": "Feed Rate (kg/day) = [Flow (m³/day) × Target ppm] / (Purity% × 1000)",
        "inputs": [
            {"id": "water_flow", "label": "Water Treatment Flow Rate", "type": "number", "unit": "m³ / hour", "default": "50", "min": "0.1", "max": "50000", "step": "1"},
            {"id": "target_ppm", "label": "Target Chemical Dosage", "type": "number", "unit": "mg/L (ppm)", "default": "15", "min": "0.1", "max": "500", "step": "0.5"},
            {"id": "chem_purity", "label": "Chemical Active Concentration / Purity", "type": "number", "unit": "%", "default": "40", "min": "1", "max": "100", "step": "1"},
            {"id": "chem_density", "label": "Solution Specific Gravity (Density)", "type": "number", "unit": "g/cm³ (kg/L)", "default": "1.25", "min": "0.8", "max": "2.0", "step": "0.01"},
            {"id": "operating_hours", "label": "Daily Plant Operating Hours", "type": "number", "unit": "hours / day", "default": "24", "min": "1", "max": "24", "step": "1"}
        ],
        "calc_js": """
            const flowM3h = parseFloat(document.getElementById('water_flow').value) || 0;
            const ppm = parseFloat(document.getElementById('target_ppm').value) || 0;
            const purity = (parseFloat(document.getElementById('chem_purity').value) || 100) / 100;
            const sg = parseFloat(document.getElementById('chem_density').value) || 1.0;
            const hours = parseFloat(document.getElementById('operating_hours').value) || 24;

            // 1 mg/L = 1 g/m3. Pure chemical per hour = Flow (m3/h) * ppm (g/m3) = grams/h = kg/h / 1000
            const pureChemKgPerHour = (flowM3h * ppm) / 1000;
            const pureChemKgPerDay = pureChemKgPerHour * hours;

            // Factoring in solution purity and specific gravity
            const grossSolutionKgPerHour = pureChemKgPerHour / purity;
            const grossSolutionKgPerDay = grossSolutionKgPerHour * hours;
            const dosingPumpLph = grossSolutionKgPerHour / sg; // Liters per hour
            const lbsPerDay = grossSolutionKgPerDay * 2.20462;

            document.getElementById('prim-val').textContent = dosingPumpLph.toFixed(2) + ' L/h';
            document.getElementById('prim-unit').textContent = '(' + grossSolutionKgPerDay.toFixed(1) + ' kg/day solution)';
            document.getElementById('m-pure-kg').textContent = pureChemKgPerDay.toFixed(2) + ' kg/day';
            document.getElementById('m-lbs').textContent = lbsPerDay.toFixed(1) + ' lbs/day';
            document.getElementById('m-daily-l').textContent = (dosingPumpLph * hours).toFixed(1) + ' Liters';
            document.getElementById('m-gph').textContent = (dosingPumpLph * 0.264172).toFixed(2) + ' GPH';
        """,
        "metrics": [
            ("m-pure-kg", "100% Active Chemical", "kg / day"),
            ("m-lbs", "Total Chemical Weight", "lbs / day"),
            ("m-daily-l", "Daily Solution Volume", "Liters / day"),
            ("m-gph", "Pump Flow in Gallons/Hr", "GPH")
        ],
        "article": {
            "summary": "Accurate dosing rates ensure effective coagulation, disinfection, or pH neutralization in municipal and industrial water treatment without hazardous overdosing.",
            "principles": "<p>In municipal potable drinking water plants, industrial effluent wastewater remediation, and reverse osmosis (RO) desalination facilities, chemical reagents (such as liquid alum, polyaluminum chloride, sodium hypochlorite, and caustic soda) are delivered via positive displacement metering diaphragm pumps. Sizing the dosing pump throughput requires converting target concentration (parts per million or mg/L) into volumetric delivery factoring in commercial solution purity and specific gravity.</p>",
            "formulas": "<p>The chemical feed rate and positive displacement pump flow rate are governed by mass conservation:</p>\\[ \\dot{m}_{pure} = Q_{\\text{water}} \\times C_{\\text{ppm}} \\times 10^{-3} \\text{ (kg/hr)} \\]\\[ Q_{\\text{pump}} (\\text{L/hr}) = \\frac{\\dot{m}_{pure}}{\\left(\\frac{\\text{Purity}\\%}{100}\\right) \\times \\rho_{\\text{solution}}} \\]",
            "table_title": "Common Water Treatment Chemicals & Properties",
            "table_headers": ["Chemical Name", "Standard Form", "Typical Commercial Purity", "Specific Gravity (g/cm³)", "Target Function"],
            "table_rows": [
                ["Alum (Aluminum Sulfate)", "Liquid Solution", "48% – 50%", "1.32 – 1.34", "Primary coagulant for turbidity removal"],
                ["Sodium Hypochlorite (Bleach)", "Liquid Solution", "10% – 15%", "1.18 – 1.22", "Disinfection & biological oxidation"],
                ["Sodium Hydroxide (Caustic Soda)", "Liquid Solution", "50%", "1.52", "pH elevation & alkalinity adjustment"],
                ["Sulfuric Acid", "Concentrated Liquid", "93% – 98%", "1.83", "pH reduction & RO acid dosing"],
                ["Polyaluminum Chloride (PAC)", "Liquid Solution", "30% – 32%", "1.20 – 1.25", "High-efficiency flocculant"]
            ],
            "example": "A municipal filtration facility treats 50 m³/hr of river water operating 24 hours daily. The jar test establishes a required alum coagulant dosage of 15 mg/L (ppm). The commercial liquid alum supplied is 40% active concentration with a specific gravity of 1.25 kg/L. Pure alum mass rate = 50 m³/hr × 15 g/m³ = 750 g/hr = 0.75 kg/hr (18 kg/day). Accounting for 40% purity requires 0.75 / 0.40 = 1.875 kg/hr of gross commercial solution. Dividing by the density (1.25 kg/L) determines the dosing pump flow setting: 1.50 Liters per hour (36 Liters per day).",
            "faqs": [
                ("What does 1 ppm equal in metric units?", "In aqueous solutions with water density of 1,000 kg/m³, 1 part per million (ppm) equals exactly 1 milligram per liter (1 mg/L) or 1 gram per cubic meter (1 g/m³)."),
                ("Why is specific gravity critical for chemical dosing?", "Many industrial chemicals are substantially denser than pure water. For example, 50% caustic soda has a specific gravity of 1.52. Neglecting density would cause a 52% volumetric dosing error."),
                ("What is a jar test?", "A jar test is a laboratory procedure simulating full-scale coagulation, flocculation, and sedimentation to experimentally determine the optimum chemical dosage required for raw water.")
            ]
        }
    }
]
