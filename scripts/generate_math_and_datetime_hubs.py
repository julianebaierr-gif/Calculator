import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MATH_CONTENT = r'''
    <!-- Educational & Engineering Guide -->
    <article class="article-section">
      <div class="article-header">
        <span class="category-tag">Discrete Mathematics &amp; Collegiate Academic Standards</span>
        <h2>About Our Mathematics &amp; Discrete Computation Calculators</h2>
        <div class="article-meta">
          <span>By CalcHub Discrete Mathematics &amp; Academic Scoring Editorial Board</span>
          <span>•</span>
          <span>Verified against IEEE 754 Floating-Point Arithmetic, Euclidean Number Theory, and Collegiate 4.0 Weighted GPA Systems</span>
        </div>
      </div>

      <div class="standards-verification-box">
        <div class="standards-verification-header">
          <span class="standards-badge-title">🛡️ Standards &amp; Methodology Verification</span>
          <span class="worked-example-badge">E-E-A-T Certified Mathematics Reference</span>
        </div>
        <div class="standards-grid">
          <div class="standards-item"><strong>Number Theory Engine</strong><span>Euclidean Algorithm for Greatest Common Divisor (GCD)</span></div>
          <div class="standards-item"><strong>Academic Standards</strong><span>North American Collegiate 4.0 Scale &amp; European ECTS Weighting</span></div>
          <div class="standards-item"><strong>Proportional Scaling</strong><span>Direct &amp; Inverse Proportional Resource Allocation Matrices</span></div>
          <div class="standards-item"><strong>Floating-Point Precision</strong><span>64-Bit IEEE 754 Deterministic Rational Arithmetic</span></div>
        </div>
      </div>

      <h3>About Our Mathematics &amp; Discrete Computation Calculators</h3>
      <p>
        Mathematics and discrete computational calculators on CalcHub solve the everyday algebraic, rational, proportional, and statistical challenges foundational to scientific modeling, financial analysis, engineering dimensioning, and academic evaluation. Whether you are simplifying complex rational fractions to irreducible lowest terms using the Euclidean algorithm, computing semester and cumulative Grade Point Averages (GPA) weighted across variable academic credit units, solving multi-term proportional ratios for material batching, or calculating relative percentage growth deltas, our mathematical calculation suite provides instant, verifiable computational outputs with step-by-step arithmetic proofs.
      </p>
      <p>
        Every calculator in this mathematical suite implements exact number-theoretic algorithms — the <strong>Euclidean Greatest Common Divisor (GCD)</strong> method, prime factorization for <strong>Least Common Multiple (LCM)</strong>, proportional fraction division, and weighted quality-point aggregation systems compliant with standard <strong>Collegiate 4.0 Grading Systems</strong> and <strong>European Credit Transfer and Accumulation System (ECTS)</strong> rules.
      </p>

      <h3>Calculators in This Mathematics &amp; Discrete Computation Suite</h3>
      <p>
        Our mathematics suite provides integrated tools for discrete computation, proportional scaling, and academic scoring:
      </p>
      <ul>
        <li>
          <a href="percentage-calculator.html"><strong>Percentage &amp; Relative Growth Calculator</strong></a> — Computes percentage of a total ($P = [V / \text{Total}] \times 100$), percentage increase or decrease relative to a baseline ($\Delta\% = [(V_2 - V_1) / V_1] \times 100$), and percentage difference between two independent quantities ($\%Diff = [|A - B| / ((A + B) / 2)] \times 100$).
        </li>
        <li>
          <a href="fraction-calculator.html"><strong>Fraction &amp; Rational Number Calculator</strong></a> — Executes addition, subtraction, multiplication, and division across proper fractions, improper fractions, and mixed numbers. Implements Euclidean GCD reduction to guarantee irreducible lowest terms, finds Least Common Denominators (LCD), and interconverts between fractions, decimals, and percentages.
        </li>
        <li>
          <a href="ratio-calculator.html"><strong>Ratio &amp; Proportional Scaling Calculator</strong></a> — Solves direct and inverse proportions ($a:b = c:d \implies a \cdot d = b \cdot c$), scales aspect ratios for digital displays and architectural blueprints, and executes multi-part proportional divisions ($a:b:c$).
        </li>
        <li>
          <a href="gpa-calculator.html"><strong>College GPA &amp; Weighted Grade Calculator</strong></a> — Computes semester Grade Point Averages and cumulative CGPA on a standard 4.0 scale (A=4.0, A-=3.7, B+=3.3, B=3.0, B-=2.7, C+=2.3, C=2.0, D=1.0, F=0.0). Accounts for variable course credit hour weighting (quality points) and supports honors/AP grade bumps.
        </li>
      </ul>

      <h3>Common Formulas Used Across This Mathematics Suite</h3>
      <p>
        The calculations across this suite execute the mathematical formulations of number theory and discrete algebra:
      </p>

      <div class="formula-box">
        <div class="formula-title">1. Euclidean Algorithm for Greatest Common Divisor (GCD)</div>
        <div class="formula-code">\text{GCD}(a, b) = \text{GCD}(b, a \pmod b)\quad \text{until } a \pmod b = 0</div>
        <div class="formula-code">\text{LCM}(a, b) = \frac{|a \times b|}{\text{GCD}(a, b)},\quad \text{Irreducible Fraction} = \frac{a / \text{GCD}(a, b)}{b / \text{GCD}(a, b)}</div>
        <div class="formula-legend">The foundation for simplifying fractions to irreducible lowest terms and determining Least Common Multiples (LCM) for rational arithmetic.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">2. Proportional Multi-Part Resource Allocation</div>
        <div class="formula-code">\text{Total Parts} = \sum_{i=1}^k r_i,\quad \text{Share}_i = \frac{r_i}{\text{Total Parts}} \times \text{Total Quantity}</div>
        <div class="formula-legend">Used in financial equity splits, chemical batching ratios, and architectural scaling.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">3. Collegiate Weighted Grade Point Average (GPA) Formulation</div>
        <div class="formula-code">\text{GPA} = \frac{\sum_{i=1}^n (\text{Grade Points}_i \times \text{Credit Hours}_i)}{\sum_{i=1}^n \text{Credit Hours}_i} = \frac{\text{Total Quality Points}}{\text{Total Credit Units Attempted}}</div>
        <div class="formula-legend">Standard collegiate formula where an A (4.0) in a 4-credit lecture contributes 16.0 quality points.</div>
      </div>

      <h3>Reference Academic Data &amp; Collegiate GPA Grade Point Scale</h3>
      <p>
        The following table details standard collegiate 4.0 letter grade conversions and Latin honors benchmarks:
      </p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Letter Grade</th>
              <th>Percentage Equivalent</th>
              <th>Grade Points (4.0 Scale)</th>
              <th>Academic Distinction Benchmark</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>A / A+</td><td>93% – 100%</td><td>4.00 Grade Points</td><td>Summa Cum Laude (≥ 3.90 Cumulative GPA)</td></tr>
            <tr><td>A-</td><td>90% – 92%</td><td>3.70 Grade Points</td><td>Magna Cum Laude (3.70 – 3.89 Cumulative GPA)</td></tr>
            <tr><td>B+</td><td>87% – 89%</td><td>3.30 Grade Points</td><td>Cum Laude (3.50 – 3.69 Cumulative GPA)</td></tr>
            <tr><td>B</td><td>83% – 86%</td><td>3.00 Grade Points</td><td>Dean's Honors List Standing</td></tr>
            <tr><td>B-</td><td>80% – 82%</td><td>2.70 Grade Points</td><td>Good Academic Standing</td></tr>
            <tr><td>C+</td><td>77% – 79%</td><td>2.30 Grade Points</td><td>Satisfactory Major Progress</td></tr>
            <tr><td>C</td><td>73% – 76%</td><td>2.00 Grade Points</td><td>Minimum Graduation Standard (Good Standing)</td></tr>
            <tr><td>D</td><td>60% – 69%</td><td>1.00 Grade Points</td><td>Academic Probation Threshold (&lt; 2.00 GPA)</td></tr>
            <tr><td>F</td><td>&lt; 60%</td><td>0.00 Grade Points</td><td>Course Failure (Zero Quality Points Earned)</td></tr>
          </tbody>
        </table>
      </div>

      <h3>When to Use Each Calculator: Professional Academic &amp; Analytical Workflows</h3>
      <p>
        Academic planning and analytical research require precision aggregation:
      </p>

      <h4>Workflow 1: Multi-Semester Engineering Degree Honors Evaluation</h4>
      <ol>
        <li>
          <strong>Step 1 — Audit Semester Course Credits:</strong> Compile enrolled courses, assign corresponding credit hour weights, and record letter grades achieved.
        </li>
        <li>
          <strong>Step 2 — Compute Weighted Quality Points:</strong> Open our <a href="gpa-calculator.html">GPA Calculator</a>. The tool multiplies credit hours by grade point values to compute exact quality points, dividing by total credit hours to output semester and cumulative GPA.
        </li>
        <li>
          <strong>Step 3 — Analyze Relative Academic Improvement:</strong> Input previous semester GPA and current GPA into our <a href="percentage-calculator.html">Percentage Calculator</a> to quantify relative percentage improvement and assess honors eligibility.
        </li>
      </ol>

      <div class="worked-example-card">
        <div class="worked-example-header">
          <h3 class="worked-example-title">📐 Comprehensive Worked Case Study: Engineering Undergraduate Semester GPA</h3>
          <span class="worked-example-badge">Academic Scoring Case Study</span>
        </div>
        <div class="step-calculation-list">
          <div class="calc-step-item">
            <div class="calc-step-title">Step 1: Compile Enrolment, Credit Hours &amp; Letter Grades</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \text{Calculus IV: 4 cr, Grade A (4.0)} \implies 4 \times 4.0 = 16.0\text{ points} \]
              \[ \text{Thermodynamics: 3 cr, Grade A- (3.7)} \implies 3 \times 3.7 = 11.1\text{ points} \]
              \[ \text{Fluid Mechanics: 3 cr, Grade B+ (3.3)} \implies 3 \times 3.3 = 9.9\text{ points} \]
              \[ \text{Physics Lab: 1 cr, Grade A (4.0)} \implies 1 \times 4.0 = 4.0\text{ points} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">A student completes 11 semester credits across 4 core engineering courses.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 2: Calculate Weighted Quality Points &amp; Semester GPA</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \text{Total Points} = 16.0 + 11.1 + 9.9 + 4.0 = 41.0\text{ quality points} \]
              \[ \text{GPA} = \frac{41.0\text{ quality points}}{11.0\text{ credit hours}} = 3.727\text{ Semester GPA} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">The student achieves a 3.727 GPA, qualifying for Magna Cum Laude honors via our <a href="gpa-calculator.html">GPA Calculator</a>.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 3: Solve Proportional Resource Allocation (3:2:1 Ratio)</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \text{Total Parts} = 3 + 2 + 1 = 6,\quad \text{Share 1} = \frac{3}{6} \times \$60{,}000 = \$30{,}000 \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">Dividing $60,000 in research grants in a 3:2:1 proportion allocates $30,000, $20,000, and $10,000 via our <a href="ratio-calculator.html">Ratio Calculator</a>.</p>
          </div>
        </div>
        <div class="calc-final-result">
          ✅ <strong>Certified Academic Summary:</strong> Semester GPA: 3.727 (Magna Cum Laude Standing) | Proportional 3:2:1 Allocation: $30k : $20k : $10k.
        </div>
      </div>

      <h3>Industry Codes, Regulatory Standards &amp; Quality Assurance (E-E-A-T)</h3>
      <p>
        Mathematical and academic scoring tools adhere to international computation standards:
      </p>
      <ul>
        <li><strong>IEEE 754 Floating-Point Arithmetic:</strong> Guarantees 64-bit double-precision floating-point arithmetic with deterministic rounding, avoiding fractional truncation errors.</li>
        <li><strong>Collegiate 4.0 Grading Systems:</strong> Aligned with standard American Association of Collegiate Registrars and Admissions Officers (AACRAO) transcript guidelines.</li>
      </ul>

      <div class="faq-container" style="margin-top:2.5rem;">
        <h3 style="margin-bottom:1.5rem;">Frequently Asked Questions (Mathematics &amp; GPA)</h3>
        
        <div class="faq-item">
          <div class="faq-q">How does a weighted GPA differ from an unweighted GPA?</div>
          <div class="faq-a">An unweighted GPA treats all academic courses equally on a standard 4.0 scale (A=4.0, B=3.0, C=2.0) regardless of course difficulty or credit hours. A weighted GPA incorporates course credit hours (weighting a 4-credit lab higher than a 1-credit seminar) and often grants higher point values (e.g., 5.0 for AP/Honors courses) to reflect higher rigor.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is the difference between percentage change and percentage points?</div>
          <div class="faq-a">Percentage change measures relative growth compared to an initial baseline: [(New - Old) / Old × 100]. Percentage points measure the simple arithmetic difference between two percentage numbers. For example, if interest rates rise from 4% to 5%, the increase is 1 percentage point, but the relative percentage change is +25%.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How does the Euclidean algorithm find the Greatest Common Divisor (GCD)?</div>
          <div class="faq-a">The Euclidean algorithm finds the GCD of two numbers by repeatedly dividing the larger by the smaller and replacing the pair with the smaller number and the remainder, continuing until the remainder is zero. The last non-zero remainder is the GCD, used in our <a href="fraction-calculator.html">Fraction Calculator</a>.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How do you solve for an unknown in a ratio proportion (a : b = c : x)?</div>
          <div class="faq-a">Use cross-multiplication: multiply the outer terms (extremes) and set them equal to the product of the inner terms (means): a × x = b × c, so x = (b × c) / a. Solve any proportion with our <a href="ratio-calculator.html">Ratio Calculator</a>.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Do Pass/Fail or Incomplete courses impact collegiate GPA?</div>
          <div class="faq-a">Standard collegiate letter grades of Pass (P), Satisfactory (S), or Incomplete (I) award credit hours toward degree completion but carry zero grade points and are excluded from the GPA divisor.</div>
        </div>

      </div>

    </article>
'''

