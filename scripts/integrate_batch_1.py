"""
Integrates Batch 1 (6 new tools) into hubs, index.html, sidebars, and sitemap.
"""
import glob
import re
import os

def update_hubs():
    # 1. Update engineering.html
    with open("engineering.html", "r", encoding="utf-8") as f:
        eng = f.read()

    # Add Conduit Fill & Motor Starting Current cards if not present
    new_eng_cards = """        <!-- 7. Conduit Fill Calculator -->
        <div class="calculator-card" style="border-top: 3px solid #D97706;">
          <div class="calc-card-icon" style="background:#FFFBEB;color:#D97706;">🔌</div>
          <h4 class="calc-card-title"><a href="conduit-fill-calculator.html">Conduit Fill (NEC Ch. 9)</a></h4>
          <p class="calc-card-desc">Calculate electrical raceway capacity across EMT, PVC, and RMC per NEC Chapter 9 Table 1 (40% fill rule) with jam ratio verification.</p>
          <div class="calc-card-meta">
            <span class="meta-tag">NEC Tables 1 &amp; 4</span>
            <span class="meta-tag">Jam Ratio</span>
          </div>
          <a href="conduit-fill-calculator.html" class="btn btn-primary" style="margin-top:1rem;display:inline-block;padding:0.45rem 1rem;font-size:0.85rem;">Open Calculator &rarr;</a>
        </div>

        <!-- 8. Motor Starting Current Calculator -->
        <div class="calculator-card" style="border-top: 3px solid #D97706;">
          <div class="calc-card-icon" style="background:#FFFBEB;color:#D97706;">⚙️</div>
          <h4 class="calc-card-title"><a href="motor-starting-current-calculator.html">Motor Starting Current</a></h4>
          <p class="calc-card-desc">Calculate 3-phase locked rotor inrush current (LRC) using NEMA Code Letters (A-V) and compare DOL, Star-Delta, Soft Starter, and VFD methods.</p>
          <div class="calc-card-meta">
            <span class="meta-tag">NEMA MG 1</span>
            <span class="meta-tag">NEC 430.7(B)</span>
          </div>
          <a href="motor-starting-current-calculator.html" class="btn btn-primary" style="margin-top:1rem;display:inline-block;padding:0.45rem 1rem;font-size:0.85rem;">Open Calculator &rarr;</a>
        </div>
      </div>"""

    if "conduit-fill-calculator.html" not in eng:
        eng = eng.replace("      </div>\n    </div>\n  </main>", new_eng_cards + "\n    </div>\n  </main>")
        eng = re.sub(r'6 Tools\b', '8 Tools', eng)
        eng = re.sub(r'suite of 6\b', 'suite of 8', eng)
        with open("engineering.html", "w", encoding="utf-8") as f:
            f.write(eng)
        print("Updated engineering.html to 8 tools")

    # 2. Update mechanical.html
    with open("mechanical.html", "r", encoding="utf-8") as f:
        mech = f.read()

    new_mech_cards = """        <!-- 4. Pump Head & Flow Calculator -->
        <div class="calculator-card" style="border-top: 3px solid #0891B2;">
          <div class="calc-card-icon" style="background:#ECFEFF;color:#0891B2;">🌊</div>
          <h4 class="calc-card-title"><a href="pump-head-calculator.html">Pump Head (TDH &amp; Flow)</a></h4>
          <p class="calc-card-desc">Compute Total Dynamic Head (TDH), static elevation lift, Hazen-Williams pipe friction, fitting losses, and drive motor brake horsepower (BHP).</p>
          <div class="calc-card-meta">
            <span class="meta-tag">Darcy-Weisbach</span>
            <span class="meta-tag">Hydraulic Inst</span>
          </div>
          <a href="pump-head-calculator.html" class="btn btn-primary" style="margin-top:1rem;display:inline-block;padding:0.45rem 1rem;font-size:0.85rem;">Open Calculator &rarr;</a>
        </div>

        <!-- 5. Gear Ratio Calculator -->
        <div class="calculator-card" style="border-top: 3px solid #0891B2;">
          <div class="calc-card-icon" style="background:#ECFEFF;color:#0891B2;">⚙️</div>
          <h4 class="calc-card-title"><a href="gear-ratio-calculator.html">Gear Ratio &amp; Speed</a></h4>
          <p class="calc-card-desc">Calculate gear train velocity reduction ratios, output shaft RPM, torque multiplication, and mechanical advantage for simple and compound sets.</p>
          <div class="calc-card-meta">
            <span class="meta-tag">AGMA / ISO 6336</span>
            <span class="meta-tag">Torque Ratio</span>
          </div>
          <a href="gear-ratio-calculator.html" class="btn btn-primary" style="margin-top:1rem;display:inline-block;padding:0.45rem 1rem;font-size:0.85rem;">Open Calculator &rarr;</a>
        </div>
      </div>"""

    if "pump-head-calculator.html" not in mech:
        mech = mech.replace("      </div>\n    </div>\n  </main>", new_mech_cards + "\n    </div>\n  </main>")
        mech = re.sub(r'3 Tools\b', '5 Tools', mech)
        mech = re.sub(r'suite of 3\b', 'suite of 5', mech)
        with open("mechanical.html", "w", encoding="utf-8") as f:
            f.write(mech)
        print("Updated mechanical.html to 5 tools")

    # 3. Update finance.html
    with open("finance.html", "r", encoding="utf-8") as f:
        fin = f.read()

    new_fin_cards = """        <!-- 8. Car Loan Calculator -->
        <div class="calculator-card" style="border-top: 3px solid #2563EB;">
          <div class="calc-card-icon" style="background:#EFF6FF;color:#2563EB;">🚗</div>
          <h4 class="calc-card-title"><a href="car-loan-calculator.html">Car Loan &amp; Financing</a></h4>
          <p class="calc-card-desc">Estimate monthly auto loan payments, trade-in sales tax savings, dealer fees, and total interest amortization under TILA standards.</p>
          <div class="calc-card-meta">
            <span class="meta-tag">TILA Reg Z</span>
            <span class="meta-tag">Trade-In Tax</span>
          </div>
          <a href="car-loan-calculator.html" class="btn btn-primary" style="margin-top:1rem;display:inline-block;padding:0.45rem 1rem;font-size:0.85rem;">Open Calculator &rarr;</a>
        </div>

        <!-- 9. ROI Calculator -->
        <div class="calculator-card" style="border-top: 3px solid #2563EB;">
          <div class="calc-card-icon" style="background:#EFF6FF;color:#2563EB;">📈</div>
          <h4 class="calc-card-title"><a href="roi-calculator.html">ROI &amp; Annualized CAGR</a></h4>
          <p class="calc-card-desc">Measure cumulative Return on Investment, annualized geometric growth (CAGR), holding period gains, and net capital yields per CFA standards.</p>
          <div class="calc-card-meta">
            <span class="meta-tag">CFA Institute</span>
            <span class="meta-tag">CAGR Formula</span>
          </div>
          <a href="roi-calculator.html" class="btn btn-primary" style="margin-top:1rem;display:inline-block;padding:0.45rem 1rem;font-size:0.85rem;">Open Calculator &rarr;</a>
        </div>
      </div>"""

    if "car-loan-calculator.html" not in fin:
        fin = fin.replace("      </div>\n    </div>\n  </main>", new_fin_cards + "\n    </div>\n  </main>")
        fin = re.sub(r'7 Tools\b', '9 Tools', fin)
        fin = re.sub(r'suite of 7\b', 'suite of 9', fin)
        with open("finance.html", "w", encoding="utf-8") as f:
            f.write(fin)
        print("Updated finance.html to 9 tools")

