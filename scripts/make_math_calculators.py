import os

OUTPUT_DIR = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"
from make_health_remaining import page_scaffold

# ==========================================
# 11. PERCENTAGE CALCULATOR
# ==========================================
pct_app_json = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Percentage Calculator",
      "url": "https://calchub.org/percentage-calculator.html",
      "applicationCategory": "MathApplication",
      "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How do you calculate percentage increase or decrease?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Percentage change is calculated by subtracting the initial value from the final value, dividing by the initial value, and multiplying by 100: Percentage Change = ((Final - Initial) / Initial) × 100."
          }
        }
      ]
    }
  ]
}"""

pct_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">🔢 Multi-Mode Percentage Solver</span>
        </div>
        <form onsubmit="return false;">
          
          <!-- Mode 1: X% of Y -->
          <div style="margin-bottom:1.5rem;padding-bottom:1.25rem;border-bottom:1px solid #E2E8F0;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:0.75rem;font-size:0.95rem;">Mode 1: What is X% of Y?</div>
            <div style="display:flex;align-items:center;gap:0.75rem;flex-wrap:wrap;">
              <span style="font-weight:600;">What is</span>
              <div class="input-wrap has-unit" style="width:110px;">
                <input type="number" id="p1-x" value="15" oninput="calcP1()">
                <span class="input-unit-badge">%</span>
              </div>
              <span style="font-weight:600;">of</span>
              <div class="input-wrap" style="width:130px;">
                <input type="number" id="p1-y" value="350" oninput="calcP1()">
              </div>
              <span style="font-weight:700;color:#2563EB;">=</span>
              <span style="font-weight:800;font-size:1.2rem;color:#0F172A;font-family:var(--font-mono);" id="p1-res">52.50</span>
            </div>
          </div>

          <!-- Mode 2: X is what % of Y -->
          <div style="margin-bottom:1.5rem;padding-bottom:1.25rem;border-bottom:1px solid #E2E8F0;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:0.75rem;font-size:0.95rem;">Mode 2: X is what percentage of Y?</div>
            <div style="display:flex;align-items:center;gap:0.75rem;flex-wrap:wrap;">
              <div class="input-wrap" style="width:110px;">
                <input type="number" id="p2-x" value="45" oninput="calcP2()">
              </div>
              <span style="font-weight:600;">is what % of</span>
              <div class="input-wrap" style="width:130px;">
                <input type="number" id="p2-y" value="180" oninput="calcP2()">
              </div>
              <span style="font-weight:700;color:#2563EB;">=</span>
              <span style="font-weight:800;font-size:1.2rem;color:#0F172A;font-family:var(--font-mono);" id="p2-res">25.00%</span>
            </div>
          </div>

          <!-- Mode 3: Percentage Increase / Decrease -->
          <div>
            <div style="font-weight:700;color:#0F172A;margin-bottom:0.75rem;font-size:0.95rem;">Mode 3: Percentage Change (Increase/Decrease)</div>
            <div style="display:flex;align-items:center;gap:0.75rem;flex-wrap:wrap;">
              <span style="font-weight:600;">From</span>
              <div class="input-wrap" style="width:110px;">
                <input type="number" id="p3-x" value="80" oninput="calcP3()">
              </div>
              <span style="font-weight:600;">to</span>
              <div class="input-wrap" style="width:110px;">
                <input type="number" id="p3-y" value="120" oninput="calcP3()">
              </div>
              <span style="font-weight:700;color:#2563EB;">=</span>
              <span style="font-weight:800;font-size:1.2rem;color:#059669;font-family:var(--font-mono);" id="p3-res">+50.00%</span>
            </div>
          </div>

          <div class="calc-actions" style="margin-top:1.5rem;">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Answers</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Worksheet</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Live Calculations</span>
          <span class="status-pill status-success">Instant Real-time</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Result of Mode 1 (X% of Y)</div>
          <div>
            <span class="primary-result-value" id="card-p1">52.5</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Mode 2 Ratio</div>
            <div class="breakdown-val" id="card-p2">25.0%</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Mode 3 Change</div>
            <div class="breakdown-val" id="card-p3">+50.0%</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Absolute Difference</div>
            <div class="breakdown-val" id="card-diff">+40.0</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Multiplier Factor</div>
            <div class="breakdown-val" id="card-mult">1.50x</div>
          </div>
        </div>
      </section>
"""

pct_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>A <strong>percentage</strong> is a number or ratio expressed as a fraction of 100 (symbolized by %). The fundamental equations are:</p>
      <ul>
        <li><strong>Find percentage of a value:</strong> <code>Result = (Percentage ÷ 100) × Total</code></li>
        <li><strong>Find what percent X is of Y:</strong> <code>Percentage = (X ÷ Y) × 100</code></li>
        <li><strong>Percentage Change (Growth/Decline):</strong> <code>% Change = ((New Value - Old Value) ÷ Old Value) × 100</code></li>
      </ul>
    </section>
