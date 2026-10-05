/**
 * CALCHUB GLOBAL CORE APPLICATION JAVASCRIPT
 * Handles Instant Header Search, Copy to Clipboard, PDF Export & Interactive UI
 */

const CALC_DIRECTORY = [
  // Category Hubs (12)
  { name: "Health & Fitness Category Hub", url: "health.html", category: "Category Hub", icon: "⚖️" },
  { name: "Finance & Investment Category Hub", url: "finance.html", category: "Category Hub", icon: "🏦" },
  { name: "Mathematics & Utilities Category Hub", url: "math.html", category: "Category Hub", icon: "🔢" },
  { name: "Electrical & Engineering Category Hub", url: "engineering.html", category: "Category Hub", icon: "⚡" },
  { name: "Solar & Renewable Energy Category Hub", url: "solar-energy.html", category: "Category Hub", icon: "☀️" },
  { name: "Mechanical & HVAC Category Hub", url: "mechanical.html", category: "Category Hub", icon: "⚙️" },
  { name: "Civil & Construction Category Hub", url: "civil.html", category: "Category Hub", icon: "🏗️" },
  { name: "Chemical & Water Treatment Category Hub", url: "chemical.html", category: "Category Hub", icon: "🧪" },
  { name: "Fire & Life Safety Category Hub", url: "fire-safety.html", category: "Category Hub", icon: "🚨" },
  { name: "Programmer & Networking Category Hub", url: "programmer.html", category: "Category Hub", icon: "👨‍💻" },
  { name: "Date & Time Utilities Category Hub", url: "datetime.html", category: "Category Hub", icon: "📅" },
  { name: "Universal Unit Converters Category Hub", url: "converter.html", category: "Category Hub", icon: "🔄" },

  // Health & Fitness Calculators
  { name: "BMI Calculator", url: "bmi-calculator.html", category: "Health & Fitness", icon: "⚖️" },
  { name: "Calorie Calculator (TDEE)", url: "calorie-calculator.html", category: "Health & Fitness", icon: "🔥" },
  { name: "Body Fat Calculator", url: "body-fat-calculator.html", category: "Health & Fitness", icon: "📏" },
  { name: "Ideal Body Weight Calculator", url: "ideal-weight-calculator.html", category: "Health & Fitness", icon: "❤️" },
  { name: "Daily Water Intake Calculator", url: "water-intake-calculator.html", category: "Health & Fitness", icon: "💧" },

  // Finance & Investment Calculators
  { name: "Loan EMI Calculator", url: "loan-emi-calculator.html", category: "Finance", icon: "🏦" },
  { name: "Compound Interest Calculator", url: "compound-interest-calculator.html", category: "Finance", icon: "📈" },
  { name: "Simple Interest Calculator", url: "simple-interest-calculator.html", category: "Finance", icon: "💰" },
  { name: "Discount & Sale Calculator", url: "discount-calculator.html", category: "Finance", icon: "🏷️" },
  { name: "Salary / Paycheck Calculator", url: "salary-calculator.html", category: "Finance", icon: "💼" },

  // Mathematics & Utilities Calculators
  { name: "Percentage Calculator", url: "percentage-calculator.html", category: "Math & Utility", icon: "🔢" },
  { name: "Exact Age Calculator", url: "age-calculator.html", category: "Math & Utility", icon: "🎂" },
  { name: "College & High School GPA Calculator", url: "gpa-calculator.html", category: "Math & Utility", icon: "🎓" },
  { name: "Fraction Calculator", url: "fraction-calculator.html", category: "Math & Utility", icon: "½" },
  { name: "Ratio Calculator & Simplifier", url: "ratio-calculator.html", category: "Math & Utility", icon: "➗" },

  // Electrical & Engineering Calculators
  { name: "Ohm's Law Calculator", url: "ohms-law-calculator.html", category: "Engineering", icon: "⚡" },
  { name: "Voltage Drop Calculator", url: "voltage-drop-calculator.html", category: "Engineering", icon: "📉" },
  { name: "Cable Sizing Calculator (IEC/NEC)", url: "cable-sizing-calculator.html", category: "Engineering", icon: "🔌" },
  { name: "Resistor Color Code Calculator", url: "resistor-color-code-calculator.html", category: "Engineering", icon: "🎨" },
  { name: "Solar Panel & Battery Sizing", url: "solar-panel-sizing-calculator.html", category: "Engineering", icon: "☀️" },

  // Solar & Renewable Energy Calculators
  { name: "Solar Battery Bank Sizing", url: "solar-battery-bank-calculator.html", category: "Solar & Renewable", icon: "🔋" },
  { name: "Solar Inverter Sizing", url: "solar-inverter-sizing-calculator.html", category: "Solar & Renewable", icon: "⚡" },
  { name: "EV Charging Time & Power", url: "ev-charging-time-calculator.html", category: "Solar & Renewable", icon: "🔌" },

  // Mechanical & HVAC Calculators
  { name: "Cooling Load (HVAC) Sizing", url: "cooling-load-calculator.html", category: "Mechanical & HVAC", icon: "❄️" },
  { name: "Pipe Sizing & Water Flow", url: "pipe-sizing-calculator.html", category: "Mechanical & HVAC", icon: "🚰" },
  { name: "Torque & Shaft Power", url: "torque-calculator.html", category: "Mechanical & HVAC", icon: "⚙️" },

  // Civil & Construction Calculators
  { name: "Concrete Slab, Footing & Column", url: "concrete-calculator.html", category: "Civil & Construction", icon: "🏗️" },
  { name: "Rebar Weight & Grid Spacing", url: "rebar-calculator.html", category: "Civil & Construction", icon: "🔩" },

  // Chemical & Water Treatment
  { name: "Chemical Dosing Rate Calculator", url: "chemical-dosing-calculator.html", category: "Chemical & Water", icon: "🧪" },

  // Fire & Life Safety
  { name: "Smoke Detector Spacing & Layout", url: "smoke-detector-spacing-calculator.html", category: "Fire & Safety", icon: "🚨" },

  // Programmer & Networking
  { name: "IPv4 Subnet & CIDR IP Calculator", url: "subnet-calculator.html", category: "Programmer & Networking", icon: "🌐" },

  // Date & Time Utilities
  { name: "Date Difference & Business Days", url: "date-difference-calculator.html", category: "Date & Time", icon: "📅" },

  // Universal Converters
  { name: "Universal Multi-Unit Converter", url: "unit-converter.html", category: "Universal Converters", icon: "🔄" }
];

