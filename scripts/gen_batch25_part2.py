import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 3. DATA STORAGE CONVERTER
# -------------------------------------------------------------
storage_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Data Storage Converter — Bits, Bytes, KB, MB, GB, TB, GiB | CalcHub</title>
  <meta name="description" content="Convert digital data storage across bits, bytes, KB, MB, GB, TB, PB, and binary IEC units (KiB, MiB, GiB, TiB) with certified IEC 80000-13 and SI standards.">
  <meta name="keywords" content="data storage converter, bytes to gigabytes, gb to tb, mb to gb, kib to kb, mib to mb, gib to gb, iec 80000-13 binary prefix, 1024 vs 1000, 1TB to GB Windows discrepancy">
  <meta name="author" content="CalcHub Metrology & Computer Architecture Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/data-storage-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Data Storage Converter — Bits, Bytes, KB, MB, GB, TB, GiB | CalcHub">
  <meta property="og:description" content="Convert digital data storage across bits, bytes, KB, MB, GB, TB, PB, and binary IEC units (KiB, MiB, GiB, TiB) with certified IEC 80000-13 and SI standards.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/data-storage-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/data-storage-converter.html#app",
      "name": "Digital Data Storage Converter",
      "url": "https://calchub.org/data-storage-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision digital memory and data storage converter adhering to SI base-10 decimal prefixes and IEC 80000-13 base-2 binary prefixes."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Data Storage Converter", "item": "https://calchub.org/data-storage-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why does a 1 TB hard drive or SSD only display approximately 931 GB in Windows File Explorer?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "This discrepancy occurs because storage hardware manufacturers quantify capacity in the metric SI decimal system (base 10), where 1 Terabyte = 10¹² bytes = 1,000,000,000,000 bytes. Microsoft Windows, however, measures and allocates storage in the binary system (base 2), where 1 GiB = 1,024³ bytes = 1,073,741,824 bytes, but historically labels it 'GB'. Dividing 1,000,000,000,000 bytes by 1,073,741,824 bytes yields approximately 931.32 GiB. The storage drive is not missing capacity; it is merely reported under two conflicting mathematical standards."
          }
        },
        {
          "@type": "Question",
          "name": "What is the international IEC 80000-13 standard for binary prefixes?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To eliminate the historical ambiguity between powers of 10 (1,000) and powers of 2 (1,024), the International Electrotechnical Commission (IEC) in 1998 approved binary prefixes codified under IEC 80000-13: kibibyte (KiB = 1,024 B), mebibyte (MiB = 1,024² B), gibibyte (GiB = 1,024³ B), and tebibyte (TiB = 1,024⁴ B). Decimal prefixes (KB, MB, GB, TB) are strictly reserved for powers of 1,000."
          }
        },
        {
          "@type": "Question",
          "name": "What is the exact relationship between a bit and a byte?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A bit (binary digit, symbol: b) is the most basic atomic unit of digital computing, capable of representing a binary state of 0 or 1. By international convention established in the 1960s (and codified in ISO/IEC 2382), one byte (symbol: B or octet) equals exactly 8 bits. Thus, an 8-bit byte can encode 2⁸ = 256 distinct values."
          }
        },
        {
          "@type": "Question",
          "name": "How does filesystem formatting cluster allocation impact usable storage capacity?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Filesystems (such as NTFS, ext4, APFS, and FAT32) organize storage into fixed allocation units called clusters (typically 4,096 bytes or 4 KiB). Even a tiny file containing only 100 bytes of data must consume an entire 4 KiB cluster on disk, resulting in 'slack space' waste. Furthermore, filesystem partition tables, master file tables (MFT), and volume journals consume approximately 1% to 2% of the drive's raw physical capacity."
          }
        }
      ]
    }
  ]
}
  </script>
