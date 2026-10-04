# -*- coding: utf-8 -*-
"""
Generator for Batch 32 - Part 3:
5. markup-calculator.html
6. density-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 5. markup-calculator.html
HTML_MARKUP = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Markup Calculator - Cost, Selling Price, Margin &amp; Profit</title>
  <meta name="description" content="Calculate markup percentage, gross profit margin, retail selling price, and profit multiplier from cost. Compare margin vs markup with formulas and step-by-step proofs.">
  <link rel="canonical" href="https://calchub.org/markup-calculator.html">
  <meta property="og:title" content="Markup Calculator - Retail Price &amp; Profit Margin Solver">
  <meta property="og:description" content="Free commercial markup calculator. Calculate selling price, dollar gross profit, profit margin percentage, and price multiplier from cost with step-by-step formulas.">
  <meta property="og:url" content="https://calchub.org/markup-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Markup Calculator - Profit Margin &amp; Price Solver">
  <meta name="twitter:description" content="Solve for retail price, markup percentage, or desired gross margin. Full conversion charts, formulas, and real-world business case studies.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Markup Calculator",
    "url": "https://calchub.org/markup-calculator.html",
    "description": "Calculates retail selling price, dollar profit, gross margin percentage, and markup percentage from wholesale or production cost.",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "All"
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the key difference between markup and profit margin?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Markup is the percentage added to the original cost price to establish the selling price (Markup = Profit / Cost). Profit margin is the percentage of the selling price that is kept as profit (Margin = Profit / Selling Price). For instance, a 100% markup corresponds to a 50% gross margin."
        }
      },
      {
        "@type": "Question",
        "name": "How do you calculate selling price from cost and desired gross margin?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "To calculate selling price from a desired gross margin, divide cost by (1 minus the margin in decimal format): Price = Cost / (1 - Margin/100). For example, if cost is $60 and desired margin is 40%, Selling Price = $60 / (1 - 0.40) = $60 / 0.60 = $100."
        }
      },
      {
        "@type": "Question",
        "name": "What is keystone pricing in retail?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Keystone pricing is a conventional retail pricing rule of thumb where wholesale cost is multiplied by 2.0 (a 100% markup), resulting in an exact 50% gross profit margin. It provides sufficient buffer for operating overhead, marketing, and seasonal clearance markdowns."
        }
      },
      {
        "@type": "Question",
        "name": "Can gross margin ever exceed 100%?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. Gross margin cannot exceed 100% because profit cannot exceed the total selling price (unless goods have negative production cost). However, markup percentage can easily exceed 100%, 500%, or even 1,000% whenever selling price is many times higher than manufacturing cost."
        }
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">CalcHub</a>
      <nav class="site-nav">
        <a href="index.html">Home</a>
        <a href="math.html">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html" class="active">Finance</a>
      </nav>
    </div>
  </header>

  <main class="calculator-container">
    <div class="calculator-header">
      <div class="calc-icon" aria-hidden="true">&#128178;</div>
      <h1>Markup Calculator</h1>
      <p class="calc-description">Compute retail selling price, profit dollar margins, markup percentages, and cost multipliers with interactive pricing solvers.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="markup-mode">Calculation Mode</label>
        <select id="markup-mode" class="form-control" onchange="switchMarkupMode()">
          <option value="cost-markup" selected>Given Cost &amp; Markup % &rarr; Solve Price &amp; Margin</option>
          <option value="cost-margin">Given Cost &amp; Desired Gross Margin % &rarr; Solve Price &amp; Markup</option>
          <option value="cost-price">Given Cost &amp; Selling Price &rarr; Solve Markup % &amp; Margin %</option>
        </select>
      </div>

      <div class="input-grid">
        <div class="input-group">
          <label for="inp-cost">Cost of Goods Sold ($)</label>
          <input type="number" id="inp-cost" class="form-control" value="50.00" step="any" min="0">
        </div>

        <div class="input-group" id="group-param2">
          <label for="inp-param2" id="lbl-param2">Markup Percentage (%)</label>
          <input type="number" id="inp-param2" class="form-control" value="60.00" step="any">
        </div>
      </div>

      <div class="input-grid">
        <div class="input-group">
          <label for="currency-sym">Currency Symbol</label>
          <select id="currency-sym" class="form-control" onchange="calculateMarkup()">
            <option value="$" selected>$ (USD / CAD / AUD)</option>
            <option value="€">€ (EUR)</option>
            <option value="£">£ (GBP)</option>
            <option value="¥">¥ (JPY / CNY)</option>
            <option value="₨">₨ (PKR / INR)</option>
          </select>
        </div>
        <div class="input-group">
          <label for="prec-digits">Rounding Precision</label>
          <select id="prec-digits" class="form-control" onchange="calculateMarkup()">
            <option value="2" selected>2 Decimals (Standard Currency)</option>
            <option value="4">4 Decimals (High Precision)</option>
            <option value="0">Whole Numbers</option>
          </select>
        </div>
      </div>

      <div class="btn-group">
        <button type="button" class="btn btn-primary" onclick="calculateMarkup()">Calculate Pricing</button>
        <button type="button" class="btn btn-secondary" onclick="resetMarkup()">Reset Defaults</button>
      </div>

      <!-- Results Display Grid -->
      <div class="results-grid" style="margin-top: 1.5rem;">
        <div class="result-card primary-result">
          <div class="result-label">Recommended Selling Price</div>
          <div class="result-value" id="res-price">$80.00</div>
          <div class="result-subtext" id="res-multiplier">Multiplier: 1.60x Cost</div>
        </div>

        <div class="result-card">
          <div class="result-label">Gross Profit Amount</div>
          <div class="result-value" id="res-profit">$30.00</div>
          <div class="result-subtext">Net dollar gain above wholesale cost</div>
        </div>

        <div class="result-card">
          <div class="result-label">Gross Profit Margin</div>
          <div class="result-value" id="res-margin">37.50%</div>
          <div class="result-subtext">Profit share of retail revenue</div>
        </div>

        <div class="result-card">
          <div class="result-label">Effective Markup</div>
          <div class="result-value" id="res-markup">60.00%</div>
          <div class="result-subtext">Surcharge percentage on cost</div>
        </div>
      </div>

      <!-- Step-by-step Math Breakdown Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Mathematical Derivation &amp; Pricing Breakdown</h3>
        <pre id="res-steps" style="white-space: pre-wrap; font-family: monospace; background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; color: var(--text-primary, #212529);"></pre>
      </div>
    </div>

    <!-- Article Content: 1000+ Words Clinical / Financial Deep Dive -->
    <article class="article-body">
      <h2>The Fundamentals of Commercial Markup and Retail Pricing Strategy</h2>
      <p>
        In modern commerce, wholesale distribution, and manufacturing economics, establishing a mathematically sound pricing structure is the foundational determinant of business solvency. Setting price points arbitrarily or relying on generic intuitions frequently leads to the classic "retail solvency paradox"—generating substantial top-line revenue while suffering catastrophic cash-flow deficits due to underestimated cost structures and misunderstood profit margins.
      </p>
      <p>
        At the core of commercial pricing mechanics are two intertwined yet fundamentally distinct concepts: <strong>markup percentage</strong> and <strong>gross profit margin percentage</strong>. While both metrics quantify the economic spread between what an enterprise pays for inventory (Cost of Goods Sold, or COGS) and the final price paid by the customer (Retail Selling Price, or \(P\)), they express this relationship relative to two completely different economic denominators. Failing to distinguish between these two ratios is one of the most widespread causes of commercial insolvency among emerging merchants, contractors, and e-commerce entrepreneurs.
      </p>

      <h2>Mathematical Formulations: Markup vs. Gross Profit Margin</h2>
      <p>
        Let \(C\) represent the total Cost of Goods Sold (including manufacturing, procurement, inbound freight, and customs duties), \(P\) represent the final retail Selling Price, and \(\Pi\) represent the gross profit dollar contribution:
      </p>
      $$\Pi = P - C$$
      <p>
        The <strong>Markup Percentage (\(M\))</strong> represents the gross profit expressed as a direct percentage of the <em>cost price</em>:
      </p>
      $$M = \frac{\Pi}{C} \times 100\% = \frac{P - C}{C} \times 100\%$$
      <p>
        Conversely, the <strong>Gross Profit Margin (\(G\))</strong> represents the gross profit expressed as a percentage of the <em>final selling price (revenue)</em>:
      </p>
      $$G = \frac{\Pi}{P} \times 100\% = \frac{P - C}{P} \times 100\%$$

      <h3>Direct Conversion Algebraic Proofs</h3>
      <p>
        Because cost, selling price, and profit form a closed algebraic system, any given markup percentage maps strictly to a single unique gross profit margin, and vice versa. Starting from the definition of margin:
      </p>
      $$G = \frac{P - C}{P} = 1 - \frac{C}{P}$$
      <p>
        Since \(P = C(1 + M)\) (where \(M\) is expressed as a decimal):
      </p>
      $$G = 1 - \frac{C}{C(1 + M)} = 1 - \frac{1}{1 + M} = \frac{(1 + M) - 1}{1 + M} = \frac{M}{1 + M}$$
      <p>
        Multiplying by 100 yields the canonical formula converting Markup Percentage to Gross Margin:
      </p>
      $$G\% = \frac{M\%}{100 + M\%} \times 100\%$$
      <p>
        Solving conversely for Markup in terms of Margin:
      </p>
      $$M\% = \frac{G\%}{100 - G\%} \times 100\%$$
      <p>
        This relationship demonstrates why markup is always strictly greater than margin for any positive profit: as margin approaches 100%, markup approaches infinity.
      </p>

      <h3>Pricing From a Desired Gross Profit Margin</h3>
      <p>
        A frequent corporate planning failure occurs when a business manager mandates a 40% profit margin and mistakenly applies a 40% markup to inventory cost. If an item costs $60 and a 40% markup is added, the selling price becomes \(\$60 \times 1.40 = \$84\). However, the realized margin is only \(\frac{\$84 - \$60}{\$84} = \frac{\$24}{\$84} \approx 28.57\%\)—a severe 11.43 percentage-point deficit below target.
      </p>
      <p>
        To achieve an authentic 40% gross profit margin, the pricing calculation must be inverted to account for revenue as the base:
      </p>
      $$P = \frac{C}{1 - \frac{G\%}{100}} = \frac{\$60}{1 - 0.40} = \frac{\$60}{0.60} = \$100.00$$
      <p>
        At $100.00, the profit is $40.00, yielding exactly \(\frac{\$40}{\$100} = 40.00\%\) gross margin, requiring a necessary markup of \(\frac{\$40}{\$60} = 66.67\%\).
      </p>

      <h2>Markup to Gross Margin Equivalence Reference Table</h2>
      <p>
        The table below provides direct conversions across standard commercial pricing benchmarks, detailing the requisite retail price multiplier (\(k = P / C\)), dollar profit on a $100 base cost, and the equivalent gross profit margin.
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Markup % (\(M\))</th>
            <th>Gross Margin % (\(G\))</th>
            <th>Revenue Multiplier (\(k\))</th>
            <th>Price for $100 Cost</th>
            <th>Dollar Profit (\(\Pi\))</th>
            <th>Standard Commercial Context</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>10.0%</td>
            <td>9.09%</td>
            <td>1.10x</td>
            <td>$110.00</td>
            <td>$10.00</td>
            <td>High-turnover wholesale commodities, bulk grains</td>
          </tr>
          <tr>
            <td>15.0%</td>
            <td>13.04%</td>
            <td>1.15x</td>
            <td>$115.00</td>
            <td>$15.00</td>
            <td>Consumer electronics hardware, major appliances</td>
          </tr>
          <tr>
            <td>25.0%</td>
            <td>20.00%</td>
            <td>1.25x</td>
            <td>$125.00</td>
            <td>$25.00</td>
            <td>Supermarket packaged goods, automotive parts</td>
          </tr>
          <tr>
            <td>33.33%</td>
            <td>25.00%</td>
            <td>1.33x</td>
            <td>$133.33</td>
            <td>$33.33</td>
            <td>Hardware retail, construction supplies</td>
          </tr>
          <tr>
            <td>50.0%</td>
            <td>33.33%</td>
            <td>1.50x</td>
            <td>$150.00</td>
            <td>$50.00</td>
            <td>Book publishing, specialty sporting goods</td>
          </tr>
          <tr>
            <td>66.67%</td>
            <td>40.00%</td>
            <td>1.67x</td>
            <td>$166.67</td>
            <td>$66.67</td>
            <td>Furniture manufacturing, specialty apparel wholesale</td>
          </tr>
          <tr>
            <td>100.0%</td>
            <td>50.00%</td>
            <td>2.00x</td>
            <td>$200.00</td>
            <td>$100.00</td>
            <td><strong>Keystone Retail:</strong> Traditional department store standard</td>
          </tr>
          <tr>
            <td>150.0%</td>
            <td>60.00%</td>
            <td>2.50x</td>
            <td>$250.00</td>
            <td>$150.00</td>
            <td>Boutique fashion, luxury footwear, giftware</td>
          </tr>
          <tr>
            <td>200.0%</td>
            <td>66.67%</td>
            <td>3.00x</td>
            <td>$300.00</td>
            <td>$200.00</td>
            <td>Commercial dining / restaurant food beverage cost</td>
          </tr>
          <tr>
            <td>300.0%</td>
            <td>75.00%</td>
            <td>4.00x</td>
            <td>$400.00</td>
            <td>$300.00</td>
            <td>Cocktails &amp; bar service, prescription eyewear frames</td>
          </tr>
          <tr>
            <td>400.0%</td>
            <td>80.00%</td>
            <td>5.00x</td>
            <td>$500.00</td>
            <td>$400.00</td>
            <td>Cosmetics, perfume, branded designer accessories</td>
          </tr>
          <tr>
            <td>900.0%</td>
            <td>90.00%</td>
            <td>10.00x</td>
            <td>$1,000.00</td>
            <td>$900.00</td>
            <td>Enterprise SaaS software licenses, high luxury jewelry</td>
          </tr>
        </tbody>
      </table>

      <h2>Cross-Industry Gross Margin Benchmarks</h2>
      <p>
        Healthy markup targets vary dramatically by industrial sector due to disparities in working capital velocity, inventory shelf life, physical storage overhead, spoilage risks, and customer acquisition costs (CAC).
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Industry Sector</th>
            <th>Typical Markup %</th>
            <th>Typical Gross Margin %</th>
            <th>Primary Cost Drivers Absorbed by Markup</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Grocery &amp; Supermarkets</td>
            <td>15% &ndash; 30%</td>
            <td>13% &ndash; 23%</td>
            <td>Perishability, refrigeration electricity, high volume scanning</td>
          </tr>
          <tr>
            <td>Consumer Electronics</td>
            <td>12% &ndash; 28%</td>
            <td>11% &ndash; 22%</td>
            <td>Rapid technological obsolescence, warranty reserves, return fraud</td>
          </tr>
          <tr>
            <td>Apparel &amp; Footwear</td>
            <td>100% &ndash; 250%</td>
            <td>50% &ndash; 71%</td>
            <td>Seasonal markdowns (unsold inventory clearance), showroom rent</td>
          </tr>
          <tr>
            <td>Restaurants &amp; Hospitality</td>
            <td>200% &ndash; 350%</td>
            <td>67% &ndash; 78%</td>
            <td>Food preparation labor, plate waste, commercial kitchen lease</td>
          </tr>
          <tr>
            <td>Pharmaceuticals (Branded)</td>
            <td>300% &ndash; 1200%</td>
            <td>75% &ndash; 92%</td>
            <td>Clinical trial R&amp;D amortization, FDA compliance, patent life</td>
          </tr>
          <tr>
            <td>Jewelry &amp; Watches</td>
            <td>100% &ndash; 300%</td>
            <td>50% &ndash; 75%</td>
            <td>Low inventory turnover, armed security, display insurance</td>
          </tr>
        </tbody>
      </table>

      <h2>Practical Real-World Business Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Specialty Coffee Roastery (Wholesale vs. Retail Packaging)</h3>
        <p><strong>Scenario:</strong> An artisan roastery imports green specialty coffee beans at $4.20 per pound. After shrinkage (18% weight loss during roasting), foil packaging, nitrogen flushing, and labor, the total unit cost per 12 oz (340 g) finished bag is $5.40.</p>
        <p><strong>Objective:</strong> Establish two pricing tiers: (A) Wholesale accounts requiring a 35% gross profit margin, and (B) Direct-to-consumer (DTC) e-commerce requiring a 65% gross profit margin.</p>
        <div class="step-solution">
          <p><strong>Wholesale Pricing Calculation:</strong></p>
          $$P_{\text{wholesale}} = \frac{C}{1 - G_{\text{wholesale}}} = \frac{\$5.40}{1 - 0.35} = \frac{\$5.40}{0.65} = \$8.31$$
          <p>Wholesale Markup: \(\frac{\$8.31 - \$5.40}{\$5.40} \times 100\% = 53.89\%\). The roaster bills cafes $8.30/bag, generating $2.90 profit per unit.</p>
          <p><strong>Retail DTC Pricing Calculation:</strong></p>
          $$P_{\text{retail}} = \frac{C}{1 - G_{\text{retail}}} = \frac{\$5.40}{1 - 0.65} = \frac{\$5.40}{0.35} = \$15.43$$
          <p>Retail Markup: \(\frac{\$15.43 - \$5.40}{\$5.40} \times 100\% = 185.74\%\). Rounding to standard psychological pricing ($15.50), the company secures a 65.16% gross margin ($10.10 gross profit), sufficient to absorb digital marketing ad spend (Meta/Google CAC).</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Keystone Pricing in Specialty Boutique Apparel</h3>
        <p><strong>Scenario:</strong> A fashion designer manufactures organic cotton jackets at a total landed cost of $45.00 per unit (fabric, assembly, shipping). The designer sells the jackets to independent boutiques, and the boutiques sell to retail consumers.</p>
        <p><strong>Objective:</strong> Determine wholesale price and manufacturer's suggested retail price (MSRP) using traditional two-stage keystone pricing.</p>
        <div class="step-solution">
          <p><strong>Stage 1 (Wholesale Sale):</strong> Designer applies keystone (100% markup / 50% margin) to landed cost:</p>
          $$P_{\text{wholesale}} = C \times (1 + 1.00) = \$45.00 \times 2.0 = \$90.00$$
          <p>Designer's gross profit is $45.00 per unit (50% gross margin).</p>
          <p><strong>Stage 2 (Retail Boutique Sale):</strong> Boutique purchases at $90.00 wholesale and applies retail keystone (100% markup / 50% margin):</p>
          $$P_{\text{MSRP}} = P_{\text{wholesale}} \times (1 + 1.00) = \$90.00 \times 2.0 = \$180.00$$
          <p>Boutique's gross profit is $90.00 per unit (50% gross margin). Total multiplier from landed production cost to final consumer MSRP is \(\frac{\$180}{\$45} = 4.0\times\) (a 300% cumulative markup).</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Contractor Bid Markups and Labor Burden Absorption</h3>
        <p><strong>Scenario:</strong> An electrical contractor bids a commercial retrofitting project. Estimated direct material cost is $18,500 and direct electrician labor is $14,000 (total direct cost \(C = \$32,500\)). The contractor's fixed overhead (trucks, insurance, licenses, estimators) is 18% of revenue, and the ownership targets an 8% net bottom-line profit.</p>
        <p><strong>Objective:</strong> Determine the required markup percentage to ensure that the target operating and net margins are preserved.</p>
        <div class="step-solution">
          <p>Target gross margin must absorb fixed overhead plus net profit: \(G = 18\% + 8\% = 26\%\).</p>
          <p>Contractor computes required project bid price:</p>
          $$P_{\text{bid}} = \frac{C}{1 - G} = \frac{\$32,500}{1 - 0.26} = \frac{\$32,500}{0.74} = \$43,918.92$$
          <p>To communicate this to project estimators via markup on direct job costs:</p>
          $$M = \frac{G}{1 - G} = \frac{0.26}{0.74} = 35.135\%$$
          <p>If the estimator had mistakenly marked up direct costs by 26% (\(\$32,500 \times 1.26 = \$40,950\)), total revenue would have fallen short by $2,968.92, completely wiping out the contractor's entire projected net profit!</p>
        </div>
      </div>

      <h2>Critical Pricing Pitfalls to Avoid in Business Operations</h2>
      <ul>
        <li><strong>Confusing Markup with Margin in Budgeting:</strong> Applying a markup percentage equal to a target margin will always result in underpricing and profit shortfalls. Remember: a 50% markup yields only a 33.3% margin; an 80% markup yields only a 44.4% margin.</li>
        <li><strong>Failing to Account for Landed Costs in COGS:</strong> Marking up factory gate invoice price without including inbound ocean/air freight, customs tariffs, port drayage, and insurance creates artificial paper profits that disappear upon financial reconciliation.</li>
        <li><strong>Overlooking Promotional Markdowns:</strong> If inventory requires an end-of-season 25% discount to clear remaining stock, starting with a 30% gross margin leaves virtually zero profit on discounted units. Initial markup (IMU) must be calculated high enough to preserve maintained markup (MMU) after allowances and shrink.</li>
        <li><strong>Ignoring Price Elasticity of Demand:</strong> High markups maximize gross margin percentage, but if customer demand drops disproportionately (high price elasticity), total gross profit dollars (\(Q \times \Pi\)) will decline. Optimization requires balancing unit profit with total sales volume.</li>
      </ul>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary class="faq-question">What is the formula to convert markup percentage to gross profit margin?</summary>
          <div class="faq-answer">
            <p>To convert markup percentage (\(M\)) to gross margin (\(G\)), divide the markup percentage by 100 plus the markup percentage, then multiply by 100: \(G = [M / (100 + M)] \times 100\). For example, a 75% markup converts to: \(75 / (100 + 75) = 75 / 175 \approx 42.86\%\) margin.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">Why is markup percentage always higher than profit margin percentage?</summary>
          <div class="faq-answer">
            <p>Markup is calculated using cost price as the denominator, while profit margin is calculated using selling price (revenue) as the denominator. Since the selling price is larger than the cost price (for any profitable transaction), dividing the identical dollar profit by the smaller cost number yields a mathematically higher percentage than dividing by the larger selling price.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What markup percentage is needed to achieve a 50% gross margin?</summary>
          <div class="faq-answer">
            <p>A 100% markup is required to achieve a 50% gross margin. This is known as keystone pricing: if cost is $50 and you add a 100% markup ($50), the selling price is $100. Profit is $50, which is exactly 50% of the $100 selling price.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How do you calculate initial markup (IMU) in retail merchandising?</summary>
          <div class="faq-answer">
            <p>Initial Markup (IMU %) accounts for planned reductions such as markdowns, employee discounts, and inventory shrinkage (theft/loss). The retail formula is: \(\text{IMU}\% = \frac{\text{Operating Expenses} + \text{Desired Profit} + \text{Reductions}}{\text{Net Sales} + \text{Reductions}} \times 100\). This ensures that after seasonal clearance sales occur, the maintained margin still meets the corporate profit goal.</p>
          </div>
        </details>
      </div>

      <!-- Cross-Disciplinary Internal Links -->
      <div class="related-calculators" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
        <h3>Related Financial &amp; Mathematics Calculators</h3>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; list-style: none; padding: 0;">
          <li><a href="percentage-change-calculator.html">&rarr; Percentage Change Calculator</a></li>
          <li><a href="sales-tax-calculator.html">&rarr; Sales Tax Calculator</a></li>
          <li><a href="discount-calculator.html">&rarr; Discount Calculator</a></li>
          <li><a href="roi-calculator.html">&rarr; Return on Investment (ROI) Solver</a></li>
          <li><a href="proportion-calculator.html">&rarr; Proportion Calculator</a></li>
          <li><a href="average-calculator.html">&rarr; Average Calculator</a></li>
        </ul>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, statistical, and engineering calculation tools.</p>
      </div>
      <div class="footer-col">
        <h4>Discipline Hubs</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    function switchMarkupMode() {
      var mode = document.getElementById('markup-mode').value;
      var lbl = document.getElementById('lbl-param2');
      var inp = document.getElementById('inp-param2');

      if (mode === 'cost-markup') {
        lbl.innerText = "Markup Percentage (%)";
        inp.value = "60.00";
      } else if (mode === 'cost-margin') {
        lbl.innerText = "Desired Gross Margin (%)";
        inp.value = "37.50";
      } else if (mode === 'cost-price') {
        lbl.innerText = "Retail Selling Price ($)";
        inp.value = "80.00";
      }
      calculateMarkup();
    }

    function calculateMarkup() {
      var mode = document.getElementById('markup-mode').value;
      var cost = parseFloat(document.getElementById('inp-cost').value);
      var param2 = parseFloat(document.getElementById('inp-param2').value);
      var sym = document.getElementById('currency-sym').value;
      var prec = parseInt(document.getElementById('prec-digits').value, 10);

      if (isNaN(cost) || isNaN(param2) || cost < 0) {
        showError("Please enter valid, non-negative numbers for cost and parameters.");
        return;
      }

      var price = 0, profit = 0, markupPct = 0, marginPct = 0;
      var steps = "";

      if (mode === 'cost-markup') {
        markupPct = param2;
        price = cost * (1 + markupPct / 100);
        profit = price - cost;
        marginPct = (price > 0) ? (profit / price) * 100 : 0;

        steps = "Mode: Given Cost and Markup Percentage\n" +
                "Cost C = " + sym + cost.toFixed(prec) + ", Markup M = " + markupPct.toFixed(2) + "%\n\n" +
                "1. Selling Price: P = C * (1 + M / 100)\n" +
                "   P = " + cost.toFixed(prec) + " * (1 + " + (markupPct / 100).toFixed(4) + ") = " + sym + price.toFixed(prec) + "\n\n" +
                "2. Dollar Profit: Π = P - C\n" +
                "   Π = " + price.toFixed(prec) + " - " + cost.toFixed(prec) + " = " + sym + profit.toFixed(prec) + "\n\n" +
                "3. Gross Profit Margin: G = (Π / P) * 100\n" +
                "   G = (" + profit.toFixed(prec) + " / " + price.toFixed(prec) + ") * 100 = " + marginPct.toFixed(2) + "%\n\n" +
                "4. Revenue Multiplier: k = P / C = " + (cost > 0 ? (price / cost).toFixed(3) : "N/A") + "x";

      } else if (mode === 'cost-margin') {
        marginPct = param2;
        if (marginPct >= 100) {
          showError("Gross profit margin cannot be 100% or greater for positive cost.");
          return;
        }
        price = cost / (1 - marginPct / 100);
        profit = price - cost;
        markupPct = (cost > 0) ? (profit / cost) * 100 : 0;

        steps = "Mode: Given Cost and Desired Gross Margin\n" +
                "Cost C = " + sym + cost.toFixed(prec) + ", Target Margin G = " + marginPct.toFixed(2) + "%\n\n" +
                "1. Selling Price: P = C / (1 - G / 100)\n" +
                "   P = " + cost.toFixed(prec) + " / (1 - " + (marginPct / 100).toFixed(4) + ") = " + sym + price.toFixed(prec) + "\n\n" +
                "2. Dollar Profit: Π = P - C\n" +
                "   Π = " + price.toFixed(prec) + " - " + cost.toFixed(prec) + " = " + sym + profit.toFixed(prec) + "\n\n" +
                "3. Required Markup: M = (Π / C) * 100 = [G / (100 - G)] * 100\n" +
                "   M = (" + profit.toFixed(prec) + " / " + cost.toFixed(prec) + ") * 100 = " + markupPct.toFixed(2) + "%\n\n" +
                "4. Revenue Multiplier: k = P / C = " + (cost > 0 ? (price / cost).toFixed(3) : "N/A") + "x";

      } else if (mode === 'cost-price') {
        price = param2;
        profit = price - cost;
        markupPct = (cost > 0) ? (profit / cost) * 100 : 0;
        marginPct = (price > 0) ? (profit / price) * 100 : 0;

        steps = "Mode: Given Cost and Retail Selling Price\n" +
                "Cost C = " + sym + cost.toFixed(prec) + ", Retail Price P = " + sym + price.toFixed(prec) + "\n\n" +
                "1. Dollar Profit: Π = P - C\n" +
                "   Π = " + price.toFixed(prec) + " - " + cost.toFixed(prec) + " = " + sym + profit.toFixed(prec) + "\n\n" +
                "2. Markup Percentage: M = (Π / C) * 100\n" +
                "   M = (" + profit.toFixed(prec) + " / " + cost.toFixed(prec) + ") * 100 = " + markupPct.toFixed(2) + "%\n\n" +
                "3. Gross Profit Margin: G = (Π / P) * 100\n" +
                "   G = (" + profit.toFixed(prec) + " / " + price.toFixed(prec) + ") * 100 = " + marginPct.toFixed(2) + "%\n\n" +
                "4. Revenue Multiplier: k = P / C = " + (cost > 0 ? (price / cost).toFixed(3) : "N/A") + "x";
      }

      var mult = (cost > 0) ? (price / cost).toFixed(2) : "0.00";

      document.getElementById('res-price').innerText = sym + price.toFixed(prec);
      document.getElementById('res-multiplier').innerText = "Multiplier: " + mult + "x Cost";
      document.getElementById('res-profit').innerText = sym + profit.toFixed(prec);
      document.getElementById('res-margin').innerText = marginPct.toFixed(2) + "%";
      document.getElementById('res-markup').innerText = markupPct.toFixed(2) + "%";
      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-price').innerText = "Error";
      document.getElementById('res-multiplier').innerText = "Invalid inputs";
      document.getElementById('res-profit').innerText = "N/A";
      document.getElementById('res-margin').innerText = "N/A";
      document.getElementById('res-markup').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetMarkup() {
      document.getElementById('markup-mode').value = 'cost-markup';
      document.getElementById('inp-cost').value = '50.00';
      document.getElementById('lbl-param2').innerText = "Markup Percentage (%)";
      document.getElementById('inp-param2').value = '60.00';
      document.getElementById('currency-sym').value = '$';
      document.getElementById('prec-digits').value = '2';
      calculateMarkup();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateMarkup();
    });
  </script>
</body>
</html>
"""

