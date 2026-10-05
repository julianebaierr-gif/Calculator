# -*- coding: utf-8 -*-
"""
Patch script to expand articles in gen_batch41_part1.py to exceed 1,150+ words
"""

with open("scripts/gen_batch41_part1.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Expand time-duration-calculator
td_extra = """
<h2>Specialized Applications: Athletic Chronometry and High-Precision Lap Splits</h2>
<p>In Olympic track and field, motorsport telemetry (Formula 1, NASCAR), and competitive swimming, time duration calculations require sub-second millisecond resolution governed by international governing bodies (World Athletics, FIA, World Aquatics). At velocities exceeding 300 km/h in Formula 1 racing, an interval of just 0.001 seconds (1 millisecond) represents approximately 8.33 centimeters of physical track displacement. Chronometric timing systems employ transponder loops embedded in the circuit asphalt that generate differential time splits:</p>

$$\Delta t_{\text{split}} = t_{\text{sector, } k} - t_{\text{sector, } k-1}$$

<p>Accumulating lap sectors into total race duration requires high-precision sexagesimal floating-point addition that prevents IEEE 754 binary floating-point roundoff drift over multi-hour endurance events like the 24 Hours of Le Mans.</p>

<h2>Relational Databases and SQL Temporal Duration Modeling</h2>
<p>In enterprise software architecture and data warehousing (PostgreSQL, Oracle, Snowflake, MySQL), durations are stored using specialized temporal data types such as SQL standard <code>INTERVAL DAY TO SECOND</code>. Evaluating differences between timestamps utilizes statutory SQL functions:</p>
<pre><code>-- PostgreSQL exact duration extraction
SELECT AGE(end_timestamp, start_timestamp) AS calendar_span,
       EXTRACT(EPOCH FROM (end_timestamp - start_timestamp)) AS elapsed_seconds;
</code></pre>
<p>Engineers must exercise care when querying durations across Daylight Saving Time adjustments: calculating duration from naive local timestamp columns without timezone offsets (<code>TIMESTAMP WITHOUT TIME ZONE</code>) introduces a 1-hour discrepancy twice annually during clock transitions.</p>
"""

# 2. Expand weeks-between-dates-calculator
wb_extra = """
<h2>Academic Semester Planning and Accreditation Credit Hour Standards</h2>
<p>Higher education institutions accredited in the United States operate under Department of Education Title IV regulations (34 CFR § 600.2) defining the statutory <strong>credit hour</strong>. A standard academic semester spans exactly 15 to 16 calendar weeks, comprising 14 weeks of formal direct instruction and 1 week of final examinations. One semester credit hour legally mandates a minimum of 1 hour (50 minutes) of classroom instruction plus 2 hours of out-of-class student work per week across the 15-week term:</p>

$$\text{Direct Instruction Time} = 15 \text{ weeks} \times 50 \text{ minutes} = 750 \text{ minutes} = 12.5 \text{ hours per credit}$$

<p>University registrars and curriculum committees compute weeks between term start and graduation dates to certify that accelerated summer terms (typically 6, 8, or 10 weeks) deliver identical cumulative contact hours by proportionally increasing weekly lecture durations.</p>

<h2>Commercial Agriculture and Phenological Crop Maturation Horizons</h2>
<p>In commercial agronomy, crop production cycles from seed germination to harvest are quantified in standardized calendar week horizons. For instance, greenhouse floriculture schedules poinsettia planting precisely 14 to 16 weeks prior to the Thanksgiving holiday. In poultry farming and livestock management, broiler chicken production operates on an exact 6- to 8-week growth cycle, while bovine gestation spans an average of 40.5 weeks (283 days). Measuring elapsed weeks allows automated feeding and climate control systems to transition through calibrated nutritional growth phases.</p>
"""

# 3. Expand best-engineering-calculator
be_extra = """
<h2>Power Subsystems: Rechargeable Lithium-Ion vs. Alkaline and Solar Arrays</h2>
<p>A crucial practical differentiator among engineering calculators is their internal power architecture. Models like the Casio fx-991EX and TI-36X Pro utilize hybrid <strong>Two-Way Power (Solar + Battery)</strong>, combining a high-efficiency photovoltaic cell with an LR44 or CR2032 button cell backup. These units operate reliably for 2 to 5 years without maintenance, making them ideal for field engineers, offshore rigs, and examination halls where dead batteries cause catastrophic failure.</p>

<p>Conversely, advanced graphing and CAS models (TI-Nspire CX II CAS, HP Prime v2, TI-84 Plus CE) feature backlit color LCD screens and high-frequency ARM processors that demand rechargeable 3.7V lithium-ion battery packs. While rechargeable via standard USB-C or micro-USB cables, they require periodic recharging every 1 to 2 weeks of intensive mathematical modeling.</p>

<h2>Software Emulators, Cloud Notebooks, and Examination Policies</h2>
<p>While physical hardware calculators remain mandatory in proctored examination settings, professional practicing engineers routinely augment physical devices with software simulation suites. Official PC and Mac emulator licenses (such as TI-SmartView and Casio ClassWiz Emulator) allow engineering professors and corporate trainers to project live calculator screens during technical lectures. Outside testing centers, cloud computing environments like Jupyter Notebooks running Python with NumPy, SymPy, and SciPy provide infinite mathematical power, complementing the handheld device for large-scale engineering R&D.</p>
"""

# Apply patches before <section class="faq-section"> in respective functions
if '<section class="faq-section">' in code:
    parts = code.split('<section class="faq-section">')
    # parts[0] is time_card
    # parts[1] is time_duration
    # parts[2] is weeks_between_dates
    # parts[3] is best_engineering
    if len(parts) == 5:
        new_code = (
            parts[0] + '<section class="faq-section">' +
            parts[1] + td_extra + '<section class="faq-section">' +
            parts[2] + wb_extra + '<section class="faq-section">' +
            parts[3] + be_extra + '<section class="faq-section">' +
            parts[4]
        )
        with open("scripts/gen_batch41_part1.py", "w", encoding="utf-8") as f:
            f.write(new_code)
        print("Successfully expanded gen_batch41_part1.py!")
    else:
        print(f"Parts length unexpected: {len(parts)}")