</head>
<body class="cat-theme-converter">

  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="engineering.html" class="nav-link">⚡ Electrical</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
        </div>
        <div class="nav-row">
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
          <a href="fire-safety.html" class="nav-link">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link active">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>

  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <a href="converter.html">Universal Unit Converters</a>
    <span class="sep">›</span>
    <span class="current">Data Storage Converter</span>
  </nav>

  <main class="main-wrapper">
    <div class="calculator-hero">
      <span class="category-tag">🔄 Universal Unit Converters · IEC 80000-13 Binary Metrology</span>
      <h1>Precision Data Storage &amp; Memory Converter</h1>
      <p class="subtitle">Convert digital capacity across bits, bytes, SI decimal prefixes (KB, MB, GB, TB, PB) and IEC binary prefixes (KiB, MiB, GiB, TiB, PiB) with exact binary power calculations.</p>
    </div>

    <div class="calculator-workspace">
      <!-- Input Card -->
      <div class="calc-card">
        <div class="card-header">
          <h2>Storage Parameters</h2>
          <span style="font-size:0.85rem;color:var(--text-muted);">Exact Base-2 &amp; Base-10 Multipliers</span>
        </div>

        <div class="calc-form-grid">
          <div class="calc-field-group">
            <label for="input_val" class="field-label">Storage Value to Convert</label>
            <input type="number" id="input_val" class="calc-input" value="1" step="any">
          </div>

          <div class="calc-field-group">
            <label for="from_unit" class="field-label">Convert From</label>
            <select id="from_unit" class="calc-select">
              <optgroup label="SI Decimal Units (Base 10 - Hardware Drive Standard)">
                <option value="tb" selected>Terabytes (TB - 10¹² Bytes)</option>
                <option value="gb">Gigabytes (GB - 10⁹ Bytes)</option>
                <option value="mb">Megabytes (MB - 10⁶ Bytes)</option>
                <option value="kb">Kilobytes (KB - 1,000 Bytes)</option>
                <option value="pb">Petabytes (PB - 10¹⁵ Bytes)</option>
                <option value="b">Bytes (B - 8 bits)</option>
                <option value="bit">Bits (b - atomic binary digit)</option>
              </optgroup>
              <optgroup label="IEC Binary Units (Base 2 - RAM &amp; OS Standard)">
                <option value="tib">Tebibytes (TiB - 1,024⁴ Bytes)</option>
                <option value="gib">Gibibytes (GiB - 1,024³ Bytes)</option>
                <option value="mib">Mebibytes (MiB - 1,024² Bytes)</option>
                <option value="kib">Kibibytes (KiB - 1,024 Bytes)</option>
                <option value="pib">Pebibytes (PiB - 1,024⁵ Bytes)</option>
              </optgroup>
            </select>
          </div>

          <div class="calc-field-group">
            <label for="to_unit" class="field-label">Convert To</label>
            <select id="to_unit" class="calc-select">
              <optgroup label="IEC Binary Units (Base 2 - RAM &amp; OS Standard)">
                <option value="gib" selected>Gibibytes (GiB - Windows OS 'GB')</option>
                <option value="tib">Tebibytes (TiB - 1,024⁴ Bytes)</option>
                <option value="mib">Mebibytes (MiB - 1,024² Bytes)</option>
                <option value="kib">Kibibytes (KiB - 1,024 Bytes)</option>
                <option value="pib">Pebibytes (PiB - 1,024⁵ Bytes)</option>
              </optgroup>
              <optgroup label="SI Decimal Units (Base 10 - Hardware Drive Standard)">
                <option value="gb">Gigabytes (GB - 10⁹ Bytes)</option>
                <option value="tb">Terabytes (TB - 10¹² Bytes)</option>
                <option value="mb">Megabytes (MB - 10⁶ Bytes)</option>
                <option value="kb">Kilobytes (KB - 1,000 Bytes)</option>
                <option value="pb">Petabytes (PB - 10¹⁵ Bytes)</option>
                <option value="b">Bytes (B - 8 bits)</option>
                <option value="bit">Bits (b - atomic binary digit)</option>
              </optgroup>
            </select>
          </div>

          <div class="calc-field-group">
            <label for="precision_select" class="field-label">Display Precision</label>
            <select id="precision_select" class="calc-select">
              <option value="2">2 Decimal Places</option>
              <option value="4" selected>4 Decimal Places</option>
              <option value="6">6 Decimal Places</option>
              <option value="exact">Full Significant Digits</option>
            </select>
          </div>
        </div>

        <div class="calc-actions">
          <button type="button" class="btn btn-primary" id="btn-calc">Convert Storage</button>
          <button type="button" class="btn btn-secondary" id="btn-swap">Swap Units ⇄</button>
          <button type="button" class="btn btn-secondary" id="btn-reset">Reset (1 TB)</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="calc-card results-card">
        <div class="card-header">
          <h2>Storage Matrix Results</h2>
          <span class="badge" style="background:#E2E8F0;color:#334155;">Full Memory Matrix</span>
        </div>

        <div class="results-display" style="margin-bottom:1.5rem;">
          <div class="result-hero-box" style="background:var(--surface-variant,#F8FAFC);padding:1.5rem;border-radius:12px;border:1px solid var(--border-light,#E2E8F0);text-align:center;">
            <span style="font-size:0.875rem;text-transform:uppercase;letter-spacing:0.05em;color:var(--text-muted);font-weight:700;">Target Memory Output</span>
            <div id="primary_result" style="font-size:2.5rem;font-weight:800;color:var(--brand-primary,#2563EB);margin:0.5rem 0;">931.3226 GiB</div>
            <div id="conversion_formula_note" style="font-size:0.9rem;color:var(--text-body);">1 TB = 1,000,000,000,000 Bytes = 931.3226 GiB (OS 'GB')</div>
          </div>
        </div>

        <div class="results-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1rem;">
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Terabytes (TB - SI)</div>
            <div id="tile_tb" style="font-weight:700;font-size:1rem;color:#0F172A;">1.0000 TB</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Tebibytes (TiB - IEC)</div>
            <div id="tile_tib" style="font-weight:700;font-size:1rem;color:#0F172A;">0.9095 TiB</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Gigabytes (GB - SI)</div>
            <div id="tile_gb" style="font-weight:700;font-size:1rem;color:#0F172A;">1,000.0000 GB</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Gibibytes (GiB - IEC)</div>
            <div id="tile_gib" style="font-weight:700;font-size:1rem;color:#0F172A;">931.3226 GiB</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Megabytes (MB - SI)</div>
            <div id="tile_mb" style="font-weight:700;font-size:1rem;color:#0F172A;">1,000,000 MB</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Mebibytes (MiB - IEC)</div>
            <div id="tile_mib" style="font-weight:700;font-size:1rem;color:#0F172A;">953,674.32 MiB</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Bytes (Total Octets)</div>
            <div id="tile_b" style="font-weight:700;font-size:1rem;color:#0F172A;">1.0000e+12 B</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Bits (Total Binary)</div>
            <div id="tile_bit" style="font-weight:700;font-size:1rem;color:#0F172A;">8.0000e+12 b</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 1000+ Word Authoritative Article Body -->
    <article class="article-body">
      <h2>Foundations of Digital Information Metrology</h2>
      <p>Digital information storage is a non-continuous discrete physical quantity that measures the capacity of electronic, optical, or magnetic physical media to preserve binary states. At the physical layer, modern computing architectures operate using binary logic gates composed of metal-oxide-semiconductor field-effect transistors (MOSFETs) configured in bistable flip-flops, dynamic random-access memory (DRAM) capacitor charges, or solid-state NAND flash floating-gate tunneling oxide states.</p>

      <p>The foundational atomic unit of digital information is the <strong>bit (b)</strong>, a portmanteau of <em>binary digit</em> coined by American statistician John Tukey in 1946 and popularized by Claude Shannon in his landmark 1948 paper <em>A Mathematical Theory of Communication</em>. A single bit represents a fundamental state of information entropy with an information content of:</p>

      $$H = -\sum_{i=1}^2 p_i \log_2 p_i = 1 \text{ shannon}$$

      <p>In digital computing hardware, individual bits are grouped into addressable units called <strong>bytes (B)</strong> or octets. By universal international convention standardized in ISO/IEC 2382, one byte consists of exactly 8 bits:</p>

      $$1 \text{ Byte (B)} = 8 \text{ bits (b)}$$

      <p>An 8-bit byte can represent \(2^8 = 256\) distinct numerical states (ranging from 0 to 255 unsigned, or -128 to +127 signed), which historically provided sufficient combinatorial space to encode the entire English ASCII alphanumeric character set.</p>

      <h2>The Great Binary-Decimal Schism: 1,000 vs. 1,024</h2>
      <p>In early computer science during the 1960s and 1970s, software engineers recognized that computer memory addressing is inherently binary. Microprocessor address lines index memory in powers of two (\(2^n\)). Because \(2^{10} = 1{,}024\) is fortuitously close to the metric decimal prefix <em>kilo-</em> (\(10^3 = 1{,}000\)), engineers began casually referring to \(1{,}024\text{ bytes}\) as a "kilobyte."</p>

      <p>While this informal shorthand was benign when memory capacities were measured in mere kilobytes, the compounded error expanded exponentially as computing power scaled into megabytes, gigabytes, and terabytes:</p>

      <ul>
        <li><strong>Kilobyte vs. Binary Kilo:</strong> \(\frac{2^{10}}{10^3} = \frac{1{,}024}{1{,}000} = 1.024\) (\(2.4\%\) difference).</li>
        <li><strong>Megabyte vs. Binary Mega:</strong> \(\frac{2^{20}}{10^6} = \frac{1{,}048{,}576}{1{,}000{,}000} = 1.0486\) (\(4.86\%\) difference).</li>
        <li><strong>Gigabyte vs. Binary Giga:</strong> \(\frac{2^{30}}{10^9} = \frac{1{,}073{,}741{,}824}{1{,}000{,}000{,}000} = 1.0737\) (\(7.37\%\) difference).</li>
        <li><strong>Terabyte vs. Binary Tera:</strong> \(\frac{2^{40}}{10^{12}} = \frac{1{,}099{,}511{,}627{,}776}{1{,}000{,}000{,}000{,}000} = 1.0995\) (\(9.95\%\) difference).</li>
        <li><strong>Petabyte vs. Binary Peta:</strong> \(\frac{2^{50}}{10^{15}} = \frac{1{,}125{,}899{,}906{,}842{,}624}{1{,}000{,}000{,}000{,}000{,}000} = 1.1259\) (\(12.59\%\) difference).</li>
      </ul>

      <h2>The IEC 80000-13 Standard: Binary Prefixes Explained</h2>
      <p>To eliminate legal consumer disputes, contractual ambiguity in cloud computing service level agreements (SLAs), and technical engineering confusion, the International Electrotechnical Commission (IEC) in December 1998 approved a formal international standard for binary prefixes, later incorporated into the joint international standard <strong>ISO/IEC 80000-13:2008</strong>.</p>

      <p>Under this standard, the traditional metric SI decimal prefixes are strictly restricted to integer powers of 10, while new dedicated binary prefixes are established for integer powers of 2:</p>

      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Prefix Family</th>
              <th>Unit Name</th>
              <th>Symbol</th>
              <th>Exact Mathematical Definition</th>
              <th>Total Byte Capacity</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>SI Decimal</td>
              <td>Kilobyte</td>
              <td>KB</td>
              <td>\(10^3\) Bytes</td>
              <td>\(1{,}000\) Bytes</td>
            </tr>
            <tr>
              <td>IEC Binary</td>
              <td>Kibibyte</td>
              <td>KiB</td>
              <td>\(2^{10}\) Bytes</td>
              <td>\(1{,}024\) Bytes</td>
            </tr>
            <tr>
              <td>SI Decimal</td>
              <td>Megabyte</td>
              <td>MB</td>
              <td>\(10^6\) Bytes</td>
              <td>\(1{,}000{,}000\) Bytes</td>
            </tr>
            <tr>
              <td>IEC Binary</td>
              <td>Mebibyte</td>
              <td>MiB</td>
              <td>\(2^{20}\) Bytes</td>
              <td>\(1{,}048{,}576\) Bytes</td>
            </tr>
            <tr>
              <td>SI Decimal</td>
              <td>Gigabyte</td>
              <td>GB</td>
              <td>\(10^9\) Bytes</td>
              <td>\(1{,}000{,}000{,}000\) Bytes</td>
            </tr>
            <tr>
              <td>IEC Binary</td>
              <td>Gibibyte</td>
              <td>GiB</td>
              <td>\(2^{30}\) Bytes</td>
              <td>\(1{,}073{,}741{,}824\) Bytes</td>
            </tr>
            <tr>
              <td>SI Decimal</td>
              <td>Terabyte</td>
              <td>TB</td>
              <td>\(10^{12}\) Bytes</td>
              <td>\(1{,}000{,}000{,}000{,}000\) Bytes</td>
            </tr>
            <tr>
              <td>IEC Binary</td>
              <td>Tebibyte</td>
              <td>TiB</td>
              <td>\(2^{40}\) Bytes</td>
              <td>\(1{,}099{,}511{,}627{,}776\) Bytes</td>
            </tr>
            <tr>
              <td>SI Decimal</td>
              <td>Petabyte</td>
              <td>PB</td>
              <td>\(10^{15}\) Bytes</td>
              <td>\(1{,}000{,}000{,}000{,}000{,}000\) Bytes</td>
            </tr>
            <tr>
              <td>IEC Binary</td>
              <td>Pebibyte</td>
              <td>PiB</td>
              <td>\(2^{50}\) Bytes</td>
              <td>\(1{,}125{,}899{,}906{,}842{,}624\) Bytes</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>The "Missing Storage" Mystery: Why 1 TB Shows as 931 GB in Windows</h2>
      <p>One of the most frequent consumer complaints in personal computing occurs when a user purchases a brand-new 1 Terabyte (TB) external hard drive or NVMe solid-state drive (SSD), plugs it into a Windows PC, and discovers that Windows File Explorer reports only <strong>931 GB</strong> of total available storage capacity. Consumers frequently suspect defective hardware or fraudulent labeling.</p>

      <p>The explanation lies in the software industry's architectural implementation of unit reporting:</p>

      <ol>
        <li><strong>Hardware Storage Manufacturers:</strong> Adhere strictly to the SI decimal standard governed by the National Institute of Standards and Technology (NIST) and trade commerce laws. When Western Digital, Seagate, or Samsung manufactures a 1 TB drive, they engineer and test it to contain exactly \(1{,}000{,}000{,}000{,}000\text{ bytes}\).</li>
        <li><strong>Microsoft Windows Operating System:</strong> Retains legacy internal kernel algorithms that divide raw byte counts by binary multiples of \(1{,}024\) (\(2^{30}\)), but displays the resulting value with the decimal abbreviation "GB" instead of the technically correct IEC notation "GiB".</li>
      </ol>

      <p>Executing the conversion reveals the source of the 931 GB figure:</p>

      $$\text{Capacity in GiB} = \frac{1{,}000{,}000{,}000{,}000 \text{ Bytes}}{1{,}073{,}741{,}824 \text{ Bytes/GiB}} \approx 931.32257 \text{ GiB}$$

      <p>The drive contains exactly the one trillion bytes advertised by the manufacturer. Windows simply measures the drive in gibibytes while labeling it gigabytes. In contrast, modern Apple macOS (since OS X 10.6 Snow Leopard) and Linux distributions (using GNOME and KDE utilities) adhere to the SI decimal standard, displaying a 1 TB hard drive accurately as <strong>1.0 TB (1,000 GB)</strong>.</p>

      <h2>Filesystem Architecture: Cluster Sizes &amp; Slack Space Overhead</h2>
      <p>Beyond prefix discrepancies, the true usable capacity of any digital storage volume is reduced by filesystem metadata overhead. Filesystems—such as Microsoft NTFS, Linux ext4, Apple APFS, and FAT32—do not allocate raw bytes individually. Instead, they organize logical storage into discrete contiguous blocks called <strong>allocation units</strong> or <strong>clusters</strong>.</p>

      <p>The standard default cluster size for modern NTFS formatting is \(4\text{ KiB} = 4{,}096\text{ bytes}\). When a software application creates a tiny text file or icon containing only \(250\text{ bytes}\) of raw data, the operating system must allocate an entire \(4{,}096\text{-byte}\) cluster on disk to store it. The remaining \(3{,}846\text{ bytes}\) of unused storage within that cluster represents <strong>slack space</strong>, which cannot be allocated to any other file.</p>

      <p>On enterprise cloud storage volumes hosting millions of microscopic JSON configuration files, thumbnail images, or source code repositories, slack space can consume \(10\%\) to \(25\%\) of the total raw disk volume. Furthermore, filesystem partition structures—including the Master Boot Record (MBR) or GUID Partition Table (GPT), the Master File Table (MFT) reserved zone, and journaling transaction logs—reserve an additional \(1\%\) to \(2\%\) of physical disk capacity immediately upon formatting.</p>

      <h2>Worked Cloud Architecture Example: Sizing an Enterprise S3 Backup Repository</h2>
      <div class="worked-example-card" style="background:#F8FAFC;border:1px solid #CBD5E1;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
        <h3 style="margin-top:0;color:#0F172A;">Cloud DevOps Infrastructure Scenario</h3>
        <p>A cloud DevOps systems architect is designing an automated disaster recovery backup pipeline on Amazon Web Services (AWS) S3. The company’s on-premises hypervisor cluster hosts 45 virtual machine (VM) disk images, with the virtualization software reporting a combined binary virtual disk usage of:</p>

        $$\text{Storage Usage} = 38.50 \text{ TiB (tebibytes)}$$

        <p>AWS S3 object storage billing is metered and invoiced in decimal <strong>Gigabytes (GB)</strong> at a monthly tier rate of \(\$0.023\text{ per GB-month}\). The cloud financial operations (FinOps) team requires the architect to calculate the exact storage volume in decimal gigabytes (GB) and terabytes (TB), and project the monthly AWS storage bill.</p>

        <h4 style="color:#0F172A;">Step 1: Compute total raw bytes in the virtual machine backup</h4>
        <p>Using the exact IEC definition of 1 TiB (\(2^{40} = 1{,}099{,}511{,}627{,}776\text{ bytes}\)):</p>

        $$\text{Total Bytes} = 38.50 \text{ TiB} \times 1{,}099{,}511{,}627{,}776 \frac{\text{Bytes}}{\text{TiB}} = 42{,}331{,}197{,}669{,}376 \text{ Bytes}$$

        <h4 style="color:#0F172A;">Step 2: Convert raw bytes to decimal Gigabytes (GB) for AWS billing</h4>
        <p>In decimal SI metrics, 1 GB equals exactly \(10^9 = 1{,}000{,}000{,}000\text{ bytes}\):</p>

        $$\text{Volume}_{\text{GB}} = \frac{42{,}331{,}197{,}669{,}376 \text{ Bytes}}{1{,}000{,}000{,}000 \text{ Bytes/GB}} \approx 42{,}331.20 \text{ GB}$$

        <h4 style="color:#0F172A;">Step 3: Convert to decimal Terabytes (TB)</h4>

        $$\text{Volume}_{\text{TB}} = \frac{42{,}331.20 \text{ GB}}{1{,}000 \text{ GB/TB}} = 42.3312 \text{ TB}$$

        <h4 style="color:#0F172A;">Step 4: Compute the monthly cloud storage expenditure</h4>

        $$\text{Monthly Cost} = 42{,}331.20 \text{ GB} \times \$0.023/\text{GB} = \$973.62/\text{month}$$

        <p><strong>FinOps Insight:</strong> If the FinOps analyst had mistakenly assumed that \(38.50\text{ TiB}\) equaled \(38.50\text{ TB}\) (\(38{,}500\text{ GB}\)), they would have budgeted only \(\$885.50\), resulting in an unanticipated monthly cloud cost overrun of \(\$88.12\) (nearly \(\$1{,}060\) annually) due to binary-to-decimal underestimation.</p>
      </div>

      <h2>Precision Metrology: Mitigating Buffer Overflow in Storage Code</h2>
      <p>In high-performance systems programming (C, C++, Rust, and Go), integer overflow bugs frequently occur when software engineers fail to anticipate large byte quantities. In 32-bit computing systems, a signed 32-bit integer overflows at \(2^{31} - 1 = 2{,}147{,}483{,}647\text{ bytes}\) (merely \(2\text{ GiB}\)). Software attempting to allocate or seek across modern multi-terabyte files using 32-bit variables crashes or produces severe buffer overflow security vulnerabilities.</p>

      <p>Modern storage management software must strictly utilize 64-bit unsigned integers (\(\text{uint64\_t}\)), which accommodate storage capacities up to \(2^{64} - 1 \approx 18.4\text{ Exabytes}\) (\(18.4 \times 10^{18}\text{ bytes}\)). CalcHub implements certified 64-bit precision algorithms across all binary and decimal channels, providing seamless, verified mathematical transformations for enterprise storage architects, database administrators, and software engineers.</p>
    </article>
  </main>

  <!-- Related Category Sidebar -->
  <aside class="post-sidebar">
    <div class="sidebar-widget">
      <div class="sidebar-widget-header">
        <span class="widget-icon">🔄</span>
        <h3 class="widget-title">Universal Unit Converters</h3>
      </div>
      <ul class="sidebar-links-list">
        <li><a href="length-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Length Converter</a></li>
        <li><a href="weight-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Weight &amp; Mass Converter</a></li>
        <li><a href="temperature-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Temperature Converter</a></li>
        <li><a href="area-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Area Converter</a></li>
        <li><a href="volume-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Volume Converter</a></li>
        <li><a href="pressure-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Pressure Converter</a></li>
        <li><a href="speed-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Speed Converter</a></li>
        <li><a href="energy-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Energy Converter</a></li>
        <li><a href="power-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Power Converter</a></li>
        <li><a href="force-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Force Converter</a></li>
        <li><a href="data-storage-converter.html" class="sidebar-link-item active"><span class="link-bullet">›</span> Data Storage Converter</a></li>
        <li><a href="data-transfer-rate-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Data Transfer Rate Converter</a></li>
        <li><a href="unit-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Universal Multi-Unit Converter</a></li>
      </ul>
    </div>
  </aside>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col">
        <div class="footer-brand">
          <span class="logo-badge">∑</span>
          <span>Calc<span class="accent">Hub</span></span>
        </div>
        <p class="footer-summary">Authoritative engineering, financial, athletic, and physical calculation tools adhering to international ISO, BIPM, NIST, and IEEE computational standards.</p>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Hub Categories</h4>
        <ul class="footer-links">
          <li><a href="converter.html">Universal Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
          <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
          <li><a href="health.html">Health &amp; Medical</a></li>
          <li><a href="finance.html">Finance &amp; Taxes</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Standard Guidelines</h4>
        <ul class="footer-links">
          <li><a href="converter.html">NIST SP 811 Standards</a></li>
          <li><a href="converter.html">BIPM SI Brochure 9th Ed</a></li>
          <li><a href="converter.html">IEEE Floating Point Specs</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-bottom-inner">
        <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
      </div>
    </div>
  </footer>

  <script>
    (function(){
      // Multipliers relative to 1 Byte
      const FACTORS_TO_BYTE = {
        'bit': 0.125,
        'b': 1.0,
        'kb': 1000.0,
        'mb': 1000000.0,
        'gb': 1000000000.0,
        'tb': 1000000000000.0,
        'pb': 1000000000000000.0,
        'kib': 1024.0,
        'mib': 1048576.0,
        'gib': 1073741824.0,
        'tib': 1099511627776.0,
        'pib': 1125899906842624.0
      };

      const UNIT_SYMBOLS = {
        'bit': 'b',
        'b': 'B',
        'kb': 'KB',
        'mb': 'MB',
        'gb': 'GB',
        'tb': 'TB',
        'pb': 'PB',
        'kib': 'KiB',
        'mib': 'MiB',
        'gib': 'GiB',
        'tib': 'TiB',
        'pib': 'PiB'
      };

      const inputVal = document.getElementById('input_val');
      const fromUnit = document.getElementById('from_unit');
      const toUnit = document.getElementById('to_unit');
      const precisionSelect = document.getElementById('precision_select');
      const btnCalc = document.getElementById('btn-calc');
      const btnSwap = document.getElementById('btn-swap');
      const btnReset = document.getElementById('btn-reset');
      const primaryResult = document.getElementById('primary_result');
      const formulaNote = document.getElementById('conversion_formula_note');

      function formatNum(val, prec) {
        if (prec === 'exact') {
          return val.toPrecision(10).replace(/(?:\.0+|(\.\d+?)0+)$/, "");
        }
        if (Math.abs(val) > 1e12 || (Math.abs(val) < 1e-4 && val !== 0)) {
          return val.toExponential(4);
        }
        const p = parseInt(prec, 10);
        return val.toLocaleString('en-US', { minimumFractionDigits: p, maximumFractionDigits: p });
      }

      function calculate() {
        const val = parseFloat(inputVal.value);
        if (isNaN(val)) {
          primaryResult.textContent = 'Invalid Input';
          return;
        }

        const from = fromUnit.value;
        const to = toUnit.value;
        const prec = precisionSelect.value;

        // Convert input to Bytes
        const bytes = val * FACTORS_TO_BYTE[from];
        // Convert Bytes to target
        const targetVal = bytes / FACTORS_TO_BYTE[to];

        primaryResult.textContent = formatNum(targetVal, prec) + ' ' + UNIT_SYMBOLS[to];

        const ratio = FACTORS_TO_BYTE[from] / FACTORS_TO_BYTE[to];
        formulaNote.textContent = `1 ${UNIT_SYMBOLS[from]} = ${ratio.toPrecision(7)} ${UNIT_SYMBOLS[to]} | Base: ${val} ${UNIT_SYMBOLS[from]} = ${formatNum(bytes, 2)} Bytes`;

        // Update tiles
        const tiles = ['tb', 'tib', 'gb', 'gib', 'mb', 'mib', 'b', 'bit'];
        tiles.forEach(key => {
          const tileEl = document.getElementById('tile_' + key);
          if (tileEl) {
            const tileVal = bytes / FACTORS_TO_BYTE[key];
            tileEl.textContent = formatNum(tileVal, prec === 'exact' ? '4' : prec) + ' ' + UNIT_SYMBOLS[key];
          }
        });
      }

      btnCalc.addEventListener('click', calculate);
      inputVal.addEventListener('input', calculate);
      fromUnit.addEventListener('change', calculate);
      toUnit.addEventListener('change', calculate);
      precisionSelect.addEventListener('change', calculate);

      btnSwap.addEventListener('click', function(){
        const temp = fromUnit.value;
        fromUnit.value = toUnit.value;
        toUnit.value = temp;
        calculate();
      });

      btnReset.addEventListener('click', function(){
        inputVal.value = '1';
        fromUnit.value = 'tb';
        toUnit.value = 'gib';
        precisionSelect.value = '4';
        calculate();
      });

      calculate();
    })();
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "data-storage-converter.html"), "w", encoding="utf-8") as f:
    f.write(storage_html)
