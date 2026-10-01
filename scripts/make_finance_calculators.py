import os

OUTPUT_DIR = r"C:\Users\Admin\.gemini\antigravity\scratch\calchub"

from make_health_remaining import page_scaffold

# ==========================================
# 6. LOAN EMI CALCULATOR
# ==========================================
emi_app_json = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Loan EMI Calculator",
      "url": "https://calchub.org/loan-emi-calculator.html",
      "applicationCategory": "FinanceApplication",
      "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How is Loan EMI calculated?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Loan EMI is calculated using the reducing balance formula: EMI = [P × r × (1+r)^n] / [(1+r)^n - 1], where P is Principal loan amount, r is the monthly interest rate (annual rate divided by 12 and 100), and n is loan tenure in months."
          }
        }
      ]
    }
  ]
}"""

emi_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">🏦 Loan Details</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="emi-amount">Loan Principal Amount</label>
              <div class="input-wrap has-unit">
                <input type="number" id="emi-amount" value="50000" min="500" max="10000000" step="500" oninput="calcEMI()">
                <span class="input-unit-badge">$</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="emi-rate">Annual Interest Rate (%)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="emi-rate" value="7.5" min="0.1" max="50" step="0.1" oninput="calcEMI()">
                <span class="input-unit-badge">%</span>
              </div>
            </div>
            <div class="input-group calc-field-full">
              <label class="input-label" for="emi-tenure">Loan Tenure (Years)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="emi-tenure" value="5" min="1" max="40" step="1" oninput="calcEMI()">
                <span class="input-unit-badge">yrs</span>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy EMI Summary</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Schedule</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Payment Breakdown</span>
          <span class="status-pill status-success">Monthly Amortization</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Monthly Equated Installment (EMI)</div>
          <div>
            <span class="primary-result-value" id="emi-monthly">$1,001.90</span>
          </div>
        </div>
        <div class="visual-bar-wrap">
          <div class="visual-bar-track">
            <div class="visual-bar-fill" id="emi-bar-p" style="width: 83%; background: #2563EB;"></div>
            <div class="visual-bar-fill" id="emi-bar-i" style="width: 17%; background: #D97706;"></div>
          </div>
          <div class="visual-bar-labels">
            <span style="color:#2563EB;">Principal: <span id="lbl-pct-p">83%</span></span>
            <span style="color:#D97706;">Total Interest: <span id="lbl-pct-i">17%</span></span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Total Principal</div>
            <div class="breakdown-val" id="emi-tot-p">$50,000</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Total Interest Payable</div>
            <div class="breakdown-val" id="emi-tot-i" style="color:#D97706;">$10,114</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Total Payment (P + I)</div>
            <div class="breakdown-val" id="emi-tot-all">$60,114</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Total Installments</div>
            <div class="breakdown-val" id="emi-months">60 months</div>
          </div>
        </div>
      </section>
"""

emi_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>An <strong>Equated Monthly Installment (EMI)</strong> is a fixed payment amount made by a borrower to a lender at a specified date each calendar month. The standard mathematical reducing balance formula is:</p>
      <p><code>EMI = [P × r × (1+r)^n] ÷ [(1+r)^n - 1]</code></p>
      <p>Where <strong>P</strong> = Principal loan amount, <strong>r</strong> = Monthly interest rate (Annual Rate ÷ 12 ÷ 100), and <strong>n</strong> = Number of monthly installments. Over time, the interest portion of each EMI payment decreases while the principal portion increases.</p>
    </section>
"""

emi_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#emi-formula">The Reducing Balance Equation</a></li>
        <li><a href="#emi-amortization">How Amortization Works Over Time</a></li>
        <li><a href="#prepayment-impact">Impact of Loan Prepayments</a></li>
        <li><a href="#emi-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

emi_article = """
      <h2 id="emi-formula">The Mathematics of Reducing Balance Loans</h2>
      <p>Banks and retail mortgage providers compute loan repayments using the amortization formula. Unlike flat-rate loans where interest is charged on the original principal for the entire term, reducing-balance loans calculate monthly interest strictly on the remaining outstanding principal.</p>

      <div class="formula-box">
        <div class="formula-title">Amortization Formula</div>
        <div class="formula-code">EMI = P × r × (1 + r)ⁿ / [ (1 + r)ⁿ - 1 ]</div>
        <div class="formula-legend">P = Loan Principal | r = Monthly Interest Rate | n = Tenure in Months</div>
      </div>

      <h2 id="emi-amortization">How Loan Amortization Shifts Over Time</h2>
      <p>In the initial months of your loan, the bulk of your EMI goes directly toward interest service. As the principal balance diminishes, the interest charge shrinks, allowing an increasingly larger portion of each subsequent installment to wipe out the principal debt.</p>

      <h2 id="prepayment-impact">The Power of Prepayment</h2>
      <p>Making even a single additional payment each year or paying an extra 5-10% above your mandatory EMI reduces the principal immediately. Because compound interest works on the remaining balance, prepaying early in the loan tenure yields massive lifetime interest savings and can shave years off your repayment timeline.</p>

      <h2 id="emi-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>What is the difference between fixed-rate and floating-rate EMI?</summary>
          <div class="faq-content">A fixed-rate loan locks your interest rate and monthly EMI for the entire tenure. A floating-rate loan adjusts periodically based on central bank benchmark rates (such as SOFR or repo rate), meaning your EMI or loan duration may rise or fall with market fluctuations.</div>
        </details>
      </div>
