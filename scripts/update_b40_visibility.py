# -*- coding: utf-8 -*-
"""
Helper script to register Batch 40 calculators in fix_all_visibility.py and apply_sidebars_all.py
"""

import os

# 1. Update fix_all_visibility.py
with open("scripts/fix_all_visibility.py", "r", encoding="utf-8") as f:
    fav = f.read()

# Add overtime to finance
fav_fin_target = '("retirement-calculator.html", "Retirement & FIRE Planner", "🏖️", "Trinity study 4% rule, nest egg sizing & inflation", "Nest Egg = (Spend - Pension)/SWR | FIRE = 25×Expenses"),'
fav_fin_add = fav_fin_target + '\n            ("overtime-calculator.html", "Overtime Pay Calculator", "💼", "FLSA time-and-a-half, regular rate & CA double time", "W_ot = 1.5·R_reg | CA Daily 2.0x Double Time"),'

if fav_fin_target in fav and "overtime-calculator.html" not in fav:
    fav = fav.replace(fav_fin_target, fav_fin_add, 1)

# Add 7 datetime tools to datetime.html
fav_dt_target = '("date-calculator.html", "Calendar Date Calculator", "📅", "Date intervals, duration between dates, years/months/days", "Δ = Date2 - Date1 | Gregorian calendar algorithm"),'
fav_dt_add = fav_dt_target + '''
            ("day-of-week-calculator.html", "Day of the Week Calculator", "📅", "Zeller's congruence, Doomsday rule & birth weekday", "Zeller's Congruence & Conway Doomsday"),
            ("day-of-year-calculator.html", "Day of the Year Calculator", "🗓️", "Ordinal date YYYY-DDD, solar declination & year percent", "ISO 8601 YYYY-DDD | Cooper Declination"),
            ("decimal-time-calculator.html", "Decimal Time Calculator", "⏱️", "Payroll hours, French metric time & Swatch .beats", "T_dec = H + M/60 + S/3600 | French & .beat"),
            ("leap-year-calculator.html", "Leap Year Calculator", "🌍", "Gregorian 400-year cycle, astronomical tropical year", "IsLeap = (Y%4==0 && Y%100!=0) || (Y%400==0)"),
            ("months-between-dates-calculator.html", "Months Between Dates", "📅", "Calendar month diff, fractional months & 30/360 basis", "ΔM = (Y2-Y1)·12 + (M2-M1) | 30/360 & Actual"),
            ("quarter-of-year-calculator.html", "Quarter of Year Calculator", "📊", "Q1-Q4 calendar, fiscal government & retail 4-4-5", "Q = ⌈M/3⌉ | US Federal & NRF 4-4-5"),
            ("time-calculator.html", "Time Calculator (Sexagesimal)", "⏰", "Add, subtract, multiply, divide durations & takt time", "T_sec = H·3600 + M·60 + S | Takt = T_avail/D"),'''

if fav_dt_target in fav and "day-of-week-calculator.html" not in fav:
    fav = fav.replace(fav_dt_target, fav_dt_add, 1)

with open("scripts/fix_all_visibility.py", "w", encoding="utf-8") as f:
    f.write(fav)
print("Updated fix_all_visibility.py successfully!")


# 2. Update apply_sidebars_all.py
with open("scripts/apply_sidebars_all.py", "r", encoding="utf-8") as f:
    asa = f.read()

asa_fin_target = '("retirement-calculator.html", "Retirement & FIRE Planner", "🏖️", "Trinity study 4% rule, nest egg sizing & inflation"),'
asa_fin_add = asa_fin_target + '\n            ("overtime-calculator.html", "Overtime Pay Calculator", "💼", "FLSA time-and-a-half, regular rate & CA double time"),'

if asa_fin_target in asa and "overtime-calculator.html" not in asa:
    asa = asa.replace(asa_fin_target, asa_fin_add, 1)

asa_dt_target = '("date-calculator.html", "Calendar Date Calculator", "📅", "Date intervals, duration & month clamping"),'
asa_dt_add = asa_dt_target + '''
            ("day-of-week-calculator.html", "Day of the Week Calculator", "📅", "Zeller's congruence, Doomsday rule & birth weekday"),
            ("day-of-year-calculator.html", "Day of the Year Calculator", "🗓️", "Ordinal date YYYY-DDD, solar declination & year percent"),
            ("decimal-time-calculator.html", "Decimal Time Calculator", "⏱️", "Payroll hours, French metric time & Swatch .beats"),
            ("leap-year-calculator.html", "Leap Year Calculator", "🌍", "Gregorian 400-year cycle, astronomical tropical year"),
            ("months-between-dates-calculator.html", "Months Between Dates", "📅", "Calendar month diff, fractional months & 30/360 basis"),
            ("quarter-of-year-calculator.html", "Quarter of Year Calculator", "📊", "Q1-Q4 calendar, fiscal government & retail 4-4-5"),
            ("time-calculator.html", "Time Calculator (Sexagesimal)", "⏰", "Add, subtract, multiply, divide durations & takt time"),'''

if asa_dt_target in asa and "day-of-week-calculator.html" not in asa:
    asa = asa.replace(asa_dt_target, asa_dt_add, 1)

# Update determine_tool_cat
# Add overtime to finance regex/keywords
asa = asa.replace('"smoking-cost", "retirement"', '"smoking-cost", "retirement", "overtime"')

# Add new datetime tools to datetime category check
old_dt_detect = '["date-difference", "age", "hours-calculator", "week-number", "add-days-to-date", "add-time", "business-days", "countdown", "date-calculator"]'
new_dt_detect = '["date-difference", "age", "hours-calculator", "week-number", "add-days-to-date", "add-time", "business-days", "countdown", "date-calculator", "day-of-week", "day-of-year", "decimal-time", "leap-year", "months-between-dates", "quarter-of-year", "time-calculator"]'
asa = asa.replace(old_dt_detect, new_dt_detect)

with open("scripts/apply_sidebars_all.py", "w", encoding="utf-8") as f:
    f.write(asa)
print("Updated apply_sidebars_all.py successfully!")