def update_index_page():
    with open("index.html", "r", encoding="utf-8") as f:
        idx = f.read()

    # Update counts: 40 -> 46
    idx = idx.replace("Explore 40+ specialized calculators across 12 core disciplines.", "Explore 46+ specialized calculators across 12 core disciplines.")
    idx = idx.replace("All 40 calculators across all 12 disciplines are 100% free", "All 46 calculators across all 12 disciplines are 100% free")
    idx = idx.replace("The platform provides <strong>40 specialized precision calculators</strong>", "The platform provides <strong>46 specialized precision calculators</strong>")
    idx = idx.replace("Explore all 40 certified calculators organized across 12 specialized disciplines.", "Explore all 46 certified calculators organized across 12 specialized disciplines.")

    # Chips
    idx = idx.replace('🏦 Finance (7)</a>', '🏦 Finance (9)</a>')
    idx = idx.replace('⚡ Electrical (6)</a>', '⚡ Electrical (8)</a>')
    idx = idx.replace('⚙️ Mechanical (3)</a>', '⚙️ Mechanical (5)</a>')

    # Card badges & lists:
    # Finance card badge
    idx = idx.replace("""          <div class="cat-icon-box" style="background:#EFF6FF;border-color:#BFDBFE;">🏦</div>
          <span class="cat-count-badge" style="background:#EFF6FF;color:#2563EB;border-color:#BFDBFE;">7 Tools</span>""", """          <div class="cat-icon-box" style="background:#EFF6FF;border-color:#BFDBFE;">🏦</div>
          <span class="cat-count-badge" style="background:#EFF6FF;color:#2563EB;border-color:#BFDBFE;">9 Tools</span>""")

    # Electrical card badge
    idx = idx.replace("""          <div class="cat-icon-box" style="background:#FFFBEB;border-color:#FDE68A;">⚡</div>
          <span class="cat-count-badge" style="background:#FFFBEB;color:#D97706;border-color:#FDE68A;">6 Tools</span>""", """          <div class="cat-icon-box" style="background:#FFFBEB;border-color:#FDE68A;">⚡</div>
          <span class="cat-count-badge" style="background:#FFFBEB;color:#D97706;border-color:#FDE68A;">8 Tools</span>""")

    # Mechanical card badge
    idx = idx.replace("""          <div class="cat-icon-box" style="background:#ECFEFF;border-color:#A5F3FC;">⚙️</div>
          <span class="cat-count-badge" style="background:#ECFEFF;color:#0891B2;border-color:#A5F3FC;">3 Tools</span>""", """          <div class="cat-icon-box" style="background:#ECFEFF;border-color:#A5F3FC;">⚙️</div>
          <span class="cat-count-badge" style="background:#ECFEFF;color:#0891B2;border-color:#A5F3FC;">5 Tools</span>""")

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(idx)
    print("Updated index.html counts")

if __name__ == "__main__":
    update_hubs()
    update_index_page()