"""

emi_script = """
  <script>
    function calcEMI() {
      const p = parseFloat(document.getElementById('emi-amount').value) || 50000;
      const rateAnnual = parseFloat(document.getElementById('emi-rate').value) || 7.5;
      const years = parseFloat(document.getElementById('emi-tenure').value) || 5;

      const n = years * 12;
      const r = (rateAnnual / 100) / 12;

      let emi = 0;
      if (r === 0) {
        emi = p / n;
      } else {
        const factor = Math.pow(1 + r, n);
        emi = (p * r * factor) / (factor - 1);
      }

      const totalPayment = emi * n;
      const totalInterest = totalPayment - p;

      const pctP = Math.round((p / totalPayment) * 100);
      const pctI = 100 - pctP;

      document.getElementById('emi-monthly').textContent = '$' + emi.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
      document.getElementById('emi-tot-p').textContent = '$' + Math.round(p).toLocaleString();
      document.getElementById('emi-tot-i').textContent = '$' + Math.round(totalInterest).toLocaleString();
      document.getElementById('emi-tot-all').textContent = '$' + Math.round(totalPayment).toLocaleString();
      document.getElementById('emi-months').textContent = `${n} months`;

      document.getElementById('emi-bar-p').style.width = pctP + '%';
      document.getElementById('emi-bar-i').style.width = pctI + '%';
      document.getElementById('lbl-pct-p').textContent = pctP + '%';
      document.getElementById('lbl-pct-i').textContent = pctI + '%';
    }
    function copyResults() {
      const emi = document.getElementById('emi-monthly').textContent;
      const tot = document.getElementById('emi-tot-all').textContent;
      window.copyToClipboard(`CalcHub Loan Report: Monthly EMI: ${emi}, Total Payment: ${tot}`);
    }
    calcEMI();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "loan-emi-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Loan EMI Calculator — Accurate Reducing Balance Amortization",
                          "Calculate your exact monthly EMI, total interest, and total repayment amount for home loans, auto loans, and personal loans with visual amortization breakdown.",
                          "loan emi calculator, home loan emi, auto loan calculator, mortgage emi, amortization schedule calculator, monthly installment",
                          "loan-emi-calculator", "Finance & Loans", "finance", emi_app_json,
                          "Plan your borrowing with confidence. Calculate exact monthly repayments, analyze total interest liability, and optimize your loan tenure.",
                          emi_workspace, emi_geo, emi_toc, emi_article, emi_script))

# ==========================================
# 7. COMPOUND INTEREST CALCULATOR
# ==========================================
ci_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Compound Interest Calculator",
  "url": "https://calchub.org/compound-interest-calculator.html",
  "applicationCategory": "FinanceApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

ci_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">📈 Investment & Growth Inputs</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="ci-principal">Initial Deposit (Principal)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="ci-principal" value="10000" min="100" max="10000000" step="500" oninput="calcCI()">
                <span class="input-unit-badge">$</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="ci-monthly">Monthly Addition</label>
              <div class="input-wrap has-unit">
                <input type="number" id="ci-monthly" value="300" min="0" max="100000" step="50" oninput="calcCI()">
                <span class="input-unit-badge">$</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="ci-rate">Estimated Annual Return (%)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="ci-rate" value="8" min="0.1" max="40" step="0.1" oninput="calcCI()">
                <span class="input-unit-badge">%</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="ci-years">Investment Period (Years)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="ci-years" value="15" min="1" max="50" step="1" oninput="calcCI()">
                <span class="input-unit-badge">yrs</span>
              </div>
            </div>
            <div class="input-group calc-field-full">
              <label class="input-label" for="ci-freq">Compounding Frequency</label>
              <div class="input-wrap">
                <select id="ci-freq" onchange="calcCI()">
                  <option value="12" selected>Monthly (12x/yr — Standard)</option>
                  <option value="1">Annually (1x/yr)</option>
                  <option value="4">Quarterly (4x/yr)</option>
                  <option value="365">Daily (365x/yr)</option>
                </select>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Portfolio Growth</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Forecast</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Projected Portfolio Value</span>
          <span class="status-pill status-success">Wealth Accumulation</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Total Future Value</div>
          <div>
            <span class="primary-result-value" id="ci-total">$135,528</span>
          </div>
        </div>
        <div class="visual-bar-wrap">
          <div class="visual-bar-track">
            <div class="visual-bar-fill" id="ci-bar-p" style="width: 47%; background: #2563EB;"></div>
            <div class="visual-bar-fill" id="ci-bar-i" style="width: 53%; background: #059669;"></div>
          </div>
          <div class="visual-bar-labels">
            <span style="color:#2563EB;">Contributions: <span id="lbl-ci-p">47%</span></span>
            <span style="color:#059669;">Compound Growth: <span id="lbl-ci-i">53%</span></span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Initial Principal</div>
            <div class="breakdown-val" id="ci-out-p">$10,000</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Total Deposits</div>
            <div class="breakdown-val" id="ci-out-deposits">$64,000</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Total Interest Earned</div>
            <div class="breakdown-val" id="ci-out-int" style="color:#059669;">$71,528</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Multiplier Effect</div>
            <div class="breakdown-val" id="ci-out-mult">2.1x</div>
          </div>
        </div>
      </section>
