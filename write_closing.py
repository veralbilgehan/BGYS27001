
closing = """
    </main>

    <!-- Right Sidebar -->
    <aside class="rightbar">
      <div class="card" style="margin-bottom:16px">
        <div style="font-weight:700;margin-bottom:12px;color:#334155">Yaklasan Terminler</div>
        <div style="display:flex;flex-direction:column;gap:8px">
          <div style="padding:8px;background:#fef3c7;border-radius:6px;border-left:3px solid #f59e0b">
            <div style="font-size:12px;font-weight:600;color:#92400e">DFI-009 - Sifre sifirlama</div>
            <div style="font-size:11px;color:#78350f">Termin: 31.01.2024 <span style="color:#ef4444;font-weight:700">(Gecikti)</span></div>
          </div>
          <div style="padding:8px;background:#fef3c7;border-radius:6px;border-left:3px solid #f59e0b">
            <div style="font-size:12px;font-weight:600;color:#92400e">R-001 - MFA kurulumu</div>
            <div style="font-size:11px;color:#78350f">Termin: 31.03.2024</div>
          </div>
          <div style="padding:8px;background:#fef3c7;border-radius:6px;border-left:3px solid #f59e0b">
            <div style="font-size:12px;font-weight:600;color:#92400e">KVKK Egitimi</div>
            <div style="font-size:11px;color:#78350f">Termin: 31.03.2024</div>
          </div>
          <div style="padding:8px;background:#e0f2fe;border-radius:6px;border-left:3px solid #3b82f6">
            <div style="font-size:12px;font-weight:600;color:#1e40af">ISO 27001 Ic Tetkikci Egitimi</div>
            <div style="font-size:11px;color:#1d4ed8">Termin: Nisan 2024</div>
          </div>
          <div style="padding:8px;background:#e0f2fe;border-radius:6px;border-left:3px solid #3b82f6">
            <div style="font-size:12px;font-weight:600;color:#1e40af">Is Surekl. Test Plani</div>
            <div style="font-size:11px;color:#1d4ed8">Termin: 30.04.2024</div>
          </div>
        </div>
      </div>
      <div class="card" style="margin-bottom:16px">
        <div style="font-weight:700;margin-bottom:12px;color:#334155">Son Olaylar</div>
        <div style="display:flex;flex-direction:column;gap:8px">
          <div style="padding:8px;background:#f8fafc;border-radius:6px">
            <div style="font-size:12px;font-weight:600">VPN brute-force girişimi</div>
            <div style="font-size:11px;color:#64748b">03.01.2024 - Kapatildi (DFI-007)</div>
          </div>
          <div style="padding:8px;background:#f8fafc;border-radius:6px">
            <div style="font-size:12px;font-weight:600">Phishing simul. %15 tiklanma</div>
            <div style="font-size:11px;color:#64748b">08.02.2024 - Egitim verildi</div>
          </div>
          <div style="padding:8px;background:#f8fafc;border-radius:6px">
            <div style="font-size:12px;font-weight:600">Yedekleme testi basarili</div>
            <div style="font-size:11px;color:#64748b">15.01.2024 - Gozlem yok</div>
          </div>
        </div>
      </div>
      <div class="card">
        <div style="font-weight:700;margin-bottom:12px;color:#334155">Hizli Erisim</div>
        <div style="display:flex;flex-direction:column;gap:6px">
          <button onclick="showSection('soa')" style="background:#e0e7ff;color:#3730a3;border:none;padding:8px;border-radius:6px;cursor:pointer;font-size:13px;text-align:left">📋 SoA - BG.SOA.01</button>
          <button onclick="showSection('assets')" style="background:#e0e7ff;color:#3730a3;border:none;padding:8px;border-radius:6px;cursor:pointer;font-size:13px;text-align:left">📦 Varlik Envanteri</button>
          <button onclick="showSection('risks')" style="background:#fce7f3;color:#9d174d;border:none;padding:8px;border-radius:6px;cursor:pointer;font-size:13px;text-align:left">⚠️ Risk Kayit Formu</button>
          <button onclick="showSection('dfi')" style="background:#fef3c7;color:#92400e;border:none;padding:8px;border-radius:6px;cursor:pointer;font-size:13px;text-align:left">🔧 Acik DFI Listesi</button>
          <button onclick="showSection('readiness')" style="background:#e0f2fe;color:#1e40af;border:none;padding:8px;border-radius:6px;cursor:pointer;font-size:13px;text-align:left">✅ Hazirlik Checklist</button>
        </div>
      </div>
    </aside>
  </div>

  <!-- Modal -->
  <div id="modal-overlay" style="display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.5);z-index:1000;align-items:center;justify-content:center">
    <div style="background:white;border-radius:12px;padding:24px;min-width:400px;max-width:600px;position:relative">
      <button onclick="closeModal()" style="position:absolute;top:12px;right:12px;background:none;border:none;font-size:20px;cursor:pointer;color:#64748b">&times;</button>
      <div id="modal-content">
        <h3>Yeni Kayit</h3>
        <p style="color:#64748b;margin-top:8px">Form icerigi burada gorunecek.</p>
        <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
          <button onclick="closeModal()" style="background:#f1f5f9;color:#334155;border:none;padding:8px 16px;border-radius:6px;cursor:pointer">Iptal</button>
          <button class="btn">Kaydet</button>
        </div>
      </div>
    </div>
  </div>

  <script>
    function showSection(id) {
      document.querySelectorAll('section').forEach(s => s.style.display = 'none');
      const sec = document.getElementById(id);
      if (sec) { sec.style.display = 'block'; }
      document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
      const navItem = document.querySelector('.nav-item[data-section="' + id + '"]');
      if (navItem) { navItem.classList.add('active'); }
    }

    function filterTable(input, tableId) {
      const filter = input.value.toUpperCase();
      const table = document.getElementById(tableId);
      if (!table) return;
      const rows = table.getElementsByTagName('tr');
      for (let i = 1; i < rows.length; i++) {
        const text = rows[i].textContent.toUpperCase();
        rows[i].style.display = text.includes(filter) ? '' : 'none';
      }
    }

    function filterTableBySelect(select, tableId, colIndex) {
      const filter = select.value.toUpperCase();
      const table = document.getElementById(tableId);
      if (!table) return;
      const rows = table.getElementsByTagName('tr');
      for (let i = 1; i < rows.length; i++) {
        const cell = rows[i].getElementsByTagName('td')[colIndex];
        if (!filter) { rows[i].style.display = ''; continue; }
        rows[i].style.display = cell && cell.textContent.toUpperCase().includes(filter) ? '' : 'none';
      }
    }

    function filterDoc(folder) {
      const table = document.getElementById('doc-table');
      if (!table) return;
      const rows = table.getElementsByTagName('tr');
      for (let i = 1; i < rows.length; i++) {
        const cell = rows[i].getElementsByTagName('td')[2];
        rows[i].style.display = cell && cell.textContent.includes(folder) ? '' : 'none';
      }
    }

    function calcRisk() {
      const p = parseInt(document.getElementById('r-prob').value) || 3;
      const i = parseInt(document.getElementById('r-impact').value) || 3;
      const score = p * i;
      document.getElementById('r-score').textContent = score;
      let level, color;
      if (score <= 4) { level = 'Dusuk'; color = '#22c55e'; }
      else if (score <= 9) { level = 'Orta'; color = '#f59e0b'; }
      else if (score <= 16) { level = 'Yuksek'; color = '#ef4444'; }
      else { level = 'Kritik'; color = '#7c3aed'; }
      document.getElementById('r-level').textContent = level;
      document.getElementById('r-score').style.color = color;
    }

    function addRisk() {
      const threat = document.getElementById('r-threat') ? document.getElementById('r-threat').value : 'Yeni Tehdit';
      const p = document.getElementById('r-prob') ? document.getElementById('r-prob').value : 3;
      const i = document.getElementById('r-impact') ? document.getElementById('r-impact').value : 3;
      const score = p * i;
      const table = document.getElementById('risk-table');
      if (!table) return;
      const tbody = table.getElementsByTagName('tbody')[0];
      const rows = tbody.getElementsByTagName('tr').length;
      const newId = 'R-' + String(rows + 1).padStart(3, '0');
      const badgeClass = score > 16 ? 'b-danger' : score > 9 ? 'b-warning' : 'b-success';
      const tr = document.createElement('tr');
      tr.innerHTML = '<td>' + newId + '</td><td>-</td><td>' + (threat || 'Yeni Tehdit') + '</td><td>-</td><td>' + p + '</td><td>' + i + '</td><td><span class="badge ' + badgeClass + '">' + score + '</span></td><td>Yeni</td><td>-</td><td>-</td>';
      tbody.appendChild(tr);
      if (document.getElementById('r-threat')) document.getElementById('r-threat').value = '';
    }

    function openModal(type) {
      const overlay = document.getElementById('modal-overlay');
      if (overlay) {
        overlay.style.display = 'flex';
        const content = document.getElementById('modal-content');
        if (content) {
          content.innerHTML = '<h3>Yeni Kayit Ekle</h3><p style="color:#64748b;margin-top:4px;font-size:13px">(' + type + ')</p><div style="margin-top:12px;display:grid;gap:10px"><div><label style="display:block;margin-bottom:4px;font-weight:600">Ad / Baslik</label><input type="text" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px" placeholder="Giriniz..."></div><div><label style="display:block;margin-bottom:4px;font-weight:600">Aciklama</label><textarea style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px;height:80px" placeholder="Aciklama..."></textarea></div></div><div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end"><button onclick="closeModal()" style="background:#f1f5f9;color:#334155;border:none;padding:8px 16px;border-radius:6px;cursor:pointer">Iptal</button><button class="btn" onclick="closeModal()">Kaydet</button></div>';
        }
      }
    }

    function closeModal() {
      const overlay = document.getElementById('modal-overlay');
      if (overlay) overlay.style.display = 'none';
    }

    // Close modal on overlay click
    document.getElementById('modal-overlay').addEventListener('click', function(e) {
      if (e.target === this) closeModal();
    });

    // Initialize risk calculator
    calcRisk();

    // Show dashboard on load
    showSection('dashboard');
  </script>
</body>
</html>
"""

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'a', encoding='utf-8') as f:
    f.write(closing)
print('OK closing tags + JS')