"""

pct_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#pct-foundations">Percentage Mathematical Foundations</a></li>
        <li><a href="#pct-points-vs-pct">Percentage Points vs. Percentage Change</a></li>
        <li><a href="#pct-worked-examples">Step-by-Step Worked Examples</a></li>
        <li><a href="#pct-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

pct_article = """
      <h2 id="pct-foundations">Percentage Mathematical Foundations</h2>
      <p>The term <em>percent</em> originates from the Latin <em>per centum</em>, meaning "by the hundred." It standardizes proportions so values of different sizes can be readily compared across commerce, statistics, and medicine.</p>

      <div class="formula-box">
        <div class="formula-title">Core Percentage Equations</div>
        <div class="formula-code">Part = (Percent / 100) · Total<br>Percent Change = (ΔV / V_initial) · 100</div>
      </div>

      <h2 id="pct-points-vs-pct">Critical Distinction: Percentage Points vs. Percentage Change</h2>
      <p>Confusion frequently arises in economic and political reporting between <em>percentage change</em> and <em>percentage points</em>. If an interest rate climbs from <strong>4.0% to 5.0%</strong>:</p>
      <ul>
        <li>It has increased by <strong>1.0 percentage point</strong> (5.0 - 4.0).</li>
        <li>However, in relative terms, it represents a <strong>25% increase</strong> ((5.0 - 4.0) / 4.0 × 100 = 25%)!</li>
      </ul>

      <h2 id="pct-worked-examples">Step-by-Step Worked Example</h2>
      <p>Suppose a stock price rises from $80 to $120. To find the percentage gain:</p>
      <ol>
        <li>Find the difference: <code>$120 - $80 = $40</code></li>
        <li>Divide by original value: <code>$40 ÷ $80 = 0.50</code></li>
        <li>Multiply by 100: <code>0.50 × 100 = 50% gain</code></li>
      </ol>

      <h2 id="pct-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>How do I calculate a reverse percentage?</summary>
          <div class="faq-content">To find the original number before an X% increase, divide by (1 + X/100). For example, if a price with 10% tax is $110, the pre-tax price is $110 ÷ 1.10 = $100.</div>
        </details>
      </div>
"""

pct_script = """
  <script>
    function calcP1() {
      const x = parseFloat(document.getElementById('p1-x').value) || 0;
      const y = parseFloat(document.getElementById('p1-y').value) || 0;
      const res = (x / 100) * y;
      document.getElementById('p1-res').textContent = res.toFixed(2);
      document.getElementById('card-p1').textContent = res.toFixed(2);
    }
    function calcP2() {
      const x = parseFloat(document.getElementById('p2-x').value) || 0;
      const y = parseFloat(document.getElementById('p2-y').value) || 0;
      const res = y !== 0 ? (x / y) * 100 : 0;
      document.getElementById('p2-res').textContent = res.toFixed(2) + '%';
      document.getElementById('card-p2').textContent = res.toFixed(1) + '%';
    }
    function calcP3() {
      const x = parseFloat(document.getElementById('p3-x').value) || 0;
      const y = parseFloat(document.getElementById('p3-y').value) || 0;
      const diff = y - x;
      const pct = x !== 0 ? (diff / x) * 100 : 0;
      const mult = x !== 0 ? y / x : 0;

      const sign = pct >= 0 ? '+' : '';
      document.getElementById('p3-res').textContent = `${sign}${pct.toFixed(2)}%`;
      document.getElementById('p3-res').style.color = pct >= 0 ? '#059669' : '#E11D48';

      document.getElementById('card-p3').textContent = `${sign}${pct.toFixed(1)}%`;
      document.getElementById('card-p3').style.color = pct >= 0 ? '#059669' : '#E11D48';
      document.getElementById('card-diff').textContent = (diff >= 0 ? '+' : '') + diff.toFixed(1);
      document.getElementById('card-mult').textContent = mult.toFixed(2) + 'x';
    }
    function copyResults() {
      const p1 = document.getElementById('p1-res').textContent;
      const p2 = document.getElementById('p2-res').textContent;
      const p3 = document.getElementById('p3-res').textContent;
      window.copyToClipboard(`CalcHub Percentage Answers: Mode 1: ${p1}, Mode 2: ${p2}, Mode 3: ${p3}`);
    }
    calcP1(); calcP2(); calcP3();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "percentage-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Percentage Calculator — Multi-Mode Percent & Change Solver",
                          "Free online percentage calculator with 3 instant modes: calculate X% of Y, what percent X is of Y, and percentage increase or decrease.",
                          "percentage calculator, percent change calculator, percent of a number, percentage decrease, calculate percentage",
                          "percentage-calculator", "Mathematics & Statistics", "math", pct_app_json,
                          "Solve any percentage problem instantly. Features dedicated interactive modes for proportions, fraction conversion, and percentage increase/decrease.",
                          pct_workspace, pct_geo, pct_toc, pct_article, pct_script))

# ==========================================
# 12. EXACT AGE CALCULATOR
# ==========================================
age_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Exact Age Calculator",
  "url": "https://calchub.org/age-calculator.html",
  "applicationCategory": "UtilitiesApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