"""

ci_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p><strong>Compound Interest</strong> is the addition of interest to the principal sum of an investment, resulting in interest earning interest on itself. The core mathematical formula is:</p>
      <p><code>A = P × (1 + r/n)^(n·t) + PMT × [ ((1 + r/n)^(n·t) - 1) / (r/n) ]</code></p>
      <p>Where <strong>A</strong> = Future Value, <strong>P</strong> = Initial Principal, <strong>r</strong> = Annual Interest Rate, <strong>n</strong> = Compounding frequency per year, <strong>t</strong> = Time in years, and <strong>PMT</strong> = Periodic monthly addition. Compounding generates exponential growth rather than linear growth.</p>
    </section>
"""

ci_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#ci-power">The Exponential Power of Compounding</a></li>
        <li><a href="#ci-rule72">The Rule of 72 Shortcut</a></li>
        <li><a href="#ci-compounding-freq">Frequency Comparison (Daily vs Monthly vs Annual)</a></li>
        <li><a href="#ci-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

ci_article = """
      <h2 id="ci-power">The Exponential Mathematics of Wealth Creation</h2>
      <p>Albert Einstein famously remarked that <em>"Compound interest is the eighth wonder of the world. He who understands it, earns it; he who doesn't, pays it."</em> In standard simple interest, earnings grow linearly along a straight line. With compound interest, the principal baseline expands every single period, producing an exponential upward trajectory.</p>

      <div class="formula-box">
        <div class="formula-title">Compound Interest Equation</div>
        <div class="formula-code">A = P · (1 + r/n)ⁿᵗ</div>
        <div class="formula-legend">P = Initial Deposit | r = Annual Rate | n = Times Compounded per Year | t = Years</div>
      </div>

      <h2 id="ci-rule72">The Rule of 72: How Fast Will Your Money Double?</h2>
      <p>To quickly calculate how many years it takes for an investment to double at a given annual interest rate without complex logarithms, divide <strong>72</strong> by the annual interest rate:</p>
      <p><code>Years to Double ≈ 72 ÷ Annual Return Rate (%)</code></p>
      <p>At an <strong>8% annual return</strong> (close to the historical S&P 500 index inflation-adjusted average), your money doubles roughly every <strong>9 years</strong> (72 ÷ 8 = 9). Over a 36-year career, an initial portfolio doubles four separate times (2⁴ = 16x growth)!</p>

      <h2 id="ci-compounding-freq">Does Compounding Frequency Matter?</h2>
      <p>More frequent compounding (daily vs annual) slightly increases your Effective Annual Rate (EAR). However, mathematically, as the compounding frequency approaches infinity, the growth converges to the continuous exponential limit <code>P · eʳᵗ</code>. Regular monthly contributions dominate terminal wealth far more than whether interest compounds monthly or daily.</p>

      <h2 id="ci-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>What is the difference between APR and APY?</summary>
          <div class="faq-content">Annual Percentage Rate (APR) is the simple annualized interest rate without taking compounding into account. Annual Percentage Yield (APY) reflects the true annual return earned after factoring in the compounding effect over 12 months.</div>
        </details>
      </div>
"""

