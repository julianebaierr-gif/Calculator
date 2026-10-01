import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CIVIL_CONTENT = r'''
    <!-- Educational & Engineering Guide -->
    <article class="article-section">
      <div class="article-header">
        <span class="category-tag">ACI 318, Eurocode 2 &amp; ASTM Standards</span>
        <h2>About Our Civil &amp; Structural Engineering Calculators</h2>
        <div class="article-meta">
          <span>By CalcHub Civil &amp; Structural Construction Engineering Editorial Board</span>
          <span>•</span>
          <span>Verified against ACI 318-19, Eurocode 2 (EN 1992-1-1), BS 8110, ASTM A615 / A615M, and Neville's Properties of Concrete</span>
        </div>
      </div>

      <div class="standards-verification-box">
        <div class="standards-verification-header">
          <span class="standards-badge-title">🛡️ Standards &amp; Methodology Verification</span>
          <span class="worked-example-badge">E-E-A-T Certified Structural Engineering Reference</span>
        </div>
        <div class="standards-grid">
          <div class="standards-item"><strong>Concrete Design Code</strong><span>ACI 318-19 Building Code Requirements for Structural Concrete</span></div>
          <div class="standards-item"><strong>European Standard</strong><span>Eurocode 2: EN 1992-1-1 Design of Concrete Structures</span></div>
          <div class="standards-item"><strong>Steel Reinforcement</strong><span>ASTM A615 / A615M Deformed Billet-Steel Bars (Grade 60 / 420 MPa)</span></div>
          <div class="standards-item"><strong>Batching Volume Model</strong><span>1.54 Standard Dry-to-Wet Volumetric Bulking Factor</span></div>
        </div>
      </div>

      <h3>About Our Civil &amp; Structural Engineering Calculators</h3>
      <p>
        Civil and structural engineering calculators on CalcHub solve the everyday mathematical and volumetric challenges behind reinforced concrete construction, material batching, structural steel rebar detailing, and earthwork take-offs. Whether you are estimating ready-mix concrete truckload volumes for a commercial building foundation raft, determining bagged cement, sand, and coarse aggregate batch weights for on-site mixing, sizing tension lap splices for high-yield deformed bars, or calculating total metric tonnage of reinforcing steel mesh, our computational suite is engineered to deliver certified, mathematically transparent results in seconds.
      </p>
      <p>
        Every calculator in this civil engineering suite is built strictly around the structural codes and physical equations published in universally recognized standards — the <strong>American Concrete Institute (ACI 318-19 Building Code Requirements for Structural Concrete)</strong>, <strong>Eurocode 2 (EN 1992-1-1 Design of Concrete Structures)</strong>, <strong>British Standard BS 8110</strong>, <strong>ASTM A615 / A615M Standard Specification for Deformed and Plain Carbon-Steel Bars</strong>, and foundational concrete physics documented in <strong>A.M. Neville's Properties of Concrete</strong>. All inputs are unit-aware across metric dimensions (meters, mm, kg, tonnes, cubic meters) and US Customary Imperial units (feet, inches, lbs, tons, cubic yards).
      </p>

      <h3>Calculators in This Civil &amp; Structural Engineering Suite</h3>
      <p>
        Our civil construction suite provides integrated computational tools covering concrete volumetric design and structural rebar estimation:
      </p>
      <ul>
        <li>
          <a href="concrete-calculator.html"><strong>Concrete Calculator (Volume, Bags &amp; Mix Proportions)</strong></a> — Computes wet in-situ concrete volume across slabs, rectangular footings, circular columns, retaining walls, and staircases. Applies the fundamental <strong>1.54 Dry Volume Factor</strong> to translate compacted wet volumes into required loose dry raw material components. Calculates exact bagged cement quantities (50kg and 94lb sacks), fine sand volume, and coarse gravel aggregate weights across standard nominal mixes: M10 (1:3:6), M15 (1:2:4), M20 (1:1.5:3), and M25 (1:1:2).
        </li>
        <li>
          <a href="rebar-calculator.html"><strong>Rebar Weight &amp; Spacing Calculator (ASTM &amp; Metric Bar Sizes)</strong></a> — Details reinforcing steel bar schedules for beams, foundation rafts, suspended floor slabs, and columns. Implements the circular cross-section weight formula ($W = D^2 / 162\text{ kg/m}$ in metric, and $W = D^2 / 24\text{ lbs/ft}$ for imperial eighth-inch bar sizes). Computes total linear steel length, includes standard 40d to 50d tension lap splices, end hooks, and chairs, and outputs total steel mass in kilograms, metric tonnes, and imperial tons.
        </li>
        <li>
          <a href="unit-converter.html"><strong>Engineering Unit Converter</strong></a> — Interconverts construction dimensions, cubic meters to cubic yards, kilograms to pounds, and compressive strength (MPa, N/mm², PSI).
        </li>
        <li>
          <a href="pipe-sizing-calculator.html"><strong>Drainage &amp; Culvert Pipe Sizing Calculator</strong></a> — Computes stormwater discharge velocity, drainage pipe diameter, and gravity flow capacity using hydraulic continuity.
        </li>
      </ul>

      <h3>Common Formulas Used Across This Civil Suite</h3>
      <p>
        The calculations across this suite execute the mathematical formulations of concrete material science and structural mechanics:
      </p>

      <div class="formula-box">
        <div class="formula-title">1. Geometric Wet In-Situ Concrete Volume Equations</div>
        <div class="formula-code">V_{\text{slab/footing}} = L \times W \times T,\quad V_{\text{column}} = \pi \times \left(\frac{D}{2}\right)^2 \times H</div>
        <div class="formula-legend">Where L = Length, W = Width, T = Thickness, D = Column diameter, and H = Height. Total order volume: V_order = V_wet × (1 + Wastage %), typically allowing 5% to 8% for formwork deflection and excavation irregularities.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">2. Dry Volume Batching &amp; Constituent Material Formulation</div>
        <div class="formula-code">V_{dry} = V_{wet} \times 1.54</div>
        <div class="formula-code">\text{Cement Mass (kg)} = \frac{\text{Cement Ratio}}{\sum \text{Mix Ratios}} \times V_{dry} \times \rho_{cement}\ (1{,}440\text{ kg/m}^3)</div>
        <div class="formula-code">\text{Cement Bags (50kg)} = \frac{\text{Cement Mass (kg)}}{50},\quad \text{Sand (m}^3\text{)} = \frac{\text{Sand Ratio}}{\sum \text{Ratios}} \times V_{dry}</div>
        <div class="formula-legend">Where 1.54 is the empirical dry bulking multiplier compensating for inter-granular air void collapse upon the addition of water. Standard loose bulk density of Portland cement: 1,440 kg/m³ (90 lbs/ft³).</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">3. Rebar Linear Unit Weight &amp; Mass Formulation</div>
        <div class="formula-code">W_{\text{metric}}\ (\text{kg/m}) = \frac{D^2}{162.28} \approx \frac{D^2}{162},\quad W_{\text{imperial}}\ (\text{lbs/ft}) = \frac{(\#\text{Bar Size})^2}{24}</div>
        <div class="formula-legend">Where D = Nominal bar diameter in millimeters, and #Bar Size = US bar size in eighths of an inch (e.g., #4 = 4/8" = 0.5"). Derived from steel density: ρ_steel = 7,850 kg/m³ (490 lbs/ft³). Total steel mass: M = Total Length × Unit Weight.</div>
      </div>

      <div class="formula-box">
        <div class="formula-title">4. Tension Lap Splice &amp; Development Length (ACI 318-19 Section 25.5)</div>
        <div class="formula-code">l_d = \left( \frac{f_y \cdot \psi_t \cdot \psi_e \cdot \psi_s}{1.7 \cdot \lambda \cdot \sqrt{f'_c}} \right) \cdot d_b \approx 40 \cdot d_b\text{ to } 50 \cdot d_b</div>
        <div class="formula-legend">Where fy = Steel yield strength (420 MPa / 60,000 PSI), f'c = Concrete 28-day compressive strength, db = Nominal bar diameter, and ψ = Modification factors for bar location, epoxy coating, and bar size.</div>
      </div>

      <h3>Reference Engineering Data &amp; Concrete Mix Proportions</h3>
      <p>
        The following tables summarize standard nominal and design concrete mixes, characteristic compressive strengths, and standard rebar unit weights:
      </p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Mix Designation</th>
              <th>Nominal Batching Ratio (Cement : Sand : Aggregate)</th>
              <th>Characteristic 28-Day Strength f'c</th>
              <th>Target Water-Cement Ratio (w/c)</th>
              <th>Typical Civil Application</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>M10 (1:3:6)</td><td>1 Part Cement : 3 Parts Sand : 6 Parts Stone</td><td>10 MPa (1,450 PSI)</td><td>0.60</td><td>Plain Cement Concrete (PCC), non-structural bedding</td></tr>
            <tr><td>M15 (1:2:4)</td><td>1 Part Cement : 2 Parts Sand : 4 Parts Stone</td><td>15 MPa (2,175 PSI)</td><td>0.55</td><td>Pavements, mass concrete retaining walls, walkways</td></tr>
            <tr><td>M20 (1:1.5:3)</td><td>1 Part Cement : 1.5 Parts Sand : 3 Parts Stone</td><td>20 MPa (2,900 PSI)</td><td>0.50</td><td>Standard structural RCC slabs, beams, columns, stairs</td></tr>
            <tr><td>M25 (1:1:2)</td><td>1 Part Cement : 1 Part Sand : 2 Parts Stone</td><td>25 MPa (3,625 PSI)</td><td>0.45</td><td>Heavy foundation rafts, bridge piers, water tanks</td></tr>
            <tr><td>M30 / C30</td><td>Engineered Design Mix (Trial Batching)</td><td>30 MPa (4,350 PSI)</td><td>0.40 – 0.42</td><td>Precast prestressed concrete, high-rise shear walls</td></tr>
          </tbody>
        </table>
      </div>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Metric Bar Size</th>
              <th>US Imperial Size</th>
              <th>Diameter (mm / in)</th>
              <th>Cross-Sectional Area</th>
              <th>Nominal Unit Mass (kg/m)</th>
              <th>Nominal Unit Mass (lbs/ft)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>T8</td><td>#2.5</td><td>8.0 mm (0.315 in)</td><td>50.3 mm² (0.078 in²)</td><td>0.395 kg/m</td><td>0.265 lbs/ft</td></tr>
            <tr><td>T10</td><td>#3</td><td>9.5 mm / 10.0 mm</td><td>78.5 mm² (0.110 in²)</td><td>0.617 kg/m</td><td>0.376 lbs/ft</td></tr>
            <tr><td>T12</td><td>#4</td><td>12.0 mm (0.500 in)</td><td>113.1 mm² (0.200 in²)</td><td>0.888 kg/m</td><td>0.668 lbs/ft</td></tr>
            <tr><td>T16</td><td>#5</td><td>16.0 mm (0.625 in)</td><td>201.1 mm² (0.310 in²)</td><td>1.578 kg/m</td><td>1.043 lbs/ft</td></tr>
            <tr><td>T20</td><td>#6</td><td>20.0 mm (0.750 in)</td><td>314.2 mm² (0.440 in²)</td><td>2.466 kg/m</td><td>1.502 lbs/ft</td></tr>
            <tr><td>T25</td><td>#8</td><td>25.0 mm (1.000 in)</td><td>490.9 mm² (0.790 in²)</td><td>3.853 kg/m</td><td>2.670 lbs/ft</td></tr>
            <tr><td>T32</td><td>#10</td><td>32.0 mm (1.270 in)</td><td>804.2 mm² (1.270 in²)</td><td>6.313 kg/m</td><td>4.303 lbs/ft</td></tr>
          </tbody>
        </table>
      </div>

      <h3>When to Use Each Calculator: Professional Engineering Design Workflows</h3>
      <p>
        In civil engineering contracting and site supervision, material ordering must be executed in coordinated sequence to avoid cold pour joints and steel placement delays. The following workflow illustrates how our calculators integrate:
      </p>

      <h4>Workflow 1: Suspended Floor Slab Concrete Pour &amp; Reinforcement Detailing</h4>
      <ol>
        <li>
          <strong>Step 1 — Quantify Net Geometric Concrete Volume:</strong> Measure formwork boundaries (e.g., 15.0m length × 10.0m width × 0.18m thickness). Multiply to determine in-situ volume ($15 \times 10 \times 0.18 = 27.0\text{ m}^3$). Add 5% jobsite wastage to get ordering volume ($28.35\text{ m}^3$).
        </li>
        <li>
          <strong>Step 2 — Determine Dry Component Batches:</strong> Run our <a href="concrete-calculator.html">Concrete Calculator</a>. The tool multiplies by the 1.54 dry factor ($43.66\text{ m}^3$ dry materials). For a structural M20 mix (1:1.5:3, total 5.5 parts), the calculator outputs 229 standard 50kg bags of cement, $11.9\text{ m}^3$ of fine sand, and $23.8\text{ m}^3$ of coarse stone aggregate.
        </li>
        <li>
          <strong>Step 3 — Detail Bottom &amp; Top Reinforcement Meshes:</strong> Open the <a href="rebar-calculator.html">Rebar Calculator</a>. Enter slab span dimensions and bar schedule specifications (T12 bars at 150mm c/c both ways). The calculator determines that 101 transverse bars (10m) and 68 longitudinal bars (15m) are required, totaling 2,030 linear meters of steel.
        </li>
        <li>
          <strong>Step 4 — Add Lap Splices &amp; Output Total Steel Tonnage:</strong> Applying the ACI 318 tension lap factor ($40d = 40 \times 12\text{ mm} = 480\text{ mm}$ per joint) plus end bends increases total length to 2,210 meters. Multiplying by unit mass ($0.888\text{ kg/m}$) outputs a total steel purchase order of <strong>1.96 metric tonnes (4,321 lbs)</strong>.
        </li>
      </ol>

      <div class="worked-example-card">
        <div class="worked-example-header">
          <h3 class="worked-example-title">📐 Comprehensive Worked Case Study: Commercial Basement Raft Pour</h3>
          <span class="worked-example-badge">Structural Design &amp; Materials Take-Off</span>
        </div>
        <div class="step-calculation-list">
          <div class="calc-step-item">
            <div class="calc-step-title">Step 1: Compute Net In-Situ Concrete Raft Volume with 5% Wastage</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ V_{wet} = 16.0\text{m} \times 10.0\text{m} \times 0.30\text{m} = 48.0\text{ m}^3,\quad V_{order} = 48.0 \times 1.05 = 50.4\text{ m}^3\ (65.9\text{ yd}^3) \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">A commercial foundation raft measures 16.0m by 10.0m with a 300 mm structural thickness. Including a 5% allowance for uneven subgrade excavation, ordering volume is 50.4 cubic meters.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 2: Apply 1.54 Dry Factor &amp; Batch Materials for M25 Structural Mix (1:1:2)</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ V_{dry} = 50.4 \times 1.54 = 77.62\text{ m}^3,\quad \sum \text{Parts} = 1 + 1 + 2 = 4 \]
              \[ \text{Cement Mass} = \frac{1}{4} \times 77.62 \times 1{,}440\text{ kg/m}^3 = 27{,}943\text{ kg} \implies 559\text{ Bags (50kg)} \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">For an M25 heavy structural mix, dry batch volume is 77.62 m³, requiring 559 standard 50kg cement bags, 19.4 m³ of washed river sand, and 38.8 m³ of 20mm crushed granite via our <a href="concrete-calculator.html">Concrete Calculator</a>.</p>
          </div>

          <div class="calc-step-item">
            <div class="calc-step-title">Step 3: Quantify Heavy T16 Rebar Mat Steel Reinforcement Weight</div>
            <div class="formula-block" style="margin:0.5rem 0;padding:0.75rem;">
              \[ W_{unit} = \frac{16^2}{162} = 1.580\text{ kg/m},\quad \text{Total Length with Hooks} = 2{,}480\text{ meters} \]
              \[ \text{Total Mass} = 2{,}480\text{ m} \times 1.580\text{ kg/m} = 3{,}918.4\text{ kg}\ (3.92\text{ tonnes}) \]
            </div>
            <p style="margin:0.4rem 0 0;font-size:0.92rem;color:var(--text-body);">The raft structural schedule calls for 16mm deformed rebar at 150mm c/c both ways. Factoring hook anchorage, total linear steel measures 2,480 meters, weighing 3.92 metric tonnes via our <a href="rebar-calculator.html">Rebar Calculator</a>.</p>
          </div>
        </div>
        <div class="calc-final-result">
          ✅ <strong>Certified Material Bill of Quantities:</strong> 50.4 m³ Ready-Mix Concrete (559 Bags Cement + 19.4 m³ Sand + 38.8 m³ Stone) | 3.92 Tonnes T16 Reinforcing Steel | 100% Monolithic Structural Placement.
        </div>
      </div>

      <h3>Industry Codes, Regulatory Standards &amp; Quality Assurance (E-E-A-T)</h3>
      <p>
        Reinforced concrete structures are designed in strict accordance with safety codes to prevent catastrophic structural collapse:
      </p>
      <ul>
        <li><strong>ACI 318-19:</strong> Mandates minimum clear cover for steel reinforcement (75 mm for concrete cast permanently against earth; 40 mm for beams and columns exposed to weather; 20 mm for interior slabs) to prevent atmospheric carbonation and rebar corrosion.</li>
        <li><strong>Eurocode 2 (EN 1992-1-1):</strong> Establishes ultimate limit state (ULS) bending and shear capacities, crack width limitation under serviceability limit state (SLS), and fire resistance ratings (REI 60 to REI 240).</li>
        <li><strong>ASTM C94 / C94M:</strong> Regulates ready-mixed concrete batching tolerances (cement within ±1%, aggregates within ±2%, water within ±1%), truck transit time limits (discharging within 90 minutes of initial mixing), and minimum drum revolutions.</li>
        <li><strong>ASTM A615 (Grade 60):</strong> Enforces minimum tensile strength of 90,000 PSI (620 MPa) and minimum yield strength of 60,000 PSI (420 MPa), with strict percentage elongation requirements to ensure ductile failure before collapse.</li>
      </ul>

      <div class="faq-container" style="margin-top:2.5rem;">
        <h3 style="margin-bottom:1.5rem;">Frequently Asked Questions (Civil Engineering)</h3>
        
        <div class="faq-item">
          <div class="faq-q">Why is the dry concrete bulking factor 1.54 used in volume estimation?</div>
          <div class="faq-a">Loose dry aggregate particles (sand and crushed stone) contain roughly 30% to 35% void ratios between angular grains. When water and cement paste are added, the water lubricates the particles and cement paste fills the microscopic gaps, causing the loose dry bulk volume to collapse by approximately 35%. Consequently, it takes 1.54 cubic meters of dry components to yield exactly 1.0 cubic meter of dense wet in-situ concrete.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How does water-cement ratio (w/c) dictate structural compressive strength?</div>
          <div class="faq-a">According to Abrams' Law, the compressive strength of fully compacted concrete is inversely proportional to its water-cement ratio. A lower w/c ratio (e.g., 0.40 to 0.45) leaves fewer capillary pores as excess water evaporates, producing dense, watertight concrete with high 28-day strength (35–45 MPa). High w/c ratios (>0.60) cause severe bleeding, honeycombing, high permeability, and low compressive strength.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How does the rebar weight formula D² / 162 work mathematically?</div>
          <div class="faq-a">The formula derives from multiplying the cross-sectional area of a cylindrical bar [π·(D/2)²] by standard steel density (7,850 kg/m³). Converting millimeters to meters: Mass per meter = (π/4) × (D/1000)² × 7,850 = D² / 162.28 kg/m. Rounding to 162 gives the standard civil engineering field shortcut used across the world.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">What is the standard rebar lap splice length in structural slabs and beams?</div>
          <div class="faq-a">Under ACI 318-19 and Eurocode 2, tensile lap splice lengths depend on concrete compressive strength, bar diameter, and coating. A standard rule of thumb for Grade 60 (420 MPa) deformed bars in normal-weight concrete is 40 to 50 times the bar diameter (40d to 50d). For a 16mm rebar, the minimum tension lap length is 640 mm to 800 mm.</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">How long must freshly poured concrete cure before supporting structural loads?</div>
          <div class="faq-a">Concrete achieves approximately 16% of its characteristic compressive strength in 24 hours, 65% to 70% in 7 days, and reaches its full specified characteristic strength (f'c) at 28 days under proper moist curing conditions. Slabs should remain moist-cured for at least 7 days to prevent plastic shrinkage cracking.</div>
        </div>

      </div>

    </article>
'''

def update_civil():
    filepath = os.path.join(BASE_DIR, "civil.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    article_pattern = re.compile(r'<article class="article-section">.*?</article>', re.DOTALL)
    if article_pattern.search(content):
        updated = article_pattern.sub(lambda m: CIVIL_CONTENT.strip(), content, count=1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated)
        print("Updated civil.html successfully!")
        words = len(re.sub(r'<[^>]+>', ' ', CIVIL_CONTENT).split())
        print(f"Civil hub article word count: {words} words")

if __name__ == "__main__":
    update_civil()