age_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">🎂 Date of Birth & Target Date</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="age-dob">Date of Birth</label>
              <div class="input-wrap">
                <input type="date" id="age-dob" value="1998-05-15" onchange="calcAge()">
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="age-target">Age at Date (Target)</label>
              <div class="input-wrap">
                <input type="date" id="age-target" onchange="calcAge()">
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Exact Age</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Milestone</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Chronological Age</span>
          <span class="status-pill status-success" id="age-pill">Exact Breakdown</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Your Exact Age</div>
          <div>
            <span class="primary-result-value" id="age-headline">28 years</span>
          </div>
          <div style="font-size:0.95rem;color:#64748B;margin-top:0.3rem;" id="age-sub">3 months, 16 days</div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Total Months Lived</div>
            <div class="breakdown-val" id="age-months">339 months</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Total Weeks Lived</div>
            <div class="breakdown-val" id="age-weeks">1,480 weeks</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Total Days Lived</div>
            <div class="breakdown-val" id="age-days">10,366 days</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Next Birthday In</div>
            <div class="breakdown-val" id="age-next-bday" style="color:#2563EB;">226 days</div>
          </div>
        </div>
      </section>
"""

age_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>Chronological age is calculated based on elapsed solar time between a date of birth and a specified target date, strictly accounting for leap years (366 days) and variable month lengths (28, 30, or 31 days). In international legal conventions, age increments on the anniversary of birth.</p>
    </section>
"""

age_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#age-math">Gregorian Calendar Mathematics & Leap Years</a></li>
        <li><a href="#cultural-age">Western vs. Traditional Asian Age Systems</a></li>
        <li><a href="#age-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

age_article = """
      <h2 id="age-math">Gregorian Calendar Mathematics & Leap Year Calculations</h2>
      <p>Determining exact chronological age in years, months, and days is not a simple division by 365.25. The Gregorian calendar features varying month lengths and quadrennial leap days (added in years divisible by 4, except for century years not divisible by 400). Accurate computation requires borrower subtraction across month boundaries.</p>

      <h2 id="cultural-age">Western vs. Traditional Asian Age Systems</h2>
      <p>While the international standard increments age on your calendar birthday (starting at 0 years at birth), traditional East Asian reckoning considered an infant to be 1 year old at birth and added an additional year on New Year's Day. South Korea officially standardized on the international system in June 2023 to eliminate administrative discrepancies.</p>

      <h2 id="age-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>How are leap year birthdays (February 29) handled in non-leap years?</summary>
          <div class="faq-content">Legally in most jurisdictions (including the United Kingdom and United States), individuals born on February 29 legally reach milestone ages on March 1 during non-leap years.</div>
        </details>
      </div>
"""

