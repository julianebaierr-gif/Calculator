# -*- coding: utf-8 -*-
"""
Helper script to register Batch 41 calculators in fix_all_visibility.py and apply_sidebars_all.py
"""

# 1. Update fix_all_visibility.py
with open("scripts/fix_all_visibility.py", "r", encoding="utf-8") as f:
    fav = f.read()

# Add time-card to finance
fav_fin_target = '("overtime-calculator.html", "Overtime Pay Calculator", "💼", "FLSA time-and-a-half, regular rate & CA double time", "W_ot = 1.5·R_reg | CA Daily 2.0x Double Time"),'
fav_fin_add = fav_fin_target + '\n            ("time-card-calculator.html", "Time Card & Weekly Timesheet", "💼", "7-day timesheet, daily & weekly overtime & gross pay", "W_gross = (H_reg · R) + (H_ot · 1.5R) | FLSA 785.48"),'

if fav_fin_target in fav and "time-card-calculator.html" not in fav:
    fav = fav.replace(fav_fin_target, fav_fin_add, 1)

# Add time-duration and weeks-between-dates to datetime
fav_dt_target = '("time-calculator.html", "Time Calculator (Sexagesimal)", "⏰", "Add, subtract, multiply, divide durations & takt time", "T_sec = H·3600 + M·60 + S | Takt = T_avail/D"),'
fav_dt_add = fav_dt_target + '''
            ("time-duration-calculator.html", "Time Duration Calculator", "⏱️", "Exact elapsed duration, decimal hours & ISO 8601", "Δt = t_end - t_start | P[n]DT[n]H[n]M[n]S"),
            ("weeks-between-dates-calculator.html", "Weeks Between Dates", "📅", "Full weeks, days, decimal weeks & gestation age", "W = ⌊ΔD / 7⌋ | D_rem = ΔD mod 7 | 40w Gestation"),'''

if fav_dt_target in fav and "time-duration-calculator.html" not in fav:
    fav = fav.replace(fav_dt_target, fav_dt_add, 1)

# Add engineering tools to engineering.html
fav_eng_target = '("neutral-conductor-sizing-calculator.html", "Neutral Conductor Sizing", "⚡", "3-Phase unbalance, triplen harmonics & NEC 220.61 reduction", "In_fund = √(Ia²+...+Ic² - IaIb...) | Triplen In_3rd = 3·Ih3"),'
fav_eng_add = fav_eng_target + '''
            ("best-engineering-calculator.html", "Best Engineering Calculator Guide", "🖩", "NCEES FE/PE exam legal models, Casio vs TI vs HP", "NCEES FE/PE Approved | TI-36X Pro & Casio ClassWiz"),
            ("cable-sizing-guide.html", "Cable Sizing Guide & Selection", "🔌", "IEC 60364-5-52, BS 7671, NEC 310 ampacity & drop", "Iz = Ib / (Ca·Cg·Ci) | k²S² ≥ I²t | 3% Drop"),
            ("engineering-formulas.html", "Engineering Formulas Compendium", "📐", "Master multi-discipline formulas & live equation solver", "σ = My/I | hf = f(L/D)(v²/2g) | P = √3·VI·cosφ"),'''

if fav_eng_target in fav and "cable-sizing-guide.html" not in fav:
    fav = fav.replace(fav_eng_target, fav_eng_add, 1)

with open("scripts/fix_all_visibility.py", "w", encoding="utf-8") as f:
    f.write(fav)
print("Updated fix_all_visibility.py successfully!")


# 2. Update apply_sidebars_all.py
with open("scripts/apply_sidebars_all.py", "r", encoding="utf-8") as f:
    asa = f.read()

asa_fin_target = '("overtime-calculator.html", "Overtime Pay Calculator", "💼", "FLSA time-and-a-half, regular rate & CA double time"),'
asa_fin_add = asa_fin_target + '\n            ("time-card-calculator.html", "Time Card Calculator", "💼", "7-day timesheet, daily/weekly overtime & gross pay"),'

if asa_fin_target in asa and "time-card-calculator.html" not in asa:
    asa = asa.replace(asa_fin_target, asa_fin_add, 1)

asa_dt_target = '("time-calculator.html", "Time Calculator (Sexagesimal)", "⏰", "Add, subtract, multiply, divide durations & takt time"),'
asa_dt_add = asa_dt_target + '''
            ("time-duration-calculator.html", "Time Duration Calculator", "⏱️", "Exact elapsed duration, decimal hours & ISO 8601"),
            ("weeks-between-dates-calculator.html", "Weeks Between Dates", "📅", "Full weeks, days, decimal weeks & gestation age"),'''

if asa_dt_target in asa and "time-duration-calculator.html" not in asa:
    asa = asa.replace(asa_dt_target, asa_dt_add, 1)

asa_eng_target = '("neutral-conductor-sizing-calculator.html", "Neutral Conductor Sizing", "⚡", "3-Phase unbalance, triplen harmonics & NEC 220.61 reduction"),'
asa_eng_add = asa_eng_target + '''
            ("best-engineering-calculator.html", "Best Engineering Calculator Guide", "🖩", "NCEES FE/PE exam legal models, Casio vs TI vs HP"),
            ("cable-sizing-guide.html", "Cable Sizing Guide & Selection", "🔌", "IEC 60364-5-52, BS 7671, NEC 310 ampacity & drop"),
            ("engineering-formulas.html", "Engineering Formulas Compendium", "📐", "Master multi-discipline formulas & live equation solver"),'''

if asa_eng_target in asa and "cable-sizing-guide.html" not in asa:
    asa = asa.replace(asa_eng_target, asa_eng_add, 1)

# Update determine_tool_cat in apply_sidebars_all.py
asa = asa.replace('"smoking-cost", "retirement", "overtime"', '"smoking-cost", "retirement", "overtime", "time-card"')
asa = asa.replace('"neutral-conductor"]', '"neutral-conductor", "best-engineering", "cable-sizing-guide", "engineering-formulas"]')
asa = asa.replace('"quarter-of-year", "time-calculator"]', '"quarter-of-year", "time-calculator", "time-duration", "weeks-between-dates"]')

with open("scripts/apply_sidebars_all.py", "w", encoding="utf-8") as f:
    f.write(asa)
print("Updated apply_sidebars_all.py successfully!")