ci_script = """
  <script>
    function calcCI() {
      const p = parseFloat(document.getElementById('ci-principal').value) || 10000;
      const pmt = parseFloat(document.getElementById('ci-monthly').value) || 300;
      const r = (parseFloat(document.getElementById('ci-rate').value) || 8) / 100;
      const t = parseFloat(document.getElementById('ci-years').value) || 15;
      const n = parseFloat(document.getElementById('ci-freq').value) || 12;

      const ratePerPeriod = r / n;
      const totalPeriods = n * t;

      // Principal compound growth
      const principalFuture = p * Math.pow(1 + ratePerPeriod, totalPeriods);

      // Monthly additions compound growth (approximated for compounding intervals)
      let contributionsFuture = 0;
      if (pmt > 0) {
        const monthlyRate = r / 12;
        const totalMonths = t * 12;
        contributionsFuture = pmt * ( (Math.pow(1 + monthlyRate, totalMonths) - 1) / monthlyRate );
      }

      const totalWealth = principalFuture + contributionsFuture;
      const totalDeposited = p + (pmt * 12 * t);
      const totalInterest = totalWealth - totalDeposited;

      const pctDep = Math.round((totalDeposited / totalWealth) * 100);
      const pctInt = 100 - pctDep;
      const mult = totalWealth / totalDeposited;

      document.getElementById('ci-total').textContent = '$' + Math.round(totalWealth).toLocaleString();
      document.getElementById('ci-out-p').textContent = '$' + Math.round(p).toLocaleString();
      document.getElementById('ci-out-deposits').textContent = '$' + Math.round(totalDeposited).toLocaleString();
      document.getElementById('ci-out-int').textContent = '$' + Math.round(totalInterest).toLocaleString();
      document.getElementById('ci-out-mult').textContent = mult.toFixed(1) + 'x';

      document.getElementById('ci-bar-p').style.width = pctDep + '%';
      document.getElementById('ci-bar-i').style.width = pctInt + '%';
      document.getElementById('lbl-ci-p').textContent = pctDep + '%';
      document.getElementById('lbl-ci-i').textContent = pctInt + '%';
    }
    function copyResults() {
      const tot = document.getElementById('ci-total').textContent;
      const int = document.getElementById('ci-out-int').textContent;
      window.copyToClipboard(`CalcHub Compound Interest Forecast: Future Value: ${tot}, Total Interest: ${int}`);
    }
    calcCI();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "compound-interest-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Compound Interest Calculator — Exponential Investment Growth",
                          "Forecast your wealth accumulation with daily, monthly, or annual compounding and recurring deposits. Includes Rule of 72 and inflation insights.",
                          "compound interest calculator, investment calculator, future value calculator, rule of 72, interest compounding formula",
                          "compound-interest-calculator", "Finance & Investment", "finance", ci_app_json,
                          "Harness the mathematics of compound growth. Project your investment portfolio with recurring monthly contributions and flexible compounding frequencies.",
                          ci_workspace, ci_geo, ci_toc, ci_article, ci_script))

# ==========================================
# 8. SIMPLE INTEREST CALCULATOR
# ==========================================
si_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Simple Interest Calculator",
  "url": "https://calchub.org/simple-interest-calculator.html",
  "applicationCategory": "FinanceApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

si_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">💰 Simple Interest Inputs</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="si-p">Principal Amount</label>
              <div class="input-wrap has-unit">
                <input type="number" id="si-p" value="5000" min="10" max="10000000" step="100" oninput="calcSI()">
                <span class="input-unit-badge">$</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="si-r">Annual Interest Rate (%)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="si-r" value="5.5" min="0.1" max="50" step="0.1" oninput="calcSI()">
                <span class="input-unit-badge">%</span>
              </div>
            </div>
            <div class="input-group calc-field-full">
              <label class="input-label" for="si-t">Time Horizon (Years)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="si-t" value="3" min="0.1" max="50" step="0.5" oninput="calcSI()">
                <span class="input-unit-badge">yrs</span>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Result</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Summary</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Calculated Payout</span>
          <span class="status-pill status-success">Linear Return</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Total Simple Interest</div>
          <div>
            <span class="primary-result-value" id="si-int" style="color:#059669;">$825.00</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Initial Principal</div>
            <div class="breakdown-val" id="si-out-p">$5,000</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Total Maturity Amount</div>
            <div class="breakdown-val" id="si-out-tot">$5,825.00</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Interest Per Year</div>
            <div class="breakdown-val" id="si-out-yr">$275.00/yr</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Interest Per Month</div>
            <div class="breakdown-val" id="si-out-mo">$22.92/mo</div>
          </div>
        </div>
      </section>
"""

si_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p><strong>Simple Interest (I)</strong> is calculated solely on the initial principal balance for the entire borrowing period without reinvesting earned interest. The formula is:</p>
      <p><code>I = (P × R × T) ÷ 100</code></p>
      <p>Where <strong>P</strong> = Principal sum, <strong>R</strong> = Annual interest rate percentage, and <strong>T</strong> = Time period in years. Total maturity value equals <code>A = P + I</code>.</p>
    </section>