age_script = """
  <script>
    // Set default target to today
    document.getElementById('age-target').valueAsDate = new Date();

    function calcAge() {
      const dobVal = document.getElementById('age-dob').value;
      const targetVal = document.getElementById('age-target').value;
      if (!dobVal || !targetVal) return;

      const dob = new Date(dobVal);
      const target = new Date(targetVal);
      if (dob > target) return;

      let years = target.getFullYear() - dob.getFullYear();
      let months = target.getMonth() - dob.getMonth();
      let days = target.getDate() - dob.getDate();

      if (days < 0) {
        months--;
        const prevMonth = new Date(target.getFullYear(), target.getMonth(), 0);
        days += prevMonth.getDate();
      }
      if (months < 0) {
        years--;
        months += 12;
      }

      // Total days
      const diffTime = target - dob;
      const totalDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
      const totalWeeks = Math.floor(totalDays / 7);
      const totalMonths = (years * 12) + months;

      // Next birthday countdown
      let nextBday = new Date(target.getFullYear(), dob.getMonth(), dob.getDate());
      if (nextBday < target) {
        nextBday.setFullYear(target.getFullYear() + 1);
      }
      const daysToNext = Math.ceil((nextBday - target) / (1000 * 60 * 60 * 24));

      document.getElementById('age-headline').textContent = `${years} years`;
      document.getElementById('age-sub').textContent = `${months} months, ${days} days`;
      document.getElementById('age-months').textContent = `${totalMonths.toLocaleString()} months`;
      document.getElementById('age-weeks').textContent = `${totalWeeks.toLocaleString()} weeks`;
      document.getElementById('age-days').textContent = `${totalDays.toLocaleString()} days`;
      document.getElementById('age-next-bday').textContent = `${daysToNext} days`;
    }
    function copyResults() {
      const y = document.getElementById('age-headline').textContent;
      const s = document.getElementById('age-sub').textContent;
      const d = document.getElementById('age-days').textContent;
      window.copyToClipboard(`CalcHub Age Milestone: ${y}, ${s} (Total days: ${d})`);
    }
    calcAge();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "age-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Exact Age Calculator — Chronological Age & Birthday Countdown",
                          "Calculate your exact chronological age in years, months, days, weeks, and total days lived. Includes an exact countdown to your next birthday.",
                          "age calculator, date of birth calculator, how old am i, chronological age, exact age in days, days until next birthday",
                          "age-calculator", "Mathematics & Daily Utilities", "math", age_app_json,
                          "Discover your exact chronological age down to the day. View total days, weeks, and months lived, plus days remaining until your next birthday milestone.",
                          age_workspace, age_geo, age_toc, age_article, age_script))

# ==========================================
# 13. GPA CALCULATOR
# ==========================================
gpa_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "GPA Calculator",
  "url": "https://calchub.org/gpa-calculator.html",
  "applicationCategory": "MathApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

gpa_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">🎓 Semester Courses & Grades</span>
        </div>
        <form onsubmit="return false;">
          <div id="gpa-rows">
            <!-- Row 1 -->
            <div style="display:flex;gap:0.75rem;margin-bottom:0.75rem;align-items:center;">
              <input type="text" value="Course 1" style="flex:1.5;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
              <select class="gpa-grade" onchange="calcGPA()" style="flex:1;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
                <option value="4.0" selected>A (4.0)</option>
                <option value="3.7">A- (3.7)</option>
                <option value="3.3">B+ (3.3)</option>
                <option value="3.0">B (3.0)</option>
                <option value="2.7">B- (2.7)</option>
                <option value="2.0">C (2.0)</option>
                <option value="1.0">D (1.0)</option>
                <option value="0.0">F (0.0)</option>
              </select>
              <input type="number" class="gpa-credits" value="3" min="1" max="10" oninput="calcGPA()" style="width:70px;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
            </div>
            <!-- Row 2 -->
            <div style="display:flex;gap:0.75rem;margin-bottom:0.75rem;align-items:center;">
              <input type="text" value="Course 2" style="flex:1.5;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
              <select class="gpa-grade" onchange="calcGPA()" style="flex:1;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
                <option value="4.0">A (4.0)</option>
                <option value="3.7" selected>A- (3.7)</option>
                <option value="3.3">B+ (3.3)</option>
                <option value="3.0">B (3.0)</option>
                <option value="2.7">B- (2.7)</option>
                <option value="2.0">C (2.0)</option>
                <option value="1.0">D (1.0)</option>
                <option value="0.0">F (0.0)</option>
              </select>
              <input type="number" class="gpa-credits" value="4" min="1" max="10" oninput="calcGPA()" style="width:70px;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
            </div>
            <!-- Row 3 -->
            <div style="display:flex;gap:0.75rem;margin-bottom:0.75rem;align-items:center;">
              <input type="text" value="Course 3" style="flex:1.5;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
              <select class="gpa-grade" onchange="calcGPA()" style="flex:1;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
                <option value="4.0">A (4.0)</option>
                <option value="3.7">A- (3.7)</option>
                <option value="3.3" selected>B+ (3.3)</option>
                <option value="3.0">B (3.0)</option>
                <option value="2.7">B- (2.7)</option>
                <option value="2.0">C (2.0)</option>
                <option value="1.0">D (1.0)</option>
                <option value="0.0">F (0.0)</option>
              </select>
              <input type="number" class="gpa-credits" value="3" min="1" max="10" oninput="calcGPA()" style="width:70px;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
            </div>
            <!-- Row 4 -->
            <div style="display:flex;gap:0.75rem;margin-bottom:0.75rem;align-items:center;">
              <input type="text" value="Course 4" style="flex:1.5;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
              <select class="gpa-grade" onchange="calcGPA()" style="flex:1;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
                <option value="4.0" selected>A (4.0)</option>
                <option value="3.7">A- (3.7)</option>
                <option value="3.3">B+ (3.3)</option>
                <option value="3.0">B (3.0)</option>
                <option value="2.7">B- (2.7)</option>
                <option value="2.0">C (2.0)</option>
                <option value="1.0">D (1.0)</option>
                <option value="0.0">F (0.0)</option>
              </select>
              <input type="number" class="gpa-credits" value="3" min="1" max="10" oninput="calcGPA()" style="width:70px;padding:0.55rem;border:1px solid #CBD5E1;border-radius:6px;">
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy GPA</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Transcript</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Academic Standing</span>
          <span class="status-pill status-success">Honor Roll</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Cumulative GPA (4.0 Scale)</div>
          <div>
            <span class="primary-result-value" id="gpa-val">3.75</span>
            <span class="primary-result-unit">/ 4.0</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Total Quality Points</div>
            <div class="breakdown-val" id="gpa-qp">48.7</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Total Credits</div>
            <div class="breakdown-val" id="gpa-tot-credits">13 hrs</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Latin Honors</div>
            <div class="breakdown-val" id="gpa-honors">Magna Cum Laude</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Grade Average</div>
            <div class="breakdown-val" id="gpa-letter">A-</div>
          </div>
        </div>
      </section>
"""

gpa_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p><strong>Grade Point Average (GPA)</strong> is calculated by dividing total quality points earned by total course credit hours attempted:</p>
      <p><code>GPA = Σ (Grade Points × Course Credits) ÷ Σ (Total Credit Hours)</code></p>
      <p>On the standard 4.0 US collegiate scale, letter grades convert to numerical points: A = 4.0, A- = 3.7, B+ = 3.3, B = 3.0, B- = 2.7, C+ = 2.3, C = 2.0, D = 1.0, and F = 0.0.</p>
    </section>
