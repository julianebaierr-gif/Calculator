# -*- coding: utf-8 -*-
"""
Generator for Batch 29 - Part 3:
5. mean-median-mode-calculator.html
6. midpoint-calculator.html
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 5. mean-median-mode-calculator.html
HTML_MEAN_MEDIAN_MODE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mean, Median, Mode & Range Calculator - Descriptive Statistics</title>
  <meta name="description" content="Calculate the mean, median, mode, range, and statistical dispersion for any dataset. Includes step-by-step sorted values, frequency tables, and skewness analysis.">
  <link rel="canonical" href="https://calchub.org/mean-median-mode-calculator.html">
  <meta property="og:title" content="Mean, Median, Mode & Range Calculator - Statistics Solver">
  <meta property="og:description" content="Compute central tendency metrics including arithmetic mean, median, multimodal modes, range, and sum with full analytical explanations.">
  <meta property="og:url" content="https://calchub.org/mean-median-mode-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Mean, Median, Mode Calculator - Complete Statistics">
  <meta name="twitter:description" content="Free descriptive statistics solver. Calculate mean, median, mode, range, and geometric mean for any dataset with step-by-step sorting.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Mean Median Mode Calculator",
    "url": "https://calchub.org/mean-median-mode-calculator.html",
    "description": "Calculates measures of central tendency: arithmetic mean, median, multimodal mode, statistical range, and geometric mean with sorted frequency arrays.",
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
        "name": "What is the difference between mean, median, and mode?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The mean is the arithmetic average (sum of all values divided by count). The median is the physical middle value when data is sorted in ascending order. The mode is the value that appears most frequently in the dataset."
        }
      },
      {
        "@type": "Question",
        "name": "Can a dataset have more than one mode?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. A dataset can be unimodal (one mode), bimodal (two modes with equal highest frequency), multimodal (three or more modes), or have no mode at all if every value occurs with identical frequency."
        }
      },
      {
        "@type": "Question",
        "name": "Which metric of central tendency is best for skewed data?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The median is significantly more robust than the mean for skewed distributions or datasets containing severe outliers (such as income, housing prices, or healthcare length of stay), because it is not distorted by extreme values."
        }
      },
      {
        "@type": "Question",
        "name": "How do you find the median when the number of observations is even?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When the sample size n is even, there is no single middle element. The median is calculated as the arithmetic average of the two middle observations: Median = (x_(n/2) + x_(n/2 + 1)) / 2."
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
        <a href="math.html" class="active">Math & Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &gt;
      <a href="math.html">Math</a> &gt;
      <span>Mean, Median, Mode Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">📊</span>
            <h1>Mean, Median, Mode & Range Calculator</h1>
          </div>
          <p class="calc-description">
            Enter a comma, space, or line-separated list of numbers to compute the arithmetic mean, median, mode, range, sum, count, and frequency distribution.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="form-group" style="margin-bottom:1.25rem;">
              <label for="dataset_input">Data Values (Separated by commas, spaces, or newlines):</label>
              <textarea id="dataset_input" class="form-control" rows="4" placeholder="e.g. 14, 18, 22, 22, 25, 30, 31, 35, 42, 50" required>14, 18, 22, 22, 25, 30, 31, 35, 42, 50</textarea>
              <span class="help-text">Accepts positive, negative, and decimal real numbers.</span>
            </div>

            <div class="input-grid">
              <div class="form-group">
                <label for="precision">Display Decimal Places:</label>
                <select id="precision" class="form-control">
                  <option value="2">2 decimal places</option>
                  <option value="4" selected>4 decimal places</option>
                  <option value="6">6 decimal places</option>
                </select>
              </div>
              <div class="form-group" style="display:flex;align-items:flex-end;">
                <button type="button" id="btn-calculate" class="btn btn-primary" style="width:100%;" onclick="calculateStatistics()">Calculate Statistics</button>
              </div>
            </div>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Descriptive Statistics Summary</h3>
            <div class="result-highlight" id="primary-result">Mean: 28.90 | Median: 27.50</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Arithmetic Mean (\(\bar{x}\)):</span>
                <span class="res-val" id="res-mean">28.9000</span>
              </div>
              <div class="result-item">
                <span class="res-label">Median (\(\tilde{x}\)):</span>
                <span class="res-val" id="res-median">27.5000</span>
              </div>
              <div class="result-item">
                <span class="res-label">Mode(s):</span>
                <span class="res-val" id="res-mode">22 (Unimodal)</span>
              </div>
              <div class="result-item">
                <span class="res-label">Statistical Range (\(R\)):</span>
                <span class="res-val" id="res-range">36.0000</span>
              </div>
              <div class="result-item">
                <span class="res-label">Sample Count (\(n\)):</span>
                <span class="res-val" id="res-count">10</span>
              </div>
              <div class="result-item">
                <span class="res-label">Sum (\(\sum x\)):</span>
                <span class="res-val" id="res-sum">289.0000</span>
              </div>
              <div class="result-item">
                <span class="res-label">Minimum (\(x_{\min}\)):</span>
                <span class="res-val" id="res-min">14.0000</span>
              </div>
              <div class="result-item">
                <span class="res-label">Maximum (\(x_{\max}\)):</span>
                <span class="res-val" id="res-max">50.0000</span>
              </div>
            </div>

            <div class="conversion-steps" id="sorted-output">
              <!-- Sorted steps -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Theoretical Dimensions of Central Tendency in Statistics</h2>
          <p>
            In mathematical statistics and exploratory data analysis (EDA), <strong>measures of central tendency</strong> are descriptive summary metrics that aim to pinpoint the central, typical, or most representative value around which a numerical distribution clusters. The three canonical classical measures are the <strong>arithmetic mean</strong>, the <strong>median</strong>, and the <strong>mode</strong>. Together with the <strong>range</strong> (a primary measure of statistical dispersion), they form the bedrock of quantitative analysis.
          </p>

          <h2>2. Rigorous Mathematical Formulations</h2>
          
          <h3>2.1 The Arithmetic Mean (\(\bar{x}\))</h3>
          <p>
            For a discrete sample dataset comprising \(n\) real observations \(x_1, x_2, \dots, x_n\), the arithmetic mean \(\bar{x}\) is defined as the sum of all elements divided by the sample cardinality \(n\):
          </p>
          $$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i = \frac{x_1 + x_2 + \dots + x_n}{n}$$
          <p>
            The arithmetic mean possesses a pivotal mechanical property: it represents the exact center of mass of the distribution. The algebraic sum of all deviations from the mean is identically zero:
          </p>
          $$\sum_{i=1}^n (x_i - \bar{x}) = 0$$

          <h3>2.2 The Median (\(\tilde{x}\))</h3>
          <p>
            The <strong>median</strong> is the physical midpoint that divides a sorted dataset into two equal halves. To evaluate the median, the dataset must first be ordered into ascending order: \(x_{(1)} \le x_{(2)} \le \dots \le x_{(n)}\).
          </p>
          <ul>
            <li>
              <strong>Odd Sample Size (\(n\) is odd):</strong> The median is the unique central element at index \(\frac{n+1}{2}\):
              $$\tilde{x} = x_{\left(\frac{n+1}{2}\right)}$$
            </li>
            <li>
              <strong>Even Sample Size (\(n\) is even):</strong> The median is the arithmetic mean of the two middle observations at positions \(\frac{n}{2}\) and \(\frac{n}{2} + 1\):
              $$\tilde{x} = \frac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2} + 1\right)}}{2}$$
            </li>
          </ul>

          <h3>2.3 The Mode</h2>
          <p>
            The <strong>mode</strong> represents the value or set of values that appears with the highest absolute frequency in the dataset. Let \(f(x)\) denote the frequency count of value \(x\). The mode is given by:
          </p>
          $$\text{Mode} = \arg\max_{x} f(x)$$
          <ul>
            <li><strong>Unimodal:</strong> Exactly one value possesses the maximal frequency.</li>
            <li><strong>Bimodal:</strong> Exactly two distinct values tie for the highest frequency.</li>
            <li><strong>Multimodal:</strong> Three or more distinct values share the highest frequency.</li>
            <li><strong>No Mode:</strong> When all observed values in the dataset occur with equal frequency (e.g., all appear once), the dataset possesses no distinct mode.</li>
          </ul>

          <h3>2.4 Statistical Range (\(R\))</h3>
          <p>
            The <strong>range</strong> quantifies the gross dispersion width across the extreme bounds of the sample:
          </p>
          $$R = x_{\max} - x_{\min} = x_{(n)} - x_{(1)}$$

          <h2>3. Comparative Matrix: Mean vs. Median vs. Mode</h2>
          <p>
            Each central tendency indicator responds differently to underlying distribution geometries, measurement scales, and outlier anomalies:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Statistical Metric</th>
                <th>Measurement Scale</th>
                <th>Sensitivity to Outliers</th>
                <th>Mathematical Existence</th>
                <th>Optimal Use Cases</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Arithmetic Mean (\(\bar{x}\))</strong></td>
                <td>Interval, Ratio</td>
                <td>High (Extremely sensitive)</td>
                <td>Always unique</td>
                <td>Symmetric, bell-shaped Gaussian distributions, inferential testing</td>
              </tr>
              <tr>
                <td><strong>Median (\(\tilde{x}\))</strong></td>
                <td>Ordinal, Interval, Ratio</td>
                <td>Zero (Extremely robust, 50% breakdown)</td>
                <td>Always unique</td>
                <td>Skewed distributions, household income, real estate prices, hospital stays</td>
              </tr>
              <tr>
                <td><strong>Mode</strong></td>
                <td>Nominal, Ordinal, Interval, Ratio</td>
                <td>Zero (Immune to outliers)</td>
                <td>May not exist, or multiple</td>
                <td>Categorical votes, inventory sizing (most popular shoe size), discrete peaks</td>
              </tr>
              <tr>
                <td><strong>Range (\(R\))</strong></td>
                <td>Interval, Ratio</td>
                <td>Maximum (Tied directly to extremes)</td>
                <td>Always unique (\(\ge 0\))</td>
                <td>Quality control acceptance thresholds, quick span estimations</td>
              </tr>
            </tbody>
          </table>

          <h2>4. Skewness and Distribution Shape Dynamics</h2>
          <p>
            The relative spatial ordering of the mean, median, and mode serves as a qualitative diagnostic tool for detecting distributional asymmetry (skewness):
          </p>
          <ul>
            <li>
              <strong>Symmetric (Normal Distribution):</strong> The three measures coincide exactly at the central peak:
              $$\text{Mean} \approx \text{Median} \approx \text{Mode}$$
            </li>
            <li>
              <strong>Positively Skewed (Right-Tailed):</strong> Extreme high values pull the arithmetic mean upward, while the median remains centrally anchored and the mode sits at the peak:
              $$\text{Mode} < \text{Median} < \text{Mean}$$
              <em>Examples:</em> Wealth distribution, insurance claims, website visit durations.
            </li>
            <li>
              <strong>Negatively Skewed (Left-Tailed):</strong> Extreme low values drag the mean down below the median:
              $$\text{Mean} < \text{Median} < \text{Mode}$$
              <em>Examples:</em> Human life expectancy in developed nations, exam scores with a ceiling cap.
            </li>
          </ul>

          <h2>5. Practical Worked Engineering & Analytical Case Studies</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: Manufacturing Precision CNC Shaft Tolerances</h3>
            <p>
              A quality assurance engineer measures the outer diameter of ten CNC-turned transmission shafts (nominal specification \(25.000\text{ mm}\)):
              \(\{25.02, 24.98, 25.01, 25.01, 25.05, 24.99, 25.01, 25.03, 24.97, 25.03\}\).
              Calculate the mean, median, mode, and range with full step-by-step arithmetic.
            </p>
            <div class="example-body">
              <p><strong>Step 1: Order the observations ascendingly (\(n = 10\)):</strong></p>
              $$\text{Sorted} = [24.97, 24.98, 24.99, 25.01, 25.01, 25.01, 25.02, 25.03, 25.03, 25.05]$$
              <p><strong>Step 2: Arithmetic Mean (\(\bar{x}\)):</strong></p>
              $$\sum x_i = 250.10\text{ mm} \implies \bar{x} = \frac{250.10}{10} = 25.0100\text{ mm}$$
              <p><strong>Step 3: Median (\(\tilde{x}\)):</strong></p>
              <p>Since \(n = 10\) (even), take the average of elements at positions 5 and 6:</p>
              $$\tilde{x} = \frac{x_{(5)} + x_{(6)}}{2} = \frac{25.01 + 25.01}{2} = 25.0100\text{ mm}$$
              <p><strong>Step 4: Mode:</strong></p>
              <p>The value \(25.01\) occurs with frequency \(f = 3\) (all others appear once or twice). Thus, the dataset is unimodal: \(\text{Mode} = 25.01\text{ mm}\).</p>
              <p><strong>Step 5: Range (\(R\)):</strong></p>
              $$R = 25.05 - 24.97 = 0.0800\text{ mm}$$
              <p><strong>Quality Conclusion:</strong> The manufacturing process exhibits near-perfect symmetry around \(25.01\text{ mm}\) with total dispersion contained within \(80\,\mu\text{m}\).</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Clinical Research Patient Hospital Stay Duration (Skewed Data)</h3>
            <p>
              A biomedical informatics team tracks post-operative hospital stay durations (in days) for seven cardiac surgery patients: \(\{4, 5, 5, 6, 7, 8, 35\}\). Evaluate the impact of the prolonged ICU stay outlier (\(35\text{ days}\)) on the mean versus the median.
            </p>
            <div class="example-body">
              <p><strong>Step 1: Sorted data (\(n = 7\)):</strong> \([4, 5, 5, 6, 7, 8, 35]\).</p>
              <p><strong>Step 2: Arithmetic Mean:</strong></p>
              $$\bar{x} = \frac{4 + 5 + 5 + 6 + 7 + 8 + 35}{7} = \frac{70}{7} = 10.0\text{ days}$$
              <p><strong>Step 3: Median:</strong></p>
              $$\text{Position} = \frac{7+1}{2} = 4 \implies \tilde{x} = x_{(4)} = 6.0\text{ days}$$
              <p><strong>Step 4: Mode:</strong> \(\text{Mode} = 5.0\text{ days}\) (frequency 2).</p>
              <p><strong>Analytical Finding:</strong> The outlier (35 days) inflates the mean to 10 days, exceeding 85% of individual patient stays. The median of 6.0 days provides an accurate clinical expectation of typical recovery duration.</p>
            </div>
          </div>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">What is a trimmed mean?</h3>
              <div class="faq-answer">
                <p>
                  A trimmed mean (or truncated mean) discards a pre-specified percentage (e.g., 5% or 10%) of the lowest and highest values before calculating the arithmetic average. This marries the algebraic properties of the mean with the robustness of the median against extreme outliers.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How does standard deviation relate to the mean?</h3>
              <div class="faq-answer">
                <p>
                  Standard deviation measures the average root-mean-squared distance of observations from the arithmetic mean. While the mean identifies where the data centers, standard deviation reveals how tightly or broadly the observations scatter around that center. You can evaluate dispersion using our <a href="standard-deviation-calculator.html">Standard Deviation Calculator</a>.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">Can the mode be used for text or qualitative data?</h3>
              <div class="faq-answer">
                <p>
                  Yes! The mode is the only measure of central tendency applicable to nominal categorical data (e.g., blood types, car colors, voting preferences), where numerical arithmetic addition and ordering are fundamentally impossible.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">What is the geometric mean?</h3>
              <div class="faq-answer">
                <p>
                  The geometric mean of \(n\) positive numbers is the \(n\)th root of their product: \(G = \left(\prod x_i\right)^{1/n}\). It is the appropriate metric for compounding rates, investment returns, and ratios where quantities multiply rather than add. You can explore sequences using our <a href="geometric-sequence-calculator.html">Geometric Sequence Calculator</a>.
                </p>
              </div>
            </div>
          </div>
        </article>
      </div>

      <aside class="sidebar-column">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Related Math Calculators</h3>
          <ul class="sidebar-nav">
            <li><a href="standard-deviation-calculator.html">Standard Deviation Calculator</a></li>
            <li><a href="percentage-calculator.html">Percentage Calculator</a></li>
            <li><a href="gpa-calculator.html">College GPA Calculator</a></li>
            <li><a href="geometric-sequence-calculator.html">Geometric Sequence Calculator</a></li>
            <li><a href="arithmetic-sequence-calculator.html">Arithmetic Sequence Calculator</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
            <li><a href="ratio-calculator.html">Ratio Simplifier</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Advanced statistical, engineering, and mathematical calculation tools.</p>
      </div>
      <div class="footer-col">
        <h4>Discipline Hubs</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical & Engineering</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    function calculateStatistics() {
      var raw = document.getElementById("dataset_input").value;
      var prec = parseInt(document.getElementById("precision").value) || 4;

      if (!raw || !raw.trim()) {
        alert("Please enter a valid list of numbers.");
        return;
      }

      // Parse tokens
      var tokens = raw.replace(/,/g, " ").replace(/\n/g, " ").split(/\s+/);
      var nums = [];
      for (var i = 0; i < tokens.length; i++) {
        var t = tokens[i].trim();
        if (t !== "") {
          var val = parseFloat(t);
          if (!isNaN(val)) {
            nums.push(val);
          }
        }
      }

      if (nums.length === 0) {
        alert("No valid numerical values found in the input.");
        return;
      }

      var n = nums.length;
      nums.sort(function(a, b) { return a - b; });

      var sum = 0;
      var minVal = nums[0];
      var maxVal = nums[n - 1];

      for (var j = 0; j < n; j++) {
        sum += nums[j];
      }

      var mean = sum / n;

      // Median
      var median = 0;
      if (n % 2 === 1) {
        median = nums[Math.floor(n / 2)];
      } else {
        median = (nums[(n / 2) - 1] + nums[n / 2]) / 2;
      }

      // Range
      var range = maxVal - minVal;

      // Mode
      var freqMap = {};
      var maxFreq = 0;
      for (var k = 0; k < n; k++) {
        var item = nums[k];
        freqMap[item] = (freqMap[item] || 0) + 1;
        if (freqMap[item] > maxFreq) {
          maxFreq = freqMap[item];
        }
      }

      var modes = [];
      for (var key in freqMap) {
        if (freqMap[key] === maxFreq) {
          modes.push(parseFloat(key));
        }
      }

      var modeText = "";
      if (maxFreq === 1 && n > 1) {
        modeText = "No Mode (All values unique)";
      } else if (modes.length === n) {
        modeText = "No Mode (Equal frequencies)";
      } else if (modes.length === 1) {
        modeText = modes[0] + " (Frequency: " + maxFreq + ", Unimodal)";
      } else if (modes.length === 2) {
        modeText = modes.join(", ") + " (Frequency: " + maxFreq + ", Bimodal)";
      } else {
        modeText = modes.join(", ") + " (Frequency: " + maxFreq + ", Multimodal)";
      }

      document.getElementById("primary-result").innerText = "Mean: " + mean.toFixed(prec) + " | Median: " + median.toFixed(prec);
      document.getElementById("res-mean").innerText = mean.toFixed(prec);
      document.getElementById("res-median").innerText = median.toFixed(prec);
      document.getElementById("res-mode").innerText = modeText;
      document.getElementById("res-range").innerText = range.toFixed(prec);
      document.getElementById("res-count").innerText = n.toString();
      document.getElementById("res-sum").innerText = sum.toFixed(prec);
      document.getElementById("res-min").innerText = minVal.toFixed(prec);
      document.getElementById("res-max").innerText = maxVal.toFixed(prec);

      var sortedStr = nums.join(", ");
      if (sortedStr.length > 250) {
        sortedStr = sortedStr.substring(0, 250) + "... [truncated]";
      }

      var steps = "<h4>Step-by-Step Calculation Breakdown:</h4><ol>";
      steps += "<li><strong>Ascending Sorted Array (n = " + n + "):</strong> " + sortedStr + "</li>";
      steps += "<li><strong>Arithmetic Mean:</strong> &sum;x / n = " + sum.toFixed(prec) + " / " + n + " = <strong>" + mean.toFixed(prec) + "</strong></li>";
      if (n % 2 === 1) {
        steps += "<li><strong>Median (Odd n = " + n + "):</strong> Central element at position (" + n + "+1)/2 = " + ((n+1)/2) + " &rarr; <strong>" + median.toFixed(prec) + "</strong></li>";
      } else {
        steps += "<li><strong>Median (Even n = " + n + "):</strong> Average of elements at positions " + (n/2) + " and " + ((n/2)+1) + " &rarr; (" + nums[(n/2)-1] + " + " + nums[n/2] + ") / 2 = <strong>" + median.toFixed(prec) + "</strong></li>";
      }
      steps += "<li><strong>Statistical Range:</strong> Max - Min = " + maxVal + " - " + minVal + " = <strong>" + range.toFixed(prec) + "</strong></li>";
      steps += "<li><strong>Mode Analysis:</strong> " + modeText + "</li>";
      steps += "</ol>";

      document.getElementById("sorted-output").innerHTML = steps;
      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculateStatistics();
    });
  </script>
</body>
</html>
"""