"""

si_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#si-basics">Simple Interest Equation Breakdown</a></li>
        <li><a href="#si-vs-ci">Simple vs. Compound Interest Comparison</a></li>
        <li><a href="#si-use-cases">When Simple Interest is Used</a></li>
        <li><a href="#si-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

si_article = """
      <h2 id="si-basics">The Simple Interest Equation</h2>
      <p>Simple interest is the easiest method of calculating borrowing cost or basic returns. Unlike compound interest, interest accrued during period 1 is paid out or set aside, never being added to the principal balance for period 2.</p>

      <div class="formula-box">
        <div class="formula-title">Simple Interest Formula</div>
        <div class="formula-code">I = P · r · t &nbsp;|&nbsp; A = P · (1 + r · t)</div>
        <div class="formula-legend">P = Principal | r = Annual Rate (decimal) | t = Time (Years) | A = Total Accrued</div>
      </div>

      <h2 id="si-vs-ci">Simple vs. Compound Interest Comparison</h2>
      <p>For short durations (under 1 year), simple and annual compound interest yield identical results. However, over multi-year horizons, compound interest diverges dramatically upward.</p>

      <h2 id="si-use-cases">Where is Simple Interest Encountered?</h2>
      <ul>
        <li>Short-term personal promissory notes between individuals.</li>
        <li>Certain non-revolving auto loans.</li>
        <li>Certain fixed certificates of deposit where coupons are directly deposited into a checking account.</li>
      </ul>

      <h2 id="si-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>How do I calculate simple interest for months or days?</summary>
          <div class="faq-content">Convert months to years by dividing by 12 (e.g. 6 months = 6/12 = 0.5 years). For days, divide by 365 (or 360 for ordinary commercial banking conventions).</div>
        </details>
      </div>
"""

si_script = """
  <script>
    function calcSI() {
      const p = parseFloat(document.getElementById('si-p').value) || 5000;
      const r = parseFloat(document.getElementById('si-r').value) || 5.5;
      const t = parseFloat(document.getElementById('si-t').value) || 3;

      const interest = (p * r * t) / 100;
      const total = p + interest;
      const perYr = interest / t;
      const perMo = interest / (t * 12);

      document.getElementById('si-int').textContent = '$' + interest.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
      document.getElementById('si-out-p').textContent = '$' + Math.round(p).toLocaleString();
      document.getElementById('si-out-tot').textContent = '$' + total.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
      document.getElementById('si-out-yr').textContent = '$' + perYr.toFixed(2) + '/yr';
      document.getElementById('si-out-mo').textContent = '$' + perMo.toFixed(2) + '/mo';
    }
    function copyResults() {
      const i = document.getElementById('si-int').textContent;
      const t = document.getElementById('si-out-tot').textContent;
      window.copyToClipboard(`CalcHub Simple Interest: Interest: ${i}, Total Maturity: ${t}`);
    }
    calcSI();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "simple-interest-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Simple Interest Calculator — Quick I = P*R*T Calculation",
                          "Compute linear simple interest and total repayment maturity amount for short-term loans, bonds, and notes. Simple, instant, and transparent.",
                          "simple interest calculator, i prt formula, basic interest calculator, simple interest rate, calculate simple interest",
                          "simple-interest-calculator", "Finance & Loans", "finance", si_app_json,
                          "Quickly compute non-compounding interest and total maturity returns for personal loans, promissory notes, and fixed coupon bonds.",
                          si_workspace, si_geo, si_toc, si_article, si_script))

# ==========================================
# 9. DISCOUNT & SALE CALCULATOR
# ==========================================
disc_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Discount Calculator",
  "url": "https://calchub.org/discount-calculator.html",
  "applicationCategory": "FinanceApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

disc_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">🏷️ Price & Discount Terms</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="disc-orig">Original Price</label>
              <div class="input-wrap has-unit">
                <input type="number" id="disc-orig" value="120" min="0.01" max="1000000" step="1" oninput="calcDiscount()">
                <span class="input-unit-badge">$</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="disc-pct">Discount Percentage (%)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="disc-pct" value="25" min="0" max="100" step="1" oninput="calcDiscount()">
                <span class="input-unit-badge">%</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="disc-extra">Additional / Coupon Discount (%)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="disc-extra" value="10" min="0" max="100" step="1" oninput="calcDiscount()">
                <span class="input-unit-badge">%</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="disc-tax">Sales Tax Rate (%)</label>
              <div class="input-wrap has-unit">
                <input type="number" id="disc-tax" value="8" min="0" max="40" step="0.25" oninput="calcDiscount()">
                <span class="input-unit-badge">%</span>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Final Price</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Receipt</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Final Checkout Total</span>
          <span class="status-pill status-success" id="disc-pill">32.5% Total Off</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Final Price to Pay (with Tax)</div>
          <div>
            <span class="primary-result-value" id="disc-final">$87.48</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Total Money Saved</div>
            <div class="breakdown-val" id="disc-saved" style="color:#059669;">$39.00</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Pre-Tax Sale Price</div>
            <div class="breakdown-val" id="disc-pretax">$81.00</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Sales Tax Amount</div>
            <div class="breakdown-val" id="disc-tax-amt">$6.48</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Effective Total Discount</div>
            <div class="breakdown-val" id="disc-eff">32.5%</div>
          </div>
        </div>
      </section>