"""

gpa_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#gpa-scale-table">The Standard 4.0 Scale Table</a></li>
        <li><a href="#weighted-vs-unweighted">Weighted vs. Unweighted GPA</a></li>
        <li><a href="#latin-honors">Latin Honors Benchmarks</a></li>
        <li><a href="#gpa-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

gpa_article = """
      <h2 id="gpa-scale-table">Standard 4.0 Collegiate Grading Scale</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead><tr><th>Letter Grade</th><th>Percentage Equivalent</th><th>Grade Points (4.0 Scale)</th></tr></thead>
          <tbody>
            <tr><td>A / A+</td><td>93–100%</td><td>4.00</td></tr>
            <tr><td>A-</td><td>90–92%</td><td>3.70</td></tr>
            <tr><td>B+</td><td>87–89%</td><td>3.30</td></tr>
            <tr><td>B</td><td>83–86%</td><td>3.00</td></tr>
            <tr><td>B-</td><td>80–82%</td><td>2.70</td></tr>
            <tr><td>C+</td><td>77–79%</td><td>2.30</td></tr>
            <tr><td>C</td><td>73–76%</td><td>2.00</td></tr>
            <tr><td>D</td><td>65–72%</td><td>1.00</td></tr>
            <tr><td>F</td><td>&lt; 65%</td><td>0.00</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="weighted-vs-unweighted">Weighted vs. Unweighted GPA</h2>
      <p>An <strong>unweighted GPA</strong> calculates all classes on a flat 4.0 maximum scale regardless of academic rigor. A <strong>weighted GPA</strong> awards extra points (typically +0.5 for Honors courses and +1.0 for Advanced Placement / International Baccalaureate courses), resulting in maximum GPAs up to 5.0.</p>

      <h2 id="latin-honors">Collegiate Latin Honors Benchmarks</h2>
      <ul>
        <li><strong>Cum Laude (With Praise):</strong> Typically top 20-25% of class or GPA 3.50 – 3.69.</li>
        <li><strong>Magna Cum Laude (With Great Praise):</strong> Top 10-15% of class or GPA 3.70 – 3.89.</li>
        <li><strong>Summa Cum Laude (With Highest Praise):</strong> Top 5% of graduating class or GPA 3.90 – 4.00.</li>
      </ul>

      <h2 id="gpa-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>Do Pass/Fail or Audited classes impact GPA?</summary>
          <div class="faq-content">No. Courses taken under a Pass/Fail (Credit/No Credit) or Audit grading option award credit hours upon passing but are completely excluded from GPA quality point calculations.</div>
        </details>
      </div>
"""

gpa_script = """
  <script>
    function calcGPA() {
      const grades = document.querySelectorAll('.gpa-grade');
      const credits = document.querySelectorAll('.gpa-credits');

      let totalPoints = 0;
      let totalCredits = 0;

      for (let i = 0; i < grades.length; i++) {
        const pts = parseFloat(grades[i].value) || 0;
        const cr = parseFloat(credits[i].value) || 0;
        totalPoints += (pts * cr);
        totalCredits += cr;
      }

      const gpa = totalCredits > 0 ? (totalPoints / totalCredits) : 0;
      let honors = "Standard Standing";
      let letter = "B";

      if (gpa >= 3.9) { honors = "Summa Cum Laude"; letter = "A"; }
      else if (gpa >= 3.7) { honors = "Magna Cum Laude"; letter = "A-"; }
      else if (gpa >= 3.5) { honors = "Cum Laude"; letter = "B+"; }
      else if (gpa >= 3.0) { honors = "Good Standing"; letter = "B"; }
      else if (gpa >= 2.0) { honors = "Satisfactory"; letter = "C"; }
      else { honors = "Academic Probation"; letter = "D/F"; }

      document.getElementById('gpa-val').textContent = gpa.toFixed(2);
      document.getElementById('gpa-qp').textContent = totalPoints.toFixed(1);
      document.getElementById('gpa-tot-credits').textContent = totalCredits + ' hrs';
      document.getElementById('gpa-honors').textContent = honors;
      document.getElementById('gpa-letter').textContent = letter;
    }
    function copyResults() {
      const gpa = document.getElementById('gpa-val').textContent;
      const h = document.getElementById('gpa-honors').textContent;
      window.copyToClipboard(`CalcHub GPA Report: Cumulative GPA: ${gpa}/4.0 (${h})`);
    }
    calcGPA();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "gpa-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("GPA Calculator — 4.0 College & High School Grade Point Average",
                          "Calculate your semester and cumulative GPA on the standard 4.0 scale with credit hours, letter grades, and Latin Honors predictions.",
                          "gpa calculator, college gpa calculator, grade point average, 4.0 scale gpa, calculate gpa, cumulative gpa",
                          "gpa-calculator", "Mathematics & Academia", "math", gpa_app_json,
                          "Compute your exact Grade Point Average across semester courses. Supports variable credit weighting, 4.0 quality points, and academic standing recognition.",
                          gpa_workspace, gpa_geo, gpa_toc, gpa_article, gpa_script))

# ==========================================
# 14. FRACTION CALCULATOR
# ==========================================
frac_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Fraction Calculator",
  "url": "https://calchub.org/fraction-calculator.html",
  "applicationCategory": "MathApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

