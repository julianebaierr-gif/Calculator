import os

def create_capital_gains_calculator():
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Capital Gains Tax Calculator | Short-Term vs Long-Term Investment Gains</title>
  <meta name="description" content="Calculate short-term and long-term capital gains tax, cost basis adjustments, Net Investment Income Tax (NIIT 3.8%), and after-tax net investment proceeds.">
  <link rel="canonical" href="https://calchub.cloud/capital-gains-calculator.html">
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
        "name": "Capital Gains Tax Calculator",
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates capital gains tax liabilities on stocks, crypto, and real estate, comparing short-term ordinary income rates against preferential long-term brackets.",
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
            "name": "What is the holding period threshold separating short-term and long-term capital gains?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Under US Internal Revenue Code (IRC), an asset held for exactly one year or less is subject to Short-Term Capital Gains, taxed at ordinary federal marginal income tax rates (up to 37%). Assets held for more than one full year qualify for preferential Long-Term Capital Gains rates (0%, 15%, or 20%)."
            }
          },
          {
            "@type": "Question",
            "name": "How is the adjusted cost basis calculated when selling securities or property?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Adjusted basis equals initial purchase price plus acquisition costs (broker commissions, closing fees, title insurance) plus capital improvements (for real estate), minus non-dividend return of capital and prior depreciation deductions."
            }
          },
          {
            "@type": "Question",
            "name": "What is the Net Investment Income Tax (NIIT 3.8%) and who is liable?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "The Net Investment Income Tax is a 3.8% surtax established under IRC Section 1411. It applies to net investment gains for single filers with modified adjusted gross income (MAGI) over $200,000 and married couples filing jointly over $250,000."
            }
          },
          {
            "@type": "Question",
            "name": "How does tax-loss harvesting offset capital gains?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Capital losses are first used to offset capital gains dollar-for-dollar (short-term against short-term, long-term against long-term). If net losses remain, up to $3,000 per tax year can offset ordinary taxable income, with excess losses carried forward indefinitely into future years."
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
        <h1>Capital Gains Tax Calculator</h1>
        <p class="lead-text">Calculate federal capital gains tax liability on equity, mutual fund, crypto, and asset sales. Compare short-term ordinary tax rates versus long-term brackets with Medicare NIIT surtaxes.</p>

        <div class="calc-card">
          <div class="calc-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="purchasePrice">Cost Basis / Purchase Price ($)</label>
                <input type="number" id="purchasePrice" value="25000" min="0" step="500" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="salePrice">Gross Sale Proceeds ($)</label>
                <input type="number" id="salePrice" value="65000" min="0" step="500" class="form-control">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-third">
                <label for="holdingPeriod">Holding Period</label>
                <select id="holdingPeriod" class="form-control">
                  <option value="long" selected>Long-Term (&gt; 1 Year)</option>
                  <option value="short">Short-Term (&le; 1 Year)</option>
                </select>
              </div>
              <div class="form-group col-third">
                <label for="filingStatus">Filing Status</label>
                <select id="filingStatus" class="form-control">
                  <option value="single" selected>Single Filer</option>
                  <option value="married">Married Filing Jointly</option>
                  <option value="head">Head of Household</option>
                </select>
              </div>
              <div class="form-group col-third">
                <label for="annualIncome">Other Taxable Income ($)</label>
                <input type="number" id="annualIncome" value="95000" min="0" step="5000" class="form-control">
              </div>
            </div>

            <div class="btn-group">
              <button type="button" id="calcBtn" class="btn btn-primary">Calculate Capital Gains Tax</button>
              <button type="button" id="resetBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </div>

          <div class="results-panel" id="resultsPanel">
            <h2>Tax & Proceeds Summary</h2>
            <div class="result-hero">
              <span class="hero-label">Estimated Federal Tax Liability</span>
              <span class="hero-value" id="resTaxDue">$6,000</span>
            </div>

            <div class="results-grid">
              <div class="result-item">
                <span class="sub-label">Net Capital Realized Gain</span>
                <span class="sub-value highlight" id="resGain">$40,000</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Return on Investment (ROI)</span>
                <span class="sub-value" id="resRoi">+160.0%</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Effective Federal Tax Rate</span>
                <span class="sub-value" id="resEffRate">15.0%</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Base Capital Gains Tax</span>
                <span class="sub-value" id="resBaseTax">$6,000</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Net Investment Income Tax (NIIT 3.8%)</span>
                <span class="sub-value" id="resNiit">$0</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Net After-Tax Take-Home Proceeds</span>
                <span class="sub-value highlight" id="resNetProceeds">$59,000</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Comprehensive Tax Finance Article (1,300+ Words) -->
        <article class="article-body">
          <h2>1. The Taxation Architecture of Capital Assets</h2>
          <p>Under Title 26 of the United States Code (the Internal Revenue Code, IRC), almost everything an individual owns and uses for personal or investment purposes constitutes a <strong>capital asset</strong>. When an investor disposes of securities, equities, cryptocurrency, exchange-traded funds, mutual funds, or real estate for a price exceeding the asset's acquisition value, a taxable <strong>capital gain</strong> is realized.</p>
          <p>The mathematical computation begins by defining the <strong>Capital Realized Gain or Loss (\(G\))</strong>:</p>
          <div class="math-block">
            $$G = \text{Gross Realized Proceeds} - \text{Adjusted Cost Basis}$$
          </div>
          <p>Where:</p>
          <ul>
            <li><strong>Gross Realized Proceeds:</strong> Total monetary and fair market value consideration received from the buyer, net of direct transactional transfer expenses (such as brokerage commissions, legal fees, exchange fees, and documentary stamps).</li>
            <li><strong>Adjusted Cost Basis:</strong> The historical purchase price augmented by capitalized acquisition costs, dividend reinvestment units, and physical capital improvements (for real estate), reduced by non-taxable returns of capital and prior MACRS/straight-line depreciation deductions.</li>
          </ul>

          <h2>2. Short-Term vs. Long-Term Holding Period Classifications</h2>
          <p>The United States tax code enforces a strict dichotomy based on holding duration:</p>
          <h3>A. Short-Term Capital Gains (Holding Period \(\le 12\text{ Months}\))</h3>
          <p>Securities held for 365 days or fewer are categorized as short-term. They receive zero tax sheltering and are taxed at ordinary individual marginal income tax rates across the 7 federal brackets: <strong>10%, 12%, 22%, 24%, 32%, 35%, and 37%</strong>.</p>

          <h3>B. Long-Term Capital Gains (Holding Period \(> 12\text{ Months}\))</h3>
          <p>Assets held for at least one year and one day enjoy statutory preferential capital gains brackets designed to incentivize long-term entrepreneurial risk and corporate capital formation: <strong>0%, 15%, or 20%</strong> depending on total taxable income.</p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Filing Status</th>
                <th>0% Long-Term Bracket</th>
                <th>15% Long-Term Bracket</th>
                <th>20% Long-Term Bracket</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Single Filer</strong></td>
                <td>Up to $47,025</td>
                <td>$47,026 &ndash; $518,900</td>
                <td>Over $518,900</td>
              </tr>
              <tr>
                <td><strong>Married Filing Jointly</strong></td>
                <td>Up to $94,050</td>
                <td>$94,051 &ndash; $583,750</td>
                <td>Over $583,750</td>
              </tr>
              <tr>
                <td><strong>Head of Household</strong></td>
                <td>Up to $63,000</td>
                <td>$63,001 &ndash; $551,350</td>
                <td>Over $551,350</td>
              </tr>
            </tbody>
          </table>

          <h2>3. Surtaxes: The Net Investment Income Tax (NIIT 3.8%)</h2>
          <p>Enacted under the Affordable Care Act and codified in IRC Section 1411, high-earning individuals are subject to an additional <strong>3.8% Net Investment Income Tax (NIIT)</strong> on investment gains, dividends, royalties, and passive rents. The surtax applies to the lesser of:</p>
          <div class="math-block">
            $$\text{NIIT Liability} = 0.038 \times \min\left( \text{Net Investment Income}, \max(0, \text{MAGI} - \text{Threshold}) \right)$$
          </div>
          <p>Statutory Modified Adjusted Gross Income (MAGI) thresholds are unindexed for inflation:</p>
          <ul>
            <li><strong>Single / Head of Household:</strong> $200,000</li>
            <li><strong>Married Filing Jointly:</strong> $250,000</li>
            <li><strong>Married Filing Separately:</strong> $125,000</li>
          </ul>
          <p>When an investor's overall income plus capital gains pushes them into the top federal bracket, the combined top marginal federal capital gains tax rate reaches <strong>23.8%</strong> (20% base + 3.8% NIIT), excluding state and municipal taxes.</p>

          <div class="worked-example-card">
            <h3>Worked Tax Case Study: Growth Stock Sale Arbitrage</h3>
            <p><strong>Scenario:</strong> An investor filing Single earns $110,000 in ordinary salary. They purchased 500 shares of a technology ETF for $50,000. Exactly 18 months later, the shares are liquidated for $130,000.</p>
            <p><strong>Step 1: Compute Realized Capital Gain</strong></p>
            <div class="math-block">
              $$G = \$130,000 - \$50,000 = \$80,000\text{ (Long-Term)}$$
            </div>
            <p><strong>Step 2: Determine Total Combined Income</strong></p>
            <div class="math-block">
              $$\text{Total Income} = \$110,000\text{ (salary)} + \$80,000\text{ (gain)} = \$190,000$$
            </div>
            <p><strong>Step 3: Apply Long-Term Capital Gains Tax Brackets</strong></p>
            <p>Since the entire $190,000 falls comfortably within the Single 15% bracket ($47,026 to $518,900), the base federal capital gains tax is:</p>
            <div class="math-block">
              $$\text{Tax}_{\text{base}} = \$80,000 \times 0.15 = \$12,000$$
            </div>
            <p><strong>Step 4: Check NIIT Threshold</strong></p>
            <p>Total MAGI is $190,000, which remains below the $200,000 Single statutory threshold. Therefore, \(\text{NIIT} = \$0\).</p>
            <p><strong>Comparative Analysis:</strong> Had the investor sold the position at 11 months (short-term), the $80,000 would have been taxed at ordinary rates (a blend of 24% and 32%), generating approximately <strong>$19,600</strong> in taxes. By waiting past the 1-year mark, the investor saved <strong>$7,600 in cash taxes</strong>.</p>
          </div>

          <h2>4. Tax-Loss Harvesting Rules and Wash-Sale Restrictions</h2>
          <p>Astute portfolio managers minimize tax liabilities via <strong>tax-loss harvesting</strong>—deliberately realizing losses on depreciated assets to offset taxable realized gains elsewhere in the portfolio:</p>
          <ul>
            <li><strong>Offset Mechanics:</strong> Short-term losses offset short-term gains, while long-term losses offset long-term gains. Any remaining net loss in one category then offsets net gains in the opposing category.</li>
            <li><strong>Ordinary Income Deduction Cap:</strong> If net total capital losses exceed total capital gains for the calendar year, a maximum of <strong>$3,000</strong> ($1,500 if married filing separately) can be deducted against ordinary taxable wages. Unused losses carry forward indefinitely to future tax years.</li>
            <li><strong>The 30-Day Wash-Sale Rule (IRC § 1091):</strong> Prevents taxpayers from claiming a tax loss if they acquire "substantially identical" stock or securities within a 61-day window (30 days before through 30 days after the date of the loss-generating sale). Disallowed losses are appended back to the cost basis of the newly acquired replacement security.</li>
          </ul>

          <h2>5. Special Exclusions: Real Estate Section 121 and Section 1031</h2>
          <p>Residential real estate investors benefit from major statutory shelters not available to equities:</p>
          <ul>
            <li><strong>Section 121 Primary Residence Exclusion:</strong> Taxpayers can exclude up to <strong>$250,000</strong> of capital gains ($500,000 for married couples filing jointly) from the sale of their primary home if they owned and occupied the residence for at least two of the five years preceding the sale date.</li>
            <li><strong>Section 1031 Like-Kind Exchange:</strong> Commercial real estate and rental property owners can indefinitely defer 100% of capital gains and depreciation recapture taxes by rolling all gross sale proceeds into a replacement like-kind investment property within 180 calendar days.</li>
          </ul>

          <h2>6. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>Are cryptocurrencies taxed as capital assets or currency?</h3>
            <p>Under IRS Notice 2014-21, virtual currencies (such as Bitcoin and Ethereum) are legally classified as property. Every crypto-to-crypto trade, token swap, or purchase of goods using crypto triggers a taxable capital gains realization event based on the token's cost basis.</p>
          </div>
          <div class="faq-item">
            <h3>Do state taxes apply to capital gains?</h3>
            <p>Yes. Most US states tax capital gains as ordinary state income (ranging from 0% in states like Texas and Florida to over 13% in California). Only a minority of states offer preferential rates for long-term gains.</p>
          </div>
          <div class="faq-item">
            <h3>How do inherited assets receive a "step-up" in basis?</h3>
            <p>Under IRC Section 1014, when a beneficiary inherits capital assets upon the owner's death, the cost basis is automatically "stepped up" to the fair market value on the date of death, permanently extinguishing all unrealized capital gains accumulated during the decedent's lifetime.</p>
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
      const basis = parseFloat(document.getElementById('purchasePrice').value) || 0;
      const proceeds = parseFloat(document.getElementById('salePrice').value) || 0;
      const period = document.getElementById('holdingPeriod').value;
      const status = document.getElementById('filingStatus').value;
      const income = parseFloat(document.getElementById('annualIncome').value) || 0;

      const gain = proceeds - basis;
      const roi = basis > 0 ? (gain / basis) * 100 : 0;

      if (gain <= 0) {
        document.getElementById('resGain').textContent = '$' + Math.round(gain).toLocaleString('en-US');
        document.getElementById('resRoi').textContent = roi.toFixed(1) + '%';
        document.getElementById('resTaxDue').textContent = '$0';
        document.getElementById('resEffRate').textContent = '0.0%';
        document.getElementById('resBaseTax').textContent = '$0';
        document.getElementById('resNiit').textContent = '$0';
        document.getElementById('resNetProceeds').textContent = '$' + Math.round(proceeds).toLocaleString('en-US');
        return;
      }

      // Total MAGI approx
      const totalIncome = income + gain;

      let baseTax = 0;
      if (period === 'long') {
        // Long-term brackets (2024 approximation)
        let b0 = 47025, b15 = 518900;
        if (status === 'married') {
          b0 = 94050; b15 = 583750;
        } else if (status === 'head') {
          b0 = 63000; b15 = 551350;
        }

        if (totalIncome <= b0) {
          baseTax = 0;
        } else if (totalIncome <= b15) {
          // If previous income was below b0, some portion might be 0%
          const taxableAt15 = Math.min(gain, totalIncome - b0);
          baseTax = taxableAt15 * 0.15;
        } else {
          // Crosses into 20%
          const portionIn20 = Math.min(gain, totalIncome - b15);
          const portionIn15 = gain - portionIn20;
          baseTax = (portionIn15 * 0.15) + (portionIn20 * 0.20);
        }
      } else {
        // Short-term: ordinary marginal rate approximation (simplified progressive)
        // Assume marginal bracket on the gain
        let rate = 0.22;
        if (totalIncome > 243725) rate = 0.35;
        else if (totalIncome > 100525) rate = 0.24;
        else if (totalIncome > 47150) rate = 0.22;
        else rate = 0.12;
        baseTax = gain * rate;
      }

      // NIIT 3.8%
      let niitThreshold = 200000;
      if (status === 'married') niitThreshold = 250000;

      let niitTax = 0;
      if (totalIncome > niitThreshold) {
        const excessMagi = totalIncome - niitThreshold;
        const subjectToNiit = Math.min(gain, excessMagi);
        niitTax = subjectToNiit * 0.038;
      }

      const totalTax = baseTax + niitTax;
      const netProceeds = proceeds - totalTax;
      const effRate = gain > 0 ? (totalTax / gain) * 100 : 0;

      const fmt = (v) => '$' + Math.round(v).toLocaleString('en-US');

      document.getElementById('resGain').textContent = fmt(gain);
      document.getElementById('resRoi').textContent = (roi >= 0 ? '+' : '') + roi.toFixed(1) + '%';
      document.getElementById('resTaxDue').textContent = fmt(totalTax);
      document.getElementById('resEffRate').textContent = effRate.toFixed(1) + '%';
      document.getElementById('resBaseTax').textContent = fmt(baseTax);
      document.getElementById('resNiit').textContent = fmt(niitTax);
      document.getElementById('resNetProceeds').textContent = fmt(netProceeds);
    }

    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculate);
      el.addEventListener('change', calculate);
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('purchasePrice').value = '25000';
      document.getElementById('salePrice').value = '65000';
      document.getElementById('holdingPeriod').value = 'long';
      document.getElementById('filingStatus').value = 'single';
      document.getElementById('annualIncome').value = '95000';
      calculate();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
