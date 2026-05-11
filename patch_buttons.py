
# Patch 1: Company buttons
# Patch 2: Policies button + table action column
# Patch 3: All table headers get Islemler column, all rows get edit/delete buttons
# Patch 4: Settings save
# Patch 5: Header newRecordBtn
# Patch 6: Comprehensive JS

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Company Kaydet / Sifirla ─────────────────────────────
html = html.replace(
    '<div class="actions"><button class="primary-btn">Kaydet</button><button class="ghost-btn">Sıfırla</button></div>',
    '<div class="actions"><button class="primary-btn" onclick="saveCompany()">Kaydet</button><button class="ghost-btn" onclick="resetCompany()">Sıfırla</button></div>'
)

# ── 2. Settings Kaydet ──────────────────────────────────────
html = html.replace(
    '<button class="btn">Kaydet</button>\n      </div>\n    </div>\n  </div>\n</section>\n\n<section id="application"',
    '<button class="btn" onclick="saveSettings()">Kaydet</button>\n      </div>\n    </div>\n  </div>\n</section>\n\n<section id="application"'
)

# ── 3. + Yeni Politika ──────────────────────────────────────
html = html.replace(
    '<button class="primary-btn">+ Yeni Politika</button>',
    '<button class="primary-btn" onclick="openAddRow(\'policies\')">+ Yeni Politika</button>'
)

# ── 4. Header + Yeni Kayit ──────────────────────────────────
html = html.replace(
    '<button class="primary-btn" id="newRecordBtn">+ Yeni Kayıt</button>',
    '<button class="primary-btn" id="newRecordBtn" onclick="openAddRow(\'current\')">+ Yeni Kayıt</button>'
)

# ── 5. Add Islemler column to all main tables ───────────────
# Helper: add <th>İşlemler</th> to thead rows of specific tables
import re

def add_actions_col(html, table_id):
    # Add th to thead
    pattern = r'(<table id="' + table_id + r'"[^>]*>.*?<thead><tr>)(.*?)(</tr></thead>)'
    def add_th(m):
        return m.group(1) + m.group(2) + '<th>İşlemler</th>' + m.group(3)
    html = re.sub(pattern, add_th, html, flags=re.DOTALL)
    # Add td with edit/delete to each tbody tr
    # We'll do this in JS dynamically instead - safer
    return html

for tid in ['pol-tbl','proc-table','asset-table','risk-table','treatment-table',
        'training-table','audit-table','dfi-table','ygg-table','app-table','soa-table',
        'doc-table','example-doc-table']:
    html = add_actions_col(html, tid)

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Patch OK')