frac_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">½ Fraction Arithmetic</span>
        </div>
        <form onsubmit="return false;">
          <div style="display:flex;align-items:center;justify-content:center;gap:1.5rem;flex-wrap:wrap;padding:1.5rem 0;">
            <!-- Fraction 1 -->
            <div style="display:flex;flex-direction:column;align-items:center;width:90px;">
              <input type="number" id="f1-num" value="3" oninput="calcFrac()" style="width:100%;text-align:center;padding:0.6rem;font-size:1.1rem;font-weight:700;border:1px solid #CBD5E1;border-radius:8px;">
              <div style="width:100%;height:2px;background:#0F172A;margin:6px 0;"></div>
              <input type="number" id="f1-den" value="4" oninput="calcFrac()" style="width:100%;text-align:center;padding:0.6rem;font-size:1.1rem;font-weight:700;border:1px solid #CBD5E1;border-radius:8px;">
            </div>

            <!-- Operator -->
            <div style="width:70px;">
              <select id="frac-op" onchange="calcFrac()" style="width:100%;padding:0.6rem;font-size:1.3rem;font-weight:800;text-align:center;border:1px solid #CBD5E1;border-radius:8px;">
                <option value="+">+</option>
                <option value="-">−</option>
                <option value="*" selected>×</option>
                <option value="/">÷</option>
              </select>
            </div>

            <!-- Fraction 2 -->
            <div style="display:flex;flex-direction:column;align-items:center;width:90px;">
              <input type="number" id="f2-num" value="2" oninput="calcFrac()" style="width:100%;text-align:center;padding:0.6rem;font-size:1.1rem;font-weight:700;border:1px solid #CBD5E1;border-radius:8px;">
              <div style="width:100%;height:2px;background:#0F172A;margin:6px 0;"></div>
              <input type="number" id="f2-den" value="5" oninput="calcFrac()" style="width:100%;text-align:center;padding:0.6rem;font-size:1.1rem;font-weight:700;border:1px solid #CBD5E1;border-radius:8px;">
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Result</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Steps</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Reduced Fraction</span>
          <span class="status-pill status-success">Exact Fraction</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Result in Lowest Terms</div>
          <div>
            <span class="primary-result-value" id="frac-res" style="color:#2563EB;">3 / 10</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Decimal Value</div>
            <div class="breakdown-val" id="frac-decimal">0.30</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Mixed Number</div>
            <div class="breakdown-val" id="frac-mixed">3/10</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Percentage</div>
            <div class="breakdown-val" id="frac-pct">30.0%</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Common Denominator</div>
            <div class="breakdown-val" id="frac-lcd">20</div>
          </div>
        </div>
      </section>
"""

frac_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>Fraction arithmetic follows algebraic reduction rules:</p>
      <ul>
        <li><strong>Addition/Subtraction:</strong> <code>a/b ± c/d = (a·d ± b·c) / (b·d)</code>, then reduced using Greatest Common Divisor (GCD).</li>
        <li><strong>Multiplication:</strong> <code>(a/b) × (c/d) = (a·c) / (b·d)</code></li>
        <li><strong>Division:</strong> Multiply by the reciprocal: <code>(a/b) ÷ (c/d) = (a·d) / (b·c)</code></li>
      </ul>
    </section>
"""

frac_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#frac-rules">Fundamental Operations: Add, Subtract, Multiply, Divide</a></li>
        <li><a href="#lcd-method">Finding the Least Common Denominator (LCD)</a></li>
        <li><a href="#simplifying-fractions">Simplifying via Greatest Common Divisor</a></li>
        <li><a href="#frac-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

frac_article = """
      <h2 id="frac-rules">Rules of Fraction Arithmetic</h2>
      <p>Fractions represent numerical proportions where the numerator indicates parts taken and the denominator indicates equal divisions of a whole.</p>

      <div class="formula-box">
        <div class="formula-title">Fraction Multiplication and Division Rules</div>
        <div class="formula-code">(a/b) × (c/d) = (a·c) / (b·d)<br>(a/b) ÷ (c/d) = (a·d) / (b·c)</div>
      </div>

      <h2 id="lcd-method">The Role of the Least Common Denominator (LCD)</h2>
      <p>Fractions cannot be directly combined via addition or subtraction without matching denominators. The Least Common Denominator is the lowest common multiple of both denominators.</p>

      <h2 id="simplifying-fractions">Simplification via Euclid's GCD Algorithm</h2>
      <p>A fraction is in its lowest reduced form when its numerator and denominator share no common factors other than 1. Dividing both terms by their Greatest Common Divisor (GCD) reduces the fraction.</p>

      <h2 id="frac-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>What happens if a denominator is zero?</summary>
          <div class="faq-content">Division by zero is undefined in mathematics. A fraction with zero in the denominator has no valid numerical value.</div>
        </details>
      </div>
"""

