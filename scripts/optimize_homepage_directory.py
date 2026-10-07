import json
import re

with open('tools-directory.json', 'r', encoding='utf-8') as f:
    tools = json.load(f)

# Trim duplicate 's' field
trimmed_tools = [{'c': t['c'], 'i': t['i'], 't': t['t'], 'u': t['u'].replace('.html', ''), 'd': t['d'], 'f': t['f']} for t in tools]

# Save trimmed tools-directory.json
with open('tools-directory.json', 'w', encoding='utf-8') as f:
    json.dump(trimmed_tools, f, separators=(',', ':'), ensure_ascii=False)

# Select top 24 diverse featured tools (2 from each category)
cats_seen = {}
featured_tools = []
remaining_tools = []

for tool in trimmed_tools:
    c = tool.get('c', '')
    if cats_seen.get(c, 0) < 2 and len(featured_tools) < 24:
        cats_seen[c] = cats_seen.get(c, 0) + 1
        featured_tools.append(tool)
    else:
        remaining_tools.append(tool)

while len(featured_tools) < 24 and remaining_tools:
    featured_tools.append(remaining_tools.pop(0))

def render_card_html(t):
    cat = t.get('c', '')
    icon = t.get('i', '🧮')
    title = t.get('t', '')
    url = t.get('u', '')
    desc = t.get('d', '')
    formula = t.get('f', '')
    search = f"{title} {url} {desc} {cat}".lower()
    clean_url = f"/{url}" if not url.startswith('/') else url
    
    return f'''        <div class="directory-tool-card" data-cat="{cat.lower()}" data-search="{search}" style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:1rem;display:flex;flex-direction:column;justify-content:space-between;transition:transform 0.2s,box-shadow 0.2s;">
          <div>
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
              <span style="font-size:1.5rem;">{icon}</span>
              <span style="font-size:0.72rem;background:#F1F5F9;color:#475569;padding:2px 8px;border-radius:12px;font-weight:600;">{cat}</span>
            </div>
            <h3 style="margin:0 0 0.35rem;font-size:1rem;color:#0F172A;"><a href="{clean_url}" style="color:#0F172A;text-decoration:none;">{title}</a></h3>
            <p style="margin:0 0 0.75rem;font-size:0.82rem;color:#64748B;line-height:1.4;">{desc}</p>
          </div>
          <div style="display:flex;align-items:center;justify-content:space-between;border-top:1px solid #F1F5F9;padding-top:0.65rem;margin-top:0.5rem;">
            <code style="font-size:0.75rem;color:#2563EB;background:#EFF6FF;padding:2px 6px;border-radius:4px;">{formula}</code>
            <a href="{clean_url}" style="font-size:0.82rem;font-weight:700;color:#2563EB;text-decoration:none;">Launch &rarr;</a>
          </div>
        </div>'''

initial_cards_html = "\n".join(render_card_html(t) for t in featured_tools)
compact_tools_json = json.dumps(trimmed_tools, separators=(',', ':'), ensure_ascii=False)

