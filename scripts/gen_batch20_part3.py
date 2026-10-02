import os

def create_net_worth_calculator():
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Net Worth Calculator | Assets Minus Liabilities Personal Balance Sheet</title>
  <meta name="description" content="Calculate your personal net worth, liquid net worth, asset allocation, and debt-to-asset ratios with a comprehensive personal balance sheet.">
  <link rel="canonical" href="https://calchub.cloud/net-worth-calculator.html">
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
        "name": "Net Worth Calculator",
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates total net worth, liquid net worth, solvency ratios, and debt-to-asset ratios across comprehensive asset and liability categories.",
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
            "name": "What is the accounting definition of net worth?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Net worth is the fundamental accounting measure of an individual's or household's total financial value: Net Worth = Total Assets - Total Liabilities. It represents the residual equity that would remain if all physical and financial assets were liquidated to satisfy all debts."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between total net worth and liquid net worth?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Total net worth includes all assets, such as real estate equity, automobiles, and jewelry. Liquid net worth excludes illiquid physical assets and penalties on retirement accounts, measuring only cash, high-yield savings, and readily tradable non-retirement brokerage accounts minus short-term debts."
            }
          },
          {
            "@type": "Question",
            "name": "What is the Stanley-Danko formula for an Expected Net Worth benchmark?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In 'The Millionaire Next Door', authors Thomas Stanley and William Danko established the benchmark: Expected Net Worth = (Age × Realized Pre-Tax Annual Household Income) / 10. Accumulating more than double this figure classifies an individual as a Prodigious Accumulator of Wealth (PAW)."
            }
          },
          {
            "@type": "Question",
            "name": "Should primary residence equity be included in net worth?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes, primary residence equity (fair market value minus mortgage balance) is formally included in GAAP personal balance sheets. However, for retirement withdrawal planning, home equity is often segregated because you cannot easily spend home equity without selling, downsizing, or taking on a reverse mortgage."
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
        <h1>Net Worth Calculator</h1>
        <p class="lead-text">Construct your personal balance sheet. Aggregate liquid cash, retirement portfolios, real estate, and liabilities to measure total net worth, liquid net worth, and household solvency.</p>

        <div class="calc-card">
          <div class="calc-form">
            <h3 style="margin-top:0;color:var(--primary,#2563eb);border-bottom:2px solid var(--border-light,#e2e8f0);padding-bottom:0.5rem;">1. Financial & Physical Assets ($)</h3>
            <div class="form-row">
              <div class="form-group col-half">
                <label for="cashSavings">Cash & High-Yield Savings</label>
                <input type="number" id="cashSavings" value="25000" min="0" step="1000" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="investmentsTaxable">Taxable Brokerage Accounts</label>
                <input type="number" id="investmentsTaxable" value="45000" min="0" step="2500" class="form-control">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="retirementAccounts">Retirement Accounts (401k, IRA)</label>
                <input type="number" id="retirementAccounts" value="120000" min="0" step="5000" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="realEstateValue">Primary Real Estate Market Value</label>
                <input type="number" id="realEstateValue" value="450000" min="0" step="10000" class="form-control">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="vehiclesValue">Automobiles & Vehicles Value</label>
                <input type="number" id="vehiclesValue" value="30000" min="0" step="1000" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="otherAssets">Other Personal Assets (Crypto, Jewelry)</label>
                <input type="number" id="otherAssets" value="10000" min="0" step="1000" class="form-control">
              </div>
            </div>

            <h3 style="margin-top:1.5rem;color:var(--danger-color,#dc2626);border-bottom:2px solid var(--border-light,#e2e8f0);padding-bottom:0.5rem;">2. Total Liabilities & Debts ($)</h3>
            <div class="form-row">
              <div class="form-group col-half">
                <label for="mortgageDebt">Mortgage Principal Remaining</label>
                <input type="number" id="mortgageDebt" value="310000" min="0" step="5000" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="autoDebt">Auto Loan Balances</label>
                <input type="number" id="autoDebt" value="18000" min="0" step="1000" class="form-control">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-half">
                <label for="studentDebt">Student Loan Balances</label>
                <input type="number" id="studentDebt" value="22000" min="0" step="1000" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="creditCardDebt">Credit Card & Other Unsecured Debt</label>
                <input type="number" id="creditCardDebt" value="5000" min="0" step="500" class="form-control">
              </div>
            </div>

            <div class="btn-group">
              <button type="button" id="calcBtn" class="btn btn-primary">Calculate Personal Net Worth</button>
              <button type="button" id="resetBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </div>

          <div class="results-panel" id="resultsPanel">
            <h2>Personal Balance Sheet Summary</h2>
            <div class="result-hero">
              <span class="hero-label">Total Personal Net Worth</span>
              <span class="hero-value" id="resNetWorth">$325,000</span>
            </div>

            <div class="results-grid">
              <div class="result-item">
                <span class="sub-label">Total Gross Assets</span>
                <span class="sub-value" id="resTotalAssets">$680,000</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Total Liabilities</span>
                <span class="sub-value" id="resTotalLiabilities">$355,000</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Liquid Net Worth (Cash + Stock - Short Debt)</span>
                <span class="sub-value highlight" id="resLiquidNetWorth">$47,000</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Debt-to-Asset Ratio</span>
                <span class="sub-value" id="resDebtToAsset">52.2%</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Home Equity Built</span>
                <span class="sub-value" id="resHomeEquity">$140,000 (31.1%)</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Solvency Status</span>
                <span class="sub-value" style="color:#16a34a;">Solvent (Positive Equity)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Comprehensive Wealth Accounting Article (1,300+ Words) -->
        <article class="article-body">
          <h2>1. The Conceptual Foundations of Personal Balance Sheets</h2>
          <p>In corporate financial accounting and high-net-worth estate planning, <strong>Net Worth</strong> is the ultimate quantitative barometer of economic health. While gross income measures the volume of money flowing <em>through</em> a household's hands, net worth measures the volume of capital that has been successfully captured, accumulated, and retained.</p>
          <p>The foundational accounting equation governing personal balance sheets is derived directly from GAAP (Generally Accepted Accounting Principles):</p>
          <div class="math-block">
            $$\text{Net Worth} = \sum \text{Assets} - \sum \text{Liabilities}$$
          </div>
          <p>Where:</p>
          <ul>
            <li><strong>Assets:</strong> Economic resources owned by the individual that possess positive exchangeable monetary value. These encompass cash reserves, equities, fixed-income bonds, retirement accounts, real estate, motorized vehicles, and business equity.</li>
            <li><strong>Liabilities:</strong> Legal financial obligations owed to external counterparties, encompassing residential mortgages, auto financing loans, student loans, credit card revolving debt, and personal promissory notes.</li>
          </ul>

          <h2>2. Granular Asset Categorization: Liquid vs. Illiquid Wealth</h2>
          <p>Not all assets provide equivalent economic utility. Sophisticated financial planners segregate a personal balance sheet into distinct asset tiers based on liquidity horizons:</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Asset Classification</th>
                <th>Typical Holdings</th>
                <th>Liquidity Speed</th>
                <th>Risk / Volatility Profile</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Liquid Cash Equivalents</strong></td>
                <td>Checking, HYSAs, Money Market, T-Bills</td>
                <td>T+0 to T+2 Days</td>
                <td>Ultra-low risk, zero nominal volatility</td>
              </tr>
              <tr>
                <td><strong>Taxable Liquid Investments</strong></td>
                <td>Public equities, Index ETFs, Mutual Funds</td>
                <td>T+1 Day (Market settlement)</td>
                <td>Moderate-to-high capital market volatility</td>
              </tr>
              <tr>
                <td><strong>Tax-Advantaged Retirement</strong></td>
                <td>Traditional 401(k), Roth IRA, 403(b), HSA</td>
                <td>Illiquid prior to age 59½ (10% penalty)</td>
                <td>Long-term capital growth compounding</td>
              </tr>
              <tr>
                <td><strong>Real Estate & Property</strong></td>
                <td>Primary residence, multi-family rentals, land</td>
                <td>30 to 90 Days (Requires sales contract)</td>
                <td>High transaction friction (6% broker commissions)</td>
              </tr>
              <tr>
                <td><strong>Depreciating Personal Property</strong></td>
                <td>Automobiles, boats, jewelry, electronics</td>
                <td>Variable (Subject to steep haircut)</td>
                <td>Depreciates rapidly; unreliable store of value</td>
              </tr>
            </tbody>
          </table>

          <h3>Liquid Net Worth vs. Headline Net Worth</h3>
          <p>While headline net worth includes all property, <strong>Liquid Net Worth</strong> is the premier metric used by accredited investor syndicates and private wealth banks. It measures capital readily deployable without liquidating shelter or incurring early retirement withdrawal penalties:</p>
          <div class="math-block">
            $$\text{Liquid Net Worth} = (\text{Cash} + \text{Taxable Brokerage}) - (\text{Credit Cards} + \text{Auto Loans} + \text{Short-Term Liabilities})$$
          </div>

          <h2>3. Balance Sheet Leverage: Debt-to-Asset and Solvency Metrics</h2>
          <p>The health of a balance sheet is determined not merely by absolute equity, but by financial leverage ratios:</p>
          <h3>A. Debt-to-Asset Ratio</h3>
          <div class="math-block">
            $$\text{Debt-to-Asset Ratio} = \left( \frac{\text{Total Liabilities}}{\text{Total Assets}} \right) \times 100\%$$
          </div>
          <p>A ratio below 50% indicates conservative financial health, meaning the household owns more unencumbered equity than outstanding debt. A ratio exceeding 80% signifies severe leverage, making the household highly vulnerable to interest rate spikes or real estate price corrections.</p>

          <h3>B. Solvency Ratio</h3>
          <div class="math-block">
            $$\text{Solvency Ratio} = \frac{\text{Net Worth}}{\text{Total Assets}} = 1 - \text{Debt-to-Asset Ratio}$$
          </div>
          <p>This reveals the percentage decline in aggregate asset values the household can absorb before crossing into technical insolvency (negative net worth).</p>

          <div class="worked-example-card">
            <h3>Worked Wealth Management Case Study: Rebalancing a Leveraged Household</h3>
            <p><strong>Scenario:</strong> A 35-year-old couple owns a $500,000 home with a $420,000 mortgage. They have $15,000 in cash, $35,000 in a 401(k), two financed vehicles worth $40,000 with $32,000 in auto loans, and $18,000 in credit card debt.</p>
            <p><strong>Step 1: Aggregate Total Assets</strong></p>
            <div class="math-block">
              $$\text{Assets} = \$15,000\text{ (cash)} + \$35,000\text{ (401k)} + \$500,000\text{ (home)} + \$40,000\text{ (cars)} = \$590,000$$
            </div>
            <p><strong>Step 2: Aggregate Total Liabilities</strong></p>
            <div class="math-block">
              $$\text{Liabilities} = \$420,000\text{ (mortgage)} + \$32,000\text{ (cars)} + \$18,000\text{ (cards)} = \$470,000$$
            </div>
            <p><strong>Step 3: Compute Headline and Liquid Net Worth</strong></p>
            <div class="math-block">
              $$\text{Headline Net Worth} = \$590,000 - \$470,000 = \$120,000$$
            </div>
            <div class="math-block">
              $$\text{Liquid Net Worth} = \$15,000\text{ (cash)} - [\$32,000\text{ (auto)} + \$18,000\text{ (cards)}] = -\$35,000\text{ (Deficit!)}$$
            </div>
            <p><strong>Financial Diagnostic:</strong> While the couple presents an apparently positive headline net worth of $120,000, 66.7% ($80,000) is trapped in illiquid home equity and $8,000 in depreciating car equity. Their liquid net worth is negative (-$35,000). A temporary job interruption would create an immediate cash flow crisis, demonstrating why tracking liquid net worth is critical.</p>
          </div>

          <h2>4. Benchmarking Wealth: The Stanley-Danko Formula</h2>
          <p>In the seminal wealth research text <em>The Millionaire Next Door</em>, Dr. Thomas Stanley and Dr. William Danko derived an empirical benchmark defining <strong>Expected Net Worth (ENW)</strong> for working-age adults:</p>
          <div class="math-block">
            $$\text{Expected Net Worth} = \frac{\text{Age} \times \text{Realized Annual Pre-Tax Income}}{10}$$
          </div>
          <p>Based on this benchmark, wealth accumulators are segmented into three distinct classes:</p>
          <ul>
            <li><strong>Under Accumulator of Wealth (UAW):</strong> Actual net worth is less than half the expected benchmark (\(\text{NW} < 0.5 \times \text{ENW}\)). Characterized by high lifestyle consumption and heavy debt relative to income.</li>
            <li><strong>Average Accumulator of Wealth (AAW):</strong> Actual net worth matches the expected benchmark (\(\text{NW} \approx \text{ENW}\)).</li>
            <li><strong>Prodigious Accumulator of Wealth (PAW):</strong> Actual net worth is at least double the expected benchmark (\(\text{NW} \ge 2.0 \times \text{ENW}\)). Characterized by disciplined savings rates (\(>25\%\)), low consumer debt, and systematic asset compounding.</li>
          </ul>

          <h2>5. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>How often should an individual update their net worth statement?</h3>
            <p>Financial planners recommend a quarterly or semi-annual review schedule. Tracking net worth too frequently (e.g., daily) induces emotional stress from short-term stock market volatility. An annual review at tax time is the minimum standard.</p>
          </div>
          <div class="faq-item">
            <h3>Should anticipated future inheritances be counted in net worth?</h3>
            <p>No. Under standard accounting principles, prospective inheritances are contingent future events subject to healthcare spend-downs, estate taxes, or testamentary modifications, and cannot be recorded on a personal balance sheet until legal probate distribution occurs.</p>
          </div>
          <div class="faq-item">
            <h3>How do taxes affect net worth in retirement accounts?</h3>
            <p>Traditional 401(k) and IRA balances are recorded as gross pre-tax figures on standard balance sheets. However, every dollar withdrawn in retirement will incur ordinary income tax (typically 12% to 24%). When modeling retirement readiness, conservative analysts discount pre-tax accounts by 15% to 20% to reflect deferred tax liabilities.</p>
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
      const cash = parseFloat(document.getElementById('cashSavings').value) || 0;
      const brokerage = parseFloat(document.getElementById('investmentsTaxable').value) || 0;
      const retirement = parseFloat(document.getElementById('retirementAccounts').value) || 0;
      const realEstate = parseFloat(document.getElementById('realEstateValue').value) || 0;
      const vehicles = parseFloat(document.getElementById('vehiclesValue').value) || 0;
      const otherAssets = parseFloat(document.getElementById('otherAssets').value) || 0;

      const mortgage = parseFloat(document.getElementById('mortgageDebt').value) || 0;
      const autoDebt = parseFloat(document.getElementById('autoDebt').value) || 0;
      const studentDebt = parseFloat(document.getElementById('studentDebt').value) || 0;
      const ccDebt = parseFloat(document.getElementById('creditCardDebt').value) || 0;

      const totalAssets = cash + brokerage + retirement + realEstate + vehicles + otherAssets;
      const totalLiabilities = mortgage + autoDebt + studentDebt + ccDebt;
      const netWorth = totalAssets - totalLiabilities;

      // Liquid net worth = (cash + brokerage) - (autoDebt + ccDebt + studentDebt)
      const liquidNetWorth = (cash + brokerage) - (autoDebt + ccDebt);
      const debtToAsset = totalAssets > 0 ? (totalLiabilities / totalAssets) * 100 : 0;
      const homeEquity = Math.max(0, realEstate - mortgage);
      const homeEquityPct = realEstate > 0 ? (homeEquity / realEstate) * 100 : 0;

      const fmtCur = (v) => '$' + Math.round(v).toLocaleString('en-US');

      document.getElementById('resNetWorth').textContent = fmtCur(netWorth);
      if (netWorth < 0) {
        document.getElementById('resNetWorth').style.color = '#dc2626';
      } else {
        document.getElementById('resNetWorth').style.color = 'var(--primary, #2563eb)';
      }

      document.getElementById('resTotalAssets').textContent = fmtCur(totalAssets);
      document.getElementById('resTotalLiabilities').textContent = fmtCur(totalLiabilities);
      document.getElementById('resLiquidNetWorth').textContent = fmtCur(liquidNetWorth);
      document.getElementById('resDebtToAsset').textContent = debtToAsset.toFixed(1) + '%';
      document.getElementById('resHomeEquity').textContent = fmtCur(homeEquity) + ' (' + homeEquityPct.toFixed(1) + '%)';
    }

    document.querySelectorAll('input').forEach(el => {
      el.addEventListener('input', calculate);
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('cashSavings').value = '25000';
      document.getElementById('investmentsTaxable').value = '45000';
      document.getElementById('retirementAccounts').value = '120000';
      document.getElementById('realEstateValue').value = '450000';
      document.getElementById('vehiclesValue').value = '30000';
      document.getElementById('otherAssets').value = '10000';
      document.getElementById('mortgageDebt').value = '310000';
      document.getElementById('autoDebt').value = '18000';
      document.getElementById('studentDebt').value = '22000';
      document.getElementById('creditCardDebt').value = '5000';
      calculate();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
'''
    with open('net-worth-calculator.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Created net-worth-calculator.html successfully!")

def create_sales_tax_calculator():
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sales Tax Calculator | State, Local & Reverse Pre-Tax Sizer</title>
  <meta name="description" content="Calculate sales tax amounts, gross checkout totals, combined state and municipal tax rates, and reverse tax-inclusive net price conversions.">
  <link rel="canonical" href="https://calchub.cloud/sales-tax-calculator.html">
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
        "name": "Sales Tax Calculator",
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates forward sales tax additions and reverse tax-inclusive deductions across combined state, county, and municipal sales tax brackets.",
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
            "name": "How is sales tax calculated from a pre-tax retail price?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Sales tax is calculated by multiplying the net pre-tax purchase price by the combined sales tax rate expressed as a decimal: Tax Amount = Pre-Tax Price × (Tax Rate / 100). The total cost equals Pre-Tax Price + Tax Amount."
            }
          },
          {
            "@type": "Question",
            "name": "How do you calculate the pre-tax price from a tax-inclusive total (reverse sales tax)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "To find the pre-tax price from a final receipt total, divide the gross total by 1 plus the tax rate in decimal form: Pre-Tax Price = Gross Total / (1 + Tax Rate / 100). Subtracting the pre-tax price from the gross total yields the embedded tax amount."
            }
          },
          {
            "@type": "Question",
            "name": "What is the difference between a single-stage sales tax and a Value-Added Tax (VAT)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A retail sales tax (common in the US) is assessed exclusively at the final point of retail sale to the end consumer. A Value-Added Tax (VAT / GST, prevalent in Europe and globally) is levied fractionally at every stage of the supply chain based on the value added by each producer."
            }
          },
          {
            "@type": "Question",
            "name": "Which US states do not levy a statewide general sales tax?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Five US states—often referred to as the NOMAD states—levy zero statewide general sales tax: New Hampshire, Oregon, Montana, Alaska (though local municipalities may levy local taxes), and Delaware."
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
        <h1>Sales Tax Calculator</h1>
        <p class="lead-text">Calculate total checkout costs, embedded sales tax amounts, combined state and municipal rates, or execute reverse calculations to extract pre-tax prices from final receipts.</p>

        <div class="calc-card">
          <div class="calc-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="priceInput">Transaction Price ($)</label>
                <input type="number" id="priceInput" value="250.00" min="0.01" step="5" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="calcMode">Calculation Mode</label>
                <select id="calcMode" class="form-control">
                  <option value="forward" selected>Add Sales Tax (Pre-Tax &rarr; Gross Total)</option>
                  <option value="reverse">Extract Sales Tax (Gross Total &rarr; Pre-Tax)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-third">
                <label for="stateRate">State Tax Rate (%)</label>
                <input type="number" id="stateRate" value="6.0" min="0" max="25" step="0.25" class="form-control">
              </div>
              <div class="form-group col-third">
                <label for="localRate">County / City Local Tax (%)</label>
                <input type="number" id="localRate" value="2.25" min="0" max="15" step="0.25" class="form-control">
              </div>
              <div class="form-group col-third">
                <label for="statePreset">Popular State Presets</label>
                <select id="statePreset" class="form-control">
                  <option value="custom" selected>Custom Tax Rate</option>
                  <option value="ca">California (7.25% state + local)</option>
                  <option value="tx">Texas (6.25% state + 2.0% local)</option>
                  <option value="ny">New York (4.0% state + 4.875% NYC)</option>
                  <option value="fl">Florida (6.0% state + 1.5% local)</option>
                  <option value="or">Oregon (0.0% Tax Free)</option>
                </select>
              </div>
            </div>

            <div class="btn-group">
              <button type="button" id="calcBtn" class="btn btn-primary">Calculate Sales Tax</button>
              <button type="button" id="resetBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </div>

          <div class="results-panel" id="resultsPanel">
            <h2>Transaction Tax Breakdown</h2>
            <div class="result-hero">
              <span class="hero-label" id="resHeroLabel">Final Gross Checkout Total</span>
              <span class="hero-value" id="resHeroValue">$270.63</span>
            </div>

            <div class="results-grid">
              <div class="result-item">
                <span class="sub-label">Net Pre-Tax Base Price</span>
                <span class="sub-value" id="resNetPrice">$250.00</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Total Sales Tax Billed</span>
                <span class="sub-value highlight" id="resTotalTax">$20.63</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Combined Effective Tax Rate</span>
                <span class="sub-value" id="resCombinedRate">8.250%</span>
              </div>
              <div class="result-item">
                <span class="sub-label">State Tax Portion (6.00%)</span>
                <span class="sub-value" id="resStatePortion">$15.00</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Local Municipal Portion (2.25%)</span>
                <span class="sub-value" id="resLocalPortion">$5.63</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Tax Overhead Percentage</span>
                <span class="sub-value" id="resOverheadPct">+8.25% on goods</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Comprehensive Fiscal Law & Taxation Article (1,300+ Words) -->
        <article class="article-body">
          <h2>1. The Fiscal Mechanics of Retail Sales and Use Taxes</h2>
          <p>A <strong>retail sales tax</strong> is an ad valorem consumption levy assessed by state, county, and municipal governmental authorities on the final retail transaction of taxable physical goods and specified consumer services. Unlike direct taxes (such as corporate or individual income taxes), sales taxes are categorized as <strong>indirect taxes</strong>: the retail vendor legally collects the tax from the end purchaser at the point of sale and remits the funds to the state department of revenue.</p>
          <p>The mathematical formulation for forward sales tax computation is expressed as:</p>
          <div class="math-block">
            $$T = P_{\text{net}} \times \left( \frac{\tau_{\text{combined}}}{100} \right)$$
          </div>
          <p>Where:</p>
          <ul>
            <li>\(P_{\text{net}}\) represents the <strong>Net Pre-Tax Base Price</strong>.</li>
            <li>\(\tau_{\text{combined}}\) represents the total aggregate sales tax rate in percent, defined as the sum of all overlapping jurisdictional levies: \(\tau_{\text{combined}} = \tau_{\text{state}} + \tau_{\text{county}} + \tau_{\text{city}} + \tau_{\text{special district}}\).</li>
            <li>\(T\) represents the total sales tax collected in currency.</li>
          </ul>
          <p>The gross out-of-pocket invoice total paid by the customer is:</p>
          <div class="math-block">
            $$P_{\text{gross}} = P_{\text{net}} + T = P_{\text{net}} \cdot \left( 1 + \frac{\tau_{\text{combined}}}{100} \right)$$
          </div>

          <h2>2. The Inverse Algebra: Reverse Sales Tax Extraction</h2>
          <p>Corporate bookkeepers, accountants, and expense auditors frequently encounter receipts displaying only a gross final total \(P_{\text{gross}}\) and must reverse-engineer the underlying pre-tax base cost and exact tax collected. A common amateur error is simply multiplying \(P_{\text{gross}}\) by \(\tau_{\text{combined}}\), which yields an inflated, legally inaccurate figure because sales tax is assessed on the <em>pre-tax base</em>, not the gross sum.</p>
          <p>The correct mathematical inversion isolates \(P_{\text{net}}\):</p>
          <div class="math-block">
            $$P_{\text{net}} = \frac{P_{\text{gross}}}{1 + \frac{\tau_{\text{combined}}}{100}}$$
          </div>
          <p>Once \(P_{\text{net}}\) is established, the embedded sales tax \(T\) is recovered via subtraction:</p>
          <div class="math-block">
            $$T = P_{\text{gross}} - P_{\text{net}} = P_{\text{gross}} \cdot \left[ \frac{\frac{\tau_{\text{combined}}}{100}}{1 + \frac{\tau_{\text{combined}}}{100}} \right]$$
          </div>

          <table class="data-table">
            <thead>
              <tr>
                <th>Gross Total Paid</th>
                <th>Combined Tax Rate (\(\tau\))</th>
                <th>Correct Pre-Tax Net Price</th>
                <th>Actual Tax Paid</th>
                <th>Flawed Simple % Error</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>$100.00</td>
                <td>5.0%</td>
                <td>$95.24</td>
                <td>$4.76</td>
                <td>+$0.24 overestimate</td>
              </tr>
              <tr>
                <td>$100.00</td>
                <td>8.25%</td>
                <td>$92.38</td>
                <td>$7.62</td>
                <td>+$0.63 overestimate</td>
              </tr>
              <tr>
                <td>$100.00</td>
                <td>10.0%</td>
                <td>$90.91</td>
                <td>$9.09</td>
                <td>+$0.91 overestimate</td>
              </tr>
              <tr>
                <td>$500.00</td>
                <td>8.875% (NYC)</td>
                <td>$459.24</td>
                <td>$40.76</td>
                <td>+$3.62 overestimate</td>
              </tr>
              <tr>
                <td>$1,000.00</td>
                <td>9.5% (TN/LA)</td>
                <td>$913.24</td>
                <td>$86.76</td>
                <td>+$8.24 overestimate</td>
              </tr>
            </tbody>
          </table>

          <h2>3. Multi-Tiered Jurisdictional Layering in the United States</h2>
          <p>Unlike European and Asian countries where a unified national Value-Added Tax (VAT) prevails, the United States possesses no federal sales tax. Instead, sales tax policy is decentralized across over <strong>13,000 distinct taxing jurisdictions</strong> nationwide:</p>
          <ul>
            <li><strong>State Baseline Tax:</strong> Forty-five states plus Washington D.C. impose a statewide baseline tax rate ranging from 2.9% (Colorado) to 7.25% (California).</li>
            <li><strong>County & Municipal Piggyback Taxes:</strong> Local county commissioners and municipal city councils routinely levy local option sales taxes (typically 0.5% to 3.5%) atop the state rate to fund municipal infrastructure, public schools, and police services.</li>
            <li><strong>Special District Assessments:</strong> Specialized public entities (such as Regional Transportation Districts, stadium authorities, or emergency medical response zones) levy targeted surcharges of 0.1% to 1.0% within micro-geographic boundaries.</li>
          </ul>

          <div class="worked-example-card">
            <h3>Worked Accounting Case Study: Commercial Asset Acquisition</h3>
            <p><strong>Scenario:</strong> A design engineering consultancy purchases $18,500 of computer CAD workstations in an urban municipality featuring a 6.25% state sales tax, a 1.25% county transit tax, and a 0.75% municipal police district levy.</p>
            <p><strong>Step 1: Compute Aggregate Combined Tax Rate</strong></p>
            <div class="math-block">
              $$\tau_{\text{combined}} = 6.25\% + 1.25\% + 0.75\% = 8.25\%$$
            </div>
            <p><strong>Step 2: Calculate Tax Liability per Jurisdictional Tranche</strong></p>
            <ul>
              <li>State Tax: \(\$18,500 \times 0.0625 = \$1,156.25\)</li>
              <li>County Transit Tax: \(\$18,500 \times 0.0125 = \$231.25\)</li>
              <li>City District Tax: \(\$18,500 \times 0.0075 = \$138.75\)</li>
              <li><strong>Total Sales Tax Billed (\(T\)):</strong> \(\$1,156.25 + \$231.25 + \$138.75 = \$1,526.25\)</li>
            </ul>
            <p><strong>Step 3: Determine Gross Final Invoice Total</strong></p>
            <div class="math-block">
              $$P_{\text{gross}} = \$18,500.00 + \$1,526.25 = \$20,026.25$$
            </div>
            <p><strong>Accounting Conclusion:</strong> The firm capitalizes the asset at its net basis ($18,500) while recording $1,526.25 under input tax expenses for corporate tax deductions.</p>
          </div>

          <h2>4. Sales Tax vs. Value-Added Tax (VAT) vs. Use Tax</h2>
          <p>Global taxation frameworks utilize distinct structures that must not be conflated:</p>
          <ul>
            <li><strong>Retail Sales Tax (RST):</strong> A single-stage turnover tax collected exclusively on final end-consumer transactions. Wholesalers, manufacturers, and business-to-business (B2B) supply chains escape sales tax through <strong>Resale Exemption Certificates</strong> to avoid cascading tax pyramiding.</li>
            <li><strong>Value-Added Tax (VAT / GST):</strong> A multi-stage tax prevalent in over 160 nations. Every intermediary business in the supply chain collects tax on its gross output, claims an "input tax credit" for tax paid on raw inputs, and remits the net differential to the state.</li>
            <li><strong>Consumer Use Tax:</strong> A complementary excise tax levied on out-of-state purchases. Following the landmark 2018 Supreme Court ruling in <em>South Dakota v. Wayfair, Inc.</em>, out-of-state online retailers with economic nexus ($100k+ in sales or 200+ transactions) must collect destination sales tax at the buyer's home address.</li>
          </ul>

          <h2>5. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>What goods and services are typically exempt from retail sales tax?</h3>
            <p>In most US states, necessities of life are fully or partially exempt: prescription pharmaceuticals, unprocessed grocery foods, residential utilities, and medical devices. Additionally, non-profit institutions and government agencies possess tax-exempt status.</p>
          </div>
          <div class="faq-item">
            <h3>What are the NOMAD states?</h3>
            <p>The acronym <strong>NOMAD</strong> represents the five US states that impose no statewide general sales tax: <strong>N</strong>ew Hampshire, <strong>O</strong>regon, <strong>M</strong>ontana, <strong>A</strong>laska, and <strong>D</strong>elaware. However, Alaskan local municipalities retain statutory authority to levy local municipal sales taxes.</p>
          </div>
          <div class="faq-item">
            <h3>How do sales tax holidays work?</h3>
            <p>Many US states enact statutory sales tax holidays (typically 2 to 3 days in August before the school year) temporarily waiving sales taxes on designated categories such as back-to-school clothing, computers under $1,500, or hurricane emergency preparedness gear.</p>
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
    const presets = {
      ca: { state: 7.25, local: 1.50 },
      tx: { state: 6.25, local: 2.00 },
      ny: { state: 4.00, local: 4.875 },
      fl: { state: 6.00, local: 1.50 },
      or: { state: 0.00, local: 0.00 }
    };

    function applyPreset() {
      const p = document.getElementById('statePreset').value;
      if (p !== 'custom' && presets[p]) {
        document.getElementById('stateRate').value = presets[p].state;
        document.getElementById('localRate').value = presets[p].local;
      }
      calculate();
    }

    function calculate() {
      const price = parseFloat(document.getElementById('priceInput').value) || 0;
      const mode = document.getElementById('calcMode').value;
      const stateRate = parseFloat(document.getElementById('stateRate').value) || 0;
      const localRate = parseFloat(document.getElementById('localRate').value) || 0;

      const combinedRate = stateRate + localRate;
      const rateDecimal = combinedRate / 100;

      let netPrice = 0;
      let totalTax = 0;
      let grossPrice = 0;

      if (mode === 'forward') {
        netPrice = price;
        totalTax = netPrice * rateDecimal;
        grossPrice = netPrice + totalTax;
      } else {
        // Reverse mode: price is gross
        grossPrice = price;
        netPrice = grossPrice / (1 + rateDecimal);
        totalTax = grossPrice - netPrice;
      }

      const statePortion = combinedRate > 0 ? totalTax * (stateRate / combinedRate) : 0;
      const localPortion = combinedRate > 0 ? totalTax * (localRate / combinedRate) : 0;

      const fmtCur = (v) => '$' + v.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

      if (mode === 'forward') {
        document.getElementById('resHeroLabel').textContent = 'Final Gross Checkout Total';
        document.getElementById('resHeroValue').textContent = fmtCur(grossPrice);
      } else {
        document.getElementById('resHeroLabel').textContent = 'Net Pre-Tax Base Price';
        document.getElementById('resHeroValue').textContent = fmtCur(netPrice);
      }

      document.getElementById('resNetPrice').textContent = fmtCur(netPrice);
      document.getElementById('resTotalTax').textContent = fmtCur(totalTax);
      document.getElementById('resCombinedRate').textContent = combinedRate.toFixed(3) + '%';
      document.getElementById('resStatePortion').textContent = fmtCur(statePortion);
      document.getElementById('resLocalPortion').textContent = fmtCur(localPortion);
      document.getElementById('resOverheadPct').textContent = '+' + combinedRate.toFixed(2) + '% on goods';
    }

    document.getElementById('statePreset').addEventListener('change', applyPreset);
    document.querySelectorAll('input, select').forEach(el => {
      if (el.id !== 'statePreset') {
        el.addEventListener('input', () => {
          if (el.id === 'stateRate' || el.id === 'localRate') {
            document.getElementById('statePreset').value = 'custom';
          }
          calculate();
        });
        el.addEventListener('change', () => {
          if (el.id === 'stateRate' || el.id === 'localRate') {
            document.getElementById('statePreset').value = 'custom';
          }
          calculate();
        });
      }
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('priceInput').value = '250.00';
      document.getElementById('calcMode').value = 'forward';
      document.getElementById('statePreset').value = 'custom';
      document.getElementById('stateRate').value = '6.0';
      document.getElementById('localRate').value = '2.25';
      calculate();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
'''
    with open('sales-tax-calculator.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Created sales-tax-calculator.html successfully!")

if __name__ == '__main__':
    create_net_worth_calculator()
    create_sales_tax_calculator()