"""

disc_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>To calculate a <strong>discounted sale price</strong>:</p>
      <p><code>Discount Amount = Original Price × (Discount % ÷ 100)</code></p>
      <p><code>Final Sale Price = Original Price - Discount Amount</code></p>
      <p>When stacking an additional coupon discount (e.g. 20% off plus an extra 10% off), the discounts apply <strong>sequentially</strong>, not additively. A 20% + 10% sequential discount equals an effective 28% total discount, not 30%.</p>
    </section>
"""

disc_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#discount-calc-formula">How Single & Stacking Discounts Work</a></li>
        <li><a href="#sequential-vs-additive">Why 20% + 10% Does Not Equal 30%</a></li>
        <li><a href="#sales-tax-impact">Factoring in Local Sales Tax</a></li>
        <li><a href="#disc-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

disc_article = """
      <h2 id="discount-calc-formula">Discount Calculations Explained</h2>
      <p>Calculating the true bargain during retail clearance events requires understanding both direct percentage discounts and compound coupon stacking.</p>

      <div class="formula-box">
        <div class="formula-title">Discount Equations</div>
        <div class="formula-code">Savings = Price × (Discount % ÷ 100)<br>Final = Price × (1 - D₁/100) × (1 - D₂/100) × (1 + Tax/100)</div>
      </div>

      <h2 id="sequential-vs-additive">Why Stacking Discounts Are Sequential</h2>
      <p>Retail stores apply second coupons to the <em>already-discounted</em> intermediate price rather than the initial sticker tag. For example, on a $100 item with 50% off and an extra 20% VIP code:</p>
      <ul>
        <li>First cut: $100 - 50% = $50</li>
        <li>Second cut: 20% of $50 = $10 reduction</li>
        <li>Final checkout: $40 (Total discount = 60%, not 70%)</li>
      </ul>

      <h2 id="sales-tax-impact">Factoring in Sales Tax</h2>
      <p>In most jurisdictions (such as the United States), sales tax is computed on the final post-discount sale price rather than the original manufacturer suggested retail price (MSRP).</p>

      <h2 id="disc-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>How do I reverse calculate the original price from a sale price?</summary>
          <div class="faq-content">Divide the sale price by (1 minus the discount percentage in decimal format). For example, if a jacket on a 25% sale costs $75: Original Price = $75 ÷ (1 - 0.25) = $75 ÷ 0.75 = $100.</div>
        </details>
      </div>
"""