'''
    with open('capital-gains-calculator.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Created capital-gains-calculator.html successfully!")

def create_cd_calculator():
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CD Calculator | Certificate of Deposit APY, Interest & Penalty Sizer</title>
  <meta name="description" content="Calculate Certificate of Deposit (CD) returns, compounding interest, effective APY yields, early withdrawal penalties, and multi-year CD ladder strategies.">
  <link rel="canonical" href="https://calchub.cloud/cd-calculator.html">
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
        "name": "Certificate of Deposit (CD) Calculator",
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "Web Browser",
        "description": "Calculates Certificate of Deposit maturity balances, cumulative interest earned, effective APY compounding, and early withdrawal penalty impacts.",
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
            "name": "How does compound interest work on a Certificate of Deposit?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "CD growth follows standard compound interest: A = P × (1 + r/n)^(n×t), where P is initial deposit, r is nominal annual interest rate, n is compounding frequency (e.g., daily n = 365), and t is term duration in years."
            }
          },
          {
            "@type": "Question",
            "name": "What is an Early Withdrawal Penalty (EWP) on a bank CD?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "An early withdrawal penalty is a fee charged by the issuing financial institution if the depositor breaks the CD before the agreed maturity date. It is typically calculated as a forfeit of several months of simple interest (e.g., 90 days of interest for terms under 1 year, 180 days for 1 to 3 years)."
            }
          },
          {
            "@type": "Question",
            "name": "How does a CD ladder strategy maximize liquidity and yield?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "A CD ladder divides a lump sum into equal tranches across varying maturities (e.g., 1-year, 2-year, 3-year, 4-year, and 5-year CDs). As each CD matures annually, the principal is reinvested into a new 5-year CD at the top tier rate, providing annual liquidity while capturing long-term yields."
            }
          },
          {
            "@type": "Question",
            "name": "Are Certificates of Deposit FDIC insured?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. CDs issued by federally insured banks are backed by the Federal Deposit Insurance Corporation (FDIC), and those issued by credit unions are backed by the National Credit Union Administration (NCUA), up to $250,000 per depositor, per insured institution."
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
        <h1>Certificate of Deposit (CD) Calculator</h1>
        <p class="lead-text">Model Certificate of Deposit maturity yields, compound growth across daily and monthly schedules, and evaluate the net financial impact of early withdrawal penalties.</p>

        <div class="calc-card">
          <div class="calc-form">
            <div class="form-row">
              <div class="form-group col-half">
                <label for="initialDeposit">Initial Deposit Amount ($)</label>
                <input type="number" id="initialDeposit" value="10000" min="100" step="500" class="form-control">
              </div>
              <div class="form-group col-half">
                <label for="statedApy">Annual Percentage Yield (APY %)</label>
                <input type="number" id="statedApy" value="4.85" min="0.01" max="25" step="0.05" class="form-control">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-third">
                <label for="cdTermMonths">Term Length (Months)</label>
                <select id="cdTermMonths" class="form-control">
                  <option value="6">6 Months</option>
                  <option value="12" selected>12 Months (1 Year)</option>
                  <option value="18">18 Months</option>
                  <option value="24">24 Months (2 Years)</option>
                  <option value="36">36 Months (3 Years)</option>
                  <option value="48">48 Months (4 Years)</option>
                  <option value="60">60 Months (5 Years)</option>
                </select>
              </div>
              <div class="form-group col-third">
                <label for="compoundingType">Compounding</label>
                <select id="compoundingType" class="form-control">
                  <option value="365" selected>Daily (n = 365)</option>
                  <option value="12">Monthly (n = 12)</option>
                  <option value="1">Annually (n = 1)</option>
                </select>
              </div>
              <div class="form-group col-third">
                <label for="penaltyMonths">Early Withdrawal Penalty</label>
                <select id="penaltyMonths" class="form-control">
                  <option value="3" selected>90 Days (3 Months Interest)</option>
                  <option value="6">180 Days (6 Months Interest)</option>
                  <option value="9">270 Days (9 Months Interest)</option>
                  <option value="12">365 Days (12 Months Interest)</option>
                </select>
              </div>
            </div>

            <div class="btn-group">
              <button type="button" id="calcBtn" class="btn btn-primary">Calculate CD Returns</button>
              <button type="button" id="resetBtn" class="btn btn-secondary">Reset Defaults</button>
            </div>
          </div>

          <div class="results-panel" id="resultsPanel">
            <h2>Maturity & Growth Summary</h2>
            <div class="result-hero">
              <span class="hero-label">Total Balance at Maturity</span>
              <span class="hero-value" id="resEndingBalance">$10,485.00</span>
            </div>

            <div class="results-grid">
              <div class="result-item">
                <span class="sub-label">Total Interest Earned</span>
                <span class="sub-value highlight" id="resInterestEarned">$485.00</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Effective APY</span>
                <span class="sub-value" id="resEffApy">4.850%</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Monthly Average Yield</span>
                <span class="sub-value" id="resMonthlyYield">$40.42 / mo</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Early Withdrawal Penalty Cost</span>
                <span class="sub-value" id="resPenaltyCost">$119.50</span>
              </div>
              <div class="result-item">
                <span class="sub-label">Net Payout (If Broken Early)</span>
                <span class="sub-value" id="resEarlyPayout">$10,365.50</span>
              </div>
              <div class="result-item">
                <span class="sub-label">FDIC Insurance Status</span>
                <span class="sub-value" style="color:var(--primary-color, #2563eb);">100% Backed (&le; $250k)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Comprehensive Banking & Fixed Income Article (1,250+ Words) -->
        <article class="article-body">
          <h2>1. The Financial Architecture of Certificates of Deposit</h2>
          <p>A <strong>Certificate of Deposit (CD)</strong> is a specialized promissory time-deposit product issued by commercial banks and credit unions. Under the contractual terms of a CD agreement, the depositor surrenders liquidity by committing an initial principal sum \(P\) for a fixed duration \(t\), in exchange for an elevated guaranteed interest rate immune to open-market interest rate fluctuations.</p>
          <p>The mathematical accumulation of wealth within a CD follows the classical compound interest model:</p>
          <div class="math-block">
            $$A(t) = P \left( 1 + \frac{r}{n} \right)^{n \cdot t}$$
          </div>
          <p>Where:</p>
          <ul>
            <li>\(A(t)\) is the future accumulated balance at maturity.</li>
            <li>\(P\) is the original principal investment.</li>
            <li>\(r\) is the nominal annual promissory interest rate (decimal equivalent of APR).</li>
            <li>\(n\) is the compounding frequency per calendar year (typically daily \(n = 365\) in modern digital banking).</li>
            <li>\(t\) is the maturity term expressed in fractional or integer years (\(t = \text{Months} / 12\)).</li>
          </ul>
          <p>Cumulative interest accrued across the term is simply the net expansion of the account balance:</p>
          <div class="math-block">
            $$\text{Total Interest} = A(t) - P = P \left[ \left( 1 + \frac{r}{n} \right)^{n \cdot t} - 1 \right]$$
          </div>

          <h2>2. The Truth in Savings Act: APR vs. APY Mandates</h2>
          <p>Under the Federal Truth in Savings Act (TISA, Consumer Financial Protection Bureau Regulation DD), depository institutions in the United States are prohibited from advertising nominal APR without prominently disclosing the <strong>Annual Percentage Yield (APY)</strong>. Because APY factors in compounding, it precisely reflects the effective yield earned over a 365-day annual horizon:</p>
          <div class="math-block">
            $$\text{APY} = \left( 1 + \frac{r}{n} \right)^n - 1$$
          </div>
          <p>When interest compounds daily (\(n = 365\)), the relationship between nominal APR \(r\) and advertised APY is given by:</p>
          <div class="math-block">
            $$r = 365 \left[ (1 + \text{APY})^{1/365} - 1 \right]$$
          </div>

          <h2>3. Early Withdrawal Penalties (EWP) and Principal Erosion</h2>
          <p>CDs are illiquid instruments designed to provide issuing banks with stable, predictable core deposit funding. If a depositor liquidates a CD prior to its contracted maturity date, the institution enforces an <strong>Early Withdrawal Penalty (EWP)</strong>.</p>
          <p>The penalty is typically structured as a forfeit of simple interest over a prescribed number of days or months, irrespective of whether that interest has already been earned:</p>
          <div class="math-block">
            $$\text{EWP} = P \times r_{\text{nominal}} \times \left( \frac{\text{Penalty Days}}{365} \right)$$
          </div>

          <table class="data-table">
            <thead>
              <tr>
                <th>CD Term Length</th>
                <th>Standard Bank Penalty</th>
                <th>Penalty Interest Formula</th>
                <th>Principal Risk if Broken Early?</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>3 to 6 Months</strong></td>
                <td>90 Days Interest</td>
                <td>\(P \times r \times (90 / 365)\)</td>
                <td>Yes (if held &lt; 90 days)</td>
              </tr>
              <tr>
                <td><strong>12 to 18 Months</strong></td>
                <td>180 Days Interest</td>
                <td>\(P \times r \times (180 / 365)\)</td>
                <td>Yes (if held &lt; 180 days)</td>
              </tr>
              <tr>
                <td><strong>24 to 36 Months</strong></td>
                <td>270 Days Interest</td>
                <td>\(P \times r \times (270 / 365)\)</td>
                <td>Yes (if held &lt; 270 days)</td>
              </tr>
              <tr>
                <td><strong>48 to 60 Months</strong></td>
                <td>365 Days Interest (1 Full Year)</td>
                <td>\(P \times r \times (365 / 365)\)</td>
                <td>Yes (if held &lt; 365 days)</td>
              </tr>
            </tbody>
          </table>
          <p><strong>Crucial Consumer Warning:</strong> If a depositor redeems a 1-year CD after only 60 days, the accrued interest is insufficient to satisfy a 180-day penalty. Under most retail bank deposit agreements, the unearned penalty portion is deducted directly from the depositor's <em>original principal investment</em>.</p>

          <div class="worked-example-card">
            <h3>Worked Financial Case Study: The Broken 5-Year CD Dilemma</h3>
            <p><strong>Scenario:</strong> An investor places $50,000 into a 5-year fixed CD yielding 4.50% APY compounded daily. The issuing credit union enforces a 12-month early withdrawal penalty. After 14 months, market interest rates spike to 6.50%, and the depositor considers breaking the CD to reinvest.</p>
            <p><strong>Step 1: Calculate Nominal Daily Rate</strong></p>
            <div class="math-block">
              $$r = 365 \left[ (1 + 0.045)^{1/365} - 1 \right] \approx 4.4023\%$$
            </div>
            <p><strong>Step 2: Calculate Accrued Balance at Month 14 (\(t = 14 / 12 = 1.1667\text{ yrs}\))</strong></p>
            <div class="math-block">
              $$A(1.1667) = 50,000 \left( 1 + \frac{0.044023}{365} \right)^{365 \times 1.1667} = \$52,637.28$$
            </div>
            <p>Total interest earned through 14 months = \(\$2,637.28\).</p>
            <p><strong>Step 3: Calculate Early Withdrawal Penalty (12 Months Simple Interest)</strong></p>
            <div class="math-block">
              $$\text{EWP} = 50,000 \times 0.044023 \times 1.0 = \$2,201.15$$
            </div>
            <p><strong>Step 4: Determine Net Cash Payout</strong></p>
            <div class="math-block">
              $$\text{Net Payout} = \$52,637.28 - \$2,201.15 = \$50,436.13$$
            </div>
            <p><strong>Conclusion:</strong> After 14 months of commitment, the investor walks away with merely <strong>$436.13</strong> in net profit—an annualized return of only 0.74%. The break-even calculation shows that switching to a 6.50% vehicle only overcomes the $2,201.15 penalty if reinvested for at least 26 additional months.</p>
          </div>

          <h2>4. Strategic Portfolio Construction: The CD Ladder</h2>
          <p>To eliminate early withdrawal penalty risks while enjoying top-tier multi-year yields, fixed-income investors deploy a <strong>CD Ladder</strong>. For example, a $50,000 portfolio is divided into five $10,000 tranches across staggered maturities:</p>
          <ul>
            <li>$10,000 in a 1-Year CD (Matures in Year 1)</li>
            <li>$10,000 in a 2-Year CD (Matures in Year 2)</li>
            <li>$10,000 in a 3-Year CD (Matures in Year 3)</li>
            <li>$10,000 in a 4-Year CD (Matures in Year 4)</li>
            <li>$10,000 in a 5-Year CD (Matures in Year 5)</li>
          </ul>
          <p>When the 1-year CD matures in Year 1, the investor re-allocates that capital into a fresh 5-year CD. In Year 2, the 2-year CD matures and is rolled into another 5-year CD. Within four years, the portfolio achieves steady-state: <strong>20% of total wealth becomes fully liquid every single year</strong>, yet 100% of the capital captures premium 5-year yields.</p>

          <h2>5. Frequently Asked Questions</h2>
          <div class="faq-item">
            <h3>How do Brokered CDs differ from traditional Bank CDs?</h3>
            <p>Brokered CDs are issued by banks through brokerage firms (e.g., Fidelity, Schwab, Vanguard). They trade on a secondary OTC market, meaning investors needing early liquidity can sell their CD at prevailing market prices without paying an early withdrawal penalty, though market prices fluctuate inversely with interest rates.</p>
          </div>
          <div class="faq-item">
            <h3>What is a Callable CD?</h3>
            <p>A callable CD grants the issuing financial institution the contractual right to terminate ("call") the deposit early—typically after an initial non-call protection window (e.g., 6 months)—if market interest rates decline. Depositors receive their principal and interest to date, but face reinvestment rate risk.</p>
          </div>
          <div class="faq-item">
            <h3>Are CD interest earnings subject to annual income taxes?</h3>
            <p>Yes. In taxable brokerage or bank accounts, CD interest is treated as ordinary taxable income in the calendar year it is credited (reported via IRS Form 1099-INT), even if the CD has not yet matured and earnings cannot be withdrawn without penalty.</p>
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
      const P = parseFloat(document.getElementById('initialDeposit').value) || 0;
      const apy = parseFloat(document.getElementById('statedApy').value) || 0;
      const months = parseInt(document.getElementById('cdTermMonths').value) || 12;
      const n = parseFloat(document.getElementById('compoundingType').value) || 365;
      const penaltyMo = parseInt(document.getElementById('penaltyMonths').value) || 3;

      if (P <= 0 || apy <= 0) return;

      const apyDecimal = apy / 100;
      // Derive nominal rate r
      let r = 0;
      if (n === 1) {
        r = apyDecimal;
      } else {
        r = n * (Math.pow(1 + apyDecimal, 1 / n) - 1);
      }

      const tYears = months / 12;
      const endingBalance = P * Math.pow(1 + r / n, n * tYears);
      const interestEarned = endingBalance - P;
      const monthlyAvgYield = interestEarned / months;

      // Early withdrawal penalty (penaltyMo of simple interest on P)
      const penaltyCost = P * r * (penaltyMo / 12);
      const netEarlyPayout = Math.max(0, endingBalance - penaltyCost);

      const fmtCur = (v) => '$' + v.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

      document.getElementById('resEndingBalance').textContent = fmtCur(endingBalance);
      document.getElementById('resInterestEarned').textContent = fmtCur(interestEarned);
      document.getElementById('resEffApy').textContent = apy.toFixed(3) + '%';
      document.getElementById('resMonthlyYield').textContent = fmtCur(monthlyAvgYield) + ' / mo';
      document.getElementById('resPenaltyCost').textContent = fmtCur(penaltyCost);
      document.getElementById('resEarlyPayout').textContent = fmtCur(netEarlyPayout);
    }

    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculate);
      el.addEventListener('change', calculate);
    });

    document.getElementById('calcBtn').addEventListener('click', calculate);
    document.getElementById('resetBtn').addEventListener('click', () => {
      document.getElementById('initialDeposit').value = '10000';
      document.getElementById('statedApy').value = '4.85';
      document.getElementById('cdTermMonths').value = '12';
      document.getElementById('compoundingType').value = '365';
      document.getElementById('penaltyMonths').value = '3';
      calculate();
    });

    window.addEventListener('DOMContentLoaded', calculate);
  </script>
</body>
</html>
'''
    with open('cd-calculator.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Created cd-calculator.html successfully!")

if __name__ == '__main__':
    create_capital_gains_calculator()
    create_cd_calculator()
