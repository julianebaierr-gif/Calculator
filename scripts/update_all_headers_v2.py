import glob
import re

CAT_MAP = [
    ("index.html", "🏠 Home", "home"),
    ("health.html", "⚖️ Health", "health"),
    ("finance.html", "🏦 Finance", "finance"),
    ("math.html", "🔢 Math", "math"),
    ("engineering.html", "⚡ Electrical", "engineering"),
    ("solar-energy.html", "☀️ Solar", "solar"),
    ("mechanical.html", "⚙️ Mechanical", "mechanical"),
    ("civil.html", "🏗️ Civil", "civil"),
    ("chemical.html", "🧪 Chemical", "chemical"),
    ("fire-safety.html", "🚨 Fire &amp; Safety", "fire"),
    ("programmer.html", "👨‍💻 Programmer", "programmer"),
    ("datetime.html", "📅 Date &amp; Time", "datetime"),
    ("converter.html", "🔄 Converter", "converter")
]

ROW1_KEYS = ["home", "health", "finance", "math", "engineering", "solar", "mechanical"]
ROW2_KEYS = ["civil", "chemical", "fire", "programmer", "datetime", "converter"]

def get_header_html(active_cat=None):
    r1_links = []
    for href, label, cat_key in [x for x in CAT_MAP if x[2] in ROW1_KEYS]:
        is_active = ' active' if active_cat == cat_key else ''
        r1_links.append(f'          <a href="{href}" class="nav-link{is_active}">{label}</a>')
    r1_str = "\n".join(r1_links)

    r2_links = []
    for href, label, cat_key in [x for x in CAT_MAP if x[2] in ROW2_KEYS]:
        is_active = ' active' if active_cat == cat_key else ''
        r2_links.append(f'          <a href="{href}" class="nav-link{is_active}">{label}</a>')
    r2_str = "\n".join(r2_links)

    return f"""  <!-- Sticky Header -->
  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
{r1_str}
        </div>
        <div class="nav-row">
{r2_str}
        </div>
      </nav>
    </div>
  </header>"""

HUB_PAGES = {
    'index.html': 'home',
    'health.html': 'health',
    'finance.html': 'finance',
    'math.html': 'math',
    'engineering.html': 'engineering',
    'solar-energy.html': 'solar',
    'mechanical.html': 'mechanical',
    'civil.html': 'civil',
    'chemical.html': 'chemical',
    'fire-safety.html': 'fire',
    'programmer.html': 'programmer',
    'datetime.html': 'datetime',
    'converter.html': 'converter',
}

PHYSICS_TOOLS = [
    'escape-velocity', 'free-fall', 'friction', 'gravitational-force',
    'hookes-law', 'kinetic-energy', 'photon-energy', 'physics',
    'simple-pendulum', 'snells-law', 'specific-heat', 'wavelength',
    'centripetal-force', 'angular-velocity', 'density', 'doppler-effect'
]

