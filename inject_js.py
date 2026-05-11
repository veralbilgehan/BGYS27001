
new_js = """
    // ── Toast ────────────────────────────────────────────────────────────
    function toast(msg, type) {
      type = type || 'success';
      var t = document.createElement('div');
      t.textContent = msg;
      var bg = type==='success'?'#22c55e':type==='error'?'#ef4444':'#3b82f6';
      t.style.cssText = 'position:fixed;bottom:24px;right:24px;padding:10px 20px;border-radius:8px;color:#fff;font-size:14px;font-weight:600;z-index:9999;box-shadow:0 4px 12px rgba(0,0,0,.2);background:'+bg;
      document.body.appendChild(t);
      setTimeout(function(){t.remove();}, 2800);
    }

    // ── Company form ────────────────────────────────────────────────────
    var _companyDefaults = {};
    document.querySelectorAll('#company .input, #company .textarea').forEach(function(el,i){
      _companyDefaults[i] = el.value;
      var sv = localStorage.getItem('company_'+i);
      if (sv !== null) el.value = sv;
    });
    function saveCompany() {
      document.querySelectorAll('#company .input, #company .textarea').forEach(function(el,i){
        localStorage.setItem('company_'+i, el.value);
      });
      toast('Kuruluş bilgileri kaydedildi.');
    }
    function resetCompany() {
      if (!confirm('Formu varsayılana sıfırlamak istiyor musunuz?')) return;
      document.querySelectorAll('#company .input, #company .textarea').forEach(function(el,i){
        el.value = _companyDefaults[i] || '';
        localStorage.removeItem('company_'+i);
      });
      toast('Form sıfırlandı.', 'info');
    }

    // ── Settings form ───────────────────────────────────────────────────
    function saveSettings() {
      document.querySelectorAll('#settings input[type=text], #settings input[type=date]').forEach(function(el,i){
        localStorage.setItem('setting_'+i, el.value);
      });
      toast('Ayarlar kaydedildi.');
    }
    document.querySelectorAll('#settings input[type=text], #settings input[type=date]').forEach(function(el,i){
      var sv = localStorage.getItem('setting_'+i);
      if (sv !== null) el.value = sv;
    });

    // ── Table action buttons ────────────────────────────────────────────
    var TABLE_COLS = {
      'pol-tbl':        ['Kod','Ad','Kapsam','Revizyon','Durum','Tarih'],
      'proc-table':     ['Kod','Ad','Kapsam','Versiyon','Durum','Tarih'],
      'asset-table':    ['ID','Varlık Adı','Tip','Sahip','G','B','E','Risk','Konum'],
      'risk-table':     ['ID','Varlık','Tehdit','Zafiyet','Olasılık','Etki','Skor','Durum','Kontrol','Kalan'],
      'treatment-table':['Risk ID','Tehdit','Yöntem','Kontrol','Sorumlu','Termin','Durum'],
      'training-table': ['Eğitim','Eğitici','Tarih','Süre','Katılımcı','Belge'],
      'audit-table':    ['No','Tip','Madde','Açıklama','Denetçi','DFI','Durum'],
      'dfi-table':      ['No','Kaynak','Açıklama','Kök Neden','Durum','Sorumlu','Termin','Kapanış'],
      'ygg-table':      ['No','Karar','Sorumlu','Termin','Durum'],
      'app-table':      ['Aşama','Aktivite','Tarih','Kurum','Durum','Notlar'],
      'soa-table':      ['Madde','Kontrol','Durum','Hariç Neden','Kanıt'],
      'doc-table':      ['Kod','Dokuman Adi','Klasor','Versiyon','Durum','Tarih'],
      'example-doc-table': ['Belge / Dokuman','Kaynak','Duzeltme Durumu','BGYS Kayit Durumu','Hedef Klasor','Sorumlu','Son Islem','Not']
    };

    function addRowActions() {
      Object.keys(TABLE_COLS).forEach(function(tid){
        var tbl = document.getElementById(tid);
        if (!tbl) return;
        tbl.querySelectorAll('tbody tr').forEach(function(tr){
          if (tr.querySelector('.row-act')) return;
          var td = document.createElement('td');
          td.className = 'row-act';
          td.style.whiteSpace = 'nowrap';
          td.innerHTML = '<button onclick="editRow(this)" style="background:#3b82f6;color:#fff;border:none;padding:3px 9px;border-radius:4px;cursor:pointer;font-size:11px;margin-right:4px">✏ Düzenle</button>'
                       + '<button onclick="deleteRow(this)" style="background:#ef4444;color:#fff;border:none;padding:3px 9px;border-radius:4px;cursor:pointer;font-size:11px">🗑 Sil</button>';
          tr.appendChild(td);
        });
      });
    }

    function deleteRow(btn) {
      var tr = btn.closest('tr');
      var preview = Array.from(tr.querySelectorAll('td')).slice(0,2).map(function(td){return td.textContent.trim();}).join(' - ');
      if (!confirm('"'+preview+'" satırını silmek istiyor musunuz?')) return;
      tr.style.transition = 'opacity .25s';
      tr.style.opacity = '0';
      setTimeout(function(){tr.remove();}, 260);
      toast('Satır silindi.', 'error');
    }

    var _editTr = null, _editCells = null;

    function editRow(btn) {
      var tr = btn.closest('tr');
      var tbl = tr.closest('table');
      var tid = tbl ? tbl.id : '';
      var cols = TABLE_COLS[tid] || [];
      var cells = Array.from(tr.querySelectorAll('td')).filter(function(td){return !td.classList.contains('row-act');});
      _editTr = tr; _editCells = cells;

      var form = '<h3 style="margin-bottom:14px">Satır Düzenle</h3><div style="display:grid;gap:9px;max-height:55vh;overflow-y:auto;padding-right:4px">';
      cells.forEach(function(td,i){
        var label = cols[i] || ('Sütun '+(i+1));
        var val = td.textContent.trim().replace(/"/g,'&quot;');
        form += '<div><label style="display:block;margin-bottom:3px;font-weight:600;font-size:12px">'+label+'</label>'
              + '<input type="text" value="'+val+'" data-col="'+i+'" style="width:100%;padding:6px 8px;border:1px solid #ddd;border-radius:5px;font-size:13px"></div>';
      });
      form += '</div><div style="margin-top:14px;display:flex;gap:8px;justify-content:flex-end">'
            + '<button onclick="closeModal()" style="background:#f1f5f9;color:#334155;border:none;padding:7px 16px;border-radius:6px;cursor:pointer">Çık</button>'
            + '<button onclick="applyEdit()" class="btn">Kaydet</button></div>';

      document.getElementById('modal-content').innerHTML = form;
      document.getElementById('modal-overlay').style.display = 'flex';
    }

    function applyEdit() {
      if (!_editTr || !_editCells) { closeModal(); return; }
      document.querySelectorAll('#modal-content input[data-col]').forEach(function(inp){
        var i = parseInt(inp.getAttribute('data-col'));
        if (_editCells[i]) {
          var badge = _editCells[i].querySelector('.badge');
          if (badge) { badge.textContent = inp.value; }
          else { _editCells[i].textContent = inp.value; }
        }
      });
      toast('Güncellendi.');
      closeModal();
    }

    // ── openAddRow: + Yeni butonlari ────────────────────────────────────
    var _currentSection = 'dashboard';
    function openAddRow(sec) {
      var sid = sec === 'current' ? _currentSection : sec;
      var secEl = document.getElementById(sid);
      if (!secEl) { toast('Bölüm bulunamadı.','error'); return; }
      var tbl = secEl.querySelector('table[id]');
      if (!tbl) { toast('Bu bölümde tablo yok.','error'); return; }
      var tid = tbl.id;
      var cols = TABLE_COLS[tid] || [];
      if (!cols.length) { toast('Sütun tanımı bulunamadı.','error'); return; }

      var form = '<h3 style="margin-bottom:14px">Yeni Kayıt Ekle</h3><div style="display:grid;gap:9px;max-height:55vh;overflow-y:auto;padding-right:4px">';
      cols.forEach(function(label){
        form += '<div><label style="display:block;margin-bottom:3px;font-weight:600;font-size:12px">'+label+'</label>'
              + '<input type="text" placeholder="'+label+'..." style="width:100%;padding:6px 8px;border:1px solid #ddd;border-radius:5px;font-size:13px"></div>';
      });
      form += '</div><div style="margin-top:14px;display:flex;gap:8px;justify-content:flex-end">'
            + '<button onclick="closeModal()" style="background:#f1f5f9;color:#334155;border:none;padding:7px 16px;border-radius:6px;cursor:pointer">Çık</button>'
            + '<button onclick="saveNewRow(\''+tid+'\')" class="btn">Kaydet</button></div>';

      document.getElementById('modal-content').innerHTML = form;
      document.getElementById('modal-overlay').style.display = 'flex';
    }

    function openAddRowByTable(tid) {
      var cols = TABLE_COLS[tid] || [];
      if (!cols.length) { toast('Sütun tanımı bulunamadı.','error'); return; }

      var form = '<h3 style="margin-bottom:14px">Yeni Kayıt Ekle</h3><div style="display:grid;gap:9px;max-height:55vh;overflow-y:auto;padding-right:4px">';
      cols.forEach(function(label){
        form += '<div><label style="display:block;margin-bottom:3px;font-weight:600;font-size:12px">'+label+'</label>'
              + '<input type="text" placeholder="'+label+'..." style="width:100%;padding:6px 8px;border:1px solid #ddd;border-radius:5px;font-size:13px"></div>';
      });
      form += '</div><div style="margin-top:14px;display:flex;gap:8px;justify-content:flex-end">'
            + '<button onclick="closeModal()" style="background:#f1f5f9;color:#334155;border:none;padding:7px 16px;border-radius:6px;cursor:pointer">Çık</button>'
            + '<button onclick="saveNewRow(\''+tid+'\')" class="btn">Kaydet</button></div>';

      document.getElementById('modal-content').innerHTML = form;
      document.getElementById('modal-overlay').style.display = 'flex';
    }

    function saveNewRow(tid) {
      var inputs = document.querySelectorAll('#modal-content input[type=text]');
      var vals = Array.from(inputs).map(function(inp){return inp.value.trim();});
      if (vals.every(function(v){return v===''})) { toast('En az bir alan doldurun.','error'); return; }
      var tbl = document.getElementById(tid);
      if (!tbl) { closeModal(); return; }
      var tbody = tbl.querySelector('tbody');
      var tr = document.createElement('tr');
      vals.forEach(function(v){
        var td = document.createElement('td');
        td.textContent = v || '-';
        tr.appendChild(td);
      });
      var tdAct = document.createElement('td');
      tdAct.className = 'row-act';
      tdAct.innerHTML = '<button onclick="editRow(this)" style="background:#3b82f6;color:#fff;border:none;padding:3px 9px;border-radius:4px;cursor:pointer;font-size:11px;margin-right:4px">✏ Düzenle</button>'
                      + '<button onclick="deleteRow(this)" style="background:#ef4444;color:#fff;border:none;padding:3px 9px;border-radius:4px;cursor:pointer;font-size:11px">🗑 Sil</button>';
      tr.appendChild(tdAct);
      tbody.appendChild(tr);
      toast('Kayıt eklendi.');
      closeModal();
    }

    // Track current section
    var _origShowSection = showSection;
    showSection = function(id) { _currentSection = id; _origShowSection(id); };

"""

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert new_js right before the Classification form comment
target = '    // ── Classification form'
if target in html:
    html = html.replace(target, new_js + '\n' + target, 1)
    print('JS injected OK')
else:
    print('TARGET NOT FOUND')

# Also fix: addRowActions() call at end - insert before "// Show dashboard on load"
html = html.replace(
    '    // Show dashboard on load\n    showSection(\'dashboard\');',
    '    // Wire up action buttons on all existing rows\n    addRowActions();\n\n    // Show dashboard on load\n    showSection(\'dashboard\');'
)

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done')