disc_script = """
  <script>
    function calcDiscount() {
      const orig = parseFloat(document.getElementById('disc-orig').value) || 0;
      const d1 = parseFloat(document.getElementById('disc-pct').value) || 0;
      const d2 = parseFloat(document.getElementById('disc-extra').value) || 0;
      const taxRate = parseFloat(document.getElementById('disc-tax').value) || 0;

      // Sequential discount
      const priceAfterD1 = orig * (1 - (d1 / 100));
      const priceAfterD2 = priceAfterD1 * (1 - (d2 / 100));
      const totalSaved = orig - priceAfterD2;
      const effDiscountPct = orig > 0 ? (totalSaved / orig) * 100 : 0;

      const taxAmount = priceAfterD2 * (taxRate / 100);
      const finalPrice = priceAfterD2 + taxAmount;

      document.getElementById('disc-final').textContent = '$' + finalPrice.toFixed(2);
      document.getElementById('disc-saved').textContent = '$' + totalSaved.toFixed(2);
      document.getElementById('disc-pretax').textContent = '$' + priceAfterD2.toFixed(2);
      document.getElementById('disc-tax-amt').textContent = '$' + taxAmount.toFixed(2);
      document.getElementById('disc-eff').textContent = effDiscountPct.toFixed(1) + '%';
      document.getElementById('disc-pill').textContent = effDiscountPct.toFixed(1) + '% Total Off';
    }
    function copyResults() {
      const f = document.getElementById('disc-final').textContent;
      const s = document.getElementById('disc-saved').textContent;
      window.copyToClipboard(`CalcHub Discount Summary: Final Price: ${f} (Saved ${s})`);
    }
    calcDiscount();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "discount-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Discount & Sale Calculator — Instant Price & Tax Savings",
                          "Calculate final sale prices, double coupon stacking discounts, and sales tax. See exact dollar savings and effective discount percentages.",
                          "discount calculator, sale price calculator, percent off calculator, coupon stacking calculator, reverse discount",
                          "discount-calculator", "Finance & Shopping", "finance", disc_app_json,
                          "Quickly calculate your final shopping cart price with sequential coupon stacking, promo codes, and state/local sales tax adjustments.",
                          disc_workspace, disc_geo, disc_toc, disc_article, disc_script))

# ==========================================
# 10. SALARY / PAYCHECK CALCULATOR
# ==========================================
sal_app_json = """{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Salary Paycheck Calculator",
  "url": "https://calchub.org/salary-calculator.html",
  "applicationCategory": "FinanceApplication",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}"""

sal_workspace = """
      <section class="calc-card">
        <div class="calc-card-header">
          <span class="calc-title">💼 Compensation Inputs</span>
        </div>
        <form onsubmit="return false;">
          <div class="calc-form-grid">
            <div class="input-group">
              <label class="input-label" for="sal-amount">Earnings Amount</label>
              <div class="input-wrap has-unit">
                <input type="number" id="sal-amount" value="35" min="1" max="10000000" step="1" oninput="calcSalary()">
                <span class="input-unit-badge">$</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="sal-unit">Pay Frequency</label>
              <div class="input-wrap">
                <select id="sal-unit" onchange="calcSalary()">
                  <option value="hourly" selected>Per Hour</option>
                  <option value="weekly">Per Week</option>
                  <option value="biweekly">Bi-Weekly (Every 2 weeks)</option>
                  <option value="monthly">Per Month</option>
                  <option value="annual">Per Year (Annual Salary)</option>
                </select>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="sal-hours">Hours per Week</label>
              <div class="input-wrap has-unit">
                <input type="number" id="sal-hours" value="40" min="1" max="100" step="1" oninput="calcSalary()">
                <span class="input-unit-badge">hrs</span>
              </div>
            </div>
            <div class="input-group">
              <label class="input-label" for="sal-weeks">Paid Weeks per Year</label>
              <div class="input-wrap has-unit">
                <input type="number" id="sal-weeks" value="52" min="1" max="52" step="1" oninput="calcSalary()">
                <span class="input-unit-badge">wks</span>
              </div>
            </div>
          </div>
          <div class="calc-actions">
            <button type="button" class="btn btn-primary" onclick="copyResults()">📋 Copy Salary Conversion</button>
            <button type="button" class="btn btn-subtle" onclick="window.print()">🖨️ Print Breakdown</button>
          </div>
        </form>
      </section>

      <section class="results-card">
        <div class="results-header">
          <span class="results-title">Annualized Earnings</span>
          <span class="status-pill status-success">Gross Compensation</span>
        </div>
        <div class="primary-result-box">
          <div class="primary-result-label">Gross Annual Salary</div>
          <div>
            <span class="primary-result-value" id="sal-annual">$72,800</span>
          </div>
        </div>
        <div class="result-breakdown-grid">
          <div class="breakdown-item">
            <div class="breakdown-label">Monthly Pay (Gross)</div>
            <div class="breakdown-val" id="sal-monthly">$6,067</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Bi-Weekly Pay (26x/yr)</div>
            <div class="breakdown-val" id="sal-biweekly">$2,800</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Weekly Pay (52x/yr)</div>
            <div class="breakdown-val" id="sal-weekly">$1,400</div>
          </div>
          <div class="breakdown-item">
            <div class="breakdown-label">Hourly Equivalent</div>
            <div class="breakdown-val" id="sal-hourly">$35.00/hr</div>
          </div>
        </div>
      </section>
"""

sal_geo = """
    <section class="geo-citation-box">
      <div class="geo-header">💡 Direct Answer (GEO & Quick Summary)</div>
      <p>To convert an <strong>hourly wage to an annual salary</strong> based on a standard 40-hour full-time work week across 52 weeks (2,080 annual working hours):</p>
      <p><code>Annual Salary = Hourly Wage × 2,080</code></p>
      <p>For example, <strong>$35.00/hour</strong> equals an annual gross salary of <strong>$72,800</strong> ($6,066.67/month or $2,800 bi-weekly). Conversely, divide annual salary by 2,080 to find your hourly equivalent rate.</p>
    </section>
"""

sal_toc = """
    <nav class="toc-container" aria-label="Table of Contents">
      <div class="toc-title">📑 Table of Contents</div>
      <ul class="toc-list">
        <li><a href="#sal-conversion-rules">The 2,080 Work Hours Standard</a></li>
        <li><a href="#biweekly-vs-bimonthly">Bi-Weekly (26 Paychecks) vs Semi-Monthly (24)</a></li>
        <li><a href="#overtime-exempt">Overtime & FLSA Exemption Rules</a></li>
        <li><a href="#sal-faq">Frequently Asked Questions</a></li>
      </ul>
    </nav>