def detect_category(filename, content):
    if filename in HUB_PAGES:
        return HUB_PAGES[filename]
    if filename in ['404.html', 'privacy.html', 'terms.html', 'about.html', 'contact.html']:
        return None

    # 1. Check existing active link in old header
    m_active = re.search(r'href=[\'"]([a-z0-9_-]+\.html)[\'"][^>]*class=[\'"][^\'"]*active[^\'"]*[\'"]', content, re.IGNORECASE)
    if not m_active:
        m_active = re.search(r'class=[\'"][^\'"]*active[^\'"]*[\'"][^>]*href=[\'"]([a-z0-9_-]+\.html)[\'"]', content, re.IGNORECASE)
    if m_active:
        target = m_active.group(1)
        if target in HUB_PAGES and target != 'index.html':
            return HUB_PAGES[target]

    # 2. Check breadcrumbs
    bc_match = re.search(r'<nav class=["\'](?:breadcrumb|breadcrumbs|breadcrumb-nav)["\'][^>]*>(.*?)</nav>', content, re.DOTALL)
    if bc_match:
        bc_text = bc_match.group(1)
        for hub_file, cat_key in HUB_PAGES.items():
            if hub_file != 'index.html' and hub_file in bc_text:
                return cat_key

    # 3. Check physics list
    fn_clean = filename.replace('-calculator.html', '').replace('.html', '')
    if any(p in fn_clean for p in PHYSICS_TOOLS):
        return 'engineering'

    # 4. Check category tags
    ct_match = re.search(r'class=["\'](?:category-tag|calc-cat|badge-tag)["\'][^>]*>(.*?)<', content)
    if ct_match:
        ct_text = ct_match.group(1).lower()
        if any(k in ct_text for k in ['health', 'fitness', 'medical', 'diet']): return 'health'
        if any(k in ct_text for k in ['finance', 'money', 'investment', 'loan', 'mortgage']): return 'finance'
        if any(k in ct_text for k in ['math', 'algebra', 'analysis', 'geometry', 'calculus']): return 'math'
        if any(k in ct_text for k in ['electr', 'circuit', 'power', 'physics']): return 'engineering'
        if any(k in ct_text for k in ['solar', 'photovoltaic']): return 'solar'
        if any(k in ct_text for k in ['mechanic', 'thermo', 'fluid', 'aerospace']): return 'mechanical'
        if any(k in ct_text for k in ['civil', 'structur', 'concrete', 'construct']): return 'civil'
        if any(k in ct_text for k in ['chemic']): return 'chemical'
        if any(k in ct_text for k in ['fire']): return 'fire'
        if any(k in ct_text for k in ['program', 'code', 'network']): return 'programmer'
        if any(k in ct_text for k in ['date', 'time', 'calendar']): return 'datetime'
        if any(k in ct_text for k in ['convert', 'unit']): return 'converter'

    # 5. Filename keywords
    fn = filename.lower()
    if 'converter' in fn or '-to-' in fn: return 'converter'
    if 'solar' in fn or 'pv-' in fn: return 'solar'
    if any(k in fn for k in ['date', 'time', 'day', 'hour', 'clock', 'calendar', 'age', 'work-days', 'business-days']): return 'datetime'
    if any(k in fn for k in ['health', 'bmi', 'bmr', 'tdee', 'calorie', 'body-fat', 'lean-body', 'macro', 'water', 'vo2', 'running', 'pace', 'heart-rate', 'a1c', 'bac']): return 'health'
    if any(k in fn for k in ['loan', 'mortgage', 'interest', 'apr', 'apy', 'investment', 'roi', 'annuity', 'dividend', 'tax', 'salary', 'finance', 'depreciation', 'amortization', 'down-payment', 'emergency-fund', 'capital-gains', 'cd-', 'credit-card', 'break-even', 'markup', 'net-worth', 'savings']): return 'finance'
    if any(k in fn for k in ['wire', 'cable', 'voltage', 'ohms', 'resistor', 'power', 'motor', 'transformer', 'conduit', 'breaker', 'ampacity', 'battery', 'generator', 'capacitive', 'inductive', 'op-amp', 'short-circuit']): return 'engineering'
    if any(k in fn for k in ['concrete', 'rebar', 'brick', 'cement', 'retaining', 'beam', 'slope', 'roof', 'asphalt', 'civil', 'aggregate', 'drywall', 'wallpaper', 'tile']): return 'civil'
    if any(k in fn for k in ['pump', 'pipe', 'gear', 'torque', 'bearing', 'hvac', 'refrigerant', 'chiller', 'pneumatic', 'hydraulic', 'spring', 'belt', 'mechanical']): return 'mechanical'
    if any(k in fn for k in ['chemical', 'molarity', 'dilution', 'chlorine', 'ph-', 'stoichiometry', 'buffer', 'titration', 'gas-law', 'alum']): return 'chemical'
    if any(k in fn for k in ['fire', 'sprinkler', 'nfpa', 'hydrant', 'smoke']): return 'fire'
    if any(k in fn for k in ['subnet', 'bandwidth', 'binary', 'hex', 'hash', 'cidr', 'ascii', 'programmer']): return 'programmer'
    if any(k in fn for k in ['math', 'percentage', 'fraction', 'ratio', 'standard-deviation', 'matrix', 'quadratic', 'pythagorean', 'mean', 'median', 'mode', 'logarithm', 'absolute-value', 'area', 'arithmetic-sequence', 'circle', 'cube-root', 'exponent', 'factorial', 'gcd-lcm', 'midrange', 'perimeter', 'permutation', 'prime-number', 'probability', 'proportion', 'quotient', 'scientific-notation', 'significant-figures', 'surface-area', 'triangle-area', 'variance', 'volume', 'z-score']): return 'math'

    return None

def main():
    files = sorted(glob.glob("*.html"))
    print(f"Standardizing headers across {len(files)} files...")

    header_regex = re.compile(
        r'(?:<!--\s*(?:Sticky\s+)?Header\s*-->\s*)?<header\b[^>]*>.*?</header>',
        re.DOTALL
    )

    updated_count = 0
    not_matched = []

    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()

        active_cat = detect_category(f, content)
        new_header = get_header_html(active_cat)

        if header_regex.search(content):
            new_content = header_regex.sub(new_header, content, count=1)
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new_content)
            updated_count += 1
        else:
            not_matched.append(f)

    print(f"Successfully standardized headers in {updated_count} files!")
    if not_matched:
        print(f"Headers not matched in {len(not_matched)} files: {not_matched}")

if __name__ == "__main__":
    main()
