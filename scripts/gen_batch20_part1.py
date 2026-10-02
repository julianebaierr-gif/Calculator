import os

def create_down_payment_calculator():
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Down Payment Calculator | Home Purchase LTV & PMI Sizer</title>
  <meta name="description" content="Calculate home down payment amounts, Loan-to-Value (LTV) ratios, Private Mortgage Insurance (PMI) monthly costs, and upfront home closing expenses.">
  <link rel="canonical" href="https://calchub.cloud/down-payment-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Down Payment Calculator",
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates required cash down payments, loan-to-value ratios, private mortgage insurance premiums, and total upfront cash to close.",
        "offers": {
          "@type": "Offer",
          "price": "0.00",
          "priceCurrency": "USD"
        }
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Why is a 20% down payment the traditional benchmark in home purchasing?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A 20% down payment establishes an 80% Loan-to-Value (LTV) ratio on a conventional mortgage, which legally eliminates the requirement for Private Mortgage Insurance (PMI) under the Homeowners Protection Act of 1998, instantly lowering monthly housing costs."
            }
          },
          {
            "@type": "Question",
            "name": "What is the minimum down payment required for common mortgage programs?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Conventional loans (Fannie Mae HomeReady, Freddie Mac Home Possible) require as little as 3% down. FHA loans require a minimum of 3.5% down for borrowers with credit scores ≥ 580. VA loans (for eligible veterans) and USDA loans (for designated rural properties) require 0% down payment."
            }
          },
          {
            "@type": "Question",
            "name": "How is Private Mortgage Insurance (PMI) calculated?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "PMI typically costs between 0.3% and 1.5% of the original loan balance annually, depending on credit score and down payment percentage. The annual premium is divided by 12 and added directly to the monthly mortgage payment."
            }
          },
          {
            "@type": "Question",
            "name": "What additional closing costs must be paid alongside the down payment?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In addition to the down payment, buyers must pay loan origination fees, appraisal costs, title insurance, attorney fees, transfer taxes, and prepaid escrow reserves (homeowners insurance and property taxes). Closing costs typically range from 2% to 5% of the purchase price."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="logo">CalcHub</a>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="finance.html" class="active">Financial</a>
        <a href="engineering.html">Electrical</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="civil.html">Civil</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <div class="content-wrapper">
      <div class="calculator-container">
        <h1>Down Payment Calculator</h1>
        <p class="lead-text">Calculate exact down payment requirements, Loan-to-Value (LTV) ratios, Private Mortgage Insurance (PMI) premiums, and estimated upfront closing cash needed to purchase a home.</p>

        <div class="calc-card">
          <div class="calc-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="homePrice">Home Purchase Price ($)</label>
                <input type="number" id="homePrice" value="400000" min="10000" step="5000" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="downPaymentMode">Down Payment Input</label>
                <select id="downPaymentMode" class="form-control">
                  <option value="percent" selected>By Percentage (%)</option>
                  <option value="dollars">By Dollar Amount ($)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-half" id="downPercentGroup">
                <label for="downPercent">Down Payment (%)</label>
                <input type="number" id="downPercent" value="20" min="0" max="100" step="0.5" class="form-control">
              </div>
              <div class="form-group col-half" id="downDollarGroup" style="display:none;">
                <label for="downDollars">Down Payment ($)</label>
                <input type="number" id="downDollars" value="80000" min="0" step="1000" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="closingCostPct">Estimated Closing Costs (%)</label>
                <input type="number" id="closingCostPct" value="3.0" min="0" max="10" step="0.25" class="form-control">
              </div>
            </div>

            <div class="btn-group">
              <button type="button" id="calcBtn" class="btn btn-primary">Calculate Down Payment</button>
              <button type="button" id="resetBtn" class="btn btn-secondary">Reset to 20%</button>
            </div>
          </div>

          <div class="results-panel" id="resultsPanel">
            <h2>Upfront Capital & Financing Breakdown</h2>
            <div class="result-hero">
              <span class="hero-label">Total Upfront Cash to Close</span>
              <span class="hero-value" id="resTotalCash">$92,000</span>
            </div>

            <div class="results-grid">
              <div class="result-item">
                <span class="sub-label">Down Payment Amount</span>
                <span class="sub-value highlight" id="resDownAmount">$80,000 (20.0%)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Mortgage Loan Amount</span>
                <span class="sub-value" id="resLoanAmount">$320,000</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Loan-to-Value (LTV) Ratio</span>
                <span class="sub-value" id="resLtv">80.0%</span>
              </div>
              <div class="result-item">
                <span class="sub-label">PMI Monthly Premium</span>
                <span class="sub-value highlight" id="resPmiMonthly">$0 / mo (No PMI)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Estimated Closing Costs</span>
                <span class="sub-value" id="resClosingCost">$12,000</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Mortgage Financing Program</span>
                <span class="sub-value" id="resProgram">Conventional (No PMI)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Comprehensive Real Estate & Mortgage Article (1,250+ Words) -->
        <article class="article-body">
          <h2>1. The Financial Role of the Down Payment in Residential Acquisition</h2>
          <p>In residential real estate financing, a <strong>down payment</strong> is the initial unborrowed equity tranche contributed by the homebuyer toward the total agreed contract purchase price. Representing immediate personal equity, the down payment establishes the foundational security buffer safeguarding mortgage lenders against default and property depreciation.</p>
          <p>The mathematical relationship governing down payments begins with the simple equity balance equation:</p>
          <div class="math-block">
            $$\text{Purchase Price} = \text{Down Payment} + \text{Loan Principal Amount}$$
          </div>
          <p>Expressed in fractional or percentage terms:</p>
          <div class="math-block">
            \text{Down Payment (\%)} = \left( \frac{\text{Down Payment (\USD)}}{\text{Purchase Price}} \right) \times 100\%
          </div>
          <p>The portion financed via promissory mortgage note dictates the <strong>Loan-to-Value (LTV) ratio</strong>:</p>
          <div class="math-block">
            $$\text{LTV} = \left( \frac{\text{Loan Principal Amount}}{\min(\text{Appraised Fair Market Value}, \text{Purchase Price})} \right) \times 100\% = 100\% - \text{Down Payment (\%)}
          </div>

          <h2>2. The Critical 20% Threshold: Private Mortgage Insurance (PMI) Economics</h2>
          <p>The traditional homebuying rule advocating a <strong>20% down payment</strong> is directly rooted in federal banking regulations and secondary market underwriting guidelines established by the Federal National Mortgage Association (Fannie Mae) and the Federal Home Loan Mortgage Corporation (Freddie Mac).</p>
          <p>When an LTV exceeds 80.0% (meaning the borrower contributes less than 20% down payment), conventional conforming lenders mandate <strong>Private Mortgage Insurance (PMI)</strong>. PMI does not protect the homeowner; it is an insurance policy protecting the lender against loss if the borrower defaults and the home is liquidated at a foreclosure discount.</p>

          <h3>PMI Cost Formulations</h3>
          <p>Annual PMI premiums typically scale between 0.30% and 1.50% of the aggregate outstanding loan balance, dictated by the borrower's FICO credit score and precise LTV tier:</p>
          <div class="math-block">
            $$\text{Annual PMI Premium} = \text{Loan Balance} \times \text{PMI Rate}$$
          </div>
          <div class="math-block">
            $$\text{Monthly PMI Payment} = \frac{\text{Annual PMI Premium}}{12}$$
          </div>

          <table class="data-table">
            <thead>
              <tr>
                <th>Down Payment %</th>
                <th>Resulting LTV</th>
                <th>Typical Annual PMI Rate</th>
                <th>Monthly PMI on $400k Home</th>
                <th>Cumulative 5-Year PMI Cost</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>3.0% Down</strong></td>
                <td>97.0% LTV</td>
                <td>0.95% &ndash; 1.40%</td>
                <td>$307 &ndash; $452 / mo</td>
                <td>$18,420 &ndash; $27,120</td>
              </tr>
              <tr>
                <td><strong>5.0% Down</strong></td>
                <td>95.0% LTV</td>
                <td>0.75% &ndash; 1.15%</td>
                <td>$238 &ndash; $364 / mo</td>
                <td>$14,280 &ndash; $21,840</td>
              </tr>
              <tr>
                <td><strong>10.0% Down</strong></td>
                <td>90.0% LTV</td>
                <td>0.50% &ndash; 0.85%</td>
                <td>$150 &ndash; $255 / mo</td>
                <td>$9,000 &ndash; $15,300</td>
              </tr>
              <tr>
                <td><strong>15.0% Down</strong></td>
                <td>85.0% LTV</td>
                <td>0.30% &ndash; 0.55%</td>
                <td>$85 &ndash; $156 / mo</td>
                <td>$5,100 &ndash; $9,360</td>
              </tr>
              <tr>
                <td><strong>20.0%+ Down</strong></td>
                <td>&le; 80.0% LTV</td>
                <td>0.00% (No PMI)</td>
                <td>$0.00 / mo</td>
                <td>$0.00 (Exempt)</td>
              </tr>
            </tbody>
          </table>

          <h2>3. Federal Protections: The Homeowners Protection Act of 1998</h2>
          <p>Under the federal <strong>Homeowners Protection Act (HPA) of 1998</strong> (codified at 12 U.S.C. § 4901), borrowers who put down less than 20% are legally safeguarded against perpetual PMI charges on conventional loans:</p>
          <ul>
            <li><strong>Borrower-Initiated Cancellation at 80% LTV:</strong> Once the principal loan balance amortizes down to exactly 80.0% of the <em>original purchase value</em> (or through validated substantial property appreciation certified by an approved appraisal), the homeowner possesses the statutory right to request PMI termination in writing.</li>
            <li><strong>Automatic Lender Termination at 78% LTV:</strong> Loan servicers are legally required to automatically cancel PMI when the loan balance is scheduled to reach 78.0% of the original property value, provided the mortgage is current and in good standing.</li>
          </ul>

          <div class="worked-example-card">
            <h3>Worked Quantitative Case Study: 5% vs. 20% Down Payment Tradeoff</h3>
            <p><strong>Scenario:</strong> A homebuyer is purchasing a $500,000 home with a 30-year fixed mortgage at 6.50% APR. They possess $120,000 in liquid savings and must decide between putting down 5% ($25,000) or 20% ($100,000). Closing costs are estimated at 3.0% ($15,000).</p>
            <p><strong>Option A: 5% Down Payment ($25,000 down, $475,000 loan, 95% LTV)</strong></p>
            <ul>
              <li>Upfront Cash Required: \(\$25,000\text{ (down)} + \$15,000\text{ (closing)} = \$40,000\).</li>
              <li>Monthly Principal & Interest (P&I): \(\$3,002.32\).</li>
              <li>Monthly PMI Premium (\(0.85\%\)): \((\$475,000 \times 0.0085) / 12 = \$336.46\).</li>
              <li>Total Monthly Payment: \(\$3,338.78\).</li>
              <li>Remaining Liquid Reserves: \(\$120,000 - \$40,000 = \$80,000\).</li>
            </ul>
            <p><strong>Option B: 20% Down Payment ($100,000 down, $400,000 loan, 80% LTV)</strong></p>
            <ul>
              <li>Upfront Cash Required: \(\$100,000\text{ (down)} + \$15,000\text{ (closing)} = \$115,000\).</li>
              <li>Monthly Principal & Interest (P&I): \(\$2,528.27\).</li>
              <li>Monthly PMI Premium: \(\$0.00\).</li>
              <li>Total Monthly Payment: \(\$2,528.27\).</li>
              <li>Remaining Liquid Reserves: \(\$120,000 - \$115,000 = \$5,000\).</li>
            </ul>
            <p><strong>Strategic Financial Analysis:</strong> The 20% down payment slashes monthly housing expenses by <strong>$810.51 per month</strong> ($474.05 lower P&I + $336.46 PMI elimination), saving $48,630 in payments over the first five years alone. However, Option B leaves only $5,000 in emergency cash reserves, heightening liquidity risk. An intermediate 10% or 15% strategy offers an optimal balance.</p>
          </div>

          <h2>4. Government-Backed Low Down Payment Mortgage Programs</h2>
          <p>First-time homebuyers unable to accumulate a full 20% down payment have access to specialized federal lending programs:</p>
          <ul>
            <li><strong>FHA Loans (Federal Housing Administration):</strong> Require only 3.5% down for credit scores \(\ge 580\). However, FHA loans mandate an Upfront Mortgage Insurance Premium (UFMIP, 1.75%) plus an ongoing annual MIP (typically 0.55%) that lasts for the <em>entire 30-year life of the loan</em> if putting down less than 10%.</li>
            <li><strong>VA Loans (Department of Veterans Affairs):</strong> Exclusive to qualifying active-duty military, veterans, and surviving spouses. Requires <strong>0% down payment</strong> and charges zero ongoing monthly mortgage insurance, requiring only a one-time VA funding fee.</li>
            <li><strong>USDA Loans (US Department of Agriculture):</strong> Offers <strong>0% down payment</strong> financing for designated rural and suburban properties for low-to-moderate income households.</li>
          </ul>

          <h2>5. Total Upfront Cash to Close: Factoring in Closing Costs</h2>
          <p>A fatal mistake made by novice homebuyers is assuming the down payment is the only liquid capital needed at the closing table. In reality, buyers must fund <strong>closing costs</strong>, which average 2.0% to 5.0% of the purchase price:</p>
          <div class="math-block">
            $$\text{Total Cash Required} = \text{Down Payment} + \text{Closing Costs} + \text{Prepaid Escrow Reserves}$$
          </div>
          <p>These encompass lender origination points (1.0%), real estate appraisal fees ($500 to $800), title search and lender title insurance ($1,500 to $2,500), recording fees, municipal transfer taxes, and 3 to 6 months of prepaid homeowners insurance and property taxes held in escrow.</p>

          <h2>6. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>Can down payments be funded via gift funds from family?</h3>
            <p>Yes. Conventional and FHA guidelines permit gift funds from immediate relatives for down payments, provided the donor signs a formal "Gift Letter" explicitly certifying that the funds are a non-repayable gift with no expectation of repayment or property lien.</p>
          </div>
          <div class="faq-item">
            <h3>Is it better to put down a smaller down payment and invest the rest in stocks?</h3>
            <p>This is an arbitrage decision. If your mortgage rate is 6.50% guaranteed (plus PMI), putting money into the down payment yields a guaranteed after-tax, risk-free return of roughly 7.5%+. When interest rates are elevated, paying down debt generally outweighs volatile equity market speculation.</p>
          </div>
          <div class="faq-item">
            <h3>Can I use my 401(k) or IRA for a first-time homebuyer down payment?</h3>
            <p>Yes. The IRS permits first-time homebuyers to withdraw up to $10,000 penalty-free from a traditional IRA (though income taxes apply). For 401(k) plans, participants can often borrow up to 50% of their vested balance (up to a maximum of $50,000) through a residential 401(k) loan.</p>
          </div>
        </article>
      </div>

      <aside class="sidebar" id="toolSidebar">
        <!-- Injected via apply_sidebars_all.py -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <p>&copy; 2026 CalcHub. All rights reserved. Precision engineering, science, and technical calculation tools.</p>
    </div>
  </footer>

  <script>
    function calculate() {
      const price = parseFloat(document.getElementById('homePrice').value) || 0;
      const mode = document.getElementById('downPaymentMode').value;
      let pct = 0;
      let dollars = 0;

      if (mode === 'percent') {
        pct = parseFloat(document.getElementById('downPercent').value) || 0;
        dollars = (price * pct) / 100;
        document.getElementById('downDollars').value = Math.round(dollars);
      } else {
        dollars = parseFloat(document.getElementById('downDollars').value) || 0;
        pct = price > 0 ? (dollars / price) * 100 : 0;
        document.getElementById('downPercent').value = pct.toFixed(1);
      }

      const closingPct = parseFloat(document.getElementById('closingCostPct').value) || 0;
      const closingCost = (price * closingPct) / 100;
      const totalCash = dollars + closingCost;
      const loanAmount = Math.max(0, price - dollars);
      const ltv = price > 0 ? (loanAmount / price) * 100 : 0;

      // Estimate PMI if LTV > 80%
      let pmiMonthly = 0;
      let pmiRate = 0;
      let programDesc = 'Conventional (No PMI)';

      if (ltv > 80) {
        if (ltv > 95) pmiRate = 0.0105;
        else if (ltv > 90) pmiRate = 0.0085;
        else if (ltv > 85) pmiRate = 0.0065;
        else pmiRate = 0.0040;

        pmiMonthly = (loanAmount * pmiRate) / 12;
        programDesc = 'Conventional (PMI Required)';
      }

      const fmtCur = (v) => '$' + Math.round(v).toLocaleString('en-US');

      document.getElementById('resTotalCash').textContent = fmtCur(totalCash);
      document.getElementById('resDownAmount').textContent = fmtCur(dollars) + ' (' + pct.toFixed(1) + '%)';
      document.getElementById('resLoanAmount').textContent = fmtCur(loanAmount);
      document.getElementById('resLtv').textContent = ltv.toFixed(1) + '%';
      
      if (pmiMonthly > 0) {
        document.getElementById('resPmiMonthly').textContent = fmtCur(pmiMonthly) + ' / mo';
        document.getElementById('resPmiMonthly').style.color = '#dc2626';
      } else {
        document.getElementById('resPmiMonthly').textContent = '$0 / mo (No PMI)';
        document.getElementById('resPmiMonthly').style.color = '#16a34a';
      }

      document.getElementById('resClosingCost').textContent = fmtCur(closingCost);
      document.getElementById('resProgram').textContent = programDesc;
    }

    document.getElementById('downPaymentMode').addEventListener('change', () => {
      const mode = document.getElementById('downPaymentMode').value;
      if (mode === 'percent') {
        document.getElementById('downPercentGroup').style.display = 'block';
        document.getElementById('downDollarGroup').style.display = 'none';
      } else {
        document.getElementById('downPercentGroup').style.display = 'none';
        document.getElementById('downDollarGroup').style.display = 'block';
      }
      calculate();
    });

    document.querySelectorAll('input').forEach(el => {
      el.addEventListener('input', calculate);
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('homePrice').value = '400000';
      document.getElementById('downPaymentMode').value = 'percent';
      document.getElementById('downPercentGroup').style.display = 'block';
      document.getElementById('downDollarGroup').style.display = 'none';
      document.getElementById('downPercent').value = '20';
      document.getElementById('closingCostPct').value = '3.0';
      calculate();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
'''
    with open('down-payment-calculator.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Created down-payment-calculator.html successfully!")

def create_emergency_fund_calculator():
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Emergency Fund Calculator | 3 to 6 Month Liquid Cash Safety Net</title>
  <meta name="description" content="Calculate your emergency fund goal based on mandatory monthly expenses, job stability, and family dependents. Determine monthly savings milestones.">
  <link rel="canonical" href="https://calchub.cloud/emergency-fund-calculator.html">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        "name": "Emergency Fund Calculator",
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates mandatory liquid cash safety reserves across 3 to 12 months of survival expenses based on personal household risk profiling.",
        "offers": {
          "@type": "Offer",
          "price": "0.00",
          "priceCurrency": "USD"
        }
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Why do financial planners recommend 3 to 6 months of living expenses in an emergency fund?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Three to six months represents the median duration required for an individual to secure replacement employment following unexpected job termination, or to absorb catastrophic uninsured medical, automotive, or home infrastructure repairs without resorting to predatory high-interest credit card debt."
            }
          },
          {
            "@type": "Question",
            "name": "What expenses should be included when calculating an emergency fund?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Only non-negotiable survival expenses must be included: rent or mortgage PITI, utilities, basic groceries, healthcare prescriptions/premiums, transportation/fuel, and minimum debt payments. Discretionary spending (dining out, streaming, travel, entertainment) must be excluded."
            }
          },
          {
            "@type": "Question",
            "name": "Where is the best place to keep an emergency fund?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Emergency funds must be held in ultra-liquid, FDIC/NCUA-insured accounts that carry zero principal risk, such as High-Yield Savings Accounts (HYSAs) or Money Market Deposit Accounts (MMDAs). They should never be invested in stocks, volatile cryptocurrencies, or long-term CDs."
            }
          },
          {
            "@type": "Question",
            "name": "Who needs a larger 9 to 12 month emergency safety net?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Self-employed freelancers, 100% commission-based earners, business owners, single-income families with multiple dependents, and workers in highly specialized or volatile industries should maintain 9 to 12 months of survival expenses."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="logo">CalcHub</a>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="finance.html" class="active">Financial</a>
        <a href="engineering.html">Electrical</a>
        <a href="mechanical.html">Mechanical</a>
        <a href="civil.html">Civil</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <div class="content-wrapper">
      <div class="calculator-container">
        <h1>Emergency Fund Calculator</h1>
        <p class="lead-text">Calculate the exact liquid cash cushion needed to protect your household against income disruption, medical emergencies, and unexpected repairs without taking on high-interest debt.</p>

        <div class="calc-card">
          <div class="calc-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="housingCost">Monthly Housing (Rent / Mortgage PITI $)</label>
                <input type="number" id="housingCost" value="1800" min="0" step="100" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="utilitiesCost">Monthly Utilities & Internet ($)</label>
                <input type="number" id="utilitiesCost" value="300" min="0" step="25" class="form-control">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="foodCost">Monthly Groceries & Essentials ($)</label>
                <input type="number" id="foodCost" value="600" min="0" step="50" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="transportCost">Transportation & Car Payments ($)</label>
                <input type="number" id="transportCost" value="450" min="0" step="25" class="form-control">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="insuranceCost">Healthcare, Insurance & Debt Minimums ($)</label>
                <input type="number" id="insuranceCost" value="350" min="0" step="25" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="targetMonths">Target Coverage Horizon</label>
                <select id="targetMonths" class="form-control">
                  <option value="3">3 Months (Dual Income / High Stability)</option>
                  <option value="6" selected>6 Months (Recommended Standard)</option>
                  <option value="9">9 Months (Single Earner / Dependents)</option>
                  <option value="12">12 Months (Self-Employed / High Volatility)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="currentSavings">Current Emergency Savings ($)</label>
                <input type="number" id="currentSavings" value="5000" min="0" step="500" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="monthlySavingsRate">Monthly Savings Capacity ($)</label>
                <input type="number" id="monthlySavingsRate" value="500" min="50" step="50" class="form-control">
              </div>
            </div>

            <div class="btn-group">
              <button type="button" id="calcBtn" class="btn btn-primary">Calculate Safety Goal</button>
              <button type="button" id="resetBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </div>

          <div class="results-panel" id="resultsPanel">
            <h2>Emergency Fund Target & Timeline</h2>
            <div class="result-hero">
              <span class="hero-label">Target Emergency Fund Goal</span>
              <span class="hero-value" id="resTargetFund">$21,000</span>
            </div>

            <div class="results-grid">
              <div class="result-item">
                <span class="sub-label">Bare-Bones Monthly Expenses</span>
                <span class="sub-value" id="resMonthlyExpense">$3,500 / mo</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Current Fund Funding Level</span>
                <span class="sub-value highlight" id="resFundPct">23.8% Funded</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Current Savings Gap Remaining</span>
                <span class="sub-value" id="resSavingsGap">$16,000</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Months to Full Funding</span>
                <span class="sub-value highlight" id="resMonthsToFund">32 Months (2.7 Yrs)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">3-Month Baseline Target</span>
                <span class="sub-value" id="res3Mo">$10,500</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Estimated HYSA Interest (at 4.5%)</span>
                <span class="sub-value" id="resHysaInterest">+$945 / yr at goal</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Comprehensive Personal Financial Engineering Article (1,300+ Words) -->
        <article class="article-body">
          <h2>1. The Strategic Role of Liquid Capital Reserves in Wealth Preservation</h2>
          <p>In household financial architecture, an <strong>emergency fund</strong> is the foundational defensive perimeter separating long-term wealth accumulation from catastrophic insolvency. Behavioral economists and certified financial planners agree: without an adequate non-volatile cash reserve, unexpected lifecycle disruptions (such as involuntary unemployment, emergency surgical procedures, or critical automotive breakdowns) inevitably force households to liquidate retirement assets prematurely or borrow via predatory high-interest revolving credit.</p>
          <p>The core mathematical formula governing emergency fund sizing is deceptively straightforward:</p>
          <div class="math-block">
            $$\text{Target Emergency Reserve} = \text{Monthly Essential Living Expenses} \times M$$
          </div>
          <p>Where \(M \in [3, 12]\) represents the coverage horizon in months, calibrated to the household's idiosyncratic financial risk profile.</p>

          <h2>2. The "Bare-Bones" Budget: Essential vs. Discretionary Outlays</h2>
          <p>A prevalent mistake in emergency fund modeling is multiplying total average historical monthly expenditures by \(M\). In an acute financial crisis (such as sudden job termination), household consumption instantly contracts to survival mode. Therefore, the monthly multiplier must exclusively reflect <strong>non-negotiable survival expenses</strong>:</p>
          <div class="math-block">
            $$E_{\text{essential}} = \text{PITI Housing} + \text{Utilities/Broadband} + \text{Core Groceries} + \text{Transportation} + \text{Health Insurance/Meds} + \text{Statutory Minimum Debts}$$
          </div>
          <p>Discretionary lifestyle consumption—including restaurant dining, bar spending, streaming subscriptions, vacation funds, luxury retail, and elective home remodeling—is completely zeroed out in an emergency scenario.</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Expense Category</th>
                <th>Essential Budget (Survival Mode)</th>
                <th>Discretionary (Eliminated in Crisis)</th>
                <th>Rationale for Inclusion / Exclusion</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Housing</strong></td>
                <td>Rent or Mortgage PITI + HOA</td>
                <td>Optional maid/gardening services</td>
                <td>Eviction and foreclosure avoidance is paramount.</td>
              </tr>
              <tr>
                <td><strong>Utilities</strong></td>
                <td>Power, water, gas, basic mobile</td>
                <td>Premium 1Gbps fiber, cable TV bundles</td>
                <td>Essential for living and active employment search.</td>
              </tr>
              <tr>
                <td><strong>Nutrition</strong></td>
                <td>Home-prepared staple groceries</td>
                <td>Dining out, takeout, premium alcohol</td>
                <td>Food staples cost 70% less than restaurant dining.</td>
              </tr>
              <tr>
                <td><strong>Transportation</strong></td>
                <td>Car note, gas, transit, basic insurance</td>
                <td>Elective rideshares, premium vehicle detailing</td>
                <td>Required for job interviews and family logistics.</td>
              </tr>
              <tr>
                <td><strong>Debt Service</strong></td>
                <td>Contractual minimum debt payments</td>
                <td>Accelerated principal prepayments</td>
                <td>Preserves credit score and prevents default.</td>
              </tr>
            </tbody>
          </table>

          <h2>3. Determining Your Optimal Coverage Multiplier (\(M\))</h2>
          <p>The standard guideline recommending "3 to 6 months" is an oversimplification. Optimal emergency fund sizing is a function of income volatility, labor market liquidity, and financial dependency ratios:</p>
          <ul>
            <li><strong>3-Month Horizon (\(M = 3\)):</strong> Suited for dual-earner households with secure W-2 employment in uncorrelated industries, no children, strong health, and reliable family support safety nets.</li>
            <li><strong>6-Month Horizon (\(M = 6\)):</strong> The premier standard for typical households. Appropriate for single-earner households, families with 1 to 2 dependent children, and professionals in moderately competitive job sectors.</li>
            <li><strong>9- to 12-Month Horizon (\(M = 9 \text{ to } 12\)):</strong> Vital for self-employed entrepreneurs, 100% commission sales executives, freelancers, workers in niche executive roles with multi-month hiring cycles, or individuals managing chronic medical conditions.</li>
          </ul>

          <div class="worked-example-card">
            <h3>Worked Quantitative Case Study: Building a 6-Month Emergency Cushion</h3>
            <p><strong>Scenario:</strong> A married professional earns $6,000/month after taxes. Their current lifestyle spending is $4,800/month. They assess their essential bare-bones living costs at $3,200/month. They have $4,000 currently in savings and can dedicate $600/month toward building their fund.</p>
            <p><strong>Step 1: Calculate Target 6-Month Emergency Fund</strong></p>
            <div class="math-block">
              $$\text{Goal} = \$3,200 \times 6 = \$19,200$$
            </div>
            <p><strong>Step 2: Determine Current Capital Deficit</strong></p>
            <div class="math-block">
              $$\text{Savings Gap} = \$19,200 - \$4,000 = \$15,200$$
            </div>
            <p><strong>Step 3: Calculate Funding Timeline at $600/month</strong></p>
            <div class="math-block">
              $$\text{Months Required} = \frac{\$15,200}{\$600} = 25.33 \implies 26\text{ Months (2.2 Years)}$$
            </div>
            <p><strong>Step 4: Incorporate High-Yield Interest Accrual (4.5% APY)</strong></p>
            <p>By placing their growing reserves into an FDIC-insured High-Yield Savings Account (HYSA) yielding 4.5% APY, compound interest generates approximately <strong>$850</strong> in cumulative interest over the accumulation phase, reducing the funding timeline by a full 1.5 months.</p>
          </div>

          <h2>4. Storage Instruments: Liquidity vs. Opportunity Cost</h2>
          <p>An emergency fund must fulfill two immutable criteria: <strong>absolute principal safety</strong> and <strong>immediate liquidity (T+0 to T+2 access)</strong>.</p>
          <ul>
            <li><strong>High-Yield Savings Accounts (HYSAs):</strong> The premier repository. Fully liquid, insured by the FDIC up to $250,000 per depositor, and currently yielding competitive interest (4.0% to 5.0% APY) to insulate reserves against inflationary erosion.</li>
            <li><strong>Money Market Deposit Accounts (MMDAs):</strong> Similar to HYSAs, offering check-writing and debit card access directly connected to bank clearing networks.</li>
            <li><strong>Where NOT to Store Emergency Reserves:</strong>
              <ul>
                <li><em>Stock Market / Equity ETFs:</em> During macroeconomic recessions, equity markets frequently plunge 30% to 50% precisely when unemployment spikes, forcing disastrous selloffs at market bottoms.</li>
                <li><em>Physical Cash Under a Mattress:</em> Carries high catastrophic risk from residential fire, theft, or flood, and yields 0%, guaranteeing severe purchasing power loss to inflation.</li>
                <li><em>Cryptocurrencies:</em> Subject to extreme intraday volatility and lack sovereign deposit insurance.</li>
              </ul>
            </li>
          </ul>

          <h2>5. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>Should I pay off high-interest credit card debt before building an emergency fund?</h3>
            <p>Financial planners recommend a phased approach: build a "starter" emergency fund of $1,000 to $2,500 first. This prevents minor unexpected expenses from being charged back onto credit cards. Once the starter cushion is secured, aggressively attack high-interest debt (>15% APR) before scaling the emergency fund to 3-6 months.</p>
          </div>
          <div class="faq-item">
            <h3>When is it acceptable to tap into the emergency fund?</h3>
            <p>Ask three diagnostic questions: (1) Is it unexpected? (2) Is it absolutely necessary? (3) Is it urgent? True emergencies include job loss, emergency medical copays, urgent roof leaks, or transmission failure on a primary commuter vehicle. Vacation sales or holiday gifts fail this test.</p>
          </div>
          <div class="faq-item">
            <h3>How often should I recalculate my emergency fund?</h3>
            <p>Review your emergency fund annually, or immediately following major lifecycle events: buying a home, having a child, a marriage/divorce, receiving a significant pay raise, or changes in monthly debt service.</p>
          </div>
        </article>
      </div>

      <aside class="sidebar" id="toolSidebar">
        <!-- Injected via apply_sidebars_all.py -->
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <p>&copy; 2026 CalcHub. All rights reserved. Precision engineering, science, and technical calculation tools.</p>
    </div>
  </footer>

  <script>
    function calculate() {
      const housing = parseFloat(document.getElementById('housingCost').value) || 0;
      const utilities = parseFloat(document.getElementById('utilitiesCost').value) || 0;
      const food = parseFloat(document.getElementById('foodCost').value) || 0;
      const transport = parseFloat(document.getElementById('transportCost').value) || 0;
      const insurance = parseFloat(document.getElementById('insuranceCost').value) || 0;
      const months = parseInt(document.getElementById('targetMonths').value) || 6;
      const current = parseFloat(document.getElementById('currentSavings').value) || 0;
      const monthlyRate = parseFloat(document.getElementById('monthlySavingsRate').value) || 500;

      const monthlyEssential = housing + utilities + food + transport + insurance;
      const targetFund = monthlyEssential * months;
      const gap = Math.max(0, targetFund - current);
      const fundingPct = targetFund > 0 ? (current / targetFund) * 100 : 0;

      let monthsToFund = monthlyRate > 0 ? Math.ceil(gap / monthlyRate) : 0;
      const yearsToFund = (monthsToFund / 12).toFixed(1);

      const baseline3Mo = monthlyEssential * 3;
      const hysaInterestAtGoal = targetFund * 0.045;

      const fmtCur = (v) => '$' + Math.round(v).toLocaleString('en-US');

      document.getElementById('resTargetFund').textContent = fmtCur(targetFund);
      document.getElementById('resMonthlyExpense').textContent = fmtCur(monthlyEssential) + ' / mo';
      document.getElementById('resFundPct').textContent = fundingPct.toFixed(1) + '% Funded';
      document.getElementById('resSavingsGap').textContent = fmtCur(gap);

      if (gap <= 0) {
        document.getElementById('resMonthsToFund').textContent = 'Fully Funded! (Goal Met)';
        document.getElementById('resMonthsToFund').style.color = '#16a34a';
      } else {
        document.getElementById('resMonthsToFund').textContent = monthsToFund + ' Months (' + yearsToFund + ' Yrs)';
        document.getElementById('resMonthsToFund').style.color = 'var(--primary, #2563eb)';
      }

      document.getElementById('res3Mo').textContent = fmtCur(baseline3Mo);
      document.getElementById('resHysaInterest').textContent = '+' + fmtCur(hysaInterestAtGoal) + ' / yr at goal';
    }

    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculate);
      el.addEventListener('change', calculate);
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('housingCost').value = '1800';
      document.getElementById('utilitiesCost').value = '300';
      document.getElementById('foodCost').value = '600';
      document.getElementById('transportCost').value = '450';
      document.getElementById('insuranceCost').value = '350';
      document.getElementById('targetMonths').value = '6';
      document.getElementById('currentSavings').value = '5000';
      document.getElementById('monthlySavingsRate').value = '500';
      calculate();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
'''
    with open('emergency-fund-calculator.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Created emergency-fund-calculator.html successfully!")

if __name__ == '__main__':
    create_down_payment_calculator()
    create_emergency_fund_calculator()