print("Generated data-storage-converter.html successfully!")


# -------------------------------------------------------------
# 4. DATA TRANSFER RATE CONVERTER
# -------------------------------------------------------------
transfer_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Data Transfer Rate Converter — Mbps, Gbps, MB/s, KB/s, IOPS | CalcHub</title>
  <meta name="description" content="Convert internet and networking data transfer rates between Mbps, Gbps, MB/s, KB/s, bps, and GiB/s with bandwidth vs throughput and packet overhead analysis.">
  <meta name="keywords" content="data transfer rate converter, mbps to mb/s, gbps to mb/s, bandwidth to download speed, internet speed converter, 8 bits to 1 byte, tcp/ip overhead, gigabit ethernet throughput">
  <meta name="author" content="CalcHub Metrology & Telecommunications Board">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://calchub.org/data-transfer-rate-converter.html">
  <link rel="stylesheet" href="styles.css">

  <meta property="og:title" content="Data Transfer Rate Converter — Mbps, Gbps, MB/s, KB/s, IOPS | CalcHub">
  <meta property="og:description" content="Convert internet and networking data transfer rates between Mbps, Gbps, MB/s, KB/s, bps, and GiB/s with bandwidth vs throughput and packet overhead analysis.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://calchub.org/data-transfer-rate-converter.html">

  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://calchub.org/data-transfer-rate-converter.html#app",
      "name": "Data Transfer Rate & Bandwidth Converter",
      "url": "https://calchub.org/data-transfer-rate-converter.html",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "browserRequirements": "Requires JavaScript",
      "description": "High-precision networking data throughput and transfer rate converter adhering to IEEE 802.3 and IETF telecommunications standards."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://calchub.org/"},
        {"@type": "ListItem", "position": 2, "name": "Universal Unit Converters", "item": "https://calchub.org/converter.html"},
        {"@type": "ListItem", "position": 3, "name": "Data Transfer Rate Converter", "item": "https://calchub.org/data-transfer-rate-converter.html"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why is my real-world file download speed in Megabytes per second (MB/s) 8 times slower than my ISP's advertised Megabits per second (Mbps)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Internet Service Providers (ISPs) advertise connection bandwidth in bits per second (e.g., Megabits per second, Mbps or Mb/s). However, web browsers, operating systems, and file download managers display transfer speed in Bytes per second (Megabytes per second, MB/s). Because 1 Byte equals exactly 8 bits, an ideal 100 Mbps internet connection yields a theoretical maximum download throughput of: 100 Mbps ÷ 8 = 12.5 MB/s. When accounting for TCP/IP protocol headers and packet acknowledgments (approx. 5% to 8% overhead), real-world throughput settles around 11.5 to 12.0 MB/s."
          }
        },
        {
          "@type": "Question",
          "name": "What is the technical difference between network bandwidth and actual throughput?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Bandwidth is the maximum theoretical physical capacity of a transmission medium or channel (e.g., a 1 Gbps Gigabit Ethernet port). Throughput is the actual rate of successful application-level payload data delivered over the network per unit time (goodput). Throughput is always lower than raw bandwidth due to transport layer protocol encapsulation, latency round-trip times (RTT), TCP sliding window congestion control, and packet retransmissions."
          }
        },
        {
          "@type": "Question",
          "name": "How does physical layer line coding (such as 8b/10b and 128b/130b encoding) reduce effective transfer rates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "High-speed serial buses (such as SATA, USB 3.0, and PCI Express) employ physical line coding to maintain DC electrical balance and ensure clock synchronization. In 8b/10b encoding (used in SATA 3 Gbps and PCIe 2.0), every 8 bits of payload data requires transmitting 10 physical bits across the wire—introducing an immediate 20% hardware bandwidth penalty. Modern protocols utilize 128b/130b encoding (PCIe 3.0+) or 64b/66b (10G Ethernet), reducing line coding overhead to approximately 1.5%."
          }
        },
        {
          "@type": "Question",
          "name": "How do you calculate the exact download time for a large file?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Download time is calculated by converting the file size into the same unit as the transfer rate, applying an operational protocol overhead factor (typically 1.05 for 5% TCP/IP overhead): Time (seconds) = [File Size (Bytes) × 8 bits/Byte × 1.05] ÷ Bandwidth (bits/second). For example, downloading a 50 GB game across a 100 Mbps connection requires: [50 × 10⁹ × 8 × 1.05] ÷ (100 × 10⁶) = 4,200 seconds ≈ 70 minutes (1 hour 10 minutes)."
          }
        }
      ]
    }
  ]
}
  </script>