frac_script = """
  <script>
    function gcd(a, b) {
      a = Math.abs(a); b = Math.abs(b);
      while (b) { let t = b; b = a % b; a = t; }
      return a;
    }
    function calcFrac() {
      const n1 = parseInt(document.getElementById('f1-num').value) || 0;
      const d1 = parseInt(document.getElementById('f1-den').value) || 1;
      const n2 = parseInt(document.getElementById('f2-num').value) || 0;
      const d2 = parseInt(document.getElementById('f2-den').value) || 1;
      const op = document.getElementById('frac-op').value;

      if (d1 === 0 || d2 === 0) {
        document.getElementById('frac-res').textContent = "Undefined (Zero Denominator)";
        return;
      }

      let resN = 0;
      let resD = 1;

      if (op === '+') {
        resN = (n1 * d2) + (n2 * d1);
        resD = (d1 * d2);
      } else if (op === '-') {
        resN = (n1 * d2) - (n2 * d1);
        resD = (d1 * d2);
      } else if (op === '*') {
        resN = n1 * n2;
        resD = d1 * d2;
      } else if (op === '/') {
        resN = n1 * d2;
        resD = d1 * n2;
      }

      if (resD === 0) {
        document.getElementById('frac-res').textContent = "Undefined";
        return;
      }

      const common = gcd(resN, resD);
      let redN = resN / common;
      let redD = resD / common;

      if (redD < 0) { redN = -redN; redD = -redD; }

      const decimal = redN / redD;
      let mixed = `${redN}/${redD}`;
      if (Math.abs(redN) >= redD && redD !== 1) {
        const whole = Math.floor(Math.abs(redN) / redD) * (redN < 0 ? -1 : 1);
        const rem = Math.abs(redN) % redD;
        mixed = `${whole} ${rem}/${redD}`;
      } else if (redD === 1) {
        mixed = `${redN}`;
      }

      document.getElementById('frac-res').textContent = (redD === 1) ? `${redN}` : `${redN} / ${redD}`;
      document.getElementById('frac-decimal').textContent = decimal.toFixed(4);
      document.getElementById('frac-mixed').textContent = mixed;
      document.getElementById('frac-pct').textContent = (decimal * 100).toFixed(2) + '%';
      document.getElementById('frac-lcd').textContent = Math.abs(d1 * d2 / gcd(d1, d2));
    }
    function copyResults() {
      const r = document.getElementById('frac-res').textContent;
      const d = document.getElementById('frac-decimal').textContent;
      window.copyToClipboard(`CalcHub Fraction Result: ${r} (Decimal: ${d})`);
    }
    calcFrac();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "fraction-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Fraction Calculator — Add, Subtract, Multiply & Divide Fractions",
                          "Free online fraction calculator. Easily add, subtract, multiply, and divide proper and improper fractions with step-by-step reduction and LCD.",
                          "fraction calculator, add fractions, simplify fractions, fraction reducer, multiply fractions, divide fractions",
                          "fraction-calculator", "Mathematics & Statistics", "math", frac_app_json,
                          "Perform accurate fraction arithmetic with automated least common denominator (LCD) resolution, step-by-step GCD reduction, and mixed number conversion.",
                          frac_workspace, frac_geo, frac_toc, frac_article, frac_script))

# ==========================================
# 15. RATIO CALCULATOR & SIMPLIFIER
# ==========================================
ratio_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Ratio Calculator",
  "url": "https://calchub.org/ratio-calculator.html",
  "applicationCategory": "MathApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

ratio_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">➗ Ratio Simplifier & Proportion Solver</span>
        </div>
        <form onsubmit="return false;">
          <div style="margin-bottom:1.5rem;padding-bottom:1.25rem;border-bottom:1px solid #E2E8F0;">
            <div style="font-weight:700;color:#0F172A;margin-bottom:0.75rem;">1. Simplify a Ratio (A : B)</div>
            <div style="display:flex;align-items:center;gap:0.75rem;flex-wrap:wrap;">
              <input type="number" id="r-a" value="1920" oninput="calcRatio()" style="width:110px;padding:0.6rem;border:1px solid #CBD5E1;border-radius:8px;">
              <span style="font-weight:800;font-size:1.3rem;">:</span>
              <input type="number" id="r-b" value="1080" oninput="calcRatio()" style="width:110px;padding:0.6rem;border:1px solid #CBD5E1;border-radius:8px;">
              <span style="font-weight:700;color:#2563EB;">=</span>
              <span style="font-weight:800;font-size:1.3rem;color:#059669;font-family:var(--font-mono);" id="r-simplified">16 : 9</span>
            </div>
          </div>

          <div>
            <div style="font-weight:700;color:#0F172A;margin-bottom:0.75rem;">2. Solve Unknown Proportion (A : B = C : X)</div>
            <div style="display:flex;align-items:center;gap:0.75rem;flex-wrap:wrap;">
              <input type="number" id="p-a" value="4" oninput="calcProp()" style="width:70px;padding:0.6rem;border:1px solid #CBD5E1;border-radius:8px;">
              <span style="font-weight:700;">:</span>
              <input type="number" id="p-b" value="3" oninput="calcProp()" style="width:70px;padding:0.6rem;border:1px solid #CBD5E1;border-radius:8px;">
              <span style="font-weight:700;color:#2563EB;">=</span>
              <input type="number" id="p-c" value="800" oninput="calcProp()" style="width:90px;padding:0.6rem;border:1px solid #CBD5E1;border-radius:8px;">
              <span style="font-weight:700;">:</span>
              <span style="font-weight:800;font-size:1.2rem;color:#2563EB;font-family:var(--font-mono);" id="p-x">600</span>
            </div>
          </div>

          <div class="calc-actions" style="margin-top:1.5rem;">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Ratio</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Summary</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Calculated Proportions</span>
          <span class="status-pill status-success">Simplified</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Simplified Ratio (A : B)</div>
          <div>
            <span class="primary-result-value" id="card-r-val" style="color:#059669;">16 : 9</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Solved Unknown X</div>
            <div class="breakdown-val" id="card-p-x">600</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Unit Ratio (1 : N)</div>
            <div class="breakdown-val" id="card-r-unit">1 : 0.562</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Decimal Multiplier</div>
            <div class="breakdown-val" id="card-r-dec">1.778</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Greatest Common Factor</div>
            <div class="breakdown-val" id="card-r-gcd">120</div>
          </div>
        </div>
      </section>
"""