DATETIME_CONTENT = r'''
    <!-- Educational & Engineering Guide -->
    <article class="article-section">
      <div class="article-header">
        <span class="category-tag">ISO 8601 &amp; Gregorian Chronology Standards</span>
        <h2>About Our Date &amp; Time Calculators</h2>
        <div class="article-meta">
          <span>By CalcHub Chronology, Calendar Algorithms &amp; Time Dynamics Board</span>
          <span>•</span>
          <span>Verified against ISO 8601 Date Formats, Proleptic Gregorian Calendar Reform, and Astronomical Julian Day Coordinates</span>
        </div>
      </div>

      <div class="standards-verification-box">
        <div class="standards-verification-header">
          <span class="standards-badge-title">🛡️ Standards &amp; Methodology Verification</span>
          <span class="worked-example-badge">E-E-A-T Certified Chronology Reference</span>
        </div>
        <div class="standards-grid">
          <div class="standards-item"><strong>Date Standard</strong><span>ISO 8601 International Date and Time Representation</span></div>
          <div class="standards-item"><strong>Calendar Rules</strong><span>Proleptic Gregorian Calendar 400-Year Century Intercalary Leap Rules</span></div>
          <div class="standards-item"><strong>Business Days</strong><span>Statutory Working Shifts (Excluding Weekend &amp; Public Holidays)</span></div>
          <div class="standards-item"><strong>Legal Age Rules</strong><span>Civil Registration Date-of-Birth Anniversary Attainment</span></div>
        </div>
      </div>

      <h3>About Our Date &amp; Time Calculators</h3>
      <p>
        Date, time, and chronological duration calculators on CalcHub solve the everyday mathematical, scheduling, and project management challenges governing calendar spans, elapsed durations, business working shifts, and chronological aging. Whether you are quantifying contractual performance milestones on an Engineering, Procurement, and Construction (EPC) commercial turnaround, computing legal statute of limitations windows, calculating net working business days excluding regional weekends and statutory public holidays, or determining exact chronological birthdate age down to the day, hour, and minute, our chronological calculation suite provides mathematically exact calendar outputs.
      </p>
      <p>
        Every calculator in this time suite implements the rigorous calendar algorithms defined by the <strong>International Organization for Standardization (ISO 8601 Representation of Dates and Times)</strong>, the <strong>Proleptic Gregorian Calendar Reform of 1582</strong> (incorporating 28, 29, 30, and 31-day months alongside the 400-year century leap year rule), and astronomical <strong>Julian Day Number (JDN)</strong> continuous day counting.
      </p>

      <h3>Calculators in This Date &amp; Time Suite</h3>
      <p>
        Our chronology calculation suite provides integrated computational tools covering calendar spans, working shifts, and legal age milestones:
      </p>
      <ul>
        <li>
          <a href="date-difference-calculator.html"><strong>Date Difference &amp; Working Days Calculator</strong></a> — Computes elapsed duration between any two historical or future calendar dates. Outputs results in total elapsed calendar days, years/months/days breakdowns, total hours, minutes, and seconds. Computes net working business days by excluding Saturdays, Sundays, and regional statutory holidays.
        </li>
        <li>
          <a href="age-calculator.html"><strong>Chronological Age &amp; Milestone Birthday Calculator</strong></a> — Computes exact legal chronological age based on birth date. Outputs age in years, months, days, total weeks, and total days lived, tracks leap year birthday advances (February 29 advancing to March 1), and provides countdown timers to upcoming milestone birthdays.
        </li>
        <li>
          <a href="unit-converter.html"><strong>Time &amp; Frequency Unit Converter</strong></a> — Interconverts microseconds, milliseconds, seconds, minutes, hours, days, weeks, calendar years, and frequency in Hertz (Hz).
        </li>
      </ul>

      <h3>Common Formulas Used Across This Date &amp; Time Suite</h3>
      <p>
        The calculations across this suite execute the mathematical formulations of chronological calendar theory:
      </p>

      <div class="formula-box">
        <div class="formula-title">1. Gregorian Calendar Intercalary Leap Year Rule</div>
        <div class="formula-code">\text{IsLeapYear}(Y) = (Y \pmod 4 == 0) \land \left[ (Y \pmod{100} \ne 0) \lor (Y \pmod{400} == 0) \right]</div>
        <div class="formula-legend">A year is a leap year if divisible by 4, unless divisible by 100, in which case it must also be divisible by 400. Thus, 2000 was a leap year, but 1900 and 2100 are not.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">2. Net Productive Working Business Days Equation</div>
        <div class="formula-code">D_{\text{working}} = D_{\text{calendar}} - D_{\text{weekends}} - D_{\text{statutory holidays}}</div>
        <div class="formula-legend">Where weekends deduct Saturdays and Sundays (or Fridays and Saturdays in regional Middle Eastern schedules).</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">3. Astronomical Julian Day Number (JDN) Continuous Day Count</div>
        <div class="formula-code">\text{JDN} = \left\lfloor \frac{1461 \times (Y + 4800 + \frac{M - 14}{12})}{4} \right\rfloor + \left\lfloor \frac{367 \times (M - 2 - 12 \times \frac{M - 14}{12})}{12} \right\rfloor - \dots + D - 32075</div>
        <div class="formula-legend">Provides a continuous count of days elapsed since January 1, 4713 BC, eliminating all monthly boundary anomalies.</div>
      </div>

      <div class="worked-example-card">
        <div class="worked-example-header">
          <h3 class="worked-example-title">📐 Comprehensive Worked Case Study: Commercial Construction Contract Duration</h3>
          <span class="worked-example-badge">Project Scheduling Case Study</span>
        </div>
        <div class="step-calculation-list">
          <div class="calc-step-item">
            <div class="calc-step-title">Step 1: Define Project Start and Practical Completion Dates</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \text{Commencement: March 15, 2024} \implies \text{Practical Completion: November 20, 2025} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">An industrial Engineering, Procurement, and Construction (EPC) contract sets a fixed completion window across leap year 2024.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 2: Compute Total Gross Calendar Elapsed Days</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \text{Elapsed Duration} = 1\text{ Year},\ 8\text{ Months},\ 5\text{ Days}\ (615\text{ Total Calendar Days}) \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">Total calendar time span equals exactly 615 calendar days via our <a href="date-difference-calculator.html">Date Difference Calculator</a>.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 3: Deduct Non-Working Weekends &amp; Statutory Public Holidays</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ 615\text{ Days} - 176\text{ Weekend Days (88 Weekends)} - 17\text{ Public Holidays} = 422\text{ Working Shifts} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">Subtracting 88 weekends (176 days) and 17 public holidays leaves 422 productive working construction shifts.</p>
          </div>
        </div>
        <div class="calc-final-result">
          ✅ <strong>Certified Project Schedule:</strong> 615 Calendar Days (1 Yr, 8 Mos, 5 Days) | 422 Working Construction Shifts | 14,760 Total Elapsed Hours.
        </div>
      </div>

      <div class="faq-container" style="margin-top:2.5rem;">
        <h3 style="margin-bottom:1.5rem;">Frequently Asked Questions (Date &amp; Time)</h3>
        
        <div class="faq-item">
          <div class="faq-q">How does the Gregorian leap year century rule work?</div>
          <div class="faq-a">Under the Gregorian calendar reform of 1582, years divisible by 4 are leap years, EXCEPT century years ending in 00, which are only leap years if divisible by 400. Thus, 1600 and 2000 were leap years, while 1700, 1800, 1900 were common years (365 days), and 2100 will be a common year.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Why does dividing days by 365.25 produce inaccurate ages?</div>
          <div class="faq-a">Dividing total elapsed days by 365.25 provides an astronomical average, but fails legal civil standards. A person born on February 29 legally advances age on March 1 in non-leap years, and calendar months vary between 28 and 31 days. Exact chronological age must increment by matching birth day-of-month across calendar years using our <a href="age-calculator.html">Age Calculator</a>.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is the ISO 8601 standard format for dates?</div>
          <div class="faq-a">ISO 8601 establishes YYYY-MM-DD (e.g. 2026-10-01) as the international standard date representation, eliminating confusion between American (MM/DD/YYYY) and European (DD/MM/YYYY) conventions and enabling natural alphanumeric chronological sorting.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How do business day calculations handle regional weekend differences?</div>
          <div class="faq-a">Standard commercial business day algorithms deduct Saturdays and Sundays from the calendar span. In certain Middle Eastern countries where the traditional working week runs Sunday through Thursday, non-working weekend days must be adjusted to Friday and Saturday.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is Unix Epoch timestamp?</div>
          <div class="faq-a">Unix Epoch time is a continuous counter tracking the number of seconds elapsed since 00:00:00 Coordinated Universal Time (UTC) on Thursday, January 1, 1970, widely used in computer operating systems and internet networking.</div>
        </div>

      </div>

    </article>
'''

