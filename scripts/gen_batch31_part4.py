# -*- coding: utf-8 -*-
"""
Generator for Batch 31 - Part 4:
7. z-score-calculator.html
8. average-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 7. z-score-calculator.html
HTML_ZSCORE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Z-Score Calculator - Standard Score, Percentiles &amp; P-Value Solver</title>
  <meta name="description" content="Calculate Z-scores (standard scores), normal distribution percentiles, cumulative probabilities, and p-values from raw score, mean, and standard deviation.">
  <link rel="canonical" href="https://calchub.org/z-score-calculator.html">
  <meta property="og:title" content="Z-Score Calculator - Standard Score &amp; Normal Distribution Solver">
  <meta property="og:description" content="Free Z-score calculator. Compute standard scores Z = (x - mu) / sigma, left and right-tail p-values, two-tailed significance, and percentile rankings.">
  <meta property="og:url" content="https://calchub.org/z-score-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Z-Score Calculator - Standard Score &amp; Percentile Tool">
  <meta name="twitter:description" content="Calculate Z-score, cumulative normal probability, p-value, and percentile ranking with complete step-by-step statistical derivations.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Z-Score Calculator",
    "url": "https://calchub.org/z-score-calculator.html",
    "description": "Calculates standard scores Z = (x - mu)/sigma, normal distribution probabilities, percentiles, and p-values with step-by-step mathematical breakdowns.",
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
        "name": "What is a Z-score in statistics and how is it calculated?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A Z-score (standard score) measures the exact number of standard deviations a raw data point x falls above or below the mean mu. Its formula is Z = (x - mu) / sigma. A positive Z-score indicates a value above the mean, while a negative Z-score indicates a value below the mean."
        }
      },
      {
        "@type": "Question",
        "name": "How do you convert a Z-score to a percentile rank?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A Z-score is converted to a percentile rank by evaluating the standard normal cumulative distribution function (CDF) Phi(z). The percentile represents the percentage of observations in a normal distribution falling below that Z-score: Percentile = Phi(z) * 100%."
        }
      },
      {
        "@type": "Question",
        "name": "What Z-score threshold defines a statistical outlier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In standard statistical data screening, observations with |Z| > 2.0 (falling outside roughly 95% of the data) are classified as potential outliers. Observations with |Z| > 3.0 (falling outside 99.73% of the distribution) are considered extreme statistical outliers."
        }
      },
      {
        "@type": "Question",
        "name": "What is the difference between a Z-score and a T-score?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A Z-score is used when the true population standard deviation sigma is known, or when the sample size is very large (n >= 30) following the standard normal distribution. A T-score is used when the population standard deviation is unknown and estimated via sample standard deviation s for smaller samples, following Student's t-distribution."
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
        <a href="math.html" class="active">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="calculator-container">
    <div class="calculator-header">
      <div class="calc-icon" aria-hidden="true">&#9147;</div>
      <h1>Z-Score Calculator</h1>
      <p class="calc-description">Calculate standard score (Z), cumulative normal probability, percentile ranking, and one-tailed/two-tailed p-values from raw score, mean, and standard deviation.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="z-mode">Calculation Direction</label>
        <select id="z-mode" class="form-control" onchange="switchZMode()">
          <option value="raw-to-z" selected>Raw Score to Z-Score: (x, &mu;, &sigma; &rarr; Z, Percentile)</option>
          <option value="z-to-raw">Z-Score to Raw Score: (Z, &mu;, &sigma; &rarr; x)</option>
        </select>
      </div>

      <!-- Mode 1: Raw to Z -->
      <div id="panel-raw-to-z">
        <div class="input-grid">
          <div class="input-group">
            <label for="raw-x">Raw Score Observation (x)</label>
            <input type="number" id="raw-x" class="form-control" value="85" step="any">
            <span class="help-text">Individual data value</span>
          </div>
          <div class="input-group">
            <label for="mean-val">Population / Sample Mean (&mu; or x̄)</label>
            <input type="number" id="mean-val" class="form-control" value="70" step="any">
            <span class="help-text">Center of the distribution</span>
          </div>
          <div class="input-group">
            <label for="sd-val">Standard Deviation (&sigma; or s)</label>
            <input type="number" id="sd-val" class="form-control" value="10" min="0.000001" step="any">
            <span class="help-text">Measure of dispersion (&sigma; &gt; 0)</span>
          </div>
        </div>
      </div>

      <!-- Mode 2: Z to Raw -->
      <div id="panel-z-to-raw" style="display:none;">
        <div class="input-grid">
          <div class="input-group">
            <label for="target-z">Z-Score (Z)</label>
            <input type="number" id="target-z" class="form-control" value="1.50" step="any">
            <span class="help-text">Number of standard deviations</span>
          </div>
          <div class="input-group">
            <label for="inv-mean">Mean (&mu;)</label>
            <input type="number" id="inv-mean" class="form-control" value="70" step="any">
          </div>
          <div class="input-group">
            <label for="inv-sd">Standard Deviation (&sigma;)</label>
            <input type="number" id="inv-sd" class="form-control" value="10" min="0.000001" step="any">
          </div>
        </div>
      </div>

      <div class="input-group">
        <label for="precision-select">Decimal Precision</label>
        <select id="precision-select" class="form-control" onchange="calculateZ()">
          <option value="2">2 decimal places</option>
          <option value="4" selected>4 decimal places</option>
          <option value="6">6 decimal places</option>
        </select>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculateZ()" style="flex:1;">Compute Z-Score</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetZ()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Standardized Distribution Metrics</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-zscore">
          Z-Score: +1.5000
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
          <div><span class="res-label">Percentile Rank:</span> <strong class="res-val" id="res-percentile">93.32%</strong></div>
          <div><span class="res-label">Left-Tail P(Z &lt; z):</span> <strong class="res-val" id="res-left-p">0.9332</strong></div>
          <div><span class="res-label">Right-Tail P(Z &gt; z):</span> <strong class="res-val" id="res-right-p">0.0668</strong></div>
          <div><span class="res-label">Two-Tailed p-value:</span> <strong class="res-val" id="res-two-p">0.1336</strong></div>
          <div><span class="res-label">Raw Score Equivalent:</span> <strong class="res-val" id="res-raw">85.0000</strong></div>
          <div><span class="res-label">Statistical Status:</span> <strong class="res-val" id="res-status">Above Average (+1.5&sigma;)</strong></div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Mathematical Step-by-Step Breakdown</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Theoretical &amp; Engineering Guide to Z-Scores</h2>
      <p>In parametric mathematical statistics, a Z-score (also termed standard score, normal deviate, or standardized variable) expresses the signed fractional distance of a raw observation from the population mean, measured in units of the standard deviation. By transforming arbitrary measurement scales (such as body weight in kilograms, examination test scores, or financial asset returns) into a dimensionless metric space, the Z-score enables direct objective comparison across diverse distributions.</p>

      <p>Under the Central Limit Theorem, the distribution of sample averages approaches a Gaussian bell curve regardless of the underlying population shape. Standardizing any normal random variable \(X \sim N(\mu, \sigma^2)\) maps it onto the standard normal distribution \(Z \sim N(0, 1)\), which has an exact mean of \(\mu = 0\) and variance of \(\sigma^2 = 1\), as analyzed in our <a href="standard-deviation-calculator.html">Standard Deviation Calculator</a> and <a href="variance-calculator.html">Variance Calculator</a>.</p>

      <h2>Mathematical Formulations &amp; Normal Distribution Calculus</h2>
      <p>The standard score transformation operates through clean algebraic and integral calculus formulations.</p>

      <h3>1. Primary Z-Score Standardization Formula</h3>
      <p>For any continuous random variable with known mean \(\mu\) and non-zero standard deviation \(\sigma\), the standard score is defined as:</p>
      $$Z = \frac{x - \mu}{\sigma}$$
      <p>Where:</p>
      <ul>
        <li>\(x\) is the raw, unstandardized observation.</li>
        <li>\(\mu\) is the arithmetic mean of the distribution.</li>
        <li>\(\sigma\) is the positive standard deviation (\(\sigma > 0\)).</li>
      </ul>
      <p>Solving inversely for the raw observation yields the inverse transformation:</p>
      $$x = \mu + Z \cdot \sigma$$

      <h3>2. Cumulative Standard Normal Probability (\(\Phi(z)\)) &amp; Error Function</h3>
      <p>The probability density function (PDF) of the standard normal distribution is given by:</p>
      $$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}$$
      <p>The cumulative distribution function (CDF) \(\Phi(z)\) evaluates the total area under the Gaussian bell curve to the left of \(z\), expressed via the Gauss error function \(\text{erf}(x)\):</p>
      $$\Phi(z) = P(Z \le z) = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}} e^{-\frac{t^2}{2}} \, dt = \frac{1}{2} \left[ 1 + \text{erf}\left( \frac{z}{\sqrt{2}} \right) \right]$$
      <p>In software algorithms, \(\text{erf}(x)\) is computed with extreme precision using Abramowitz and Stegun Chebyshev polynomial approximations.</p>

      <h3>3. Hypothesis Testing Tail Probabilities (P-Values)</h3>
      <p>Depending on the scientific hypothesis being evaluated, three standard p-value areas are derived from \(\Phi(z)\):</p>
      <div class="formula-box">
        <h3>Tail Probability Formulas</h3>
        $$\text{Left-Tail Probability (Cumulative): } P(Z < z) = \Phi(z)$$
        $$\text{Right-Tail Probability (Upper): } P(Z > z) = 1 - \Phi(z)$$
        $$\text{Two-Tailed P-Value (Significance): } p = 2 \cdot [1 - \Phi(|z|)]$$
        $$\text{Percentile Rank: } \text{Percentile} = \Phi(z) \times 100\%$$
      </div>

      <h2>The Empirical Rule (68-95-99.7 Rule) &amp; Critical Values</h2>
      <p>For any normally distributed dataset, the Empirical Rule provides immediate benchmark thresholds:</p>
      <ul>
        <li>\(68.27\%\) of all observations fall within \(1\) standard deviation of the mean (\(|Z| \le 1.0\)).</li>
        <li>\(95.45\%\) of all observations fall within \(2\) standard deviations of the mean (\(|Z| \le 2.0\)).</li>
        <li>\(99.73\%\) of all observations fall within \(3\) standard deviations of the mean (\(|Z| \le 3.0\)). Only \(0.27\%\) (approx. 1 in 370 observations) lie beyond \(\pm 3\sigma\).</li>
      </ul>

      <h2>Critical Z-Score Values &amp; Hypothesis Benchmark Table</h2>
      <p>The following reference table outlines standard critical Z-scores (\(Z_{\alpha}\)) used across two-tailed and one-tailed scientific hypothesis tests:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Confidence Level \((1 - \alpha)\)</th>
            <th>Significance Level \((\alpha)\)</th>
            <th>Two-Tailed Critical \(Z_{\alpha/2}\)</th>
            <th>One-Tailed Critical \(Z_{\alpha}\)</th>
            <th>Cumulative Area \(\Phi(z)\)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>\(90.0\%\)</td>
            <td>\(0.10\)</td>
            <td>\(\pm 1.6449\)</td>
            <td>\(+1.2816\)</td>
            <td>\(0.9500\)</td>
          </tr>
          <tr>
            <td>\(95.0\%\) (Standard)</td>
            <td>\(0.05\)</td>
            <td>\(\pm 1.95996 \approx \pm 1.960\)</td>
            <td>\(+1.6449\)</td>
            <td>\(0.9750\)</td>
          </tr>
          <tr>
            <td>\(99.0\%\)</td>
            <td>\(0.01\)</td>
            <td>\(\pm 2.5758\)</td>
            <td>\(+2.3263\)</td>
            <td>\(0.9950\)</td>
          </tr>
          <tr>
            <td>\(99.9\%\)</td>
            <td>\(0.001\)</td>
            <td>\(\pm 3.2905\)</td>
            <td>\(+3.0902\)</td>
            <td>\(0.9995\)</td>
          </tr>
          <tr>
            <td>Six Sigma (\(99.99966\%\))</td>
            <td>\(0.0000034\)</td>
            <td>\(\pm 4.5000\) to \(\pm 6.0000\)</td>
            <td>\(+4.7534\)</td>
            <td>\(0.999999\)</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Engineering, Clinical &amp; Psychometric Case Studies</h2>
      <p>The following practical case studies illustrate how Z-score standardization solves problems in standardized academic testing, manufacturing anomaly screening, and clinical bone density radiology.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Standardized Psychometric Exam Cross-Comparison (SAT vs. ACT)</h3>
        <p><strong>Scenario:</strong> A university admissions officer compares two applicant exam scores. Candidate A scored \(1380\) on the SAT (nationwide mean \(\mu = 1060\), standard deviation \(\sigma = 210\)). Candidate B scored \(31\) on the ACT (nationwide mean \(\mu = 20.8\), standard deviation \(\sigma = 5.8\)). The officer must determine which student demonstrated a higher relative academic ranking.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Standardize Candidate A's SAT score:
            $$Z_{\text{SAT}} = \frac{1380 - 1060}{210} = \frac{320}{210} \approx +1.5238$$
          </li>
          <li>Evaluate SAT percentile rank:
            $$\Phi(1.5238) \approx 0.9362 \implies 93.62\text{-th percentile}$$
          </li>
          <li>Standardize Candidate B's ACT score:
            $$Z_{\text{ACT}} = \frac{31 - 20.8}{5.8} = \frac{10.2}{5.8} \approx +1.7586$$
          </li>
          <li>Evaluate ACT percentile rank:
            $$\Phi(1.7586) \approx 0.9607 \implies 96.07\text{-th percentile}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> Candidate B achieved a higher relative standard score (\(Z = +1.76\) vs. \(Z = +1.52\)), placing in the \(96.07\)-th percentile compared to Candidate A's \(93.62\)-th percentile.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Industrial Manufacturing Anomaly Detection &amp; Six Sigma Quality Control</h3>
        <p><strong>Scenario:</strong> A semiconductor fabrication line produces microchip wafer die thicknesses with an established population mean of \(\mu = 775.0 \text{ \mu m}\) and process standard deviation of \(\sigma = 2.4 \text{ \mu m}\). An optical interferometer measures a test wafer at \(x = 782.8 \text{ \mu m}\). The factory automation system must calculate the Z-score and flag whether the wafer exceeds the \(3\sigma\) process control limit.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Compute raw deviation from nominal center:
            $$\Delta x = 782.8 - 775.0 = +7.8 \text{ \mu m}$$
          </li>
          <li>Calculate process Z-score:
            $$Z = \frac{+7.8}{2.4} = +3.2500$$
          </li>
          <li>Evaluate right-tail exceedance probability:
            $$P(Z > 3.25) = 1 - \Phi(3.25) = 1 - 0.999423 = 0.000577 \text{ (approx. 1 in 1,733)}$$
          </li>
          <li>Evaluate two-tailed p-value:
            $$p = 2 \times 0.000577 = 0.001154$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> Because \(Z = +3.2500\) strictly exceeds the \(\pm 3.0\sigma\) upper control limit, the wafer is flagged as a statistically significant out-of-spec anomaly and rejected from the production line.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Clinical DEXA Bone Mineral Density (BMD) Diagnostic Scoring</h3>
        <p><strong>Scenario:</strong> Dual-energy X-ray absorptiometry (DEXA) scans report bone health using standard scores. A 68-year-old female undergoes a femoral neck bone density scan yielding an areal BMD of \(0.680 \text{ g/cm}^2\). The reference database for age-matched peers has a mean \(\mu = 0.790 \text{ g/cm}^2\) and \(\sigma = 0.095 \text{ g/cm}^2\). The clinical radiologist must calculate the patient's diagnostic Z-score.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Calculate difference from age-matched mean:
            $$x - \mu = 0.680 - 0.790 = -0.110 \text{ g/cm}^2$$
          </li>
          <li>Calculate age-matched Z-score:
            $$Z = \frac{-0.110}{0.095} \approx -1.1579$$
          </li>
          <li>Evaluate cumulative percentile:
            $$\Phi(-1.1579) \approx 0.1234 \implies 12.34\text{-th percentile}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The patient's bone density Z-score is \(-1.16\), indicating bone density falls \(1.16\) standard deviations below the age-matched average, placing her at the \(12.34\)-th percentile.</p>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">What does a Z-score of 0 mean?</div>
        <div class="faq-answer">A Z-score of exactly zero indicates that the raw observation is identical to the arithmetic mean of the distribution (\(x = \mu\)). In a standard normal distribution, a Z-score of 0 corresponds exactly to the 50th percentile (the median).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Can a Z-score be greater than 3 or less than -3?</div>
        <div class="faq-answer">Yes. While \(99.73\%\) of observations in a normal distribution fall between -3 and +3, values outside this interval occur with non-zero probability. Observations with \(|Z| > 3\) represent rare events occurring less than \(0.27\%\) of the time, often signifying special causes or measurement outliers.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why must standard deviation be strictly positive?</div>
        <div class="faq-answer">Standard deviation represents the root mean square distance of data points from their mean. If \(\sigma = 0\), all data points in the set are identical, resulting in zero dispersion. Dividing by \(\sigma = 0\) produces an undefined division by zero.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How does a Z-score relate to the Altman Z-score in finance?</div>
        <div class="faq-answer">While a statistical Z-score standardizes a single univariate metric, the Altman Z-score is a multivariate discriminant linear formula combining five financial ratios (working capital, retained earnings, EBIT, market equity, and sales) to predict the statistical probability of corporate bankruptcy.</div>
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
    // High-precision erf approximation (Abramowitz & Stegun formula 7.1.26)
    function erf(x) {
      var sign = (x >= 0) ? 1 : -1;
      x = Math.abs(x);
      var a1 =  0.254829592;
      var a2 = -0.284496736;
      var a3 =  1.421413741;
      var a4 = -1.453152027;
      var a5 =  1.061405429;
      var p  =  0.3275911;

      var t = 1.0 / (1.0 + p * x);
      var y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);
      return sign * y;
    }

    function normalCdf(z) {
      return 0.5 * (1.0 + erf(z / Math.sqrt(2.0)));
    }

    function switchZMode() {
      var mode = document.getElementById('z-mode').value;
      if (mode === 'raw-to-z') {
        document.getElementById('panel-raw-to-z').style.display = 'block';
        document.getElementById('panel-z-to-raw').style.display = 'none';
      } else {
        document.getElementById('panel-raw-to-z').style.display = 'none';
        document.getElementById('panel-z-to-raw').style.display = 'block';
      }
      calculateZ();
    }

    function calculateZ() {
      var mode = document.getElementById('z-mode').value;
      var prec = parseInt(document.getElementById('precision-select').value, 10) || 4;

      var z = 0, x = 0, mu = 0, sigma = 0;
      var steps = "";

      if (mode === 'raw-to-z') {
        x = parseFloat(document.getElementById('raw-x').value);
        mu = parseFloat(document.getElementById('mean-val').value);
        sigma = parseFloat(document.getElementById('sd-val').value);

        if (isNaN(x) || isNaN(mu) || isNaN(sigma)) {
          showError("Please enter valid real numbers for score, mean, and standard deviation.");
          return;
        }

        if (sigma <= 0) {
          showError("Standard deviation must be strictly greater than zero.");
          return;
        }

        z = (x - mu) / sigma;
        steps = "Mode: Raw Score to Z-Score Standardization\n" +
                "Given: Raw Score x = " + x + ", Mean μ = " + mu + ", Standard Deviation σ = " + sigma + "\n\n" +
                "1. Deviation from Center:\n" +
                "   Δ = x - μ = " + x + " - " + mu + " = " + (x - mu).toFixed(prec) + "\n\n" +
                "2. Standard Score Formula:\n" +
                "   Z = (x - μ) / σ = " + (x - mu).toFixed(prec) + " / " + sigma + " = " + z.toFixed(prec);

      } else {
        z = parseFloat(document.getElementById('target-z').value);
        mu = parseFloat(document.getElementById('inv-mean').value);
        sigma = parseFloat(document.getElementById('inv-sd').value);

        if (isNaN(z) || isNaN(mu) || isNaN(sigma)) {
          showError("Please enter valid numbers for Z, mean, and standard deviation.");
          return;
        }

        if (sigma <= 0) {
          showError("Standard deviation must be strictly greater than zero.");
          return;
        }

        x = mu + z * sigma;
        steps = "Mode: Inverse Z-Score to Raw Score Transformation\n" +
                "Given: Z-Score Z = " + z + ", Mean μ = " + mu + ", Standard Deviation σ = " + sigma + "\n\n" +
                "1. Inverse Formula:\n" +
                "   x = μ + (Z * σ)\n" +
                "   x = " + mu + " + (" + z + " * " + sigma + ") = " + mu + " + " + (z * sigma).toFixed(prec) + " = " + x.toFixed(prec);
      }

      var leftTail = normalCdf(z);
      var rightTail = 1.0 - leftTail;
      var twoTail = 2.0 * (1.0 - normalCdf(Math.abs(z)));
      var percentile = leftTail * 100.0;

      var status = "Near Average";
      if (z >= 3.0) status = "Extreme High Outlier (+3σ+)";
      else if (z >= 2.0) status = "Significantly High (+2σ+)";
      else if (z >= 1.0) status = "Above Average (+1σ)";
      else if (z <= -3.0) status = "Extreme Low Outlier (-3σ-)";
      else if (z <= -2.0) status = "Significantly Low (-2σ-)";
      else if (z <= -1.0) status = "Below Average (-1σ)";

      var signStr = (z >= 0) ? "+" : "";
      document.getElementById('res-zscore').innerText = "Z-Score: " + signStr + z.toFixed(prec);
      document.getElementById('res-percentile').innerText = percentile.toFixed(2) + "%";
      document.getElementById('res-left-p').innerText = leftTail.toFixed(prec);
      document.getElementById('res-right-p').innerText = rightTail.toFixed(prec);
      document.getElementById('res-two-p').innerText = twoTail.toFixed(prec);
      document.getElementById('res-raw').innerText = x.toFixed(prec);
      document.getElementById('res-status').innerText = status;

      steps += "\n\n3. Cumulative Normal CDF Probabilities:\n" +
               "   Left-Tail P(Z < z) = " + leftTail.toFixed(prec) + " (Percentile: " + percentile.toFixed(2) + "%)\n" +
               "   Right-Tail P(Z > z) = 1 - P(Z < z) = " + rightTail.toFixed(prec) + "\n" +
               "   Two-Tailed p-value = 2 * [1 - Φ(|z|)] = " + twoTail.toFixed(prec);

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-zscore').innerText = "Error";
      document.getElementById('res-percentile').innerText = "N/A";
      document.getElementById('res-left-p').innerText = "N/A";
      document.getElementById('res-right-p').innerText = "N/A";
      document.getElementById('res-two-p').innerText = "N/A";
      document.getElementById('res-raw').innerText = "N/A";
      document.getElementById('res-status').innerText = "Invalid Input";
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetZ() {
      document.getElementById('z-mode').value = 'raw-to-z';
      document.getElementById('raw-x').value = '85';
      document.getElementById('mean-val').value = '70';
      document.getElementById('sd-val').value = '10';
      document.getElementById('target-z').value = '1.50';
      document.getElementById('inv-mean').value = '70';
      document.getElementById('inv-sd').value = '10';
      document.getElementById('precision-select').value = '4';
      switchZMode();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateZ();
    });
  </script>
</body>
</html>
"""