document.addEventListener("DOMContentLoaded", () => {
  initSearch();
  initToast();
  initTOC();
  initQuickCalc();
  initCategoryFilter();
  if (typeof window.rotateSidebarTools === "function") {
    window.rotateSidebarTools();
  }
});

// Search Autocomplete
function initSearch() {
  const searchInput = document.getElementById("header-search-input");
  const dropdown = document.getElementById("search-results-dropdown");
  if (!searchInput || !dropdown) return;

  searchInput.addEventListener("input", (e) => {
    const val = e.target.value.toLowerCase().trim();
    if (!val) {
      dropdown.style.display = "none";
      dropdown.innerHTML = "";
      return;
    }

    const matches = CALC_DIRECTORY.filter(c => 
      c.name.toLowerCase().includes(val) || 
      c.category.toLowerCase().includes(val)
    ).slice(0, 6);

    if (matches.length === 0) {
      dropdown.innerHTML = `<div style="padding:10px 14px;color:#64748B;font-size:0.88rem;">No matching calculators found</div>`;
    } else {
      dropdown.innerHTML = matches.map(m => `
        <a href="${m.url}" class="search-result-item">
          <span style="font-weight:600;display:flex;align-items:center;gap:6px;"><span>${m.icon}</span> ${m.name}</span>
          <span class="search-result-category">${m.category}</span>
        </a>
      `).join("");
    }
    dropdown.style.display = "block";
  });

  // Close on outside click
  document.addEventListener("click", (e) => {
    if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
      dropdown.style.display = "none";
    }
  });

  // Hotkey Ctrl+K / Cmd+K
  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      searchInput.focus();
    }
  });
}

// Toast notification helper
function initToast() {
  if (document.getElementById("toast-notice")) return;
  const toast = document.createElement("div");
  toast.id = "toast-notice";
  toast.className = "toast-notice";
  toast.innerHTML = `<span id="toast-msg">Copied to clipboard!</span>`;
  document.body.appendChild(toast);
}

window.showToast = function(msg = "Copied to clipboard!") {
  const toast = document.getElementById("toast-notice");
  const msgEl = document.getElementById("toast-msg");
  if (!toast || !msgEl) return;
  msgEl.textContent = msg;
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 2500);
};

window.copyToClipboard = function(text, successMsg = "Result copied to clipboard!") {
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text).then(() => showToast(successMsg));
  } else {
    const input = document.createElement("textarea");
    input.value = text;
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    document.body.removeChild(input);
    showToast(successMsg);
  }
};

window.printCalculatorReport = function() {
  window.print();
};

