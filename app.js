/**
 * CALCHUB GLOBAL CORE APPLICATION JAVASCRIPT
 * Handles Instant Header Search, Copy to Clipboard, PDF Export & Interactive UI
 */

const CALC_DIRECTORY = [
  { name: "BMI Calculator", url: "bmi-calculator.html", category: "Health & Fitness", icon: "⚖️" },
  { name: "Calorie Calculator (TDEE)", url: "calorie-calculator.html", category: "Health & Fitness", icon: "🔥" },
  { name: "Body Fat Calculator", url: "body-fat-calculator.html", category: "Health & Fitness", icon: "📏" },
  { name: "Ideal Body Weight Calculator", url: "ideal-weight-calculator.html", category: "Health & Fitness", icon: "❤️" },
  { name: "Daily Water Intake Calculator", url: "water-intake-calculator.html", category: "Health & Fitness", icon: "💧" },
  { name: "Loan EMI Calculator", url: "loan-emi-calculator.html", category: "Finance", icon: "🏦" },
  { name: "Compound Interest Calculator", url: "compound-interest-calculator.html", category: "Finance", icon: "📈" },
  { name: "Simple Interest Calculator", url: "simple-interest-calculator.html", category: "Finance", icon: "💰" },
  { name: "Discount & Sale Calculator", url: "discount-calculator.html", category: "Finance", icon: "🏷️" },
  { name: "Salary / Paycheck Calculator", url: "salary-calculator.html", category: "Finance", icon: "💼" },
  { name: "Percentage Calculator", url: "percentage-calculator.html", category: "Math & Utility", icon: "🔢" },
  { name: "Exact Age Calculator", url: "age-calculator.html", category: "Math & Utility", icon: "🎂" },
  { name: "College & High School GPA Calculator", url: "gpa-calculator.html", category: "Math & Utility", icon: "🎓" },
  { name: "Fraction Calculator", url: "fraction-calculator.html", category: "Math & Utility", icon: "½" },
  { name: "Ratio Calculator & Simplifier", url: "ratio-calculator.html", category: "Math & Utility", icon: "➗" },
  { name: "Ohm's Law Calculator", url: "ohms-law-calculator.html", category: "Engineering", icon: "⚡" },
  { name: "Voltage Drop Calculator", url: "voltage-drop-calculator.html", category: "Engineering", icon: "📉" },
  { name: "Cable Sizing Calculator (IEC/NEC)", url: "cable-sizing-calculator.html", category: "Engineering", icon: "🔌" },
  { name: "Resistor Color Code Calculator", url: "resistor-color-code-calculator.html", category: "Engineering", icon: "🎨" },
  { name: "Solar Panel & Battery Sizing", url: "solar-panel-sizing-calculator.html", category: "Engineering", icon: "☀️" }
];

document.addEventListener("DOMContentLoaded", () => {
  initSearch();
  initToast();
  initTOC();
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
