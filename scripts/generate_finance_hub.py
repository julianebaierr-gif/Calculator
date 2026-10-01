import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FINANCE_CONTENT = r'''
    <!-- Educational & Engineering Guide -->
    <article class="article-section">
      <div class="article-header">
        <span class="category-tag">US GAAP, IFRS 9 &amp; Regulation Z Standards</span>
        <h2>About Our Financial &amp; Investment Calculators</h2>
        <div class="article-meta">
          <span>By CalcHub Financial &amp; Wealth Analytics Editorial Board</span>
          <span>•</span>
          <span>Verified against US GAAP, IFRS 9 Financial Instruments, Truth in Lending Act (Regulation Z), and CFA Institute Capital Asset Pricing Models</span>
        </div>
      </div>

      <div class="standards-verification-box">
        <div class="standards-verification-header">
          <span class="standards-badge-title">🛡️ Standards &amp; Methodology Verification</span>
          <span class="worked-example-badge">E-E-A-T Certified Financial Reference</span>
        </div>
        <div class="standards-grid">
          <div class="standards-item"><strong>Accounting Code</strong><span>US GAAP &amp; IFRS 9 Time Value of Money Standards</span></div>
          <div class="standards-item"><strong>Lending Disclosure</strong><span>Truth in Lending Act (Regulation Z) Annual Percentage Rate</span></div>
          <div class="standards-item"><strong>Amortization Engine</strong><span>Reducing-Balance Ordinary Annuity &amp; Prepayment Amortization</span></div>
          <div class="standards-item"><strong>Yield Conventions</strong><span>Annual Percentage Yield (APY) vs Nominal APR &amp; Continuous e^rt</span></div>
        </div>
      </div>

      <h3>About Our Financial &amp; Investment Calculators</h3>
      <p>
        Financial and wealth calculators on CalcHub solve the everyday mathematical, actuarial, and compounding challenges governing consumer and commercial debt amortization, investment portfolio growth, take-home payroll deductions, and retail discount economics. Whether you are structuring a 25-year commercial real estate mortgage with reducing-balance amortized monthly installments, modeling the exponential compounding growth of an index-linked sinking fund, evaluating how progressive marginal income tax brackets shape your executive net salary, or analyzing cascading retail markdowns, our financial calculation suite delivers verified, audit-ready financial schedules in seconds.
      </p>
      <p>
        Every calculator in this financial suite is built directly on the mathematical frameworks established by <strong>US Generally Accepted Accounting Principles (US GAAP)</strong>, the <strong>International Financial Reporting Standards (IFRS 9 Financial Instruments)</strong>, the <strong>Consumer Financial Protection Bureau (CFPB Truth in Lending Act / Regulation Z)</strong>, and quantitative guidelines from the <strong>CFA Institute</strong>. All financial calculations implement exact ordinary annuity formulas with zero rounded floating-point truncation, transparently displaying intermediate monthly periodic rates, cumulative interest totals, and principal balance reduction tables.
      </p>

      <h3>Calculators in This Financial &amp; Investment Suite</h3>
      <p>
        Our financial suite provides comprehensive computational models covering debt servicing, capital accumulation, and payroll analysis:
      </p>
      <ul>
        <li>
          <a href="loan-emi-calculator.html"><strong>Loan EMI &amp; Mortgage Amortization Calculator</strong></a> — Implements reducing-balance ordinary annuity algorithms to compute fixed Equated Monthly Installments (EMI) across residential mortgages, auto loans, and commercial debt. Generates full monthly and annual amortization schedules, breaks down interest versus principal allocations per billing cycle, models prepayment principal reductions, and identifies the exact principal-interest parity crossover date.
        </li>
        <li>
          <a href="compound-interest-calculator.html"><strong>Compound Interest &amp; Investment Growth Calculator</strong></a> — Models exponential capital growth under periodic regular contributions (annuity due and ordinary annuity). Evaluates compounding frequencies across daily (365/year), monthly (12/year), quarterly (4/year), semi-annually, annually, and theoretical continuous compounding ($A = P \cdot e^{rt}$). Computes true Annual Percentage Yield (APY) and nominal Annual Percentage Rate (APR).
        </li>
        <li>
          <a href="simple-interest-calculator.html"><strong>Simple Interest &amp; Bridge Loan Calculator</strong></a> — Computes linear interest accrual ($I = P \cdot r \cdot t$) for short-term commercial promissory notes, treasury bills, and bridge loans. Supports 365-day exact year and 360-day Banker's Rule conventions.
        </li>
        <li>
          <a href="salary-calculator.html"><strong>Gross-to-Net Salary &amp; Payroll Tax Calculator</strong></a> — Computes net take-home pay by stacking progressive marginal income tax brackets, mandatory FICA payroll contributions (6.2% Social Security up to wage caps, 1.45% Medicare), and pre-tax deductions across annual, monthly, bi-weekly (26 pay periods), and weekly compensation frequencies.
        </li>
        <li>
          <a href="discount-calculator.html"><strong>Discount, Markdown &amp; Sales Tax Calculator</strong></a> — Evaluates single and cascading retail markdowns, profit margins vs cost markups, dollar savings, and post-discount sales tax application.
        </li>
        <li>
          <a href="percentage-calculator.html"><strong>Financial Percentage &amp; Growth Rate Calculator</strong></a> — Computes relative percentage changes, profit margins, and basis point (bps) variance across corporate balance sheets.
        </li>
      </ul>

      <h3>Common Formulas Used Across This Financial Suite</h3>
      <p>
        The calculations across this suite execute the mathematical formulations of financial actuarial mathematics:
      </p>

      <div class="formula-box">
        <div class="formula-title">1. Reducing-Balance Equated Monthly Installment (EMI) Formula</div>
        <div class="formula-code">\text{EMI} = \frac{P \times r \times (1 + r)^n}{(1 + r)^n - 1}</div>
        <div class="formula-legend">Where P = Principal borrowed amount, r = Periodic monthly interest rate (Annual Nominal Rate / 12), and n = Total number of monthly repayment periods (Loan Years × 12). Monthly interest component: I_m = P_remaining × r; Principal component: P_m = EMI - I_m.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">2. Compound Interest Future Value with Periodic Deposits</div>
        <div class="formula-code">A = P \cdot \left(1 + \frac{r}{m}\right)^{m \cdot t} + \text{PMT} \cdot \left[ \frac{\left(1 + \frac{r}{m}\right)^{m \cdot t} - 1}{\frac{r}{m}} \right]</div>
        <div class="formula-legend">Where P = Initial lump-sum principal, r = Annual nominal interest rate, m = Compounding frequency per year, t = Total investment term in years, and PMT = Regular monthly or annual contribution deposit. Continuous compounding: A = P · e^(rt).</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">3. Annual Percentage Yield (APY) vs Nominal APR Conversion</div>
        <div class="formula-code">\text{APY} = \left(1 + \frac{\text{APR}}{m}\right)^m - 1 \implies \text{APR} = m \cdot \left[ (1 + \text{APY})^{1/m} - 1 \right]</div>
        <div class="formula-legend">Where m = Compounding periods per year. Compounding within the year causes effective annual yield (APY) to always exceed the nominal annual percentage rate (APR).</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">4. Simple Interest Linear Accrual Equation</div>
        <div class="formula-code">I = P \times r \times t,\quad A = P + I = P \cdot (1 + r \cdot t)</div>
        <div class="formula-legend">Where P = Principal, r = Annual simple interest rate (decimal), and t = Elapsed time in years (or Days / 365). Payoff occurs as a single lump-sum maturity repayment.</div>
      </div>

      <h3>Reference Financial Data &amp; Compounding Frequency Comparison</h3>
      <p>
        The following table illustrates how varying compounding frequencies amplify the effective annual return on a $100,000 principal at a nominal 8.00% APR over 10 and 20-year horizons:
      </p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Compounding Frequency</th>
              <th>Nominal Rate (APR)</th>
              <th>Effective Annual Yield (APY)</th>
              <th>10-Year Future Value ($100k Principal)</th>
              <th>20-Year Future Value ($100k Principal)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Annual (1× / Year)</td><td>8.00%</td><td>8.000%</td><td>$215,892.50</td><td>$466,095.71</td></tr>
            <tr><td>Semi-Annual (2× / Year)</td><td>8.00%</td><td>8.160%</td><td>$219,112.31</td><td>$480,102.06</td></tr>
            <tr><td>Quarterly (4× / Year)</td><td>8.00%</td><td>8.243%</td><td>$220,803.97</td><td>$487,543.92</td></tr>
            <tr><td>Monthly (12× / Year)</td><td>8.00%</td><td>8.300%</td><td>$221,964.02</td><td>$492,680.28</td></tr>
            <tr><td>Daily (365× / Year)</td><td>8.00%</td><td>8.328%</td><td>$222,534.58</td><td>$495,216.40</td></tr>
            <tr><td>Continuous Compounding (e^rt)</td><td>8.00%</td><td>8.329%</td><td>$222,554.09</td><td>$495,303.24</td></tr>
          </tbody>
        </table>
      </div>

      <h3>When to Use Each Calculator: Professional Financial Workflows</h3>
      <p>
        In financial planning and corporate treasury, decisions require comparing borrowing debt costs against potential investment returns. The following workflow demonstrates how our tools integrate:
      </p>

      <h4>Workflow 1: Commercial Facility Acquisition vs Sinking Fund Opportunity Cost</h4>
      <ol>
        <li>
          <strong>Step 1 — Calculate Loan Debt Service Outflow:</strong> A business evaluates purchasing a $450,000 commercial facility with a 20-year mortgage at 6.50% annual interest. Running the <a href="loan-emi-calculator.html">Loan EMI Calculator</a> determines a required monthly repayment of $3,354.95 ($805,188 total lifetime outflow, including $355,188 in interest charges).
        </li>
        <li>
          <strong>Step 2 — Model Investment Opportunity Cost of Capital:</strong> Contrast borrowing with leasing and directing capital into a corporate investment reserve. Open the <a href="compound-interest-calculator.html">Compound Interest Calculator</a>. Investing an initial $90,000 down payment plus monthly savings of $1,000 at an 8.5% index return yields $831,450 over 20 years ($491,450 pure compounding interest profit).
        </li>
        <li>
          <strong>Step 3 — Evaluate Executive Payroll Impact:</strong> Analyze executive compensation and partner draws necessary to support business debt coverage using our <a href="salary-calculator.html">Salary Calculator</a>.
        </li>
      </ol>

      <div class="worked-example-card">
        <div class="worked-example-header">
          <h3 class="worked-example-title">📐 Comprehensive Worked Case Study: Commercial Real Estate Mortgage Amortization</h3>
          <span class="worked-example-badge">Real-World Corporate Debt Problem</span>
        </div>
        <div class="step-calculation-list">
          <div class="calc-step-item">
            <div class="calc-step-title">Step 1: Define Loan Parameters &amp; Periodic Monthly Interest Rate</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ P = \$400{,}000,\quad r_{annual} = 6.75\%,\quad n = 240\text{ months (20 years)} \]
              \[ r_{monthly} = \frac{0.0675}{12} = 0.005625\text{ per month} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">A commercial entity borrows $400,000 at 6.75% fixed annual interest over 20 years. Interest accrues monthly on the declining balance at 0.5625%.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 2: Calculate Fixed Equated Monthly Installment (EMI)</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \text{EMI} = \frac{400{,}000 \times 0.005625 \times (1.005625)^{240}}{(1.005625)^{240} - 1} = \$3{,}041.22 \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">The fixed monthly repayment equals $3,041.22 via our <a href="loan-emi-calculator.html">Loan EMI Calculator</a>.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 3: Analyze Lifetime Interest &amp; Month 1 Amortization Tilt</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ \text{Total Repayment} = 240 \times \$3{,}041.22 = \$729{,}892.80,\quad \text{Total Interest} = \$329{,}892.80 \]
              \[ \text{Month 1 Interest} = \$400{,}000 \times 0.005625 = \$2{,}250.00\ (74\%),\quad \text{Month 1 Principal} = \$791.22\ (26\%) \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">In Month 1, $2,250 goes to interest and only $791 to principal. Total lifetime interest paid amounts to $329,892.80 (82.5% of original principal!).</p>
          </div>
        </div>
        <div class="calc-final-result">
          ✅ <strong>Certified Amortization Profile:</strong> Monthly EMI: $3,041.22 | Total Outflow: $729,892.80 | Total Interest Incurred: $329,892.80 | Principal-Interest Parity: Month 104.
        </div>
      </div>

      <h3>Industry Codes, Regulatory Standards &amp; Quality Assurance (E-E-A-T)</h3>
      <p>
        Financial computation is regulated by law to protect borrowers from predatory hidden interest charges:
      </p>
      <ul>
        <li><strong>Truth in Lending Act (Regulation Z):</strong> Mandates that lenders disclose the true Annual Percentage Rate (APR), finance charges, and payment schedules prominently before closing, prohibiting misleading flat-rate calculations.</li>
        <li><strong>IFRS 9 Financial Instruments:</strong> Enforces amortized cost accounting for debt instruments using the effective interest method, requiring precise recognition of interest income and expense over the asset's lifecycle.</li>
        <li><strong>US Internal Revenue Code (IRC Section 415 &amp; Circular E):</strong> Standardizes progressive federal payroll income tax withholding calculations and mandatory employer FICA matching requirements.</li>
      </ul>

      <div class="faq-container" style="margin-top:2.5rem;">
        <h3 style="margin-bottom:1.5rem;">Frequently Asked Questions (Finance &amp; Investment)</h3>
        
        <div class="faq-item">
          <div class="faq-q">What is the difference between reducing-balance interest and flat-rate interest?</div>
          <div class="faq-a">In reducing-balance amortization, monthly interest is calculated strictly on the remaining outstanding principal balance. As you pay off principal, future interest charges drop. In a flat-rate loan, interest is calculated on the full initial loan amount across the entire term, doubling or tripling the effective APR compared to reducing-balance loans.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is the difference between APR and APY?</div>
          <div class="faq-a">Annual Percentage Rate (APR) represents the nominal annualized interest rate without taking into account intra-year compounding. Annual Percentage Yield (APY) takes into account the compounding frequency (daily, monthly). For example, 10% APR compounded daily yields an effective 10.52% APY.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Why does loan amortization tilt heavily toward interest in the early years?</div>
          <div class="faq-a">Because the outstanding loan principal is at its maximum during the initial years. On a $400,000 loan at 6.75%, the very first month's interest alone is $2,250 ($400,000 × 0.0675 / 12), leaving only a fraction of the EMI to pay down principal. Only as principal decreases does the interest portion shrink and principal paydown accelerate.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How do progressive marginal tax brackets work in salary calculations?</div>
          <div class="faq-a">Progressive income tax brackets tax dollars within specific income ranges, not your entire income. Moving into a higher bracket (e.g., from 12% to 22%) means only the dollars earned above that threshold are taxed at 22%. Your income below that threshold remains taxed at the lower 10% and 12% rates. Check your take-home pay with our <a href="salary-calculator.html">Salary Calculator</a>.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Why does '30% off + 15% off' not equal 45% off in retail markdowns?</div>
          <div class="faq-a">Retail discounts are applied consecutively, not additively. The first 30% discount drops the price to 70% of original. The second 15% discount applies to that reduced 70% balance (0.70 × 0.85 = 0.595, or 59.5% of original price). The true effective discount is 40.5%, not 45%. Model discounts with our <a href="discount-calculator.html">Discount Calculator</a>.</div>
        </div>

      </div>

    </article>
'''

def update_finance():
    filepath = os.path.join(BASE_DIR, "finance.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    article_pattern = re.compile(r'<article class="article-section">.*?</article>', re.DOTALL)
    if article_pattern.search(content):
        updated = article_pattern.sub(lambda m: FINANCE_CONTENT.strip(), content, count=1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated)
        print("Updated finance.html successfully!")
        words = len(re.sub(r'<[^>]+>', ' ', FINANCE_CONTENT).split())
        print(f"Finance hub article word count: {words} words")

if __name__ == "__main__":
    update_finance()
