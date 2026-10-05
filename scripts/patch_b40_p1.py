# -*- coding: utf-8 -*-
with open('scripts/gen_batch40_part1.py', 'r', encoding='utf-8') as f:
    content = f.read()

dow_extra = """
<h2>Perpetual Calendar Cycles and the 400-Year Gregorian Periodicity</h2>
<p>Because the Gregorian calendar introduces 97 leap days across every 400-year cycle, the total number of days in 400 Gregorian years is exactly:
$$400 \\times 365 + 97 = 146,097 \\text{ days}$$
Dividing 146,097 by 7 yields:
$$\\frac{146,097}{7} = 20,871 \\text{ weeks exactly with 0 remainder!}$$
This remarkable mathematical identity means that the Gregorian calendar repeats in an exact, unbroken cycle every 400 years. October 5, 2026 will fall on the exact same weekday as October 5, 2426, and fell on the same day in 1626. Furthermore, within any single century, days of the week shift forward by 1 day in standard years ($365 \\bmod 7 = 1$) and by 2 days in leap years ($366 \\bmod 7 = 2$). This simple modular shift governs all perpetual calendar mechanical wheels and digital perpetual clock algorithms.</p>

<section class="faq-section">
    <h2>Frequently Asked Questions About Day of the Week Calculations</h2>
    <div class="faq-item">
        <h3>How does Zeller's Congruence handle leap years?</h3>
        <p>Zeller's congruence handles leap years by re-indexing January and February as months 13 and 14 of the preceding year. Because February is treated as the final month of the year, leap day adjustments (February 29th) are naturally captured by the term $\\lfloor K/4 \\rfloor$ and $\\lfloor J/4 \\rfloor$ without perturbing March through December calculations.</p>
    </div>
    <div class="faq-item">
        <h3>Why did October 1582 lose 10 days?</h3>
        <p>In October 1582, Pope Gregory XIII implemented the Gregorian calendar reform to correct the 10-day drift accumulated by the Julian calendar's assumption that an astronomical solar year was exactly 365.25 days (rather than approximately 365.2422 days). To re-align the vernal equinox with March 21 for Easter computations, October 4, 1582 was immediately followed by October 15, 1582.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Doomsday rule mnemonic for months?</h3>
        <p>John Conway's Doomsday rule uses memorable calendar anchors that always share the identical day of the week within any given year: 4/4, 6/6, 8/8, 10/10, 12/12 for even months, and the mnemonic "I work 9-to-5 at 7-11" for odd months (9/5, 5/9, 7/11, 11/7).</p>
    </div>
    <div class="faq-item">
        <h3>Can Zeller's Congruence be used for dates BC / BCE?</h3>
        <p>Standard Zeller's congruence requires astronomical year numbering where 1 BC is Year 0, 2 BC is Year -1, etc. In software, negative modulo operations must also be carefully normalized to prevent incorrect weekday mappings.</p>
    </div>
</section>
"""

doy_extra = """
<h2>Agricultural Growing Degree Days and Phenological Modeling</h2>
<p>Agronomists, horticulturists, and climate scientists rely on continuous day-of-the-year numbering to track Growing Degree Days (GDD) and biological life cycle milestones (phenology). Standard calendar months introduce uneven day intervals (28 to 31 days) that distort thermal accumulation integrals. By utilizing continuous ordinal days $N$, daily mean temperatures $T_{\\text{mean}}$ above a base physiological threshold $T_{\\text{base}}$ are integrated seamlessly:
$$\\text{GDD}_{\\text{cumulative}} = \\sum_{N = N_{\\text{bio}}}^{N_{\\text{harvest}}} \\max\\left(0, \\frac{T_{\\text{max}}(N) + T_{\\text{min}}(N)}{2} - T_{\\text{base}}\\right)$$
This enables predictive harvesting models for commercial corn, wheat, viticulture, and orchard pest emergence regardless of leap year discrepancies.</p>

<h2>Satellite Orbital Telemetry and TLE Epoch Formats</h2>
<p>In aerospace geodesy and space situational awareness, North American Aerospace Defense Command (NORAD) and NASA publish Two-Line Element sets (TLE) using fractional day-of-the-year notation. For example, epoch <code>26278.41666667</code> denotes the year 2026, day 278, at precisely 10:00:00 UTC. Using ordinal days avoids sexagesimal time conversions and eliminates ambiguity across planetary coordinate reference frames.</p>

<section class="faq-section">
    <h2>Frequently Asked Questions About Day of the Year</h2>
    <div class="faq-item">
        <h3>What is an ISO 8601 Ordinal Date?</h3>
        <p>An ISO 8601 ordinal date consists of a 4-digit calendar year followed by a 3-digit continuous day count, formatted as <code>YYYY-DDD</code> (e.g., <code>2026-001</code> for January 1st, or <code>2026-365</code> for December 31st). It eliminates monthly boundaries for logistics, packaging expiry tracking, and manufacturing lot codes.</p>
    </div>
    <div class="faq-item">
        <h3>How does a leap year change the day of the year?</h3>
        <p>In a leap year, February has 29 days instead of 28. Consequently, all calendar dates from March 1st onward have an ordinal day that is 1 higher than in a common year (e.g., March 1st is Day 60 in a common year, but Day 61 in a leap year).</p>
    </div>
    <div class="faq-item">
        <h3>Why is Day of the Year preferred in solar engineering?</h3>
        <p>Day of the year provides a smooth, monotonically increasing index $N \\in [1, 365]$ that feeds directly into trigonometric equations for solar declination, equation of time, solar zenith angles, and atmospheric air mass without complex date-parsing overhead.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between Day of the Year and Julian Day?</h3>
        <p>Day of the year (ordinal day) counts days from 1 to 365 (or 366) within a single calendar year. Julian Day Number (JDN) is a continuous astronomical count of elapsed solar days since January 1, 4713 BCE (over 2.46 million days). Though often confused in legacy business programming, they are completely distinct concepts.</p>
    </div>
</section>
"""

target = '</ol>"""\n\n    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)'
parts = content.split(target)
if len(parts) == 3:
    new_content = parts[0] + '</ol>' + dow_extra + '"""\n\n    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)' + parts[1] + '</ol>' + doy_extra + '"""\n\n    return get_page_html(title, desc, slug, schema, h1, short_desc, calc_ui, article)' + parts[2]
    with open('scripts/gen_batch40_part1.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully patched gen_batch40_part1.py!")
else:
    print(f"Mismatch: found {len(parts)} parts")
