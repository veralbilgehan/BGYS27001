
dfi_mgmt = """
<section id="dfi" style="display:none">
  <div class="section-header"><h2>Duzeltici Faaliyet (DFI)</h2><button class="btn" onclick="openModal('newDFI')">+ DFI Ac</button></div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px">
    <div class="stat-card"><div class="stat-value" style="color:#3b82f6">8</div><div class="stat-label">Toplam Acik DFI</div></div>
    <div class="stat-card"><div class="stat-value" style="color:#22c55e">12</div><div class="stat-label">Tamamlanan</div></div>
    <div class="stat-card"><div class="stat-value" style="color:#f59e0b">3</div><div class="stat-label">Gecikti</div></div>
    <div class="stat-card"><div class="stat-value" style="color:#8b5cf6">2</div><div class="stat-label">Dogrulama Bekliyor</div></div>
  </div>
  <div class="card">
    <div style="display:flex;gap:12px;margin-bottom:12px">
      <select onchange="filterTableBySelect(this,'dfi-table',4)" style="padding:6px 10px;border:1px solid #ddd;border-radius:6px">
        <option value="">Tum Durumlar</option>
        <option>Acik</option>
        <option>Devam Ediyor</option>
        <option>Dogrulama</option>
        <option>Kapandi</option>
        <option>Gecikti</option>
      </select>
      <input type="text" class="search-box" style="flex:1" placeholder="DFI ara..." onkeyup="filterTable(this,'dfi-table')">
    </div>
    <table id="dfi-table">
      <thead><tr><th>DFI No</th><th>Kaynak</th><th>Aciklama</th><th>Kok Neden</th><th>Durum</th><th>Sorumlu</th><th>Termin</th><th>Kapanis</th></tr></thead>
      <tbody>
        <tr><td>DFI-001</td><td>Ic Tetkik 2023</td><td>Erisim hakki gozden gecirme kaydi eksik</td><td>Prosedur bilinmiyor</td><td><span class="badge b-success">Kapandi</span></td><td>BG.PRD.03 sahibi</td><td>30.10.2023</td><td>28.10.2023</td></tr>
        <tr><td>DFI-002</td><td>Ic Tetkik 2023</td><td>Yama yonetimi uygulanmamis</td><td>Kaynak yetersizligi</td><td><span class="badge b-success">Kapandi</span></td><td>Sistem Birimi</td><td>30.11.2023</td><td>25.11.2023</td></tr>
        <tr><td>DFI-003</td><td>Ic Tetkik 2023</td><td>Egitim katilim kaydi eksik</td><td>Kayit sistemi yok</td><td><span class="badge b-success">Kapandi</span></td><td>Zerrin MERAL</td><td>15.10.2023</td><td>12.10.2023</td></tr>
        <tr><td>DFI-004</td><td>Ic Tetkik 2023</td><td>Ziyaretci kayit defteri bosluk</td><td>Personel farkindaligi dusuk</td><td><span class="badge b-success">Kapandi</span></td><td>Teknik Servis</td><td>31.10.2023</td><td>27.10.2023</td></tr>
        <tr><td>DFI-005</td><td>Ic Tetkik 2023</td><td>Is surekliligi testi yapilmamis</td><td>Test plani yok</td><td><span class="badge b-warning">Devam Ediyor</span></td><td>Sistem Birimi</td><td>30.04.2024</td><td>-</td></tr>
        <tr><td>DFI-006</td><td>Dis Tetkik 2023</td><td>Guvenli gelistirme prensipleri dokumante edilmemis</td><td>Kapsam disinda tutulmus</td><td><span class="badge b-warning">Devam Ediyor</span></td><td>Yazilim Birimi</td><td>28.02.2024</td><td>-</td></tr>
        <tr><td>DFI-007</td><td>Olay Bildirimi</td><td>VPN erisiminde yetkisiz deneme tespit edildi</td><td>Brute force saldirisi</td><td><span class="badge b-success">Kapandi</span></td><td>Ag Birimi</td><td>05.01.2024</td><td>03.01.2024</td></tr>
        <tr><td>DFI-008</td><td>YGG 2023</td><td>Kapasite izleme otomasyonu eksik</td><td>Araç butcesi yok</td><td><span class="badge b-info">Acik</span></td><td>Sistem Birimi</td><td>30.06.2024</td><td>-</td></tr>
        <tr><td>DFI-009</td><td>Kullanici sikayet</td><td>Sifre sifirlama sureci cok uzun</td><td>Manuel prosedur</td><td><span class="badge b-danger">Gecikti</span></td><td>Sistem Birimi</td><td>31.01.2024</td><td>-</td></tr>
        <tr><td>DFI-010</td><td>Performans izleme</td><td>Log saklama suresi uyumsuz (6 ay yerine 1 yil)</td><td>Mevzuat gozden kacmis</td><td><span class="badge b-warning">Dogrulama</span></td><td>Sistem Birimi</td><td>15.03.2024</td><td>-</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section id="management" style="display:none">
  <div class="section-header"><h2>Yonetim Gozden Gecirme (YGG)</h2></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px">
    <div class="card">
      <h3 style="margin-bottom:12px">Son YGG - Aralik 2023</h3>
      <table>
        <tbody>
          <tr><td style="color:#64748b;font-size:13px">Tarih</td><td style="font-weight:600">18 Aralik 2023</td></tr>
          <tr><td style="color:#64748b;font-size:13px">Baskan</td><td style="font-weight:600">Evren KOKSAL (Daire Baskani)</td></tr>
          <tr><td style="color:#64748b;font-size:13px">BG Temsilcisi</td><td style="font-weight:600">Zerrin MERAL</td></tr>
          <tr><td style="color:#64748b;font-size:13px">Katilimci</td><td style="font-weight:600">12 kisi (tum birim amirleri)</td></tr>
          <tr><td style="color:#64748b;font-size:13px">Sure</td><td style="font-weight:600">3 saat</td></tr>
          <tr><td style="color:#64748b;font-size:13px">Belge</td><td><span class="badge b-success">Tutanak imzalandi</span></td></tr>
        </tbody>
      </table>
    </div>
    <div class="card">
      <h3 style="margin-bottom:12px">YGG Gundem Maddeleri</h3>
      <div style="display:flex;flex-direction:column;gap:8px">
        <div style="display:flex;align-items:center;gap:8px;font-size:13px"><span style="color:#22c55e">✓</span> Onceki YGG kararlarinin takibi</div>
        <div style="display:flex;align-items:center;gap:8px;font-size:13px"><span style="color:#22c55e">✓</span> BG olaylari ve olaylara yanit sonuclari</div>
        <div style="display:flex;align-items:center;gap:8px;font-size:13px"><span style="color:#22c55e">✓</span> Ic ve dis denetim sonuclari</div>
        <div style="display:flex;align-items:center;gap:8px;font-size:13px"><span style="color:#22c55e">✓</span> Ilgili taraflardan geri bildirim</div>
        <div style="display:flex;align-items:center;gap:8px;font-size:13px"><span style="color:#22c55e">✓</span> Risk degerlendirme ve risk isleme durumu</div>
        <div style="display:flex;align-items:center;gap:8px;font-size:13px"><span style="color:#22c55e">✓</span> Performans gostergeler (KPI/KRI)</div>
        <div style="display:flex;align-items:center;gap:8px;font-size:13px"><span style="color:#22c55e">✓</span> Iyilestirme firsatlari ve BGYS kapsam degisiklikleri</div>
        <div style="display:flex;align-items:center;gap:8px;font-size:13px"><span style="color:#22c55e">✓</span> Kaynak gereksinimleri (insan, finansal, teknoloji)</div>
      </div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:12px">YGG Kararlari - Aralik 2023</h3>
    <table id="ygg-table">
      <thead><tr><th>Karar No</th><th>Karar</th><th>Sorumlu</th><th>Termin</th><th>Durum</th></tr></thead>
      <tbody>
        <tr><td>YGG-2023-01</td><td>MFA sistemi kurulumu butce onaylandi</td><td>Ag Birimi + Daire Baskani</td><td>31.03.2024</td><td><span class="badge b-warning">Devam Ediyor</span></td></tr>
        <tr><td>YGG-2023-02</td><td>KVKK uyum sureci hizlandirilmasi</td><td>Idari Isler + Hukuk</td><td>31.03.2024</td><td><span class="badge b-success">Tamamlandi</span></td></tr>
        <tr><td>YGG-2023-03</td><td>Yillik phishing simul. bascetme egitimi</td><td>Zerrin MERAL</td><td>28.02.2024</td><td><span class="badge b-success">Tamamlandi</span></td></tr>
        <tr><td>YGG-2023-04</td><td>Is surekliligi test plani hazirlanmasi</td><td>Sistem Birimi</td><td>30.04.2024</td><td><span class="badge b-warning">Devam Ediyor</span></td></tr>
        <tr><td>YGG-2023-05</td><td>Tedarikci guvenlik degerlendirme formu olusturulmasi</td><td>Idari Isler</td><td>28.02.2024</td><td><span class="badge b-success">Tamamlandi</span></td></tr>
        <tr><td>YGG-2023-06</td><td>BGYS kapsam guncellemesi (bulut hizmetleri dahil)</td><td>Zerrin MERAL</td><td>30.06.2024</td><td><span class="badge b-info">Planlanmis</span></td></tr>
      </tbody>
    </table>
  </div>
</section>
"""

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'a', encoding='utf-8') as f:
    f.write(dfi_mgmt)
print('OK dfi+management')