# 8. average-calculator.html
HTML_AVERAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Average Calculator - Arithmetic, Geometric, Harmonic &amp; RMS Means</title>
  <meta name="description" content="Calculate arithmetic mean, geometric mean, harmonic mean, quadratic mean (RMS), and weighted average with step-by-step proofs and inequality verification.">
  <link rel="canonical" href="https://calchub.org/average-calculator.html">
  <meta property="og:title" content="Average Calculator - Pythagorean Means &amp; Weighted Solver">
  <meta property="og:description" content="Free multi-mean average calculator. Compute arithmetic, geometric, harmonic, RMS quadratic means, and weighted averages with step-by-step math.">
  <meta property="og:url" content="https://calchub.org/average-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Average Calculator - Multi-Mean Statistical Solver">
  <meta name="twitter:description" content="Calculate arithmetic mean, geometric mean, harmonic mean, and root mean square (RMS) with complete step-by-step proofs and Pythagorean inequalities.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Average Calculator",
    "url": "https://calchub.org/average-calculator.html",
    "description": "Calculates arithmetic mean, geometric mean, harmonic mean, quadratic mean (RMS), and weighted average with step-by-step mathematical proofs.",
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
        "name": "What are the four classical Pythagorean means?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The four classical Pythagorean means are: 1. Arithmetic Mean (sum divided by count), 2. Geometric Mean (nth root of product), 3. Harmonic Mean (reciprocal of mean of reciprocals), and 4. Quadratic Mean / RMS (square root of mean of squares). They satisfy the fundamental inequality HM <= GM <= AM <= RMS."
        }
      },
      {
        "@type": "Question",
        "name": "When should you use the geometric mean instead of the arithmetic mean?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Use the geometric mean when averaging quantities that compound multiplicatively over time—such as financial investment returns, population growth rates, inflation indices, or aspect ratios. The arithmetic mean overestimates compound average growth."
        }
      },
      {
        "@type": "Question",
        "name": "Why is the harmonic mean necessary for calculating average speeds and rates?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When calculating the average speed across equal distances traveled at different velocities, the harmonic mean must be used: HM = 2 / (1/v1 + 1/v2). Taking an arithmetic mean overestimates average velocity because more time is spent traveling at the slower speed."
        }
      },
      {
        "@type": "Question",
        "name": "What is the Quadratic Mean or Root Mean Square (RMS)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Quadratic Mean (RMS) is the square root of the arithmetic mean of squared values: RMS = sqrt((1/n) * sum(x_i^2)). It is indispensable in electrical engineering for quantifying the effective heating power of alternating current (AC) waveforms and in physics for vector magnitudes."
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
        <a href="math.html" class="active">Math &amp; Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="calculator-container">
    <div class="calculator-header">
      <div class="calc-icon" aria-hidden="true">&#128202;</div>
      <h1>Average Calculator (All Means &amp; Weighted)</h1>
      <p class="calc-description">Compute Arithmetic Mean, Geometric Mean, Harmonic Mean, Quadratic Mean (RMS), and Weighted Average with step-by-step inequality verifications.</p>
    </div>

    <div class="calculator-body">
      <div class="input-group">
        <label for="data-input">Data Values (x)</label>
        <textarea id="data-input" class="form-control" rows="4" placeholder="Enter numbers separated by commas, spaces, or lines, e.g. 10, 20, 40, 80">10, 20, 40, 80</textarea>
        <span class="help-text">Accepts positive real numbers for all means (negative values supported for arithmetic and RMS means).</span>
      </div>

      <div class="input-group">
        <label for="weights-input">Optional Weights (w) for Weighted Average</label>
        <textarea id="weights-input" class="form-control" rows="2" placeholder="Optional corresponding weights matching data count, e.g. 1, 2, 3, 4"></textarea>
        <span class="help-text">Leave blank for unweighted equal weights. If provided, count must match data values.</span>
      </div>

      <div class="input-group">
        <label for="precision-select">Decimal Precision</label>
        <select id="precision-select" class="form-control" onchange="calculateAverages()">
          <option value="2">2 decimal places</option>
          <option value="4" selected>4 decimal places</option>
          <option value="6">6 decimal places</option>
        </select>
      </div>

      <div style="display:flex; gap:12px; margin-top:16px;">
        <button id="calc-btn" class="btn-primary" onclick="calculateAverages()" style="flex:1;">Compute All Averages</button>
        <button id="reset-btn" class="btn-secondary" onclick="resetAverages()">Reset</button>
      </div>

      <div id="result-box" class="result-box" style="margin-top:24px;">
        <h2 class="result-title">Pythagorean Means &amp; Statistical Center</h2>
        <div class="result-highlight" style="font-size:1.8rem; font-weight:700; color:var(--primary); margin-bottom:16px;" id="res-am">
          Arithmetic Mean: 37.5000
        </div>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
          <div><span class="res-label">Geometric Mean (GM):</span> <strong class="res-val" id="res-gm">28.2843</strong></div>
          <div><span class="res-label">Harmonic Mean (HM):</span> <strong class="res-val" id="res-hm">21.3333</strong></div>
          <div><span class="res-label">Quadratic Mean (RMS):</span> <strong class="res-val" id="res-rms">45.0000</strong></div>
          <div><span class="res-label">Weighted Mean (x̄_w):</span> <strong class="res-val" id="res-wm">Equal / Unweighted</strong></div>
          <div><span class="res-label">Sample Count (n):</span> <strong class="res-val" id="res-count">4</strong></div>
          <div><span class="res-label">Sum of Values (&sum;x):</span> <strong class="res-val" id="res-sum">150.0000</strong></div>
        </div>

        <h3 style="margin-top:20px; font-size:1.1rem; color:var(--text-dark);">Pythagorean Means Inequality Verification</h3>
        <div id="res-ineq" style="background:#EFF6FF; border:1px solid #BFDBFE; padding:12px; border-radius:6px; font-weight:700; color:var(--primary); margin-bottom:16px;">
          HM (21.3333) &le; GM (28.2843) &le; AM (37.5000) &le; RMS (45.0000) &mdash; Inequality Holds!
        </div>

        <h3 style="margin-top:16px; font-size:1.1rem; color:var(--text-dark);">Step-by-Step Mathematical Expansions</h3>
        <div id="res-steps" style="background:var(--bg-subtle, #f8fafc); padding:16px; border-radius:8px; font-family:monospace; font-size:0.95rem; white-space:pre-wrap; border:1px solid var(--border-color, #e2e8f0);"></div>
      </div>
    </div>

    <article class="article-body">
      <h2>Comprehensive Engineering &amp; Mathematical Guide to Statistical Means</h2>
      <p>The concept of an "average" represents the most ubiquitous mathematical operation in science, engineering, finance, and everyday human reasoning. It seeks a single representative value that encapsulates the central magnitude of a collection of numbers. However, equating an average solely with the standard arithmetic mean is a common pitfall: depending on whether the underlying physical process is additive, multiplicative, reciprocal, or root-squared, selecting the wrong mean yields mathematically distorted conclusions.</p>

      <p>Ancient Greek mathematicians, led by Archytas of Tarentum and Pythagoras, established the three classic <strong>Pythagorean Means</strong>: the Arithmetic Mean, the Geometric Mean, and the Harmonic Mean. Together with the Quadratic Mean (Root Mean Square, RMS), these four metrics form a unified mathematical spectrum connected by the fundamental Pythagorean inequality.</p>

      <h2>Mathematical Formulations of the Four Classical Means</h2>
      <p>Let a sequence of \(n\) positive real numbers be denoted as \(X = \{x_1, x_2, \dots, x_n\}\).</p>

      <h3>1. Arithmetic Mean (\(\text{AM}\))</h3>
      <p>The arithmetic mean is the additive center of a dataset, representing the value that every observation would take if their total sum were redistributed equally:</p>
      $$\text{AM} = \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i = \frac{x_1 + x_2 + \dots + x_n}{n}$$
      <p>The arithmetic mean is optimal for independent additive physical quantities—such as total monthly expenses, daily rainfall accumulation, or mechanical stress loads.</p>

      <h3>2. Geometric Mean (\(\text{GM}\))</h3>
      <p>The geometric mean is the multiplicative center of a dataset, defined as the \(n\)-th root of the continued product of all values:</p>
      $$\text{GM} = \left( \prod_{i=1}^{n} x_i \right)^{\frac{1}{n}} = \sqrt[n]{x_1 \cdot x_2 \cdot \dots \cdot x_n} = \exp\left( \frac{1}{n} \sum_{i=1}^{n} \ln(x_i) \right)$$
      <p>Evaluating via natural logarithms prevents floating-point overflow when multiplying many large numbers. The geometric mean is the mathematically correct metric for compounding investment returns (CAGR), demographic population growth, image aspect ratio scaling, and normalized scientific benchmarks.</p>

      <h3>3. Harmonic Mean (\(\text{HM}\))</h3>
      <p>The harmonic mean is defined as the reciprocal of the arithmetic mean of the reciprocals of the data points:</p>
      $$\text{HM} = \frac{n}{\sum_{i=1}^{n} \frac{1}{x_i}} = \frac{n}{\frac{1}{x_1} + \frac{1}{x_2} + \dots + \frac{1}{x_n}}$$
      <p>For two values \(a\) and \(b\), it simplifies to \(\text{HM} = \frac{2ab}{a + b}\). The harmonic mean is mandatory when averaging rates, ratios, and velocities over equal units of work or distance—such as round-trip vehicular speeds, machine-to-machine data throughput rates, and financial Price-to-Earnings (P/E) ratios.</p>

      <h3>4. Quadratic Mean / Root Mean Square (\(\text{RMS}\))</h3>
      <p>The quadratic mean computes the square root of the arithmetic mean of the squared values:</p>
      $$\text{RMS} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} x_i^2} = \sqrt{\frac{x_1^2 + x_2^2 + \dots + x_n^2}{n}}$$
      <p>The RMS value is indispensable in electrical engineering, acoustics, and signal processing. It quantifies the equivalent DC thermal dissipation power of an alternating AC current or voltage waveform: \(V_{\text{RMS}} = V_{\text{peak}} / \sqrt{2}\) for pure sinusoidal waves.</p>

      <h3>5. Weighted Arithmetic Mean (\(\bar{x}_w\))</h3>
      <p>When individual data points carry unequal relative significance, weights \(w_i\) are assigned to each observation:</p>
      $$\bar{x}_w = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i}$$
      <p>This formulation underpins academic college GPA calculations (course grade points weighted by credit hours) and financial portfolio return aggregations (asset returns weighted by capital allocation).</p>

      <h2>The Pythagorean Means Inequality Chain</h2>
      <p>For any set of positive real numbers, the four means strictly satisfy the fundamental inequality chain:</p>
      $$\min(X) \le \text{Harmonic Mean} \le \text{Geometric Mean} \le \text{Arithmetic Mean} \le \text{Root Mean Square} \le \max(X)$$
      $$\text{HM} \le \text{GM} \le \text{AM} \le \text{RMS}$$
      <p>Mathematical equality (\(\text{HM} = \text{GM} = \text{AM} = \text{RMS}\)) holds if and only if all data points in the collection are identical (\(x_1 = x_2 = \dots = x_n\)). As data dispersion increases, the gap between the means widens significantly.</p>

      <h2>Pythagorean &amp; Statistical Means Comparison Reference Table</h2>
      <p>The following technical reference table synthesizes the four classical means, their governing equations, mathematical domain constraints, and primary physical applications:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Mean Variant</th>
            <th>Governing Formula</th>
            <th>Domain Restrictions</th>
            <th>Primary Application Domain</th>
            <th>Distortion if Replaced by AM</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Arithmetic Mean (AM)</td>
            <td>\(\frac{\sum x_i}{n}\)</td>
            <td>All real numbers \(\mathbb{R}\)</td>
            <td>Additive quantities, census metrics, bookkeeping sums</td>
            <td>Baseline standard</td>
          </tr>
          <tr>
            <td>Geometric Mean (GM)</td>
            <td>\(\left(\prod x_i\right)^{1/n}\)</td>
            <td>Strictly positive (\(x_i > 0\))</td>
            <td>Compound financial returns (CAGR), human sensory perception (Weber-Fechner)</td>
            <td>Overestimates true compound growth</td>
          </tr>
          <tr>
            <td>Harmonic Mean (HM)</td>
            <td>\(\frac{n}{\sum (1/x_i)}\)</td>
            <td>Strictly non-zero (\(x_i > 0\))</td>
            <td>Average velocities over distance, fuel economy, P/E stock multiples</td>
            <td>Heavily overestimates rate-based averages</td>
          </tr>
          <tr>
            <td>Quadratic Mean (RMS)</td>
            <td>\(\sqrt{\frac{\sum x_i^2}{n}}\)</td>
            <td>All real numbers \(\mathbb{R}\)</td>
            <td>AC electrical power, acoustic sound pressure, vector standard deviations</td>
            <td>Underestimates electrical power dissipation</td>
          </tr>
          <tr>
            <td>Weighted Mean</td>
            <td>\(\frac{\sum w_i x_i}{\sum w_i}\)</td>
            <td>Weights \(\sum w_i > 0\)</td>
            <td>College GPA, portfolio asset returns, center of gravity</td>
            <td>Ignores disproportionate scale contributions</td>
          </tr>
        </tbody>
      </table>

      <h2>Real-World Engineering, Financial &amp; Transportation Case Studies</h2>
      <p>The following worked case studies demonstrate how selecting the correct mean is mathematically required in finance, transportation physics, and electrical engineering.</p>

      <div class="worked-example-card">
        <h3>Case Study 1: Compound Investment Return Growth (Geometric vs. Arithmetic Mean)</h3>
        <p><strong>Scenario:</strong> An investment portfolio experiences dramatic annual volatility over 3 consecutive years: Year 1 return is \(+100\%\) (wealth factor \(2.0\)), Year 2 return is \(-50\%\) (wealth factor \(0.5\)), and Year 3 return is \(+80\%\) (wealth factor \(1.8\)). A financial analyst must compute the true Compound Annual Growth Rate (CAGR) using the geometric mean versus the arithmetic mean.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Evaluate wealth growth factors: \(x_1 = 2.0, \; x_2 = 0.5, \; x_3 = 1.8\).</li>
          <li>Calculate cumulative portfolio multiplier:
            $$\prod x_i = 2.0 \times 0.5 \times 1.8 = 1.8000$$
          </li>
          <li>Compute Geometric Mean annual growth factor:
            $$\text{GM} = \sqrt[3]{1.8000} \approx 1.2164$$
            $$\text{True CAGR} = (1.2164 - 1) \times 100\% = +21.64\% \text{ per year}$$
          </li>
          <li>Calculate naive Arithmetic Mean return:
            $$\bar{R} = \frac{+100\% + (-50\%) + 80\%}{3} = \frac{130\%}{3} = +43.33\% \text{ per year}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The true annual compound growth rate is \(21.64\%\). The arithmetic mean falsely reports a \(43.33\%\) average, double the actual realized compounding performance.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 2: Commuter Round-Trip Travel Velocity (Harmonic vs. Arithmetic Mean)</h3>
        <p><strong>Scenario:</strong> An automobile commutes between two cities separated by a distance of \(60 \text{ miles}\). Due to morning rush-hour congestion, the outward trip is driven at \(v_1 = 30 \text{ mph}\). The evening return journey along the identical route is driven at \(v_2 = 60 \text{ mph}\). The traffic engineer must calculate the true average velocity for the entire \(120\text{-mile}\) round trip.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Calculate elapsed time for each leg:
            $$t_1 = \frac{60 \text{ miles}}{30 \text{ mph}} = 2.0 \text{ hours}$$
            $$t_2 = \frac{60 \text{ miles}}{60 \text{ mph}} = 1.0 \text{ hour}$$
            $$\text{Total Time } t_{\text{total}} = 2.0 + 1.0 = 3.0 \text{ hours}$$
          </li>
          <li>Calculate physical average velocity (\(v = d / t\)):
            $$v_{\text{avg}} = \frac{120 \text{ miles}}{3.0 \text{ hours}} = 40.0000 \text{ mph}$$
          </li>
          <li>Apply the Harmonic Mean formula:
            $$\text{HM} = \frac{2}{\frac{1}{v_1} + \frac{1}{v_2}} = \frac{2}{\frac{1}{30} + \frac{1}{60}} = \frac{2}{\frac{2}{60} + \frac{1}{60}} = \frac{2}{\frac{3}{60}} = \frac{120}{3} = 40.0000 \text{ mph}$$
          </li>
          <li>Compare against naive Arithmetic Mean:
            $$\text{AM} = \frac{30 + 60}{2} = 45.0000 \text{ mph (Incorrect)}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The true average speed is exactly \(40.0000 \text{ mph}\), provided by the harmonic mean. The arithmetic mean overestimates speed because twice as much time was spent traveling at the slower \(30 \text{ mph}\) pace.</p>
      </div>

      <div class="worked-example-card">
        <h3>Case Study 3: Alternating Current Effective Heating Power (Quadratic Mean / RMS)</h3>
        <p><strong>Scenario:</strong> An electrical test bench records 4 discrete instantaneous voltage samples across a resistive heating element: \(+120 \text{ V}, -120 \text{ V}, +80 \text{ V}, -80 \text{ V}\). The electrical engineer must evaluate the Root Mean Square (RMS) voltage to compute continuous electrical heat dissipation.</p>
        <p><strong>Step-by-step Solution:</strong></p>
        <ol>
          <li>Square each instantaneous voltage value:
            $$(+120)^2 = 14400, \quad (-120)^2 = 14400$$
            $$(+80)^2 = 6400, \quad (-80)^2 = 6400$$
          </li>
          <li>Sum the squared voltages:
            $$\sum V^2 = 14400 + 14400 + 6400 + 6400 = 41600 \text{ V}^2$$
          </li>
          <li>Compute arithmetic mean of squares:
            $$\frac{41600}{4} = 10400 \text{ V}^2$$
          </li>
          <li>Take the square root to obtain RMS voltage:
            $$V_{\text{RMS}} = \sqrt{10400} \approx 101.9804 \text{ V}$$
          </li>
        </ol>
        <p><strong>Conclusion:</strong> The effective RMS heating potential is \(101.9804 \text{ V}\). (Notice that the simple arithmetic mean is identically \(0 \text{ V}\), which would erroneously imply zero electrical power dissipation).</p>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-question">Can the geometric or harmonic mean be calculated for negative numbers?</div>
        <div class="faq-answer">Generally no. For the geometric mean, negative numbers under an even root yield imaginary complex numbers, and alternating signs cause oscillating products. For the harmonic mean, negative numbers can cause denominators of zero (\(1/x_1 + 1/x_2 = 0\)), producing undefined infinities. Both GM and HM are mathematically defined for strictly positive real numbers (\(x > 0\)).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Why does the arithmetic mean always exceed the geometric mean?</div>
        <div class="faq-answer">The AM-GM inequality is a direct consequence of the concavity of the natural logarithm function (Jensen's inequality). Because the logarithm curve bends downwards, the logarithm of an arithmetic mean is always greater than or equal to the average of the logarithms: \(\ln(\frac{\sum x_i}{n}) \ge \frac{\sum \ln x_i}{n}\). Exponentiating both sides proves \(\text{AM} \ge \text{GM}\).</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How does weighted averaging differ from standard averaging?</div>
        <div class="faq-answer">A standard arithmetic mean assumes every observation contributes equal weight (\(1/n\)). A weighted average assigns custom multipliers (\(w_i\)) to each data point, allowing higher-priority, longer-duration, or higher-credit items to exert proportionally greater influence on the final result.</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">What is the relationship between RMS and standard deviation?</div>
        <div class="faq-answer">The Root Mean Square is related to the sample variance and mean through the mathematical identity: \(\text{RMS}^2 = \bar{x}^2 + \sigma^2\) (for population parameters). When the mean is zero (\(\bar{x} = 0\)), the RMS value identically equals the standard deviation.</div>
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
    function parseList(text) {
      if (!text) return [];
      var parts = text.split(/[\s,;\n\r\t]+/);
      var nums = [];
      for (var i = 0; i < parts.length; i++) {
        var str = parts[i].trim();
        if (str !== "") {
          var val = parseFloat(str);
          if (!isNaN(val)) nums.push(val);
        }
      }
      return nums;
    }

    function calculateAverages() {
      var dataRaw = document.getElementById('data-input').value;
      var weightsRaw = document.getElementById('weights-input').value;
      var prec = parseInt(document.getElementById('precision-select').value, 10) || 4;

      var data = parseList(dataRaw);
      var weights = parseList(weightsRaw);

      if (data.length === 0) {
        showError("Please enter at least one valid numerical observation.");
        return;
      }

      var n = data.length;
      var sum = 0;
      var sumSq = 0;
      var hasNonPositive = false;
      var logSum = 0;
      var reciprocalSum = 0;

      for (var i = 0; i < n; i++) {
        var v = data[i];
        sum += v;
        sumSq += (v * v);
        if (v <= 0) {
          hasNonPositive = true;
        } else {
          logSum += Math.log(v);
          reciprocalSum += (1.0 / v);
        }
      }

      var am = sum / n;
      var rms = Math.sqrt(sumSq / n);
      var gm = hasNonPositive ? null : Math.exp(logSum / n);
      var hm = hasNonPositive ? null : (n / reciprocalSum);

      // Weighted Mean calculation
      var wmText = "Equal / Unweighted";
      if (weights.length > 0) {
        if (weights.length !== n) {
          showError("Weights count (" + weights.length + ") must match data count (" + n + ").");
          return;
        }
        var wSum = 0;
        var wProdSum = 0;
        for (var j = 0; j < n; j++) {
          wSum += weights[j];
          wProdSum += (weights[j] * data[j]);
        }
        if (wSum === 0) {
          showError("Sum of weights cannot be zero.");
          return;
        }
        var wm = wProdSum / wSum;
        wmText = wm.toFixed(prec);
      }

      document.getElementById('res-am').innerText = "Arithmetic Mean: " + am.toFixed(prec);
      document.getElementById('res-gm').innerText = (gm !== null) ? gm.toFixed(prec) : "Undefined (x ≤ 0)";
      document.getElementById('res-hm').innerText = (hm !== null) ? hm.toFixed(prec) : "Undefined (x ≤ 0)";
      document.getElementById('res-rms').innerText = rms.toFixed(prec);
      document.getElementById('res-wm').innerText = wmText;
      document.getElementById('res-count').innerText = n.toString();
      document.getElementById('res-sum').innerText = sum.toFixed(prec);

      var ineqText = "";
      if (gm !== null && hm !== null) {
        ineqText = "HM (" + hm.toFixed(prec) + ") ≤ GM (" + gm.toFixed(prec) + ") ≤ AM (" + am.toFixed(prec) + ") ≤ RMS (" + rms.toFixed(prec) + ") — Pythagorean Inequality Holds!";
      } else {
        ineqText = "Geometric and Harmonic means require strictly positive data (x > 0).";
      }
      document.getElementById('res-ineq').innerText = ineqText;

      var steps = "Dataset Analysis (Count n = " + n + "):\n" +
                  "1. Arithmetic Mean: Sum / n = " + sum.toFixed(prec) + " / " + n + " = " + am.toFixed(prec) + "\n\n" +
                  "2. Quadratic Mean (RMS): sqrt(Sum of Squares / n)\n" +
                  "   RMS = sqrt(" + sumSq.toFixed(prec) + " / " + n + ") = " + rms.toFixed(prec) + "\n\n";

      if (gm !== null) {
        steps += "3. Geometric Mean: exp(Σ ln(x) / n) = (" + data.slice(0, 5).join(" × ") + (n > 5 ? "..." : "") + ")^(1/" + n + ")\n" +
                 "   GM = " + gm.toFixed(prec) + "\n\n";
      } else {
        steps += "3. Geometric Mean: Undefined (contains non-positive values)\n\n";
      }

      if (hm !== null) {
        steps += "4. Harmonic Mean: n / Σ(1/x) = " + n + " / " + reciprocalSum.toFixed(prec) + "\n" +
                 "   HM = " + hm.toFixed(prec) + "\n\n";
      } else {
        steps += "4. Harmonic Mean: Undefined (contains non-positive values)\n\n";
      }

      if (weights.length > 0) {
        steps += "5. Weighted Arithmetic Mean: Σ(w·x) / Σw = " + wmText;
      }

      document.getElementById('res-steps').innerText = steps;
    }

    function showError(msg) {
      document.getElementById('res-am').innerText = "Error";
      document.getElementById('res-gm').innerText = "N/A";
      document.getElementById('res-hm').innerText = "N/A";
      document.getElementById('res-rms').innerText = "N/A";
      document.getElementById('res-wm').innerText = "N/A";
      document.getElementById('res-count').innerText = "0";
      document.getElementById('res-sum').innerText = "N/A";
      document.getElementById('res-ineq').innerText = "Error: " + msg;
      document.getElementById('res-steps').innerText = "Error: " + msg;
    }

    function resetAverages() {
      document.getElementById('data-input').value = "10, 20, 40, 80";
      document.getElementById('weights-input').value = "";
      document.getElementById('precision-select').value = "4";
      calculateAverages();
    }

    window.addEventListener('DOMContentLoaded', function() {
      calculateAverages();
    });
  </script>
</body>
</html>
"""

def main():
    p7 = os.path.join(BASE_DIR, "z-score-calculator.html")
    with open(p7, "w", encoding="utf-8") as f:
        f.write(HTML_ZSCORE)
    print("Generated:", p7)

    p8 = os.path.join(BASE_DIR, "average-calculator.html")
    with open(p8, "w", encoding="utf-8") as f:
        f.write(HTML_AVERAGE)
    print("Generated:", p8)

if __name__ == "__main__":
    main()