// Smooth Table of Contents Scrolling
function initTOC() {
  document.querySelectorAll(".toc-list a").forEach(link => {
    link.addEventListener("click", (e) => {
      const targetId = link.getAttribute("href");
      if (targetId && targetId.startsWith("#")) {
        const el = document.querySelector(targetId);
        if (el) {
          e.preventDefault();
          el.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }
    });
  });
}

// Interactive Hero Quick Calculator
function initQuickCalc() {
  const keysContainer = document.getElementById("quick-calc-keys");
  const valEl = document.getElementById("quick-calc-val");
  const exprEl = document.getElementById("quick-calc-expr");
  if (!keysContainer || !valEl) return;

  const KEYS = ["AC", "⌫", "%", "÷", "7", "8", "9", "×", "4", "5", "6", "−", "1", "2", "3", "+", "0", ".", "="];
  let expr = "";
  let justEvaluated = false;

  keysContainer.innerHTML = "";
  KEYS.forEach(k => {
    const btn = document.createElement("div");
    btn.textContent = k;
    let cls = "q-key";
    if (["÷", "×", "−", "+"].includes(k)) cls += " op";
    else if (k === "=") cls += " eq";
    else if (["AC", "⌫", "%"].includes(k)) cls += " fn";
    btn.className = cls;

    btn.addEventListener("click", () => handlePress(k));
    keysContainer.appendChild(btn);
  });

  function handlePress(k) {
    if (k === "AC") {
      expr = "";
      valEl.textContent = "0";
      if (exprEl) exprEl.innerHTML = "&nbsp;";
      return;
    }
    if (k === "⌫") {
      expr = expr.slice(0, -1);
      valEl.textContent = expr || "0";
      return;
    }
    if (k === "=") {
      if (!expr) return;
      try {
        let clean = expr.replace(/%/g, "/100").replace(/×/g, "*").replace(/÷/g, "/").replace(/−/g, "-");
        if (!/^[0-9+\-*/.() ]+$/.test(clean)) throw new Error("Invalid");
        let result = Function('"use strict";return (' + clean + ')')();
        if (!isFinite(result)) throw new Error("Math error");
        if (exprEl) exprEl.textContent = expr + " =";
        let displayVal = Math.round(result * 100000000) / 100000000;
        valEl.textContent = String(displayVal);
        expr = String(displayVal);
        justEvaluated = true;
      } catch (err) {
        valEl.textContent = "Error";
        expr = "";
      }
      return;
    }

    if (justEvaluated && /[0-9.]/.test(k)) {
      expr = "";
    }
    justEvaluated = false;

    // Prevent double operators
    const lastChar = expr.slice(-1);
    const ops = ["+", "−", "×", "÷"];
    if (ops.includes(k) && ops.includes(lastChar)) {
      expr = expr.slice(0, -1) + k;
    } else {
      expr += k;
    }
    valEl.textContent = expr;
  }
}

// Interactive Category Filter Bar
function initCategoryFilter() {
  const filterPills = document.querySelectorAll(".category-filter-nav .filter-pill");
  const sections = document.querySelectorAll(".category-block-section");
  if (!filterPills.length) return;

  filterPills.forEach(pill => {
    pill.addEventListener("click", () => {
      filterPills.forEach(p => p.classList.remove("active"));
      pill.classList.add("active");

      const cat = pill.getAttribute("data-cat");
      sections.forEach(sec => {
        if (cat === "all" || sec.getAttribute("data-cat") === cat) {
          sec.style.display = "block";
        } else {
          sec.style.display = "none";
        }
      });
    });
  });
}

// Global Dynamic Rotating Top 5 Sidebar System
window.rotateSidebarTools = function(btn) {
  const widget = btn ? btn.closest('.sidebar-widget') : document.querySelector('.sidebar-widget');
  if (!widget) return;
  const poolScript = widget.querySelector('.sidebar-pool-data');
  const list = widget.querySelector('.sidebar-tools-list');
  if (!poolScript || !list) return;

  try {
    const pool = JSON.parse(poolScript.textContent);
    const currentPath = window.location.pathname.split('/').pop() || '';
    const available = pool.filter(item => item.slug !== currentPath);
    if (!available.length) return;

    for (let i = available.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [available[i], available[j]] = [available[j], available[i]];
    }

    const selected = available.slice(0, 5);
    list.innerHTML = selected.map(item => `
      <li>
        <a href="${item.slug}" class="sidebar-tool-item">
          <span class="st-icon">${item.icon}</span>
          <div class="st-info">
            <span class="st-title">${item.title}</span>
            <span class="st-desc">${item.desc}</span>
          </div>
          <span class="st-arrow">›</span>
        </a>
      </li>
    `).join('');

    if (btn) {
      btn.classList.add('shuffling');
      setTimeout(() => btn.classList.remove('shuffling'), 400);
    }
  } catch (err) {
    console.error('Sidebar rotation error:', err);
  }
};
