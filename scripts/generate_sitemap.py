"""
Generates sitemap.xml for all HTML pages in CalcHub using clean URLs.
Complies with Vercel's cleanUrls: true setting.
"""

import os
import glob
from datetime import date

def main():
    today = date.today().isoformat()
    html_files = glob.glob("*.html")
    # Exclude 404 error page and canonical redirects
    aliases = {
        "3-phase-power-calculator.html",
        "waist-to-height-ratio-calculator.html",
        "fire-sprinkler-calculator.html",
        "privacy.html",
        "legal.html"
    }
    html_files = [f for f in html_files if f != "404.html" and f not in aliases]

    categories = [
        "health.html", "finance.html", "math.html", "engineering.html",
        "solar-energy.html", "mechanical.html", "civil.html", "chemical.html",
        "fire-safety.html", "programmer.html", "datetime.html", "converter.html"
    ]

    legal_pages = [
        "about.html", "privacy-policy.html", "terms.html", "disclaimer.html", "contact.html"
    ]

    tools = [f for f in html_files if f != "index.html" and f not in categories and f not in legal_pages]

    urls = []
    # 1. Homepage
    urls.append(f"""  <url>
    <loc>https://calchub.org/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""")

    # 2. Category Hubs
    for cat in sorted(categories):
        if os.path.exists(cat):
            clean_name = cat.replace(".html", "")
            urls.append(f"""  <url>
    <loc>https://calchub.org/{clean_name}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.95</priority>
  </url>""")

    # 3. Calculators
    for tool in sorted(tools):
        clean_name = tool.replace(".html", "")
        urls.append(f"""  <url>
    <loc>https://calchub.org/{clean_name}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>""")

    # 4. Legal & EEAT Pages
    for lp in sorted(legal_pages):
        if os.path.exists(lp):
            clean_name = lp.replace(".html", "")
            urls.append(f"""  <url>
    <loc>https://calchub.org/{clean_name}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.70</priority>
  </url>""")

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">

{"\n".join(urls)}

</urlset>
"""

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    print(f"Generated clean sitemap.xml with {len(urls)} URLs.")

if __name__ == "__main__":
    main()
