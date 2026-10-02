import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEADER_HTML = """  <!-- Sticky Header -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="finance.html" class="nav-link{FIN_ACTIVE}">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="engineering.html" class="nav-link{EE_ACTIVE}">⚡ Electrical</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
        </div>
        <div class="nav-row">
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
          <a href="fire-safety.html" class="nav-link">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>"""

FOOTER_HTML = """  <!-- Footer -->
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col">
        <div class="brand-logo" style="margin-bottom:0.75rem;">
          <span class="logo-badge">∑</span>
          <span>Calc<span class="accent">Hub</span></span>
        </div>
        <p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;">
          Professional engineering, financial, health, and academic calculation suite. Built for precision, regulatory compliance, and verified decision-making.
        </p>
      </div>
      <div class="footer-col">
        <h4 class="footer-col-title">Engineering</h4>
        <ul class="footer-links">
          <li><a href="engineering.html">Electrical Engineering</a></li>
          <li><a href="solar-energy.html">Solar PV &amp; Storage</a></li>
          <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
          <li><a href="civil.html">Civil &amp; Structural</a></li>
          <li><a href="chemical.html">Chemical &amp; Water</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-col-title">Everyday Hubs</h4>
        <ul class="footer-links">
          <li><a href="finance.html">Finance &amp; Loans</a></li>
          <li><a href="health.html">Health &amp; Fitness</a></li>
          <li><a href="math.html">Math &amp; Ratios</a></li>
          <li><a href="datetime.html">Date &amp; Calendar</a></li>
          <li><a href="converter.html">Unit Converter</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-col-title">Standards</h4>
        <ul class="footer-links">
          <li><a href="civil.html">ACI 318 &amp; Eurocodes</a></li>
          <li><a href="engineering.html">IEC 60364 &amp; NEC NFPA 70</a></li>
          <li><a href="mechanical.html">ASME B31 &amp; ASHRAE 183</a></li>
          <li><a href="fire-safety.html">NFPA 13 &amp; NFPA 72</a></li>
          <li><a href="programmer.html">IETF RFC 1918 &amp; CIDR</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. Professional client-side calculation engine. All algorithms verified against published standards.</p>
    </div>
  </footer>"""

print("Base layout constants ready.")
