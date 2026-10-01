# 🧮 CalcHub — High-Precision Online Calculators Suite

A production-grade suite of **20 specialized, high-precision web calculators** engineered according to published international mathematical, clinical (WHO), financial, and industrial engineering standards (IEC 60364 & NEC NFPA 70).

---

## 🌟 Key Features

* **100% Light Theme Design:** Clean, modern, high-contrast aesthetic crafted for long-session readability and professional trust. Pure white, soft slate, and electric indigo typography.
* **Instant Client-Side Computation:** Zero server lag, 100% private, zero user registration, and INP (Interaction to Next Paint) under 50ms.
* **GEO (Generative Engine Optimization) / LLMO Ready:** High-priority citation definition boxes (`.geo-citation-box`) tailored for direct attribution in Google AI Overviews, Perplexity, and ChatGPT Search.
* **Level 1–6 Technical SEO:**
  * Clean semantic static URLs with automated extension stripping via `vercel.json`.
  * Advanced JSON-LD Schema on every page: `WebApplication`, `MathSolver`, `FAQPage`, `BreadcrumbList`, and `Organization`.
  * Interactive Table of Contents (TOC) generating Google Mini Sitelinks.
  * Anti-scraper self-referencing canonical structure.
  * Anti-crawl trap `robots.txt` blocking duplicate parameter queries (`/?s=*`, `/?q=*`).
  * Dynamic `sitemap.xml` with verified priority scoring.
  * Instant Indexing Protocol script for Bing IndexNow and Google Sitemap pinging.

---

## 📂 Live Calculator Directory (20 Initial Production Tools)

### ⚖️ Health & Fitness Silo
1. **BMI Calculator** (`bmi-calculator.html`): Metric & Imperial, WHO categories, BMI Prime, and Ponderal Index.
2. **Calorie Calculator (TDEE)** (`calorie-calculator.html`): Clinical Mifflin-St Jeor formula, BMR, and deficit/surplus goals.
3. **Body Fat Calculator** (`body-fat-calculator.html`): US Navy circumference method, lean body mass, and fat mass in kg.
4. **Ideal Body Weight Calculator** (`ideal-weight-calculator.html`): Devine, Robinson, Miller, and Hamwi medical equations.
5. **Daily Water Intake Calculator** (`water-intake-calculator.html`): NASEM hydration standards with exercise and climate scaling.

### 🏦 Finance & Investment Silo
6. **Loan EMI Calculator** (`loan-emi-calculator.html`): Reducing-balance amortization, monthly installment, and visual P vs I ratio bar.
7. **Compound Interest Calculator** (`compound-interest-calculator.html`): Exponential wealth accumulation, recurring monthly deposits, and Rule of 72.
8. **Simple Interest Calculator** (`simple-interest-calculator.html`): Linear $I = P \cdot R \cdot T / 100$ calculations and maturity values.
9. **Discount & Sale Calculator** (`discount-calculator.html`): Sequential coupon stacking, percentage markdowns, and sales tax.
10. **Salary / Paycheck Calculator** (`salary-calculator.html`): 2,080 annual work hours standard, hourly-to-salary, bi-weekly, and monthly pay.

### 🔢 Mathematics & Daily Utilities Silo
11. **Percentage Calculator** (`percentage-calculator.html`): Multi-mode solver (X% of Y, X is what % of Y, Percentage change).
12. **Exact Age Calculator** (`age-calculator.html`): Gregorian leap-year math, exact years/months/days, and next birthday countdown.
13. **GPA Calculator** (`gpa-calculator.html`): 4.0 collegiate grading scale, course credit weighting, and Latin Honors predictions.
14. **Fraction Calculator** (`fraction-calculator.html`): Add, subtract, multiply, and divide fractions with automated LCD and GCD reduction.
15. **Ratio Calculator & Simplifier** (`ratio-calculator.html`): Ratio simplification to lowest terms and proportion solver ($A:B = C:X$).

### ⚡ Technical & Electrical Engineering Silo
16. **Ohm's Law Calculator** (`ohms-law-calculator.html`): Circular 12-equation Ohm's law wheel solving Volts, Amps, Ohms, and Watts.
17. **Voltage Drop Calculator** (`voltage-drop-calculator.html`): NEC 210.19 and IEC 60364 compliant single-phase and 3-phase conductor voltage drop.
18. **Cable Sizing Calculator** (`cable-sizing-calculator.html`): IEC 60364-5-52 and BS 7671 standard, temperature derating ($C_a$), and grouping factors ($C_g$).
19. **Resistor Color Code Calculator** (`resistor-color-code-calculator.html`): Interactive visual SVG resistor with real-time colored bands and tolerance bounds.
20. **Solar Panel & Battery Sizing** (`solar-panel-sizing-calculator.html`): Peak Sun Hours (PSh), PV array wattage, panel counts, and LiFePO4 battery bank capacity.

---

## 🚀 How to Push to GitHub & Deploy on Vercel

### Step 1: Push Local Code to GitHub

1. Open your terminal in this directory:
   ```bash
   cd C:\Users\Admin\.gemini\antigravity\scratch\calchub
   ```
2. Create a new empty repository on your **[GitHub](https://github.com/new)** (e.g. named `calchub` or `online-calculators`).
3. Connect your local git repository and push:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy to Vercel (1-Click)

1. Log in to **[Vercel](https://vercel.com/)**.
2. Click **"Add New Project"** and select **"Import Git Repository"**.
3. Choose the repository you just pushed.
4. Framework Preset: Leave as **Other / None** (Vercel automatically recognizes static HTML/CSS/JS and the included `vercel.json`).
5. Click **"Deploy"**.

Your website will be live worldwide across Vercel's Global Edge Network with free SSL, clean URLs, and instant cache invalidation!

---

## 🛠️ Project Structure

```
calchub/
├── index.html                   # Main portal hub with Silo categories & quick search
├── 404.html                     # Custom light theme 404 error page
├── styles.css                   # Master light theme design system
├── app.js                       # Global search, toast, and copy/print utilities
├── robots.txt                   # Strict SEO crawl-budget rules
├── sitemap.xml                  # Validated XML sitemap for all 21 URLs
├── vercel.json                  # Clean URLs and security headers configuration
├── ping_indexnow.py             # Instant Indexing Protocol for Bing & Google
├── .gitignore                   # Standard ignore rules
│
├── [20 Live Calculator Pages]   # Complete calculator HTML files with schemas & articles
└── scripts/                     # Automation & generation utilities
```

---

## 📜 License & Compliance
Mathematical calculations are based on published public domain standards (WHO, NASEM, IEC, NEC, EIA). Free for commercial and non-commercial educational use.