# 6. density-calculator.html
HTML_DENSITY = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Density Calculator - Mass, Volume, Specific Gravity &amp; Buoyancy</title>
  <meta name="description" content="Calculate density (ρ = m/V), mass, or volume with unit conversions. Computes specific gravity, buoyancy status, and API gravity with step-by-step physics formulas.">
  <link rel="canonical" href="https://calchub.org/density-calculator.html">
  <meta property="og:title" content="Density Calculator - Volumetric Mass Density Solver">
  <meta property="og:description" content="Free multi-unit physics density calculator. Solve for density, mass, or volume. Calculate specific gravity and buoyant force with full step-by-step mathematical proofs.">
  <meta property="og:url" content="https://calchub.org/density-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Density Calculator - Physics &amp; Materials Solver">
  <meta name="twitter:description" content="Calculate mass density ρ = m/V with material presets, specific gravity, and multi-unit conversions (kg/m³, g/cm³, lb/ft³, lb/gal).">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Density Calculator",
    "url": "https://calchub.org/density-calculator.html",
    "description": "Calculates material density, mass, volume, specific gravity, and buoyancy status across engineering and physics units.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All"
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the formula for calculating density?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The fundamental formula for volumetric mass density is rho = m / V, where rho is density, m is mass, and V is volume. In the International System of Units (SI), density is measured in kilograms per cubic meter (kg/m^3)."
        }
      },
      {
        "@type": "Question",
        "name": "What is specific gravity and how does it relate to density?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Specific gravity (SG), or relative density, is a dimensionless ratio comparing the density of a substance to that of a reference fluid (typically pure liquid water at 4 degrees Celsius, where water density is 1000 kg/m^3 or 1 g/cm^3). If SG < 1, the substance floats in water; if SG > 1, it sinks."
        }
      },
      {
        "@type": "Question",
        "name": "How does temperature affect the density of liquids and gases?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "As temperature increases, thermal kinetic energy causes substances to expand, increasing their volume and consequently decreasing their density. In gases, density is directly proportional to pressure and inversely proportional to absolute temperature per the ideal gas law: rho = P*M / (R*T)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the conversion between g/cm³ and kg/m³?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "One gram per cubic centimeter (1 g/cm^3) equals exactly 1,000 kilograms per cubic meter (1,000 kg/m^3). To convert g/cm^3 to kg/m^3, multiply by 1,000; to convert kg/m^3 to g/cm^3, divide by 1,000."
        }
      }
    ]
  }
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-container">
      <a href="index.html" class="site-logo">CalcHub</a>
      <nav class="site-nav">
        <a href="index.html">Home</a>
        <a href="math.html">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html" class="active">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="calculator-container">
    <div class="calculator-header">
      <div class="calc-icon" aria-hidden="true">&#9878;</div>
      <h1>Density Calculator</h1>
      <p class="calc-description">Solve for mass density (\(\rho = m/V\)), mass, or volume with material presets, specific gravity, and multi-unit conversions.</p>
    </div>

    <div class="calculator-body">
      <div class="input-grid">
        <div class="input-group">
          <label for="solve-target">Variable to Calculate</label>
          <select id="solve-target" class="form-control" onchange="switchDensityMode()">
            <option value="density" selected>Density (\(\rho = m / V\))</option>
            <option value="mass">Mass (\(m = \rho \times V\))</option>
            <option value="volume">Volume (\(V = m / \rho\))</option>
          </select>
        </div>

        <div class="input-group">
          <label for="preset-material">Load Standard Material Preset</label>
          <select id="preset-material" class="form-control" onchange="loadMaterialPreset()">
            <option value="custom" selected>-- Custom User Values --</option>
            <option value="1000">Water (Fresh, 4°C) &ndash; 1,000 kg/m³</option>
            <option value="1025">Seawater &ndash; 1,025 kg/m³</option>
            <option value="789">Ethanol (Pure) &ndash; 789 kg/m³</option>
            <option value="13546">Mercury (Liquid) &ndash; 13,546 kg/m³</option>
            <option value="1.225">Air (Sea Level, 15°C) &ndash; 1.225 kg/m³</option>
            <option value="2700">Aluminum &ndash; 2,700 kg/m³</option>
            <option value="7850">Steel / Iron &ndash; 7,850 kg/m³</option>
            <option value="8960">Copper &ndash; 8,960 kg/m³</option>
            <option value="19320">Gold &ndash; 19,320 kg/m³</option>
            <option value="2400">Concrete &ndash; 2,400 kg/m³</option>
            <option value="750">Oak Wood (Seasoned) &ndash; 750 kg/m³</option>
          </select>
        </div>
      </div>

      <!-- Inputs Grid -->
      <div class="input-grid">
        <!-- Mass Group -->
        <div class="input-group" id="grp-mass">
          <label for="inp-mass">Mass (\(m\))</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="number" id="inp-mass" class="form-control" value="2500" step="any" min="0" style="flex: 2;">
            <select id="unit-mass" class="form-control" style="flex: 1;" onchange="calculateDensity()">
              <option value="kg" selected>kg</option>
              <option value="g">g</option>
              <option value="mg">mg</option>
              <option value="lb">lb</option>
              <option value="oz">oz</option>
              <option value="t">metric ton</option>
            </select>
          </div>
        </div>

        <!-- Volume Group -->
        <div class="input-group" id="grp-volume">
          <label for="inp-volume">Volume (\(V\))</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="number" id="inp-volume" class="form-control" value="0.3185" step="any" min="0" style="flex: 2;">
            <select id="unit-volume" class="form-control" style="flex: 1;" onchange="calculateDensity()">
              <option value="m3" selected>m³</option>
              <option value="cm3">cm³</option>
              <option value="L">L</option>
              <option value="mL">mL</option>
              <option value="ft3">ft³</option>
              <option value="in3">in³</option>
              <option value="gal">gal (US)</option>
            </select>
          </div>
        </div>

        <!-- Density Group -->
        <div class="input-group" id="grp-density" style="display: none;">
          <label for="inp-density">Density (\(\rho\))</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="number" id="inp-density" class="form-control" value="7850" step="any" min="0" style="flex: 2;">
            <select id="unit-density" class="form-control" style="flex: 1;" onchange="calculateDensity()">
              <option value="kg_m3" selected>kg/m³</option>
              <option value="g_cm3">g/cm³</option>
              <option value="lb_ft3">lb/ft³</option>
              <option value="lb_gal">lb/gal (US)</option>
            </select>
          </div>
        </div>
      </div>

      <div class="btn-group">
        <button type="button" class="btn btn-primary" onclick="calculateDensity()">Compute Physics Properties</button>
        <button type="button" class="btn btn-secondary" onclick="resetDensity()">Reset Defaults</button>
      </div>

      <!-- Results Display Grid -->
      <div class="results-grid" style="margin-top: 1.5rem;">
        <div class="result-card primary-result">
          <div class="result-label" id="res-primary-label">Material Density (\(\rho\))</div>
          <div class="result-value" id="res-primary-val">7,849.29 kg/m³</div>
          <div class="result-subtext" id="res-primary-sub">7.849 g/cm³ &bull; 489.99 lb/ft³</div>
        </div>

        <div class="result-card">
          <div class="result-label">Specific Gravity (\(SG\))</div>
          <div class="result-value" id="res-sg">7.85</div>
          <div class="result-subtext">Relative to pure water at 4°C</div>
        </div>

        <div class="result-card">
          <div class="result-label">Freshwater Buoyancy</div>
          <div class="result-value" id="res-buoyancy" style="color: #dc3545;">Sinks</div>
          <div class="result-subtext">Archimedes immersion status</div>
        </div>

        <div class="result-card">
          <div class="result-label">API Gravity (Petroleum)</div>
          <div class="result-value" id="res-api">-113.5° API</div>
          <div class="result-subtext">Hydrometer scale for liquids</div>
        </div>
      </div>

      <!-- Equivalent Units Conversion Table Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Equivalent Multi-System Densities</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem; margin-top: 0.5rem;">
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">SI Metric (kg/m³)</div>
            <strong id="eq-kgm3">7,849.29 kg/m³</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">CGS Metric (g/cm³ or g/mL)</div>
            <strong id="eq-gcm3">7.849 g/cm³</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Imperial / US (lb/ft³)</div>
            <strong id="eq-lbft3">489.99 lb/ft³</strong>
          </div>
          <div style="background: var(--bg-primary, #fff); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color, #e9ecef);">
            <div style="font-size: 0.8rem; color: var(--text-muted, #6c757d);">Liquid US (lb/gal)</div>
            <strong id="eq-lbgal">65.50 lb/gal</strong>
          </div>
        </div>
      </div>

      <!-- Step-by-step Math Breakdown Card -->
      <div class="info-card" style="margin-top: 1.5rem;">
        <h3>Step-by-Step Physics &amp; Dimensional Analysis</h3>
        <pre id="res-steps" style="white-space: pre-wrap; font-family: monospace; background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; color: var(--text-primary, #212529);"></pre>
      </div>
    </div>

    <!-- Article Content: 1000+ Words Physics & Materials Engineering Guide -->
    <article class="article-body">
      <h2>The Physics of Volumetric Mass Density in Mechanics and Materials Science</h2>
      <p>
        In classical mechanics, continuum thermodynamics, and materials engineering, <strong>density</strong> (\(\rho\), the Greek letter rho) is an intrinsic scalar property that quantifies the amount of mass packed into a given unit of three-dimensional space. Unlike extrinsic physical quantities such as mass or volume—which scale proportionally with the overall quantity of matter present—density is an intensive property characteristic of the substance itself under specified conditions of temperature and ambient pressure.
      </p>
      <p>
        Understanding and precisely calculating density is paramount across foundational disciplines: naval architects rely on it to ensure vessel buoyancy and transverse stability; aerospace engineers optimize structural density to maximize payload-to-weight ratios; civil engineers compute geotechnical soil compaction densities to prevent structural foundation subsidence; and chemical engineers utilize density differentials in fractional distillation columns and centrifugal separators.
      </p>

      <h2>Governing Mathematical Equations and Dimensional Analysis</h2>
      <p>
        The definitive equation defining volumetric mass density is the ratio of mass to volume:
      </p>
      $$\rho = \frac{m}{V}$$
      <p>
        Where:
      </p>
      <ul>
        <li>\(\rho\) is the mass density, having fundamental physical dimensions of \([M L^{-3}]\). In the International System of Units (SI), the coherent derived unit is the kilogram per cubic meter (\(\text{kg/m}^3\)).</li>
        <li>\(m\) is the total mass of the object or fluid sample, measured in kilograms (\(\text{kg}\)).</li>
        <li>\(V\) is the net three-dimensional geometric volume occupied by that mass, measured in cubic meters (\(\text{m}^3\)).</li>
      </ul>

      <h3>Algebraic Rearrangements for Mass and Volume</h3>
      <p>
        Depending on the experimental or engineering parameters known, the governing relation is algebraically inverted:
      </p>
      <p><strong>Solving for Mass:</strong> When the material density and geometric boundaries are specified, total mass is computed directly via volumetric integration:</p>
      $$m = \rho \times V$$
      <p><strong>Solving for Volume:</strong> When a given mass of material must be stored, packaged, or displaced:</p>
      $$V = \frac{m}{\rho}$$

      <h3>Specific Gravity (Relative Density)</h3>
      <p>
        <strong>Specific Gravity (\(SG\))</strong>, or relative density, is a dimensionless ratio comparing the density of an investigated material to the density of a benchmark reference fluid at a strictly defined temperature and pressure:
      </p>
      $$SG = \frac{\rho_{\text{substance}}}{\rho_{\text{reference}}}$$
      <p>
        For solids and liquids, the standard international reference is pure, air-free liquid water at its point of maximum density (\(3.98^\circ\text{C} \approx 4^\circ\text{C}\)) under 1 standard atmosphere (\(101.325\text{ kPa}\)), where:
      </p>
      $$\rho_{\text{water, } 4^\circ\text{C}} = 1,000.00\text{ kg/m}^3 = 1.000\text{ g/cm}^3$$
      <p>
        For gases, the reference standard is clean, dry atmospheric air at standard temperature and pressure (STP, \(0^\circ\text{C}\) and \(1\text{ atm}\)), where \(\rho_{\text{air}} \approx 1.293\text{ kg/m}^3\).
      </p>

      <h3>Archimedes' Principle and Hydrostatic Buoyancy</h3>
      <p>
        The hydrostatic equilibrium of an object immersed in a fluid is dictated by Archimedes' principle, formulated in 246 BCE: any physical body partially or wholly submerged in a fluid is buoyed up by a net vertical force equal to the gravitational weight of the fluid displaced:
      </p>
      $$F_b = \rho_{\text{fluid}} \times V_{\text{submerged}} \times g$$
      <p>
        Where \(g\) is standard gravitational acceleration (\(9.80665\text{ m/s}^2\)). An object placed in a fluid will behave according to its relative density:
      </p>
      <ul>
        <li><strong>\(\rho_{\text{object}} &lt; \rho_{\text{fluid}}\) (\(SG &lt; 1\)):</strong> Positive net buoyancy. The object ascends to the surface and floats in equilibrium with submerged volume fraction \(f = \frac{V_{\text{sub}}}{V_{\text{total}}} = \frac{\rho_{\text{obj}}}{\rho_{\text{fluid}}} = SG\).</li>
        <li><strong>\(\rho_{\text{object}} &gt; \rho_{\text{fluid}}\) (\(SG &gt; 1\)):</strong> Negative net buoyancy. The gravitational weight exceeds the maximum buoyant force, causing the object to sink to the floor of the fluid reservoir.</li>
        <li><strong>\(\rho_{\text{object}} = \rho_{\text{fluid}}\) (\(SG = 1\)):</strong> Neutral buoyancy. The object remains suspended at its current depth without ascending or descending.</li>
      </ul>

      <h3>Petroleum API Gravity</h3>
      <p>
        In the global oil and energy industry, petroleum hydrometer measurements are quantified using the American Petroleum Institute (API) gravity scale, defined inversely relative to water specific gravity at \(60^\circ\text{F}\) (\(15.56^\circ\text{C}\)):
      </p>
      $$^{\circ}\text{API} = \frac{141.5}{SG} - 131.5$$
      <p>
        Crude oils with \(^{\circ}\text{API} &gt; 31.1^\circ\) are classified as "Light" (floating easily on water and yielding higher gasoline fractions), while crude with \(^{\circ}\text{API} &lt; 22.3^\circ\) is designated as "Heavy". Pure water at \(60^\circ\text{F}\) has \(SG = 1.00\), corresponding to exactly \(10.0^\circ\text{ API}\).
      </p>

      <h2>Material Densities Reference Table across Physical States</h2>
      <p>
        The table below catalogs benchmark mass densities for elemental metals, structural engineering alloys, common liquids, building materials, and atmospheric gases at standard ambient temperature and pressure (\(20^\circ\text{C}\) and \(1\text{ atm}\)).
      </p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Material / Substance</th>
            <th>State</th>
            <th>Density (\(\text{kg/m}^3\))</th>
            <th>Density (\(\text{g/cm}^3\))</th>
            <th>Density (\(\text{lb/ft}^3\))</th>
            <th>Specific Gravity (\(SG\))</th>
            <th>Freshwater Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Hydrogen Gas (\(\text{H}_2\))</td>
            <td>Gas</td>
            <td>0.0899</td>
            <td>0.00009</td>
            <td>0.0056</td>
            <td>0.00009</td>
            <td>Ascends rapidly in air</td>
          </tr>
          <tr>
            <td>Helium (\(\text{He}\))</td>
            <td>Gas</td>
            <td>0.1785</td>
            <td>0.00018</td>
            <td>0.0111</td>
            <td>0.00018</td>
            <td>Ascends rapidly in air</td>
          </tr>
          <tr>
            <td>Dry Air (Sea Level, 20°C)</td>
            <td>Gas</td>
            <td>1.204</td>
            <td>0.00120</td>
            <td>0.0752</td>
            <td>0.00120</td>
            <td>Neutral in ambient air</td>
          </tr>
          <tr>
            <td>Carbon Dioxide (\(\text{CO}_2\))</td>
            <td>Gas</td>
            <td>1.977</td>
            <td>0.00198</td>
            <td>0.1234</td>
            <td>0.00198</td>
            <td>Sinks in ambient air</td>
          </tr>
          <tr>
            <td>Gasoline / Petrol (Octane)</td>
            <td>Liquid</td>
            <td>730 &ndash; 770</td>
            <td>0.73 &ndash; 0.77</td>
            <td>45.6 &ndash; 48.1</td>
            <td>0.73 &ndash; 0.77</td>
            <td>Floats on surface</td>
          </tr>
          <tr>
            <td>Pure Ethanol (20°C)</td>
            <td>Liquid</td>
            <td>789.2</td>
            <td>0.789</td>
            <td>49.27</td>
            <td>0.789</td>
            <td>Miscible / Floats</td>
          </tr>
          <tr>
            <td>Olive Oil</td>
            <td>Liquid</td>
            <td>915</td>
            <td>0.915</td>
            <td>57.12</td>
            <td>0.915</td>
            <td>Floats on surface</td>
          </tr>
          <tr>
            <td>Pure Water (4°C, Maximum)</td>
            <td>Liquid</td>
            <td>1,000.0</td>
            <td>1.000</td>
            <td>62.43</td>
            <td>1.000</td>
            <td>Neutral equilibrium</td>
          </tr>
          <tr>
            <td>Open Ocean Seawater (3.5% salinity)</td>
            <td>Liquid</td>
            <td>1,025.0</td>
            <td>1.025</td>
            <td>63.99</td>
            <td>1.025</td>
            <td>Sinks in fresh water</td>
          </tr>
          <tr>
            <td>Liquid Mercury (\(\text{Hg}\), 20°C)</td>
            <td>Liquid</td>
            <td>13,546.0</td>
            <td>13.546</td>
            <td>845.64</td>
            <td>13.546</td>
            <td>Sinks instantly</td>
          </tr>
          <tr>
            <td>Balsa Wood</td>
            <td>Solid</td>
            <td>130 &ndash; 160</td>
            <td>0.13 &ndash; 0.16</td>
            <td>8.1 &ndash; 10.0</td>
            <td>0.13 &ndash; 0.16</td>
            <td>High flotation reserve</td>
          </tr>
          <tr>
            <td>Seasoned White Oak Wood</td>
            <td>Solid</td>
            <td>750</td>
            <td>0.750</td>
            <td>46.82</td>
            <td>0.750</td>
            <td>Floats (75% submerged)</td>
          </tr>
          <tr>
            <td>Ice (\(\text{H}_2\text{O}\), 0°C)</td>
            <td>Solid</td>
            <td>917.0</td>
            <td>0.917</td>
            <td>57.25</td>
            <td>0.917</td>
            <td>Floats (91.7% submerged)</td>
          </tr>
          <tr>
            <td>Structural Concrete (Reinforced)</td>
            <td>Solid</td>
            <td>2,400.0</td>
            <td>2.400</td>
            <td>149.83</td>
            <td>2.400</td>
            <td>Sinks</td>
          </tr>
          <tr>
            <td>Aluminum Alloy (6061-T6)</td>
            <td>Solid</td>
            <td>2,700.0</td>
            <td>2.700</td>
            <td>168.55</td>
            <td>2.700</td>
            <td>Sinks</td>
          </tr>
          <tr>
            <td>Carbon Steel (AISI 1018)</td>
            <td>Solid</td>
            <td>7,850.0</td>
            <td>7.850</td>
            <td>490.06</td>
            <td>7.850</td>
            <td>Sinks</td>
          </tr>
          <tr>
            <td>Copper (Electrolytic Tough Pitch)</td>
            <td>Solid</td>
            <td>8,960.0</td>
            <td>8.960</td>
            <td>559.36</td>
            <td>8.960</td>
            <td>Sinks</td>
          </tr>
          <tr>
            <td>Lead (\(\text{Pb}\))</td>
            <td>Solid</td>
            <td>11,340.0</td>
            <td>11.340</td>
            <td>707.93</td>
            <td>11.340</td>
            <td>Sinks</td>
          </tr>
          <tr>
            <td>Gold (\(\text{Au}\))</td>
            <td>Solid</td>
            <td>19,320.0</td>
            <td>19.320</td>
            <td>1,206.11</td>
            <td>19.320</td>
            <td>Sinks</td>
          </tr>
          <tr>
            <td>Platinum (\(\text{Pt}\))</td>
            <td>Solid</td>
            <td>21,450.0</td>
            <td>21.450</td>
            <td>1,339.10</td>
            <td>21.450</td>
            <td>Sinks</td>
          </tr>
          <tr>
            <td>Osmium (\(\text{Os}\), Densest Element)</td>
            <td>Solid</td>
            <td>22,590.0</td>
            <td>22.590</td>
            <td>1,410.25</td>
            <td>22.590</td>
            <td>Sinks</td>
          </tr>
        </tbody>
      </table>

      <h2>Practical Real-World Engineering Case Studies</h2>

      <div class="worked-example-card">
        <h3>Case Study 1: Marine Engineering &ndash; Steel Cargo Barge Displacement</h3>
        <p><strong>Scenario:</strong> A commercial rectangular flat-bottom cargo barge has length \(L = 40.0\text{ m}\), width \(W = 10.0\text{ m}\), and total hull height \(H = 4.0\text{ m}\). The dry steel hull and machinery have an empty mass of \(m_{\text{empty}} = 320,000\text{ kg}\) (320 metric tons). The barge operates in seawater (\(\rho_{\text{sw}} = 1,025\text{ kg/m}^3\)).</p>
        <p><strong>Objective:</strong> Compute the lightship draft (submerged depth without cargo) and determine the maximum cargo capacity that leaves a minimum safety freeboard of \(1.0\text{ m}\) above the water line.</p>
        <div class="step-solution">
          <p><strong>1. Unloaded (Lightship) Submerged Draft:</strong></p>
          <p>Per Archimedes' principle, displaced water mass equals vessel mass: \(m_{\text{disp}} = \rho_{\text{sw}} \times V_{\text{sub}} = \rho_{\text{sw}} \times (L \times W \times d_{\text{light}})\):</p>
          $$d_{\text{light}} = \frac{m_{\text{empty}}}{\rho_{\text{sw}} \times L \times W} = \frac{320,000\text{ kg}}{1,025\text{ kg/m}^3 \times 40.0\text{ m} \times 10.0\text{ m}} = \frac{320,000}{410,000} \approx 0.7805\text{ m}$$
          <p>The empty barge sinks to a shallow draft of 78.05 cm.</p>
          <p><strong>2. Maximum Safe Cargo Capacity:</strong></p>
          <p>With a required safety freeboard of 1.0 m, maximum allowable draft is \(d_{\text{max}} = 4.0\text{ m} - 1.0\text{ m} = 3.0\text{ m}\):</p>
          $$V_{\text{sub, max}} = 40.0\text{ m} \times 10.0\text{ m} \times 3.0\text{ m} = 1,200\text{ m}^3$$
          $$m_{\text{total, max}} = \rho_{\text{sw}} \times V_{\text{sub, max}} = 1,025\text{ kg/m}^3 \times 1,200\text{ m}^3 = 1,230,000\text{ kg} \text{ (1,230 metric tons)}$$
          <p>Deducting the barge hull mass yields maximum safe payload:</p>
          $$m_{\text{cargo, max}} = 1,230,000\text{ kg} - 320,000\text{ kg} = 910,000\text{ kg} \text{ (910 metric tons)}$$
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Aerospace Materials Selection &ndash; Mass Optimization</h3>
        <p><strong>Scenario:</strong> An aerospace structural engineer is designing a solid wing-spar reinforcement flange that requires a net volume of \(V = 0.045\text{ m}^3\). The engineer is comparing standard aircraft-grade Aluminum 7075-T6 against Titanium Ti-6Al-4V (Grade 5).</p>
        <p><strong>Material Data:</strong> Aluminum 7075-T6 has density \(\rho_{\text{Al}} = 2,810\text{ kg/m}^3\) and yield strength \(\sigma_{y, \text{Al}} = 503\text{ MPa}\). Titanium Ti-6Al-4V has density \(\rho_{\text{Ti}} = 4,430\text{ kg/m}^3\) and yield strength \(\sigma_{y, \text{Ti}} = 880\text{ MPa}\).</p>
        <div class="step-solution">
          <p><strong>1. Direct Component Mass Comparison:</strong></p>
          $$m_{\text{Al}} = \rho_{\text{Al}} \times V = 2,810\text{ kg/m}^3 \times 0.045\text{ m}^3 = 126.45\text{ kg}$$
          $$m_{\text{Ti}} = \rho_{\text{Ti}} \times V = 4,430\text{ kg/m}^3 \times 0.045\text{ m}^3 = 199.35\text{ kg}$$
          <p>At constant volume, the titanium component is \(72.90\text{ kg}\) heavier (+57.6%).</p>
          <p><strong>2. Specific Strength Analysis (Strength-to-Weight Ratio):</strong></p>
          $$\text{Specific Strength}_{\text{Al}} = \frac{503\text{ MPa}}{2,810\text{ kg/m}^3} = 0.1790\text{ MPa}\cdot\text{m}^3/\text{kg}$$
          $$\text{Specific Strength}_{\text{Ti}} = \frac{880\text{ MPa}}{4,430\text{ kg/m}^3} = 0.1986\text{ MPa}\cdot\text{m}^3/\text{kg}$$
          <p>Because Titanium provides a higher specific strength (+10.95%), the structural engineer can redesign the flange with thinner structural walls (\(V_{\text{Ti, req}} = 0.045 \times \frac{503}{880} \approx 0.0257\text{ m}^3\)), achieving a lighter net component mass of \(m_{\text{redesigned}} = 4,430 \times 0.0257 \approx 113.85\text{ kg}\), saving 12.6 kg while meeting identical structural load safety margins!</p>
        </div>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Chemical Quality Control &ndash; Verifying Gold Purity via Water Displacement</h3>
        <p><strong>Scenario:</strong> A forensic metallurgist inspects a cast medallion claimed to be pure 24-karat gold (\(\rho_{\text{pure Au}} = 19,320\text{ kg/m}^3 = 19.32\text{ g/cm}^3\)). An analytical balance measures the dry mass of the medallion as \(m = 482.50\text{ g}\). When completely submerged in a graduated pycnometer cylinder filled with water, the fluid volume rises from \(120.00\text{ mL}\) to \(152.60\text{ mL}\).</p>
        <p><strong>Objective:</strong> Calculate the density of the medallion and detect counterfeit core composition.</p>
        <div class="step-solution">
          <p><strong>1. Submerged Volume Determination:</strong></p>
          $$V = V_{\text{final}} - V_{\text{initial}} = 152.60\text{ mL} - 120.00\text{ mL} = 32.60\text{ mL} = 32.60\text{ cm}^3$$
          <p><strong>2. Density Calculation:</strong></p>
          $$\rho_{\text{sample}} = \frac{m}{V} = \frac{482.50\text{ g}}{32.60\text{ cm}^3} \approx 14.801\text{ g/cm}^3 = 14,801\text{ kg/m}^3$$
          <p><strong>3. Forensic Determination:</strong></p>
          <p>The sample density of \(14.80\text{ g/cm}^3\) is 23.4% below pure gold (\(19.32\text{ g/cm}^3\)). By comparing against standard alloy models, the metallurgist determines the medallion is approximately 14-karat gold (58.3% gold alloyed with silver and copper, \(\rho \approx 13.1 - 14.5\text{ g/cm}^3\)) or a tungsten core clad in gold, definitively disproving the 24-karat purity claim!</p>
        </div>
      </div>

      <h2>Thermodynamic Influences: Temperature and Pressure Effects</h2>
      <p>
        Unlike mass, volumetric density is not strictly invariant; it fluctuates under changing thermodynamic conditions:
      </p>
      <ul>
        <li><strong>Thermal Expansion of Liquids and Solids:</strong> Supplying thermal energy increases atomic vibrational amplitude, expanding the crystal lattice or molecular spacing. For liquids, volumetric thermal expansion coefficient \(\beta\) dictates density at temperature \(T\):
        $$\rho(T) = \frac{\rho_0}{1 + \beta(T - T_0)}$$
        Anomalously, pure liquid water exhibits a density inversion between \(0^\circ\text{C}\) and \(3.98^\circ\text{C}\), where open tetrahedral hydrogen bonding clusters collapse into denser packing, reaching peak density of \(1,000.00\text{ kg/m}^3\) before traditional thermal expansion dominates above \(4^\circ\text{C}\).</li>
        <li><strong>Gas Compressibility:</strong> Gases possess vast intermolecular voids and are highly compressible. Per the ideal gas equation of state:
        $$\rho = \frac{P \cdot M_{\text{molar}}}{R \cdot T}$$
        Where \(P\) is absolute pressure, \(M_{\text{molar}}\) is molecular weight, \(R\) is the universal gas constant (\(8.31446\text{ J/(mol}\cdot\text{K)}\)), and \(T\) is thermodynamic temperature in Kelvin. Tripling atmospheric pressure triples air density, directly impacting aerodynamic lift and combustion engine stoichiometry.</li>
      </ul>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-accordion">
        <details class="faq-item">
          <summary class="faq-question">Why does ice float on liquid water when most solid states sink?</summary>
          <div class="faq-answer">
            <p>Most substances contract and become denser upon freezing. Water is a rare anomaly: as it cools below 3.98°C and crystallizes into hexagonal ice at 0°C, rigid hydrogen bonds force H₂O molecules into an open, cage-like hexagonal lattice. This increases volume by approximately 9%, reducing solid ice density to 917 kg/m³, which is less than liquid water's 1,000 kg/m³. Consequently, ice floats with roughly 91.7% of its volume submerged.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What is the difference between true density and bulk density?</summary>
          <div class="faq-answer">
            <p>True (or skeletal) density measures the mass of a solid divided strictly by the volume of the solid material itself, excluding internal pores and external voids. Bulk density (commonly used in soil science, agriculture, and pharmaceutical powders) divides the total mass by the entire macroscopic bulk volume, including interstitial voids and air gaps between granular particles. Bulk density is always lower than true density.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">How does salinity change the density of water?</summary>
          <div class="faq-answer">
            <p>Dissolving sodium chloride and mineral salts into water increases its mass more than its volume, significantly increasing density. Standard freshwater has a density of approximately 1,000 kg/m³, typical ocean seawater (3.5% salinity) has a density of 1,025 kg/m³, and hyper-saline bodies like the Dead Sea reach densities exceeding 1,240 kg/m³, creating extreme buoyancy where humans float effortlessly.</p>
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">What laboratory instruments are used to measure density with high precision?</summary>
          <div class="faq-answer">
            <p>High-precision density measurement tools include: (1) <strong>Pycnometers:</strong> calibrated glass vessels that determine liquid or powder density by mass displacement; (2) <strong>Hydrometers:</strong> weighted glass floats calibrated to read specific gravity or API gravity directly from fluid meniscus levels; (3) <strong>Oscillating U-Tube Density Meters:</strong> digital electronic instruments measuring harmonic resonant frequency changes in an oscillating sample tube (ASTM D4052); and (4) <strong>Hydrostatic Analytical Balances:</strong> which weigh submerged specimens to apply Archimedes' principle directly.</p>
          </div>
        </details>
      </div>

      <!-- Cross-Disciplinary Internal Links -->
      <div class="related-calculators" style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
        <h3>Related Engineering &amp; Physics Calculators</h3>
        <ul style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem; list-style: none; padding: 0;">
          <li><a href="volume-calculator.html">&rarr; Volume Calculator (3D Solids)</a></li>
          <li><a href="percentage-change-calculator.html">&rarr; Percentage Change Calculator</a></li>
          <li><a href="speed-calculator.html">&rarr; Speed &amp; Kinematics Calculator</a></li>
          <li><a href="pressure-calculator.html">&rarr; Fluid &amp; Mechanical Pressure Calculator</a></li>
          <li><a href="force-converter.html">&rarr; Force &amp; Newton's Laws Solver</a></li>
          <li><a href="scientific-notation-calculator.html">&rarr; Scientific Notation Calculator</a></li>
        </ul>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive mathematical, statistical, and engineering calculation tools.</p>
      </div>
      <div class="footer-col">
        <h4>Discipline Hubs</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Engineering</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    // Conversion factors to SI base units (kg and m³)
    var MASS_FACTORS = {
      'kg': 1.0,
      'g': 0.001,
      'mg': 0.000001,
      'lb': 0.45359237,
      'oz': 0.028349523125,
      't': 1000.0
    };

    var VOL_FACTORS = {
      'm3': 1.0,
      'cm3': 0.000001,
      'L': 0.001,
      'mL': 0.000001,
      'ft3': 0.028316846592,
      'in3': 0.000016387064,
      'gal': 0.003785411784
    };

    var DENS_FACTORS = {
      'kg_m3': 1.0,
      'g_cm3': 1000.0,
      'lb_ft3': 16.018463,
      'lb_gal': 119.826427
    };

    function switchDensityMode() {
      var target = document.getElementById('solve-target').value;
      var grpMass = document.getElementById('grp-mass');
      var grpVol = document.getElementById('grp-volume');
      var grpDens = document.getElementById('grp-density');

      grpMass.style.display = (target === 'mass') ? 'none' : 'block';
      grpVol.style.display = (target === 'volume') ? 'none' : 'block';
      grpDens.style.display = (target === 'density') ? 'none' : 'block';

      var lbl = document.getElementById('res-primary-label');
      if (target === 'density') {
        lbl.innerText = "Material Density (ρ)";
      } else if (target === 'mass') {
        lbl.innerText = "Calculated Mass (m)";
      } else if (target === 'volume') {
        lbl.innerText = "Calculated Volume (V)";
      }

      calculateDensity();
    }

    function loadMaterialPreset() {
      var val = document.getElementById('preset-material').value;
      if (val === 'custom') return;

      var densKgM3 = parseFloat(val);
      var target = document.getElementById('solve-target').value;

      if (target === 'density') {
        // If solving for density, update mass according to current volume
        var vVal = parseFloat(document.getElementById('inp-volume').value);
        var vUnit = document.getElementById('unit-volume').value;
        if (!isNaN(vVal) && vVal > 0) {
          var vM3 = vVal * VOL_FACTORS[vUnit];
          var mKg = densKgM3 * vM3;
          var mUnit = document.getElementById('unit-mass').value;
          document.getElementById('inp-mass').value = (mKg / MASS_FACTORS[mUnit]).toPrecision(6);
        }
      } else {
        var dUnit = document.getElementById('unit-density').value;
        document.getElementById('inp-density').value = (densKgM3 / DENS_FACTORS[dUnit]).toPrecision(6);
      }
      calculateDensity();
    }

    function calculateDensity() {
      var target = document.getElementById('solve-target').value;
      var mVal = parseFloat(document.getElementById('inp-mass').value);
      var mUnit = document.getElementById('unit-mass').value;
      var vVal = parseFloat(document.getElementById('inp-volume').value);
      var vUnit = document.getElementById('unit-volume').value;
      var dVal = parseFloat(document.getElementById('inp-density').value);
      var dUnit = document.getElementById('unit-density').value;

      var rho_kg_m3 = 0, m_kg = 0, v_m3 = 0;
      var steps = "";

      if (target === 'density') {
        if (isNaN(mVal) || isNaN(vVal) || mVal <= 0 || vVal <= 0) {
          showError("Mass and volume must be strictly positive real numbers.");
          return;
        }
        m_kg = mVal * MASS_FACTORS[mUnit];
        v_m3 = vVal * VOL_FACTORS[vUnit];
        rho_kg_m3 = m_kg / v_m3;

        steps = "Mode: Solve for Density (ρ = m / V)\n" +
                "Inputs: m = " + mVal + " " + mUnit + ", V = " + vVal + " " + vUnit + "\n\n" +
                "1. Convert Mass to SI Base: m = " + m_kg.toExponential(4) + " kg\n" +
                "2. Convert Volume to SI Base: V = " + v_m3.toExponential(4) + " m³\n\n" +
                "3. Density Formula: ρ = m / V = " + m_kg.toExponential(4) + " / " + v_m3.toExponential(4) + "\n" +
                "   ρ = " + rho_kg_m3.toFixed(2) + " kg/m³";

        document.getElementById('res-primary-val').innerText = rho_kg_m3.toLocaleString(undefined, {maximumFractionDigits: 2}) + " kg/m³";
        document.getElementById('res-primary-sub').innerText = (rho_kg_m3 / 1000).toFixed(4) + " g/cm³ • " + (rho_kg_m3 / 16.018463).toFixed(2) + " lb/ft³";

      } else if (target === 'mass') {
        if (isNaN(dVal) || isNaN(vVal) || dVal <= 0 || vVal <= 0) {
          showError("Density and volume must be strictly positive real numbers.");
          return;
        }
        rho_kg_m3 = dVal * DENS_FACTORS[dUnit];
        v_m3 = vVal * VOL_FACTORS[vUnit];
        m_kg = rho_kg_m3 * v_m3;

        var mDisplay = m_kg / MASS_FACTORS[mUnit];

        steps = "Mode: Solve for Mass (m = ρ * V)\n" +
                "Inputs: ρ = " + dVal + " " + dUnit.replace('_', '/') + ", V = " + vVal + " " + vUnit + "\n\n" +
                "1. Convert Density to SI Base: ρ = " + rho_kg_m3.toFixed(2) + " kg/m³\n" +
                "2. Convert Volume to SI Base: V = " + v_m3.toExponential(4) + " m³\n\n" +
                "3. Mass Formula: m = ρ * V = " + rho_kg_m3.toFixed(2) + " * " + v_m3.toExponential(4) + "\n" +
                "   m = " + m_kg.toFixed(4) + " kg (" + mDisplay.toFixed(4) + " " + mUnit + ")";

        document.getElementById('res-primary-val').innerText = mDisplay.toLocaleString(undefined, {maximumFractionDigits: 4}) + " " + mUnit;
        document.getElementById('res-primary-sub').innerText = m_kg.toFixed(4) + " kg • " + (m_kg * 2.20462).toFixed(4) + " lb";

      } else if (target === 'volume') {
        if (isNaN(mVal) || isNaN(dVal) || mVal <= 0 || dVal <= 0) {
          showError("Mass and density must be strictly positive real numbers.");
          return;
        }
        m_kg = mVal * MASS_FACTORS[mUnit];
        rho_kg_m3 = dVal * DENS_FACTORS[dUnit];
        v_m3 = m_kg / rho_kg_m3;

        var vDisplay = v_m3 / VOL_FACTORS[vUnit];

        steps = "Mode: Solve for Volume (V = m / ρ)\n" +
                "Inputs: m = " + mVal + " " + mUnit + ", ρ = " + dVal + " " + dUnit.replace('_', '/') + "\n\n" +
                "1. Convert Mass to SI Base: m = " + m_kg.toFixed(4) + " kg\n" +
                "2. Convert Density to SI Base: ρ = " + rho_kg_m3.toFixed(2) + " kg/m³\n\n" +
                "3. Volume Formula: V = m / ρ = " + m_kg.toFixed(4) + " / " + rho_kg_m3.toFixed(2) + "\n" +
                "   V = " + v_m3.toExponential(4) + " m³ (" + vDisplay.toFixed(4) + " " + vUnit + ")";

        document.getElementById('res-primary-val').innerText = vDisplay.toLocaleString(undefined, {maximumFractionDigits: 4}) + " " + vUnit;
        document.getElementById('res-primary-sub').innerText = (v_m3 * 1000).toFixed(2) + " L • " + (v_m3 * 35.3147).toFixed(2) + " ft³";
      }

      // Specific Gravity relative to water at 4°C (1000 kg/m³)
      var sg = rho_kg_m3 / 1000.0;
      document.getElementById('res-sg').innerText = sg.toFixed(3);

      // Freshwater buoyancy
      var buoyEl = document.getElementById('res-buoyancy');
      if (sg < 0.999) {
        buoyEl.innerText = "Floats (" + (sg * 100).toFixed(1) + "% Submerged)";
        buoyEl.style.color = "#28a745";
      } else if (sg > 1.001) {
        buoyEl.innerText = "Sinks (Negative Buoyancy)";
        buoyEl.style.color = "#dc3545";
      } else {
        buoyEl.innerText = "Neutral Buoyancy";
        buoyEl.style.color = "#007bff";
      }

      // API Gravity: 141.5 / SG - 131.5
      var api = (sg > 0) ? (141.5 / sg - 131.5) : 0;
      document.getElementById('res-api').innerText = api.toFixed(1) + "° API";

      // Equivalent multi-system table
      document.getElementById('eq-kgm3').innerText = rho_kg_m3.toLocaleString(undefined, {maximumFractionDigits: 2}) + " kg/m³";
      document.getElementById('eq-gcm3').innerText = (rho_kg_m3 / 1000).toFixed(4) + " g/cm³";
      document.getElementById('eq-lbft3').innerText = (rho_kg_m3 / 16.018463).toFixed(2) + " lb/ft³";
      document.getElementById('eq-lbgal').innerText = (rho_kg_m3 / 119.826427).toFixed(2) + " lb/gal";

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-primary-val').innerText = "Error";
      document.getElementById('res-primary-sub').innerText = "Invalid calculation";
      document.getElementById('res-sg').innerText = "N/A";
      document.getElementById('res-buoyancy').innerText = "N/A";
      document.getElementById('res-buoyancy').style.color = "#6c757d";
      document.getElementById('res-api').innerText = "N/A";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetDensity() {
      document.getElementById('solve-target').value = 'density';
      document.getElementById('preset-material').value = 'custom';
      document.getElementById('inp-mass').value = '2500';
      document.getElementById('unit-mass').value = 'kg';
      document.getElementById('inp-volume').value = '0.3185';
      document.getElementById('unit-volume').value = 'm3';
      document.getElementById('inp-density').value = '7850';
      document.getElementById('unit-density').value = 'kg_m3';
      switchDensityMode();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateDensity();
    });
  </script>
</body>
</html>
"""

def generate_part3():
    f5 = os.path.join(BASE_DIR, "markup-calculator.html")
    with open(f5, "w", encoding="utf-8") as fp:
        fp.write(HTML_MARKUP.strip() + "\n")
    print(f"Generated: {f5}")

    f6 = os.path.join(BASE_DIR, "density-calculator.html")
    with open(f6, "w", encoding="utf-8") as fp:
        fp.write(HTML_DENSITY.strip() + "\n")
    print(f"Generated: {f6}")

if __name__ == "__main__":
    generate_part3()