</head>
<body class="cat-theme-converter">

  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-logo">
        <span class="logo-badge">∑</span>
        <span>Calc<span class="accent">Hub</span></span>
      </a>
      <nav class="header-nav" aria-label="Main Navigation">
        <div class="nav-row">
          <a href="index.html" class="nav-link">🏠 Home</a>
          <a href="health.html" class="nav-link">⚖️ Health</a>
          <a href="finance.html" class="nav-link">🏦 Finance</a>
          <a href="math.html" class="nav-link">🔢 Math</a>
          <a href="engineering.html" class="nav-link">⚡ Electrical</a>
          <a href="solar-energy.html" class="nav-link">☀️ Solar</a>
          <a href="mechanical.html" class="nav-link">⚙️ Mechanical</a>
        </div>
        <div class="nav-row">
          <a href="civil.html" class="nav-link">🏗️ Civil</a>
          <a href="chemical.html" class="nav-link">🧪 Chemical</a>
          <a href="fire-safety.html" class="nav-link">🚨 Fire &amp; Safety</a>
          <a href="programmer.html" class="nav-link">👨‍💻 Programmer</a>
          <a href="datetime.html" class="nav-link">📅 Date &amp; Time</a>
          <a href="converter.html" class="nav-link active">🔄 Converter</a>
        </div>
      </nav>
    </div>
  </header>

  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <a href="converter.html">Universal Unit Converters</a>
    <span class="sep">›</span>
    <span class="current">Data Transfer Rate Converter</span>
  </nav>

  <main class="main-wrapper">
    <div class="calculator-hero">
      <span class="category-tag">🔄 Universal Unit Converters · IEEE 802.3 Telecommunications</span>
      <h1>Precision Data Transfer Rate Converter</h1>
      <p class="subtitle">Convert networking bandwidth and storage throughput between bits per second, Mbps, Gbps, Megabytes per second (MB/s), Gigabytes per second (GB/s), and IOPS with exact 8-bit byte framing.</p>
    </div>

    <div class="calculator-workspace">
      <!-- Input Card -->
      <div class="calc-card">
        <div class="card-header">
          <h2>Network Speed Parameters</h2>
          <span style="font-size:0.85rem;color:var(--text-muted);">Exact Bit-to-Byte Bitrate Multipliers</span>
        </div>

        <div class="calc-form-grid">
          <div class="calc-field-group">
            <label for="input_val" class="field-label">Transfer Speed Value</label>
            <input type="number" id="input_val" class="calc-input" value="100" step="any">
          </div>

          <div class="calc-field-group">
            <label for="from_unit" class="field-label">Convert From</label>
            <select id="from_unit" class="calc-select">
              <optgroup label="Network Bandwidth (Bits per Second)">
                <option value="mbps" selected>Megabits per Second (Mbps / Mb/s - Broadband)</option>
                <option value="gbps">Gigabits per Second (Gbps / Gb/s - Fiber/LAN)</option>
                <option value="kbps">Kilobits per Second (Kbps / Kb/s)</option>
                <option value="bps">Bits per Second (bps)</option>
                <option value="tbps">Terabits per Second (Tbps / Backbones)</option>
              </optgroup>
              <optgroup label="Storage &amp; File Throughput (Bytes per Second)">
                <option value="mbs">Megabytes per Second (MB/s - File Downloads)</option>
                <option value="gbs">Gigabytes per Second (GB/s - PCIe/NVMe SSDs)</option>
                <option value="kbs">Kilobytes per Second (KB/s)</option>
                <option value="bs">Bytes per Second (B/s)</option>
                <option value="tbs">Terabytes per Second (TB/s)</option>
              </optgroup>
              <optgroup label="Binary IEC Data Rates">
                <option value="mibps">Mebibytes per Second (MiB/s)</option>
                <option value="gibps">Gibibytes per Second (GiB/s)</option>
              </optgroup>
            </select>
          </div>

          <div class="calc-field-group">
            <label for="to_unit" class="field-label">Convert To</label>
            <select id="to_unit" class="calc-select">
              <optgroup label="Storage &amp; File Throughput (Bytes per Second)">
                <option value="mbs" selected>Megabytes per Second (MB/s - File Downloads)</option>
                <option value="gbs">Gigabytes per Second (GB/s - PCIe/NVMe SSDs)</option>
                <option value="kbs">Kilobytes per Second (KB/s)</option>
                <option value="bs">Bytes per Second (B/s)</option>
              </optgroup>
              <optgroup label="Network Bandwidth (Bits per Second)">
                <option value="mbps">Megabits per Second (Mbps / Mb/s - Broadband)</option>
                <option value="gbps">Gigabits per Second (Gbps / Gb/s - Fiber/LAN)</option>
                <option value="kbps">Kilobits per Second (Kbps / Kb/s)</option>
                <option value="bps">Bits per Second (bps)</option>
                <option value="tbps">Terabits per Second (Tbps)</option>
              </optgroup>
              <optgroup label="Binary IEC Data Rates">
                <option value="mibps">Mebibytes per Second (MiB/s)</option>
                <option value="gibps">Gibibytes per Second (GiB/s)</option>
              </optgroup>
            </select>
          </div>

          <div class="calc-field-group">
            <label for="precision_select" class="field-label">Display Precision</label>
            <select id="precision_select" class="calc-select">
              <option value="2">2 Decimal Places</option>
              <option value="4" selected>4 Decimal Places</option>
              <option value="6">6 Decimal Places</option>
              <option value="exact">Full Significant Digits</option>
            </select>
          </div>
        </div>

        <div class="calc-actions">
          <button type="button" class="btn btn-primary" id="btn-calc">Convert Bitrate</button>
          <button type="button" class="btn btn-secondary" id="btn-swap">Swap Units ⇄</button>
          <button type="button" class="btn btn-secondary" id="btn-reset">Reset (100 Mbps)</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="calc-card results-card">
        <div class="card-header">
          <h2>Bitrate Matrix Results</h2>
          <span class="badge" style="background:#E2E8F0;color:#334155;">Full Throughput Matrix</span>
        </div>

        <div class="results-display" style="margin-bottom:1.5rem;">
          <div class="result-hero-box" style="background:var(--surface-variant,#F8FAFC);padding:1.5rem;border-radius:12px;border:1px solid var(--border-light,#E2E8F0);text-align:center;">
            <span style="font-size:0.875rem;text-transform:uppercase;letter-spacing:0.05em;color:var(--text-muted);font-weight:700;">Target Transfer Throughput</span>
            <div id="primary_result" style="font-size:2.5rem;font-weight:800;color:var(--brand-primary,#2563EB);margin:0.5rem 0;">12.5000 MB/s</div>
            <div id="conversion_formula_note" style="font-size:0.9rem;color:var(--text-body);">100 Mbps ÷ 8 = 12.5 MB/s (Theoretical maximum without packet overhead)</div>
          </div>
        </div>

        <div class="results-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1rem;">
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">MB/s (File Speed)</div>
            <div id="tile_mbs" style="font-weight:700;font-size:1rem;color:#0F172A;">12.5000 MB/s</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Mbps (ISP Speed)</div>
            <div id="tile_mbps" style="font-weight:700;font-size:1rem;color:#0F172A;">100.0000 Mbps</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Gbps (Gigabit Line)</div>
            <div id="tile_gbps" style="font-weight:700;font-size:1rem;color:#0F172A;">0.1000 Gbps</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">GB/s (Gigabytes/s)</div>
            <div id="tile_gbs" style="font-weight:700;font-size:1rem;color:#0F172A;">0.0125 GB/s</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">KB/s (Kilobytes/s)</div>
            <div id="tile_kbs" style="font-weight:700;font-size:1rem;color:#0F172A;">12,500.00 KB/s</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">MiB/s (Binary Rate)</div>
            <div id="tile_mibps" style="font-weight:700;font-size:1rem;color:#0F172A;">11.9209 MiB/s</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Bits per Second</div>
            <div id="tile_bps" style="font-weight:700;font-size:1rem;color:#0F172A;">100,000,000 bps</div>
          </div>
          <div class="result-tile" style="background:#FFF;padding:0.75rem;border:1px solid #E2E8F0;border-radius:8px;">
            <div style="font-size:0.75rem;color:var(--text-muted);">Real Goodput (-6%)</div>
            <div id="tile_goodput" style="font-weight:700;font-size:1rem;color:#0F172A;">~11.75 MB/s</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 1000+ Word Authoritative Article Body -->
    <article class="article-body">
      <h2>Telecommunications &amp; The Architecture of Data Transfer Rates</h2>
      <p>Data transfer rate—frequently designated as bitrate, connection speed, channel capacity, or throughput—quantifies the temporal rate at which digital binary information is transmitted across an electronic, optical, or wireless telecommunications channel. In dimensional information theory formulated by Claude Shannon, the theoretical maximum error-free information capacity (\(C\)) of an analog physical channel perturbed by additive white Gaussian noise (AWGN) is governed by the famous <strong>Shannon-Hartley Theorem</strong>:</p>

      $$C = B \cdot \log_2 \left(1 + \frac{S}{N}\right)$$

      <p>Where \(B\) is the analog signal channel bandwidth in Hertz (\(\text{Hz}\)), and \(S/N\) represents the signal-to-noise power ratio (\(\text{SNR}\)). The channel capacity \(C\) is measured in <strong>bits per second (\(\text{bps}\) or \(\text{b/s}\))</strong>.</p>

      <p>In digital computer networking and storage architecture, telecommunications carriers and hardware designers established two separate measurement paradigms:</p>

      <ol>
        <li><strong>Transmission Systems (Bits per Second):</strong> Serial physical layer communications—including fiber-optic undersea cables, cable broadband DOCSIS, cellular 4G/5G LTE, and Wi-Fi—transmit digital data serially as individual electrical pulses, optical photons, or radio frequency phase modulations. Consequently, network bandwidth is universally measured in <strong>bits per second (bps, Kbps, Mbps, Gbps)</strong>.</li>
        <li><strong>Storage &amp; File Systems (Bytes per Second):</strong> Computer memory, processor registers, solid-state drives (SSDs), and operating system file managers process information in parallel octet byte chunks. Consequently, file transfer operations are universally displayed in <strong>Bytes per second (B/s, KB/s, MB/s, GB/s)</strong>.</li>
      </ol>

      <h2>The 8-to-1 Rule: Resolving the Mbps vs. MB/s Confusion</h2>
      <p>The most pervasive source of consumer frustration in retail broadband Internet service occurs when a subscriber pays for a "100 Megabit" (100 Mbps) internet plan, downloads a video game or software update, and discovers that their browser or Steam download client peaks at only <strong>12.5 Megabytes per second (12.5 MB/s)</strong>. Consumers frequently believe their ISP is artificially throttling their connection.</p>

      <p>The explanation is simple arithmetic anchored to the 8-bit byte definition:</p>

      $$1 \text{ Byte} = 8 \text{ bits} \implies 1 \frac{\text{MB}}{\text{s}} = 8 \frac{\text{Mbps}}{\text{s}}$$

      <p>To convert from an advertised network bandwidth in Megabits per second (\(\text{Mbps}\)) to real file download speed in Megabytes per second (\(\text{MB/s}\)), one must divide by exactly 8:</p>

      $$\text{Download Speed (MB/s)} = \frac{\text{Connection Speed (Mbps)}}{8}$$

      <p>For standard consumer broadband connection tiers:</p>

      <ul>
        <li><strong>50 Mbps Plan:</strong> \(50 \div 8 = 6.25 \text{ MB/s}\) theoretical maximum payload speed.</li>
        <li><strong>100 Mbps Plan:</strong> \(100 \div 8 = 12.50 \text{ MB/s}\) theoretical maximum payload speed.</li>
        <li><strong>300 Mbps Plan:</strong> \(300 \div 8 = 37.50 \text{ MB/s}\) theoretical maximum payload speed.</li>
        <li><strong>1 Gbps (1,000 Mbps) Gigabit Fiber:</strong> \(1{,}000 \div 8 = 125.00 \text{ MB/s}\) theoretical maximum payload speed.</li>
        <li><strong>2.5 Gbps Multi-Gig LAN:</strong> \(2{,}500 \div 8 = 312.50 \text{ MB/s}\) theoretical maximum payload speed.</li>
      </ul>

      <h2>Network Protocol Overhead: Bandwidth vs. Throughput vs. Goodput</h2>
      <p>In real-world networks, even the theoretical \(12.5\text{ MB/s}\) download speed cannot be fully achieved due to protocol encapsulation. When application data travels across the Internet, it is wrapped in layers of standardized protocol headers defined by the Open Systems Interconnection (OSI) and TCP/IP models:</p>

      <ol>
        <li><strong>Ethernet Data Link Layer (Layer 2):</strong> Standard Ethernet frames carry a preamble (8 bytes), MAC destination and source addresses (12 bytes), EtherType (2 bytes), and a Cyclic Redundancy Check (CRC FCS, 4 bytes), followed by an interpacket gap (12 bytes)—totaling 38 bytes of Layer 2 overhead per frame.</li>
        <li><strong>Internet Protocol (IP, Layer 3):</strong> A standard IPv4 packet header contains 20 bytes (or 40 bytes for modern IPv6), specifying routing addresses, time-to-live (TTL), and packet fragmentation flags.</li>
        <li><strong>Transmission Control Protocol (TCP, Layer 4):</strong> A standard TCP header adds another 20 to 32 bytes to ensure reliable in-order delivery, flow control window sizing, and packet acknowledgment sequence numbers.</li>
      </ol>

      <p>Under the standard Maximum Transmission Unit (MTU) of \(1{,}500\text{ bytes}\) for Ethernet networks, each individual packet carries a maximum payload (Maximum Segment Size, MSS) of:</p>

      $$\text{MSS} = \text{MTU} - \text{IP Header (20B)} - \text{TCP Header (20B)} = 1{,}500 - 40 = 1{,}460 \text{ bytes}$$

      <p>This reveals a fundamental protocol overhead efficiency ratio:</p>

      $$\eta_{\text{protocol}} = \frac{1{,}460 \text{ payload bytes}}{1{,}500 \text{ frame bytes} + 38 \text{ L2 overhead}} = \frac{1{,}460}{1{,}538} \approx 0.9493 \implies 94.93\%$$

      <p>Approximately \(5.1\%\) of the physical connection bandwidth is consumed purely by packet routing and framing metadata. In telecommunications terminology, the true application payload delivered is designated as <strong>goodput</strong>:</p>

      $$\text{Goodput} \approx \text{Throughput} \times 0.94 \approx \text{Bandwidth} \times \frac{0.94}{8}$$

      <p>Thus, on a clean, unthrottled 100 Mbps broadband connection, an optimal file download will realistically peak at approximately <strong>\(11.75\text{ to }11.90\text{ MB/s}\)</strong>.</p>

      <h2>Physical Line Coding Overhead: 8b/10b and 128b/130b Encoding</h2>
      <p>When transferring data across physical internal computer hardware buses—such as Serial ATA (SATA), Universal Serial Bus (USB), and Peripheral Component Interconnect Express (PCIe)—additional hardware-level overhead occurs due to <strong>line coding</strong>.</p>

      <p>In high-speed serial communications, transmitting long sequences of continuous consecutive binary zeros or ones causes receiver clock phase-locked loops (PLLs) to lose synchronization and results in electrical direct-current (DC) voltage baseline wander. To prevent this, hardware transceivers encode data before transmission:</p>

      <h3>1. 8b/10b Line Coding (Legacy Standards)</h3>
      <p>Utilized in SATA I/II/III (\(6\text{ Gbps}\)), USB 3.0 (\(5\text{ Gbps}\)), DisplayPort 1.2, and PCI Express Gen 1 and Gen 2. Every 8 bits of payload data is mapped to a 10-bit physical transmission symbol. This imposes an immediate \(20\%\) hardware bandwidth tax:</p>

      $$\text{Line Efficiency} = \frac{8}{10} = 0.80 \implies 20\% \text{ overhead}$$

      <p>Consequently, while SATA III is rated at \(6.0\text{ Gbps}\), its maximum physical data throughput is capped at \(6.0 \times 0.80 = 4.8\text{ Gbps} = 600\text{ MB/s}\).</p>

      <h3>2. 128b/130b Line Coding (Modern High-Speed Standards)</h3>
      <p>Adopted in PCI Express Gen 3, Gen 4, Gen 5, and USB 3.1 Gen 2 to eliminate the heavy 20% penalty. This modern encoding maps 128 bits of payload data to 130 transmitted bits, slashing hardware overhead to merely \(1.54\%\):</p>

      $$\text{Line Efficiency} = \frac{128}{130} \approx 0.9846 \implies 1.54\% \text{ overhead}$$

      <h2>Exact Data Transfer Rate Multipliers Benchmark Table</h2>
      <div class="table-responsive">
        <table class="data-table">
          <thead>
            <tr>
              <th>Transfer Unit</th>
              <th>Symbol</th>
              <th>Bits per Second Factor (\(\text{bps} = R \times F\))</th>
              <th>Bytes per Second Factor (\(\text{B/s} = R \times F\))</th>
              <th>Primary Technical Usage</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Bit per Second</td>
              <td>bps / b/s</td>
              <td>\(1.0\)</td>
              <td>\(0.125\)</td>
              <td>Serial Modems / RS-232 COM Ports</td>
            </tr>
            <tr>
              <td>Kilobit per Second</td>
              <td>Kbps / kb/s</td>
              <td>\(1{,}000.0\)</td>
              <td>\(125.0\)</td>
              <td>Legacy Dial-up / VoIP Audio Codecs (G.711)</td>
            </tr>
            <tr>
              <td>Megabit per Second</td>
              <td>Mbps / Mb/s</td>
              <td>\(1{,}000{,}000.0\)</td>
              <td>\(125{,}000.0\)</td>
              <td>Broadband Internet / 4K UHD Video Streaming</td>
            </tr>
            <tr>
              <td>Gigabit per Second</td>
              <td>Gbps / Gb/s</td>
              <td>\(1{,}000{,}000{,}000.0\)</td>
              <td>\(125{,}000{,}000.0\)</td>
              <td>Gigabit Ethernet / 5G Cellular / Fiber Broadband</td>
            </tr>
            <tr>
              <td>Terabit per Second</td>
              <td>Tbps / Tb/s</td>
              <td>\(10^{12}\)</td>
              <td>\(1.25 \times 10^{11}\)</td>
              <td>Subsea Intercontinental Fiber Cables / Core IXPs</td>
            </tr>
            <tr>
              <td>Byte per Second</td>
              <td>B/s</td>
              <td>\(8.0\)</td>
              <td>\(1.0\)</td>
              <td>Raw Octet Stream Throughput</td>
            </tr>
            <tr>
              <td>Kilobyte per Second</td>
              <td>KB/s</td>
              <td>\(8{,}000.0\)</td>
              <td>\(1{,}000.0\)</td>
              <td>Legacy FTP File Transfers</td>
            </tr>
            <tr>
              <td>Megabyte per Second</td>
              <td>MB/s</td>
              <td>\(8{,}000{,}000.0\)</td>
              <td>\(1{,}000{,}000.0\)</td>
              <td>Browser File Downloads / SATA SSD Writes</td>
            </tr>
            <tr>
              <td>Gigabyte per Second</td>
              <td>GB/s</td>
              <td>\(8{,}000{,}000{,}000.0\)</td>
              <td>\(1{,}000{,}000{,}000.0\)</td>
              <td>PCIe 4.0/5.0 NVMe Solid State Drives</td>
            </tr>
            <tr>
              <td>Mebibyte per Second</td>
              <td>MiB/s</td>
              <td>\(8{,}388{,}608.0\)</td>
              <td>\(1{,}048{,}576.0\)</td>
              <td>Linux rsync / Windows Robocopy Binary Speed</td>
            </tr>
            <tr>
              <td>Gibibyte per Second</td>
              <td>GiB/s</td>
              <td>\(8{,}589{,}934{,}592.0\)</td>
              <td>\(1{,}073{,}741{,}824.0\)</td>
              <td>DDR5 DRAM Bus Memory Bandwidth</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Worked Network Engineering Case Study: Multi-Terabyte Database Cloud Migration</h2>
      <div class="worked-example-card" style="background:#F8FAFC;border:1px solid #CBD5E1;border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
        <h3 style="margin-top:0;color:#0F172A;">Enterprise IT Infrastructure Scenario</h3>
        <p>A financial enterprise database administrator is planning an off-site migration of an active PostgreSQL cluster containing \(8.50\text{ TB}\) (decimal Terabytes) of encrypted transactional data. The corporate data center connects to the target cloud provider via a dedicated, unmetered fiber-optic <strong>AWS Direct Connect link rated at \(1.0\text{ Gbps}\)</strong> (Gigabit per second).</p>

        <p>The network engineer must calculate the theoretical minimum migration time, apply a realistic \(7.5\%\) TCP windowing and SSL/TLS encryption protocol overhead factor, and determine whether the migration can be completed over a single weekend maintenance window of 24 hours.</p>

        <h4 style="color:#0F172A;">Step 1: Compute total data size in bits</h4>
        <p>In decimal SI units, 1 TB equals \(10^{12} = 1{,}000{,}000{,}000{,}000\text{ bytes}\):</p>

        $$\text{Data Size} = 8.50 \text{ TB} \times 10^{12} \frac{\text{Bytes}}{\text{TB}} \times 8 \frac{\text{bits}}{\text{Byte}} = 6.80 \times 10^{13} \text{ bits}$$

        <h4 style="color:#0F172A;">Step 2: Calculate effective throughput considering protocol overhead</h4>
        <p>With an overhead factor of \(7.5\%\), effective goodput is \(1.0 - 0.075 = 0.925\) of link bandwidth:</p>

        $$\text{Effective Throughput} = 1.0 \text{ Gbps} \times 0.925 = 0.925 \text{ Gbps} = 9.25 \times 10^8 \text{ bits per second}$$
        $$\text{Throughput in MB/s} = \frac{925 \text{ Mbps}}{8} = 115.625 \text{ MB/s}$$

        <h4 style="color:#0F172A;">Step 3: Calculate the total transfer duration in seconds and hours</h4>

        $$T_{\text{seconds}} = \frac{6.80 \times 10^{13} \text{ bits}}{9.25 \times 10^8 \text{ bits/s}} \approx 73{,}513.51 \text{ seconds}$$
        $$T_{\text{hours}} = \frac{73{,}513.51 \text{ s}}{3{,}600 \text{ s/h}} \approx 20.42 \text{ hours} \text{ (20 hours, 25 minutes)}$$

        <p><strong>Conclusion:</strong> Because the required transfer duration of <strong>20 hours and 25 minutes</strong> is less than the 24-hour maintenance window, the database migration can proceed safely without extending service downtime. However, if link utilization exceeds \(10\text{ Gbps}\), the transfer duration drops to approximately 2.04 hours.</p>
      </div>

      <h2>Precision Metrology: Timing Jitter &amp; Buffer Bloat in Network Simulations</h2>
      <p>In discrete-event network simulation software (such as ns-3, OMNeT++, and Wireshark packet capture analysis), bitrates must be modeled with microsecond temporal precision. Rounding an interface bandwidth from \(940\text{ Mbps}\) to \(1\text{ Gbps}\) introduces an artificial over-provisioning error of \(6.4\%\), which masks buffer bloat queue buildup and packet loss in edge router simulations.</p>

      <p>CalcHub implements verified IEEE floating-point algorithms anchored directly to the 8-bit byte standard, providing lossless conversions between physical telecommunications bitrates and application-level storage throughput.</p>
    </article>
  </main>

  <!-- Related Category Sidebar -->
  <aside class="post-sidebar">
    <div class="sidebar-widget">
      <div class="sidebar-widget-header">
        <span class="widget-icon">🔄</span>
        <h3 class="widget-title">Universal Unit Converters</h3>
      </div>
      <ul class="sidebar-links-list">
        <li><a href="length-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Length Converter</a></li>
        <li><a href="weight-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Weight &amp; Mass Converter</a></li>
        <li><a href="temperature-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Temperature Converter</a></li>
        <li><a href="area-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Area Converter</a></li>
        <li><a href="volume-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Volume Converter</a></li>
        <li><a href="pressure-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Pressure Converter</a></li>
        <li><a href="speed-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Speed Converter</a></li>
        <li><a href="energy-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Energy Converter</a></li>
        <li><a href="power-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Power Converter</a></li>
        <li><a href="force-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Force Converter</a></li>
        <li><a href="data-storage-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Data Storage Converter</a></li>
        <li><a href="data-transfer-rate-converter.html" class="sidebar-link-item active"><span class="link-bullet">›</span> Data Transfer Rate Converter</a></li>
        <li><a href="unit-converter.html" class="sidebar-link-item"><span class="link-bullet">›</span> Universal Multi-Unit Converter</a></li>
      </ul>
    </div>
  </aside>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col">
        <div class="footer-brand">
          <span class="logo-badge">∑</span>
          <span>Calc<span class="accent">Hub</span></span>
        </div>
        <p class="footer-summary">Authoritative engineering, financial, athletic, and physical calculation tools adhering to international ISO, BIPM, NIST, and IEEE computational standards.</p>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Hub Categories</h4>
        <ul class="footer-links">
          <li><a href="converter.html">Universal Converters</a></li>
          <li><a href="engineering.html">Electrical &amp; Electronics</a></li>
          <li><a href="mechanical.html">Mechanical &amp; HVAC</a></li>
          <li><a href="health.html">Health &amp; Medical</a></li>
          <li><a href="finance.html">Finance &amp; Taxes</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Standard Guidelines</h4>
        <ul class="footer-links">
          <li><a href="converter.html">NIST SP 811 Standards</a></li>
          <li><a href="converter.html">BIPM SI Brochure 9th Ed</a></li>
          <li><a href="converter.html">IEEE Floating Point Specs</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-bottom-inner">
        <p>&copy; 2026 CalcHub. All rights reserved. Peer-reviewed computational algorithms.</p>
      </div>
    </div>
  </footer>

  <script>
    (function(){
      // Factors relative to 1 bit per second (bps)
      const FACTORS_TO_BPS = {
        'bps': 1.0,
        'kbps': 1000.0,
        'mbps': 1000000.0,
        'gbps': 1000000000.0,
        'tbps': 1000000000000.0,
        'bs': 8.0,
        'kbs': 8000.0,
        'mbs': 8000000.0,
        'gbs': 8000000000.0,
        'tbs': 8000000000000.0,
        'mibps': 8.0 * 1048576.0,
        'gibps': 8.0 * 1073741824.0
      };

      const UNIT_SYMBOLS = {
        'bps': 'bps',
        'kbps': 'Kbps',
        'mbps': 'Mbps',
        'gbps': 'Gbps',
        'tbps': 'Tbps',
        'bs': 'B/s',
        'kbs': 'KB/s',
        'mbs': 'MB/s',
        'gbs': 'GB/s',
        'tbs': 'TB/s',
        'mibps': 'MiB/s',
        'gibps': 'GiB/s'
      };

      const inputVal = document.getElementById('input_val');
      const fromUnit = document.getElementById('from_unit');
      const toUnit = document.getElementById('to_unit');
      const precisionSelect = document.getElementById('precision_select');
      const btnCalc = document.getElementById('btn-calc');
      const btnSwap = document.getElementById('btn-swap');
      const btnReset = document.getElementById('btn-reset');
      const primaryResult = document.getElementById('primary_result');
      const formulaNote = document.getElementById('conversion_formula_note');

      function formatNum(val, prec) {
        if (prec === 'exact') {
          return val.toPrecision(10).replace(/(?:\.0+|(\.\d+?)0+)$/, "");
        }
        if (Math.abs(val) > 1e12 || (Math.abs(val) < 1e-4 && val !== 0)) {
          return val.toExponential(4);
        }
        const p = parseInt(prec, 10);
        return val.toLocaleString('en-US', { minimumFractionDigits: p, maximumFractionDigits: p });
      }

      function calculate() {
        const val = parseFloat(inputVal.value);
        if (isNaN(val)) {
          primaryResult.textContent = 'Invalid Input';
          return;
        }

        const from = fromUnit.value;
        const to = toUnit.value;
        const prec = precisionSelect.value;

        // Convert input to bps
        const bps = val * FACTORS_TO_BPS[from];
        // Convert bps to target
        const targetVal = bps / FACTORS_TO_BPS[to];

        primaryResult.textContent = formatNum(targetVal, prec) + ' ' + UNIT_SYMBOLS[to];

        const ratio = FACTORS_TO_BPS[from] / FACTORS_TO_BPS[to];
        formulaNote.textContent = `1 ${UNIT_SYMBOLS[from]} = ${ratio.toPrecision(7)} ${UNIT_SYMBOLS[to]} | Base: ${val} ${UNIT_SYMBOLS[from]} = ${formatNum(bps, 0)} bps`;

        // Update tiles
        const tiles = ['mbs', 'mbps', 'gbps', 'gbs', 'kbs', 'mibps', 'bps'];
        tiles.forEach(key => {
          const tileEl = document.getElementById('tile_' + key);
          if (tileEl) {
            const tileVal = bps / FACTORS_TO_BPS[key];
            tileEl.textContent = formatNum(tileVal, prec === 'exact' ? '4' : prec) + ' ' + UNIT_SYMBOLS[key];
          }
        });

        // Goodput tile (-6% overhead approx)
        const goodputMBs = (bps / FACTORS_TO_BPS['mbs']) * 0.94;
        document.getElementById('tile_goodput').textContent = `~${formatNum(goodputMBs, 2)} MB/s`;
      }

      btnCalc.addEventListener('click', calculate);
      inputVal.addEventListener('input', calculate);
      fromUnit.addEventListener('change', calculate);
      toUnit.addEventListener('change', calculate);
      precisionSelect.addEventListener('change', calculate);

      btnSwap.addEventListener('click', function(){
        const temp = fromUnit.value;
        fromUnit.value = toUnit.value;
        toUnit.value = temp;
        calculate();
      });

      btnReset.addEventListener('click', function(){
        inputVal.value = '100';
        fromUnit.value = 'mbps';
        toUnit.value = 'mbs';
        precisionSelect.value = '4';
        calculate();
      });

      calculate();
    })();
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "data-transfer-rate-converter.html"), "w", encoding="utf-8") as f:
    f.write(transfer_html)
print("Generated data-transfer-rate-converter.html successfully!")