ratio_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>A <strong>ratio</strong> indicates how many times one number contains another (expressed as A : B). To simplify a ratio, divide both terms by their <strong>Greatest Common Divisor (GCD)</strong>. To solve a proportion where <code>A : B = C : X</code>, cross-multiply: <code>X = (B × C) ÷ A</code>.</p>
    </section>
"""

ratio_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#ratio-simplification">How Ratio Simplification Works</a></li>
        <li><a href="#aspect-ratios">Common Aspect Ratios (16:9, 4:3, 21:9)</a></li>
        <li><a href="#cross-multiplication">Cross-Multiplication in Proportions</a></li>
        <li><a href="#ratio-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

ratio_article = """
      <h2 id="ratio-simplification">The Mechanics of Ratio Simplification</h2>
      <p>Ratios express relative quantities in design, engineering mixtures, and cooking recipes. Simplifying a ratio to its lowest integer terms involves calculating the greatest common divisor using the Euclidean algorithm.</p>

      <div class="formula-box">
        <div class="formula-title">Proportion Solving Equation</div>
        <div class="formula-code">A / B = C / X  ⟹  X = (B · C) / A</div>
      </div>

      <h2 id="aspect-ratios">Display & Cinematic Aspect Ratios</h2>
      <p>Digital displays and photography depend on standardized aspect ratios:</p>
      <ul>
        <li><strong>16:9 (1.78:1):</strong> High-definition television (1920×1080, 4K UHD 3840×2160).</li>
        <li><strong>4:3 (1.33:1):</strong> Traditional television, iPad displays, and standard format photography.</li>
        <li><strong>21:9 (2.33:1):</strong> Ultrawide panoramic gaming monitors and anamorphic cinema.</li>
      </ul>

      <h2 id="cross-multiplication">Scaling Proportions with Cross-Multiplication</h2>
      <p>When resizing images or scaling culinary ingredients, setting up an equality between two ratios ensures that proportions remain preserved without geometric distortion.</p>

      <h2 id="ratio-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>What is a Golden Ratio?</summary>
          <div class="faq-content">The Golden Ratio (represented by φ, roughly 1 : 1.618) occurs when the ratio of the sum of two quantities to the larger equals the ratio of the larger to the smaller. It appears frequently in natural phyllotaxis and classical architectural geometry.</div>
        </details>
      </div>
"""

ratio_script = """
  <script>
    function gcd(a, b) {
      a = Math.abs(a); b = Math.abs(b);
      while (b) { let t = b; b = a % b; a = t; }
      return a;
    }
    function calcRatio() {
      const a = parseInt(document.getElementById('r-a').value) || 1;
      const b = parseInt(document.getElementById('r-b').value) || 1;
      const g = gcd(a, b);
      const sA = a / g;
      const sB = b / g;
      const simplified = `${sA} : ${sB}`;
      const unit = `1 : ${(b / a).toFixed(3)}`;
      const dec = (a / b).toFixed(3);

      document.getElementById('r-simplified').textContent = simplified;
      document.getElementById('card-r-val').textContent = simplified;
      document.getElementById('card-r-unit').textContent = unit;
      document.getElementById('card-r-dec').textContent = dec;
      document.getElementById('card-r-gcd').textContent = g;
    }
    function calcProp() {
      const a = parseFloat(document.getElementById('p-a').value) || 1;
      const b = parseFloat(document.getElementById('p-b').value) || 1;
      const c = parseFloat(document.getElementById('p-c').value) || 1;

      const x = (b * c) / a;
      document.getElementById('p-x').textContent = x % 1 === 0 ? x : x.toFixed(2);
      document.getElementById('card-p-x').textContent = x % 1 === 0 ? x : x.toFixed(2);
    }
    function copyResults() {
      const r = document.getElementById('r-simplified').textContent;
      const x = document.getElementById('p-x').textContent;
      window.copyToClipboard(`CalcHub Ratio Summary: Simplified: ${r}, Solved X: ${x}`);
    }
    calcRatio(); calcProp();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "ratio-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Ratio Calculator & Simplifier — Solve A:B = C:X Proportions",
                          "Simplify ratios to lowest terms using GCD and solve unknown proportions (A:B = C:X). Ideal for display aspect ratios, scaling recipes, and geometry.",
                          "ratio calculator, simplify ratio, proportion calculator, solve for x ratio, aspect ratio calculator, scale ratio",
                          "ratio-calculator", "Mathematics & Proportions", "math", ratio_app_json,
                          "Simplify numerical ratios with automated greatest common divisor (GCD) reduction. Solve missing proportion values for image aspect ratios and engineering scale models.",
                          ratio_workspace, ratio_geo, ratio_toc, ratio_article, ratio_script))

print("Created all 5 Math Calculators successfully!")