js_code = """
      <script>
        let allToolsData = null;
        let isAllLoaded = false;

        function getAllToolsData() {
          if (!allToolsData) {
            try {
              const el = document.getElementById('all-directory-data');
              allToolsData = el ? JSON.parse(el.textContent) : [];
            } catch (e) {
              allToolsData = [];
            }
          }
          return allToolsData;
        }

        function createToolCardElement(t) {
          const cleanUrl = t.u.startsWith('/') ? t.u : '/' + t.u;
          const card = document.createElement('div');
          card.className = 'directory-tool-card';
          card.setAttribute('data-cat', (t.c || '').toLowerCase());
          card.setAttribute('data-search', (t.t + ' ' + t.u + ' ' + t.d + ' ' + t.c).toLowerCase());
          card.style.cssText = 'background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:1rem;display:flex;flex-direction:column;justify-content:space-between;transition:transform 0.2s,box-shadow 0.2s;';
          card.innerHTML = `
            <div>
              <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">
                <span style="font-size:1.5rem;">${t.i || '🧮'}</span>
                <span style="font-size:0.72rem;background:#F1F5F9;color:#475569;padding:2px 8px;border-radius:12px;font-weight:600;">${t.c || ''}</span>
              </div>
              <h3 style="margin:0 0 0.35rem;font-size:1rem;color:#0F172A;"><a href="${cleanUrl}" style="color:#0F172A;text-decoration:none;">${t.t}</a></h3>
              <p style="margin:0 0 0.75rem;font-size:0.82rem;color:#64748B;line-height:1.4;">${t.d}</p>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between;border-top:1px solid #F1F5F9;padding-top:0.65rem;margin-top:0.5rem;">
              <code style="font-size:0.75rem;color:#2563EB;background:#EFF6FF;padding:2px 6px;border-radius:4px;">${t.f || ''}</code>
              <a href="${cleanUrl}" style="font-size:0.82rem;font-weight:700;color:#2563EB;text-decoration:none;">Launch &rarr;</a>
            </div>
          `;
          return card;
        }

        function loadAllDirectoryTools() {
          if (isAllLoaded) return;
          const grid = document.getElementById('directory-tools-grid');
          const data = getAllToolsData();
          grid.innerHTML = '';
          const frag = document.createDocumentFragment();
          data.forEach(t => {
            frag.appendChild(createToolCardElement(t));
          });
          grid.appendChild(frag);
          isAllLoaded = true;
          const loadBtn = document.getElementById('directory-load-more');
          if (loadBtn) loadBtn.style.display = 'none';
        }

        function filterDirectoryTools() {
          const q = document.getElementById('directory-search-input').value.toLowerCase().trim();
          const grid = document.getElementById('directory-tools-grid');
          const noResults = document.getElementById('no-search-results');
          const loadBtn = document.getElementById('directory-load-more');

          if (!q) {
            if (noResults) noResults.style.display = 'none';
            if (loadBtn) loadBtn.style.display = isAllLoaded ? 'none' : 'block';
            if (isAllLoaded) {
              const cards = grid.querySelectorAll('.directory-tool-card');
              cards.forEach(c => c.style.display = 'flex');
            } else {
              grid.innerHTML = '';
              const frag = document.createDocumentFragment();
              getAllToolsData().slice(0, 24).forEach(t => {
                frag.appendChild(createToolCardElement(t));
              });
              grid.appendChild(frag);
            }
            return;
          }

          if (loadBtn) loadBtn.style.display = 'none';
          const data = getAllToolsData();
          const matches = data.filter(t => {
            const searchData = (t.t + ' ' + t.u + ' ' + t.d + ' ' + (t.c || '')).toLowerCase();
            return searchData.includes(q);
          });

          grid.innerHTML = '';
          if (matches.length === 0) {
            if (noResults) noResults.style.display = 'block';
          } else {
            if (noResults) noResults.style.display = 'none';
            const frag = document.createDocumentFragment();
            matches.forEach(t => {
              frag.appendChild(createToolCardElement(t));
            });
            grid.appendChild(frag);
          }
        }
      </script>"""

directory_replacement = f'''      <div id="directory-tools-grid" style="display:grid;grid-template-columns:repeat(auto-fill, minmax(260px, 1fr));gap:1rem;">
{initial_cards_html}
      </div>

      <div id="directory-load-more" style="text-align:center;margin-top:2.5rem;">
        <button type="button" id="btn-load-all-tools" onclick="loadAllDirectoryTools()" class="btn btn-secondary" style="padding:0.85rem 2.25rem;font-weight:600;font-size:1rem;background:#FFFFFF;border:2px solid #2563EB;color:#2563EB;border-radius:10px;cursor:pointer;transition:all 0.2s;">
          📂 Explore All 387 Online Calculators (Expand Full Directory)
        </button>
      </div>

      <div id="no-search-results" style="display:none;text-align:center;padding:3rem;color:#64748B;">
        <p style="font-size:1.1rem;margin-bottom:0.5rem;">No calculators match your search.</p>
        <button type="button" class="btn btn-secondary" onclick="document.getElementById('directory-search-input').value='';filterDirectoryTools();">Clear Search</button>
      </div>

      <script id="all-directory-data" type="application/json">
{compact_tools_json}
      </script>
{js_code}'''

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

start_marker = '<div id="directory-tools-grid"'
end_marker = '</section>\n  </main>'

idx_start = index_content.find(start_marker)
idx_end = index_content.find(end_marker)

if idx_start == -1 or idx_end == -1:
    print(f"Error finding markers: start={idx_start}, end={idx_end}")
else:
    new_index_content = index_content[:idx_start] + directory_replacement + '\n    ' + index_content[idx_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_index_content)
    
    old_size = len(index_content.encode('utf-8')) / 1024
    new_size = len(new_index_content.encode('utf-8')) / 1024
    print(f"Successfully optimized index.html!")
    print(f"New size: {new_size:.1f} KB (Reduced by {old_size - new_size:.1f} KB)")
