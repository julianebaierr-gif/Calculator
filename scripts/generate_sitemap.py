"""
Generates sitemap.xml for all HTML pages in CalcHub.
"""

import os
import glob
from datetime import date

def main():
    today = date.today().isoformat()
    html_files = glob.glob("*.html")
    html_files = [f for f in html_files if f != "404.html"]

    # Sort files logically: index first, category hubs, then tools
    categories = [
        "health.html", "finance.html", "math.html", "engineering.html",
        "solar-energy.html", "mechanical.html", "civil.html", "chemical.html",
        "fire-safety.html", "programmer.html", "datetime.html", "converter.html"
    ]

    tools = [f for f in html_files if f != "index.html" and f not in categories]

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
            urls.append(f"""  <url>
    <loc>https://calchub.org/{cat}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.95</priority>
  </url>""")

    # 3. Calculators
    for tool in sorted(tools):
        urls.append(f"""  <url>
    <loc>https://calchub.org/{tool}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
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

    print(f"Generated sitemap.xml with {len(urls)} URLs.")

if __name__ == "__main__":
    main()