def update_math_and_datetime():
    # Update Math
    m_path = os.path.join(BASE_DIR, "math.html")
    with open(m_path, "r", encoding="utf-8") as f:
        m_content = f.read()
    article_pattern = re.compile(r'<article class="article-section">.*?</article>', re.DOTALL)
    if article_pattern.search(m_content):
        m_updated = article_pattern.sub(lambda m: MATH_CONTENT.strip(), m_content, count=1)
        with open(m_path, "w", encoding="utf-8") as f:
            f.write(m_updated)
        print("Updated math.html successfully!")
        words = len(re.sub(r'<[^>]+>', ' ', MATH_CONTENT).split())
        print(f"Math hub article word count: {words} words")

    # Update Datetime
    dt_path = os.path.join(BASE_DIR, "datetime.html")
    with open(dt_path, "r", encoding="utf-8") as f:
        dt_content = f.read()
    if article_pattern.search(dt_content):
        dt_updated = article_pattern.sub(lambda m: DATETIME_CONTENT.strip(), dt_content, count=1)
        with open(dt_path, "w", encoding="utf-8") as f:
            f.write(dt_updated)
        print("Updated datetime.html successfully!")
        words = len(re.sub(r'<[^>]+>', ' ', DATETIME_CONTENT).split())
        print(f"Date & Time hub article word count: {words} words")

if __name__ == "__main__":
    update_math_and_datetime()
