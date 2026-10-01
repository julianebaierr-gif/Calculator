import os
import json

OUTPUT_DIR = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"

def generate_header(active_cat=""):
    return f"""
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <a href="index.html#health" class="nav-link {'active' if active_cat=='health' else ''}">Health</a>
        <a href="index.html#finance" class="nav-link {'active' if active_cat=='finance' else ''}">Finance</a>
        <a href="index.html#math" class="nav-link {'active' if active_cat=='math' else ''}">Math</a>
        <a href="index.html#engineering" class="nav-link {'active' if active_cat=='engineering' else ''}">Engineering</a>
      </nav>
      <div class="header-search">
        <span class="search-icon">🔍</span>
        <input type="text" id="header-search-input" placeholder="Search 20+ calculators... (Ctrl+K)" autocomplete="off">
        <div id="search-results-dropdown" class="search-results-dropdown"></div>
      </div>
    </div>
  </header>
"""

def generate_footer():
    return """
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand-logo">
            <span class="logo-badge">∑</span>
            <span>Calc<span class="accent">Hub</span></span>
          </a>
          <p>High-precision, free online calculators designed according to published mathematical, clinical, and industrial engineering standards. 100% free, browser-based, with zero tracking.</p>
        </div>
        <div class="footer-col">
          <h4>Health & Fitness</h4>
          <ul class="footer-links">
            <li><a href="bmi-calculator.html">BMI Calculator</a></li>
            <li><a href="calorie-calculator.html">Calorie Calculator (TDEE)</a></li>
            <li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
            <li><a href="ideal-weight-calculator.html">Ideal Body Weight</a></li>
            <li><a href="water-intake-calculator.html">Daily Water Intake</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Finance & Money</h4>
          <ul class="footer-links">
            <li><a href="loan-emi-calculator.html">Loan EMI Calculator</a></li>
            <li><a href="compound-interest-calculator.html">Compound Interest</a></li>
            <li><a href="simple-interest-calculator.html">Simple Interest</a></li>
            <li><a href="discount-calculator.html">Discount & Sale</a></li>
            <li><a href="salary-calculator.html">Salary / Paycheck</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Math & Engineering</h4>
          <ul class="footer-links">
            <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
            <li><a href="age-calculator.html">Exact Age Calculator</a></li>
            <li><a href="ohms-law-calculator.html">Ohm's Law Calculator</a></li>
            <li><a href="voltage-drop-calculator.html">Voltage Drop (NEC/IEC)</a></li>
            <li><a href="cable-sizing-calculator.html">Cable Sizing Calculator</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CalcHub. All rights reserved. Mathematical tools are for educational and guidance purposes.</p>
        <div>
          <a href="sitemap.xml" style="color:#64748B;margin-left:1rem;">Sitemap</a>
          <a href="index.html" style="color:#64748B;margin-left:1rem;">Privacy & Terms</a>
        </div>
      </div>
    </div>
  </footer>
"""

print("Base layout helper defined.")
