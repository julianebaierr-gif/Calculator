# -*- coding: utf-8 -*-
import os
import glob
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def make_unique():
    html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    updated = 0

    pattern = re.compile(
        r'<p style="color: var\(--text-secondary, #475569\); margin-bottom: 1\.25rem;\">Accelerate your engineering, mathematical, or scientific analysis with these verified companion tools from our <a href="([^"]+)">([^<]+)</a> suite:</p>'
    )

    for filepath in html_files:
        filename = os.path.basename(filepath)
        tool_clean = filename.replace("-calculator.html", "").replace(".html", "").replace("-", " ")
        
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        def repl(m):
            hub_url = m.group(1)
            hub_name = m.group(2)
            return f'<p style="color: var(--text-secondary, #475569); margin-bottom: 1.25rem;">Explore precision analytical companion models and dedicated verification solvers from our <a href="{hub_url}">{hub_name}</a> directory for {tool_clean} analysis:</p>'

        new_content = pattern.sub(repl, content)
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated += 1

    print(f"Updated {updated} files with 100% unique subtitles.")

if __name__ == "__main__":
    make_unique()
