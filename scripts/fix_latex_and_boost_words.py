# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOOSTS = {
    "discount-calculator.html": """
      <h3>Behavioral Economics of Price Elasticity & Charm Pricing ($9.99 Effect)</h3>
      <p>Beyond elementary markdown algebra, pricing strategies interact with consumer psychology and cognitive heuristics. Research in behavioral economics confirms the pervasive power of 'charm pricing'—pricing an asset at $19.99 or $99.95 rather than rounded whole-dollar increments ($20.00 or $100.00). The human brain processes multi-digit figures sequentially from left to right; encountering a leading digit of 1 instead of 2 anchors perception in an entirely different numerical tier.</p>
      <p>Furthermore, Price Elasticity of Demand ($\varepsilon_d = \frac{\% \Delta Q}{\% \Delta P}$) dictates whether discount promotions expand net operating cash flows. In price-elastic commodity markets ($|\varepsilon_d| > 1.0$), a $20\%$ discount that increases customer transaction volume by $40\%$ generates positive revenue growth. Conversely, in inelastic luxury or staple categories ($|\varepsilon_d| < 1.0$), promotional discounting erodes gross contribution margins without generating sufficient incremental sales volume.</p>
""",
    "fraction-calculator.html": """
      <h3>Fractional Exponents, Radical Expressions & Modular Congruence</h3>
      <p>Rational fractions extend seamlessly into exponentiation and continuous mathematical analysis through the definition of rational exponents. For any non-negative real base $b$ and irreducible fraction $\frac{m}{n} \in \mathbb{Q}$, power operations map into principal $n$-th radicals:</p>
      <div class="math-block">
        $$b^{m/n} = \left( b^{1/n} \right)^m = \sqrt[n]{b^m}$$
      </div>
      <p>In discrete mathematics, number theory, and modern cryptography (RSA encryption), fractional modular arithmetic evaluates division modulo a prime integer $p$. While integer division $\frac{a}{b} \pmod p$ is non-trivial, it is resolved uniquely by calculating the modular multiplicative inverse $b^{-1} \pmod p$ via the Extended Euclidean Algorithm, such that $b \cdot b^{-1} \equiv 1 \pmod p$, establishing that $\frac{a}{b} \equiv a \cdot b^{-1} \pmod p$.</p>
""",
    "percentage-calculator.html": """
      <h3>Logarithmic Returns vs Linear Percentage Changes in Quantitative Finance</h3>
      <p>In quantitative portfolio management, algorithmic trading, and time-series econometrics, arithmetic percentage returns ($R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$) present significant statistical non-additivity across consecutive temporal horizons. A sequence of arithmetic gains and losses cannot simply be summed together.</p>
      <p>To overcome this limitation, financial engineers model asset price fluctuations using continuous <strong>Logarithmic Returns ($r_t$)</strong>, defined as the natural logarithm of the price ratio:</p>
      <div class="math-block">
        $$r_t = \ln\left( \frac{P_t}{P_{t-1}} \right) = \ln(P_t) - \ln(P_{t-1})$$
      </div>
      <p>Log returns are strictly time-additive: the multi-period cumulative logarithmic return over $k$ trading intervals is the exact linear sum of per-period log returns ($r_{0,k} = \sum_{t=1}^k r_t$). For small daily price fluctuations ($|R_t| < 0.05$), the linear percentage change closely mirrors logarithmic yield ($r_t \approx R_t$).</p>
""",
    "ratio-calculator.html": """
      <h3>Stoichiometric Reaction Ratios & Chemical Mass Balance</h3>
      <p>In chemical engineering and analytical metallurgy, stoichiometric molar ratios dictate reaction mass balances and yield limits. In the synthesis of water ($2\text{H}_2 + \text{O}_2 \longrightarrow 2\text{H}_2\text{O}$), molecular hydrogen and oxygen combine in an exact $2 : 1$ molar stoichiometric proportion. When feed reactants deviate from this ratio, the reagent supplied in lesser proportional quantity acts as the <strong>Limiting Reactant</strong>, governing maximum product yield:</p>
      <div class="math-block">
        $$\text{Molar Ratio} = \frac{n_{\text{reactant 1}}}{n_{\text{reactant 2}}} = \frac{\text{Mass}_1 / M_1}{\text{Mass}_2 / M_2}$$
      </div>
      <p>Similarly, in mechanical powertrain design, gear reduction ratios ($i = \frac{z_{\text{driven}}}{z_{\text{drive}}}$) balance rotational shaft torque against angular velocity, where torque amplifies proportionally to gear ratio ($\tau_{\text{out}} = \tau_{\text{in}} \cdot i \cdot \eta$) while rotational output speed diminishes ($N_{\text{out}} = N_{\text{in}} / i$).</p>
""",
    "simple-interest-calculator.html": """
      <h3>Continuous Yield Curves & Comparison with Compound Annuities</h3>
      <p>While simple interest governs short-term liquidity instruments (commercial paper, certificates of deposit, intra-bank money market advances), financial assets held beyond 12 months capitalize interest earnings into the principal base. If an investor leaves simple interest payouts uninvested, their purchasing power degrades relative to continuous inflation:</p>
      <div class="math-block">
        $$\text{Real Terminal Purchasing Power: } A_{\text{real}} = \frac{P(1 + r \cdot t)}{(1 + i)^t}$$
      </div>
      <p>Where $i$ represents the average annualized inflation rate. If the simple interest rate $r = 5.0\%$ and annual inflation $i = 4.0\%$, an investment held for 10 years yields nominal funds $A = P(1 + 0.50) = 1.50 P$, but true inflation-adjusted capital is $A_{\text{real}} = \frac{1.50 P}{1.4802} = 1.013 P$, resulting in near-zero real purchasing power expansion over the decade!</p>
"""
}

def fix_and_boost():
    # 1. Boost the 5 files
    for filename, boost_content in BOOSTS.items():
        filepath = os.path.join(BASE_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Insert before FAQ or </article>
            faq_match = re.search(r'(<div class="faq-(container|accordion)"|<div class="faq-item"|<h2[^>]*>Frequently Asked Questions)', content)
            if faq_match:
                pos = faq_match.start()
                content = content[:pos] + boost_content + "\n\n      " + content[pos:]
            else:
                art_close = content.find("</article>")
                if art_close != -1:
                    content = content[:art_close] + boost_content + "\n    " + content[art_close:]
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Boosted {filename}")

    # 2. Fix corrupted escapes (\text, \frac, \times) across all html files
    all_html = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]
    fixed_count = 0
    for f_name in all_html:
        filepath = os.path.join(BASE_DIR, f_name)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()

        orig = c
        # Replace accidental tab+ext or formfeed+rac
        c = c.replace("\text", "\\text")
        c = c.replace("\frac", "\\frac")
        c = c.replace("\times", "\\times")
        c = c.replace("\ne", "\\ne")

        if c != orig:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(c)
            fixed_count += 1

    print(f"Fixed LaTeX formatting in {fixed_count} files.")

if __name__ == "__main__":
    fix_and_boost()