"""

sal_article = """
      <h2 id="sal-conversion-rules">The 2,080 Work Hours Standard</h2>
      <p>In payroll accounting and human resource compliance under the US Department of Labor and international labor conventions, a standard full-time position consists of 40 hours per week across 52 weeks per calendar year, amounting to exactly <strong>2,080 working hours</strong>.</p>

      <div class="formula-box">
        <div class="formula-title">Salary Conversion Rules</div>
        <div class="formula-code">Annual = Hourly × Weekly Hours × Weeks per Year<br>Hourly = Annual ÷ (Weekly Hours × Weeks per Year)</div>
      </div>

      <h2 id="biweekly-vs-bimonthly">Bi-Weekly (26 Paychecks) vs Semi-Monthly (24 Paychecks)</h2>
      <p>A frequent point of employee confusion lies between bi-weekly and semi-monthly pay periods:</p>
      <ul>
        <li><strong>Bi-Weekly:</strong> Paid every two weeks on a set day (usually Friday), resulting in <strong>26 paychecks</strong> per calendar year. In two months of each year, employees receive three paychecks!</li>
        <li><strong>Semi-Monthly:</strong> Paid twice per month (typically on the 15th and the final day of the month), producing exactly <strong>24 paychecks</strong> per year.</li>
      </ul>

      <h2 id="overtime-exempt">Overtime & Fair Labor Standards</h2>
      <p>Non-exempt employees working beyond 40 hours within a designated 7-day workweek are legally entitled to 1.5× their regular hourly rate ("time-and-a-half") under the Fair Labor Standards Act (FLSA).</p>

      <h2 id="sal-faq">Frequently Asked Questions</h2>
      <div class="faq-wrap">
        <details class="faq-item">
          <summary>Does this calculation include taxes and deductions?</summary>
          <div class="faq-content">This tool calculates Gross Pay (pre-tax total earnings). Take-home Net Pay will be lower depending on federal and state income taxes, FICA (Social Security & Medicare), health insurance premiums, and retirement contributions (such as 401k).</div>
        </details>
      </div>
"""

sal_script = """
  <script>
    function calcSalary() {
      const amt = parseFloat(document.getElementById('sal-amount').value) || 0;
      const unit = document.getElementById('sal-unit').value;
      const hpw = parseFloat(document.getElementById('sal-hours').value) || 40;
      const wpy = parseFloat(document.getElementById('sal-weeks').value) || 52;

      let annual = 0;
      if (unit === 'hourly') {
        annual = amt * hpw * wpy;
      } else if (unit === 'weekly') {
        annual = amt * wpy;
      } else if (unit === 'biweekly') {
        annual = amt * (wpy / 2);
      } else if (unit === 'monthly') {
        annual = amt * 12;
      } else if (unit === 'annual') {
        annual = amt;
      }

      const totalHours = hpw * wpy;
      const hourly = totalHours > 0 ? annual / totalHours : 0;
      const monthly = annual / 12;
      const biweekly = annual / 26;
      const weekly = wpy > 0 ? annual / wpy : 0;

      document.getElementById('sal-annual').textContent = '$' + Math.round(annual).toLocaleString();
      document.getElementById('sal-monthly').textContent = '$' + Math.round(monthly).toLocaleString();
      document.getElementById('sal-biweekly').textContent = '$' + Math.round(biweekly).toLocaleString();
      document.getElementById('sal-weekly').textContent = '$' + Math.round(weekly).toLocaleString();
      document.getElementById('sal-hourly').textContent = '$' + hourly.toFixed(2) + '/hr';
    }
    function copyResults() {
      const a = document.getElementById('sal-annual').textContent;
      const m = document.getElementById('sal-monthly').textContent;
      const h = document.getElementById('sal-hourly').textContent;
      window.copyToClipboard(`CalcHub Compensation Conversion: Annual: ${a}, Monthly: ${m}, Hourly: ${h}`);
    }
    calcSalary();
  </script>
"""

with open(os.path.join(OUTPUT_DIR, "salary-calculator.html"), "w", encoding="utf-8") as f:
    f.write(page_scaffold("Salary / Paycheck Calculator — Hourly to Annual Conversion",
                          "Convert hourly wage to annual salary, monthly, bi-weekly, and weekly gross income based on your work hours and weeks worked per year.",
                          "salary calculator, hourly to salary, paycheck calculator, annual income calculator, wage converter, 40 hours week salary",
                          "salary-calculator", "Finance & Employment", "finance", sal_app_json,
                          "Convert seamlessly between hourly rates, bi-weekly paychecks, monthly earnings, and total annual salary. Model flexible working hours and unpaid leave.",
                          sal_workspace, sal_geo, sal_toc, sal_article, sal_script))

print("Created all 5 Finance Calculators!")