# 6. midpoint-calculator.html
HTML_MIDPOINT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Midpoint Calculator - 2D & 3D Coordinates & Distance</title>
  <meta name="description" content="Calculate the exact midpoint, 3D centroid, Euclidean distance, and internal section ratio between two points in Cartesian coordinate space.">
  <link rel="canonical" href="https://calchub.org/midpoint-calculator.html">
  <meta property="og:title" content="Midpoint Calculator - 2D and 3D Coordinate Geometry">
  <meta property="og:description" content="Compute midpoints and distances in 2D and 3D Euclidean space with step-by-step vector algebra, fraction simplification, and section formulas.">
  <meta property="og:url" content="https://calchub.org/midpoint-calculator.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Midpoint Calculator - Coordinates & Distance Solver">
  <meta name="twitter:description" content="Free 2D & 3D midpoint solver. Computes coordinate midpoints, vector distance, and section ratios with full geometric derivations.">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '\\(', right: '\\)', display: false}]});"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "Midpoint Calculator",
    "url": "https://calchub.org/midpoint-calculator.html",
    "description": "Calculates 2D and 3D coordinate midpoints, Euclidean spatial distance, line slope, and internal division points with complete mathematical steps.",
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
        "name": "What is the midpoint formula in 2D coordinate geometry?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The midpoint M between Point 1 (x1, y1) and Point 2 (x2, y2) in a 2D Cartesian plane is given by the average of their respective coordinates: M = ((x1 + x2)/2, (y1 + y2)/2)."
        }
      },
      {
        "@type": "Question",
        "name": "How is the midpoint calculated in 3D space?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In 3D Euclidean space with Point 1 (x1, y1, z1) and Point 2 (x2, y2, z2), the midpoint formula averages all three orthogonal coordinates: M = ((x1 + x2)/2, (y1 + y2)/2, (z1 + z2)/2)."
        }
      },
      {
        "@type": "Question",
        "name": "What is the distance between two points?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "By the Pythagorean Theorem, the Euclidean distance d in 2D is: d = √((x2 - x1)² + (y2 - y1)²). In 3D space, d = √((x2 - x1)² + (y2 - y1)² + (z2 - z1)²)."
        }
      },
      {
        "@type": "Question",
        "name": "How does the section formula divide a line segment internally?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The section formula calculates a point P that partitions a line segment in a ratio m:n: P = ((m·x2 + n·x1)/(m + n), (m·y2 + n·y1)/(m + n)). When m = n = 1, this formula simplifies identically to the midpoint."
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
        <a href="math.html" class="active">Math & Statistics</a>
        <a href="converter.html">Converters</a>
        <a href="engineering.html">Engineering</a>
        <a href="finance.html">Finance</a>
      </nav>
    </div>
  </header>

  <main class="page-container">
    <nav class="breadcrumb-nav">
      <a href="index.html">Home</a> &gt;
      <a href="math.html">Math</a> &gt;
      <span>Midpoint Calculator</span>
    </nav>

    <div class="content-layout">
      <div class="main-column">
        <div class="calculator-card">
          <div class="calculator-header">
            <span class="calc-icon">📍</span>
            <h1>Midpoint & Distance Calculator</h1>
          </div>
          <p class="calc-description">
            Determine the exact Cartesian midpoint coordinates, Euclidean linear distance, and segment slope in 2D plane or 3D space with step-by-step vector derivations.
          </p>

          <form id="calc-form" class="calc-form" onsubmit="return false;">
            <div class="form-group" style="margin-bottom:1.25rem;">
              <label for="dim_select">Coordinate Dimensions:</label>
              <select id="dim_select" class="form-control" onchange="toggleDimension(this.value)">
                <option value="2" selected>2D Space (x, y)</option>
                <option value="3">3D Space (x, y, z)</option>
              </select>
            </div>

            <h4 style="margin:1rem 0 0.5rem;color:var(--text-primary);">Point 1 (\(P_1\))</h4>
            <div class="input-grid">
              <div class="form-group">
                <label for="x1">\(x_1\):</label>
                <input type="number" id="x1" class="form-control" value="2" step="any" placeholder="e.g. 2" required>
              </div>
              <div class="form-group">
                <label for="y1">\(y_1\):</label>
                <input type="number" id="y1" class="form-control" value="4" step="any" placeholder="e.g. 4" required>
              </div>
              <div class="form-group" id="group-z1" style="display:none;">
                <label for="z1">\(z_1\):</label>
                <input type="number" id="z1" class="form-control" value="0" step="any" placeholder="e.g. 0">
              </div>
            </div>

            <h4 style="margin:1rem 0 0.5rem;color:var(--text-primary);">Point 2 (\(P_2\))</h4>
            <div class="input-grid">
              <div class="form-group">
                <label for="x2">\(x_2\):</label>
                <input type="number" id="x2" class="form-control" value="8" step="any" placeholder="e.g. 8" required>
              </div>
              <div class="form-group">
                <label for="y2">\(y_2\):</label>
                <input type="number" id="y2" class="form-control" value="12" step="any" placeholder="e.g. 12" required>
              </div>
              <div class="form-group" id="group-z2" style="display:none;">
                <label for="z2">\(z_2\):</label>
                <input type="number" id="z2" class="form-control" value="0" step="any" placeholder="e.g. 0">
              </div>
            </div>

            <div class="input-grid" style="margin-top:1rem;">
              <div class="form-group">
                <label for="precision">Output Precision:</label>
                <select id="precision" class="form-control">
                  <option value="2">2 decimal places</option>
                  <option value="4" selected>4 decimal places</option>
                  <option value="6">6 decimal places</option>
                </select>
              </div>
              <div class="form-group" style="display:flex;align-items:flex-end;">
                <button type="button" id="btn-calculate" class="btn btn-primary" style="width:100%;" onclick="calculateMidpoint()">Compute Midpoint & Distance</button>
              </div>
            </div>
          </form>

          <div id="result-box" class="result-box" style="display:none;">
            <h3>Geometric Solution</h3>
            <div class="result-highlight" id="primary-result">Midpoint: (5.0000, 8.0000)</div>
            
            <div class="result-grid">
              <div class="result-item">
                <span class="res-label">Midpoint Coordinates (\(M\)):</span>
                <span class="res-val" id="res-midpoint">(5.0000, 8.0000)</span>
              </div>
              <div class="result-item">
                <span class="res-label">Euclidean Distance (\(d\)):</span>
                <span class="res-val" id="res-distance">10.0000</span>
              </div>
              <div class="result-item">
                <span class="res-label">2D Line Slope (\(m\)):</span>
                <span class="res-val" id="res-slope">1.3333 (\(\Delta y / \Delta x\))</span>
              </div>
              <div class="result-item">
                <span class="res-label">Vector Displacement (\(\vec{v}\)):</span>
                <span class="res-val" id="res-vector">\(\langle 6, 8 \rangle\)</span>
              </div>
            </div>

            <div class="conversion-steps" id="steps-output">
              <!-- Steps rendered dynamically -->
            </div>
          </div>
        </div>

        <article class="article-body">
          <h2>1. Mathematical Foundations of the Midpoint Theorem</h2>
          <p>
            In Euclidean analytic geometry, the <strong>midpoint</strong> of a line segment is the unique geometric point that divides the segment connecting two endpoints into two congruent segments of identical length. Equidistant from both endpoints, the midpoint represents the center of mass (centroid) of a finite two-point system with equal point masses.
          </p>

          <h2>2. Algebraic Derivations in 2D and 3D Space</h2>
          
          <h3>2.1 Two-Dimensional Cartesian Plane</h3>
          <p>
            Let \(P_1 = (x_1, y_1)\) and \(P_2 = (x_2, y_2)\) denote two arbitrary points in \(\mathbb{R}^2\). The midpoint \(M(x_m, y_m)\) is derived from the component-wise arithmetic mean:
          </p>
          $$M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)$$
          <p>
            Simultaneously, the straight-line <strong>Euclidean distance</strong> \(d\) connecting \(P_1\) and \(P_2\) is established via the Pythagorean Theorem:
          </p>
          $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
          <p>
            The slope \(m\) of the connecting line segment is:
          </p>
          $$m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} \quad (\text{for } x_1 \neq x_2)$$

          <h3>2.2 Three-Dimensional Euclidean Space</h3>
          <p>
            When extended to three-dimensional physical space \(\mathbb{R}^3\) with coordinates \(P_1 = (x_1, y_1, z_1)\) and \(P_2 = (x_2, y_2, z_2)\), the orthogonal decoupling of Cartesian axes allows calculating the midpoint by averaging the third coordinate:
          </p>
          $$M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}, \frac{z_1 + z_2}{2} \right)$$
          <p>
            The 3D spatial Euclidean distance becomes:
          </p>
          $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

          <h2>3. The Generalized Section Formula (Internal & External Division)</h2>
          <p>
            The midpoint formula is a specific symmetric case of the more general <strong>section formula</strong>. If a point \(P\) divides the line segment \(P_1 P_2\) internally in a specified positive ratio \(m : n\) (such that \(\frac{P_1 P}{P P_2} = \frac{m}{n}\)), its coordinates are given by:
          </p>
          $$P = \left( \frac{m x_2 + n x_1}{m + n}, \frac{m y_2 + n y_1}{m + n}, \frac{m z_2 + n z_1}{m + n} \right)$$
          <p>
            When the partition ratio is strictly equal (\(m = 1, n = 1\)), the fraction simplifies directly:
          </p>
          $$P = \left( \frac{1 \cdot x_2 + 1 \cdot x_1}{1 + 1}, \frac{1 \cdot y_2 + 1 \cdot y_1}{1 + 1} \right) = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right) = M$$

          <h2>4. Coordinate Geometry Reference Benchmark Table</h2>
          <p>
            The matrix below details sample endpoint coordinate pairs in 2D and 3D, presenting their exact midpoints, spatial distances, and geometric vectors:
          </p>

          <table class="data-table">
            <thead>
              <tr>
                <th>Point 1 (\(P_1\))</th>
                <th>Point 2 (\(P_2\))</th>
                <th>Dimension</th>
                <th>Exact Midpoint (\(M\))</th>
                <th>Distance (\(d\))</th>
                <th>Displacement Vector (\(\vec{v}\))</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>\((0, 0)\)</td>
                <td>\((6, 8)\)</td>
                <td>2D</td>
                <td>\((3, 4)\)</td>
                <td>10.0</td>
                <td>\(\langle 6, 8 \rangle\)</td>
              </tr>
              <tr>
                <td>\((-4, 2)\)</td>
                <td>\((4, 6)\)</td>
                <td>2D</td>
                <td>\((0, 4)\)</td>
                <td>8.9443</td>
                <td>\(\langle 8, 4 \rangle\)</td>
              </tr>
              <tr>
                <td>\((1, -3)\)</td>
                <td>\((5, 7)\)</td>
                <td>2D</td>
                <td>\((3, 2)\)</td>
                <td>10.7703</td>
                <td>\(\langle 4, 10 \rangle\)</td>
              </tr>
              <tr>
                <td>\((0, 0, 0)\)</td>
                <td>\((2, 4, 6)\)</td>
                <td>3D</td>
                <td>\((1, 2, 3)\)</td>
                <td>7.4833</td>
                <td>\(\langle 2, 4, 6 \rangle\)</td>
              </tr>
              <tr>
                <td>\((-2, 5, 8)\)</td>
                <td>\((6, -1, 2)\)</td>
                <td>3D</td>
                <td>\((2, 2, 5)\)</td>
                <td>11.6619</td>
                <td>\(\langle 8, -6, -6 \rangle\)</td>
              </tr>
              <tr>
                <td>\((10, 20, 30)\)</td>
                <td>\((30, 40, 50)\)</td>
                <td>3D</td>
                <td>\((20, 30, 40)\)</td>
                <td>34.6410</td>
                <td>\(\langle 20, 20, 20 \rangle\)</td>
              </tr>
            </tbody>
          </table>

          <h2>5. Engineering and Geospatial Applied Case Studies</h2>

          <div class="worked-example-card">
            <h3>Case Study 1: Structural Civil Engineering Truss Mid-Span Node</h3>
            <p>
              A structural engineering CAD team models a steel roof truss. The bottom chord spans between two foundation support pins located at \(P_1 = (-12.50\text{ m}, 0.00\text{ m}, 4.20\text{ m})\) and \(P_2 = (12.50\text{ m}, 0.00\text{ m}, 4.20\text{ m})\). Determine: (a) the mid-span central tie connection point coordinates, and (b) the total structural span distance.
            </p>
            <div class="example-body">
              <p><strong>Step 1: Compute 3D midpoint coordinates:</strong></p>
              $$x_m = \frac{-12.50 + 12.50}{2} = \frac{0.00}{2} = 0.00\text{ m}$$
              $$y_m = \frac{0.00 + 0.00}{2} = 0.00\text{ m}$$
              $$z_m = \frac{4.20 + 4.20}{2} = 4.20\text{ m}$$
              $$\text{Mid-Span Node } M = (0.00\text{ m}, 0.00\text{ m}, 4.20\text{ m})$$
              <p><strong>Step 2: Compute clear span distance (\(d\)):</strong></p>
              $$d = \sqrt{(12.50 - (-12.50))^2 + (0 - 0)^2 + (4.20 - 4.20)^2} = \sqrt{25.00^2} = 25.00\text{ m}$$
              <p><strong>Structural Conclusion:</strong> The central king-post vertical member must be installed exactly at coordinates \((0, 0, 4.20)\text{ m}\) to divide the \(25.00\text{ m}\) clear span symmetrically.</p>
            </div>
          </div>

          <div class="worked-example-card">
            <h3>Case Study 2: Robotics 6-DOF Manipulator Linear Path Interpolation</h3>
            <p>
              An automated welding robot must execute a straight-line seam weld between tool center point (TCP) start position \(P_1 = (140, 220)\text{ mm}\) and end position \(P_2 = (380, 540)\text{ mm}\). The trajectory planner requires an intermediate waypoint at the exact 50% midpoint to recalibrate laser seam tracking.
            </p>
            <div class="example-body">
              <p><strong>Step 1: Calculate midpoint waypoint:</strong></p>
              $$M = \left( \frac{140 + 380}{2}, \frac{220 + 540}{2} \right) = \left( \frac{520}{2}, \frac{760}{2} \right) = (260, 380)\text{ mm}$$
              <p><strong>Step 2: Calculate weld trajectory length:</strong></p>
              $$\Delta x = 380 - 140 = 240\text{ mm}, \quad \Delta y = 540 - 220 = 320\text{ mm}$$
              $$d = \sqrt{240^2 + 320^2} = \sqrt{57,600 + 102,400} = \sqrt{160,000} = 400.00\text{ mm}$$
              <p><strong>Robotics Finding:</strong> The waypoint is programmed at \((260, 380)\text{ mm}\) along a total weld trajectory of \(400\text{ mm}\).</p>
            </div>
          </div>

          <h2>6. Frequently Asked Questions (FAQ)</h2>
          <div class="faq-accordion">
            <div class="faq-item">
              <h3 class="faq-question">What is the perpendicular bisector of a segment?</h3>
              <div class="faq-answer">
                <p>
                  The perpendicular bisector is the line that passes through the midpoint of a segment at a right angle (\(90^\circ\)). Its slope is the negative reciprocal of the segment's slope: \(m_{\perp} = -1 / m\).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How do you find the other endpoint if the midpoint and one endpoint are known?</h3>
              <div class="faq-answer">
                <p>
                  To find endpoint \(P_2 = (x_2, y_2)\) given midpoint \(M = (x_m, y_m)\) and endpoint \(P_1 = (x_1, y_1)\), algebraically rearrange the midpoint formula:
                  $$x_2 = 2 x_m - x_1, \quad y_2 = 2 y_m - y_1$$
                  For example, if \(P_1 = (2, 3)\) and \(M = (5, 7)\), then \(P_2 = (2(5)-2, 2(7)-3) = (8, 11)\).
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">Does the midpoint formula work on spherical surfaces like Earth?</h3>
              <div class="faq-answer">
                <p>
                  Standard Cartesian midpoint formulas apply strictly to flat Euclidean planes. On a spherical surface like Earth, the midpoint along a great-circle geodesic route requires converting geographic latitude and longitude into 3D Cartesian vectors \((X, Y, Z)\), computing the vector average, and re-projecting back onto the sphere.
                </p>
              </div>
            </div>

            <div class="faq-item">
              <h3 class="faq-question">How does this relate to the Pythagorean Theorem?</h3>
              <div class="faq-answer">
                <p>
                  The distance formula is a direct algebraic application of the Pythagorean Theorem \(a^2 + b^2 = c^2\), where \(\Delta x\) and \(\Delta y\) represent the orthogonal legs of a right triangle, and the Euclidean distance \(d\) represents the hypotenuse. You can verify hypotenuse calculations with our <a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a>.
                </p>
              </div>
            </div>
          </div>
        </article>
      </div>

      <aside class="sidebar-column">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Related Math Calculators</h3>
          <ul class="sidebar-nav">
            <li><a href="pythagorean-theorem-calculator.html">Pythagorean Theorem Calculator</a></li>
            <li><a href="area-calculator.html">Geometric Area Calculator</a></li>
            <li><a href="circle-calculator.html">Circle Calculator</a></li>
            <li><a href="quadratic-equation-calculator.html">Quadratic Equation Calculator</a></li>
            <li><a href="scientific-notation-calculator.html">Scientific Notation Calculator</a></li>
            <li><a href="significant-figures-calculator.html">Significant Figures Calculator</a></li>
            <li><a href="mean-median-mode-calculator.html">Mean Median Mode Calculator</a></li>
            <li><a href="fraction-calculator.html">Fraction Calculator</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>CalcHub</h4>
        <p>Comprehensive engineering, geometrical, and scientific calculation tools.</p>
      </div>
      <div class="footer-col">
        <h4>Discipline Hubs</h4>
        <ul class="footer-links">
          <li><a href="index.html">All Calculators</a></li>
          <li><a href="math.html">Mathematics</a></li>
          <li><a href="converter.html">Unit Converters</a></li>
          <li><a href="engineering.html">Electrical & Engineering</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
    </div>
  </footer>

  <script>
    function toggleDimension(dim) {
      var is3D = (dim === "3");
      document.getElementById("group-z1").style.display = is3D ? "block" : "none";
      document.getElementById("group-z2").style.display = is3D ? "block" : "none";
      calculateMidpoint();
    }

    function calculateMidpoint() {
      var dim = document.getElementById("dim_select").value;
      var is3D = (dim === "3");
      var prec = parseInt(document.getElementById("precision").value) || 4;

      var x1 = parseFloat(document.getElementById("x1").value);
      var y1 = parseFloat(document.getElementById("y1").value);
      var x2 = parseFloat(document.getElementById("x2").value);
      var y2 = parseFloat(document.getElementById("y2").value);

      var z1 = is3D ? parseFloat(document.getElementById("z1").value) : 0;
      var z2 = is3D ? parseFloat(document.getElementById("z2").value) : 0;

      if (isNaN(x1) || isNaN(y1) || isNaN(x2) || isNaN(y2) || (is3D && (isNaN(z1) || isNaN(z2)))) {
        alert("Please enter valid numerical coordinates for all points.");
        return;
      }

      var xm = (x1 + x2) / 2;
      var ym = (y1 + y2) / 2;
      var zm = (z1 + z2) / 2;

      var dx = x2 - x1;
      var dy = y2 - y1;
      var dz = is3D ? (z2 - z1) : 0;

      var dist = Math.sqrt(dx * dx + dy * dy + dz * dz);

      var midStr = is3D ?
        "(" + xm.toFixed(prec) + ", " + ym.toFixed(prec) + ", " + zm.toFixed(prec) + ")" :
        "(" + xm.toFixed(prec) + ", " + ym.toFixed(prec) + ")";

      var slopeStr = "";
      if (Math.abs(dx) < 1e-12) {
        slopeStr = "Undefined (Vertical Line)";
      } else {
        slopeStr = (dy / dx).toFixed(prec);
      }

      var vecStr = is3D ?
        "&lang;" + dx.toFixed(prec) + ", " + dy.toFixed(prec) + ", " + dz.toFixed(prec) + "&rang;" :
        "&lang;" + dx.toFixed(prec) + ", " + dy.toFixed(prec) + "&rang;";

      document.getElementById("primary-result").innerText = "Midpoint: " + midStr;
      document.getElementById("res-midpoint").innerText = midStr;
      document.getElementById("res-distance").innerText = dist.toFixed(prec);
      document.getElementById("res-slope").innerText = slopeStr;
      document.getElementById("res-vector").innerHTML = vecStr;

      var steps = "<h4>Step-by-Step Geometric Derivation:</h4><ol>";
      steps += "<li><strong>X-Coordinate:</strong> (" + x1 + " + " + x2 + ") / 2 = " + (x1 + x2) + " / 2 = <strong>" + xm.toFixed(prec) + "</strong></li>";
      steps += "<li><strong>Y-Coordinate:</strong> (" + y1 + " + " + y2 + ") / 2 = " + (y1 + y2) + " / 2 = <strong>" + ym.toFixed(prec) + "</strong></li>";
      if (is3D) {
        steps += "<li><strong>Z-Coordinate:</strong> (" + z1 + " + " + z2 + ") / 2 = " + (z1 + z2) + " / 2 = <strong>" + zm.toFixed(prec) + "</strong></li>";
      }
      steps += "<li><strong>Midpoint M:</strong> <strong>" + midStr + "</strong></li>";
      steps += "<li><strong>Euclidean Distance d:</strong> &radic;[ (" + dx.toFixed(2) + ")&sup2; + (" + dy.toFixed(2) + ")&sup2;" + (is3D ? " + (" + dz.toFixed(2) + ")&sup2;" : "") + " ] = <strong>" + dist.toFixed(prec) + "</strong></li>";
      steps += "</ol>";

      document.getElementById("steps-output").innerHTML = steps;
      document.getElementById("result-box").style.display = "block";
    }

    window.addEventListener("DOMContentLoaded", function() {
      calculateMidpoint();
    });
  </script>
</body>
</html>
"""

def main():
    p5 = os.path.join(BASE_DIR, "mean-median-mode-calculator.html")
    with open(p5, "w", encoding="utf-8") as f:
        f.write(HTML_MEAN_MEDIAN_MODE)
    print(f"Generated: {p5}")

    p6 = os.path.join(BASE_DIR, "midpoint-calculator.html")
    with open(p6, "w", encoding="utf-8") as f:
        f.write(HTML_MIDPOINT)
    print(f"Generated: {p6}")

if __name__ == "__main__":
    main()
