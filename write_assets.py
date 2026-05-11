
assets = """
<section id="assets" style="display:none">
  <div class="section-header"><h2>Varlik Envanteri</h2><button class="btn" onclick="openModal('newAsset')">+ Varlik Ekle</button></div>
  <div class="card">
    <div style="display:flex;gap:12px;margin-bottom:12px;flex-wrap:wrap">
      <select onchange="filterTableBySelect(this,'asset-table',2)" style="padding:6px 10px;border:1px solid #ddd;border-radius:6px">
        <option value="">Tum Tipler</option>
        <option>Donanim</option>
        <option>Yazilim</option>
        <option>Veri</option>
        <option>Servis</option>
        <option>Personel</option>
        <option>Fiziksel</option>
      </select>
      <input type="text" class="search-box" style="flex:1" placeholder="Varlik ara..." onkeyup="filterTable(this,'asset-table')">
    </div>
    <table id="asset-table">
      <thead><tr><th>ID</th><th>Varlik Adi</th><th>Tip</th><th>Sahip</th><th>G</th><th>B</th><th>E</th><th>Risk</th><th>Konum</th></tr></thead>
      <tbody>
        <tr><td>V-001</td><td>Active Directory Sunucu</td><td>Donanim</td><td>Ag Birimi</td><td>5</td><td>5</td><td>5</td><td><span class="badge b-danger">Yuksek</span></td><td>Sunucu Odasi</td></tr>
        <tr><td>V-002</td><td>Web Sunucu (Apache)</td><td>Yazilim</td><td>Yazilim Birimi</td><td>4</td><td>4</td><td>5</td><td><span class="badge b-danger">Yuksek</span></td><td>DMZ</td></tr>
        <tr><td>V-003</td><td>Ogrenci Bilgi Sistemi (OBS)</td><td>Yazilim</td><td>Yazilim Birimi</td><td>5</td><td>5</td><td>4</td><td><span class="badge b-danger">Yuksek</span></td><td>Sunucu Odasi</td></tr>
        <tr><td>V-004</td><td>E-posta Sunucu</td><td>Servis</td><td>Sistem Birimi</td><td>4</td><td>4</td><td>5</td><td><span class="badge b-danger">Yuksek</span></td><td>Sunucu Odasi</td></tr>
        <tr><td>V-005</td><td>Yedekleme Sistemi (Veeam)</td><td>Yazilim</td><td>Sistem Birimi</td><td>5</td><td>5</td><td>3</td><td><span class="badge b-warning">Orta</span></td><td>Sunucu Odasi</td></tr>
        <tr><td>V-006</td><td>Guvenlik Duvari (Fortinet)</td><td>Donanim</td><td>Ag Birimi</td><td>4</td><td>5</td><td>5</td><td><span class="badge b-danger">Yuksek</span></td><td>Ag Odasi</td></tr>
        <tr><td>V-007</td><td>Log Yonetim Sistemi (SIEM)</td><td>Yazilim</td><td>Sistem Birimi</td><td>4</td><td>4</td><td>4</td><td><span class="badge b-warning">Orta</span></td><td>Sunucu Odasi</td></tr>
        <tr><td>V-008</td><td>Personel Ozluk Dosyalari</td><td>Veri</td><td>IK Birimi</td><td>5</td><td>4</td><td>3</td><td><span class="badge b-warning">Orta</span></td><td>Arsiv</td></tr>
        <tr><td>V-009</td><td>Ogrenci Kisisel Verileri (KVKK)</td><td>Veri</td><td>Yazilim Birimi</td><td>5</td><td>5</td><td>3</td><td><span class="badge b-danger">Yuksek</span></td><td>VT Sunucu</td></tr>
        <tr><td>V-010</td><td>Network Switch Altyapisi</td><td>Donanim</td><td>Ag Birimi</td><td>3</td><td>4</td><td>5</td><td><span class="badge b-warning">Orta</span></td><td>Dagitim Odalari</td></tr>
        <tr><td>V-011</td><td>UPS Sistemleri</td><td>Donanim</td><td>Teknik Servis</td><td>2</td><td>3</td><td>5</td><td><span class="badge b-warning">Orta</span></td><td>Sunucu Odasi</td></tr>
        <tr><td>V-012</td><td>Antiviurs Yonetim Konsolu</td><td>Yazilim</td><td>Sistem Birimi</td><td>3</td><td>4</td><td>4</td><td><span class="badge b-warning">Orta</span></td><td>Sunucu Odasi</td></tr>
        <tr><td>V-013</td><td>SharePoint Dokuman Yonetim</td><td>Servis</td><td>Idari Isler</td><td>4</td><td>4</td><td>4</td><td><span class="badge b-warning">Orta</span></td><td>Bulut (M365)</td></tr>
        <tr><td>V-014</td><td>Kamera Guvenligi Sistemi</td><td>Donanim</td><td>Teknik Servis</td><td>3</td><td>3</td><td>4</td><td><span class="badge b-warning">Orta</span></td><td>Kampus</td></tr>
        <tr><td>V-015</td><td>BG Temsilcisi (Zerrin MERAL)</td><td>Personel</td><td>BDB Baskanligi</td><td>4</td><td>4</td><td>4</td><td><span class="badge b-warning">Orta</span></td><td>BDB Bina</td></tr>
        <tr><td>V-016</td><td>Sunucu Odasi</td><td>Fiziksel</td><td>Teknik Servis</td><td>4</td><td>5</td><td>5</td><td><span class="badge b-danger">Yuksek</span></td><td>BDB Bina B Blok</td></tr>
        <tr><td>V-017</td><td>VPN Sunucu</td><td>Servis</td><td>Ag Birimi</td><td>4</td><td>4</td><td>5</td><td><span class="badge b-danger">Yuksek</span></td><td>Sunucu Odasi</td></tr>
        <tr><td>V-018</td><td>Veritabani Sunucu (MS SQL)</td><td>Donanim</td><td>Yazilim Birimi</td><td>5</td><td>5</td><td>4</td><td><span class="badge b-danger">Yuksek</span></td><td>Sunucu Odasi</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section id="classification" style="display:none">
  <div class="section-header"><h2>Bilgi Siniflandirma</h2></div>
  <div class="card">
    <h3 style="margin-bottom:16px">Siniflandirma Seviyeleri (BG.PLT.03)</h3>
    <table>
      <thead><tr><th>Seviye</th><th>Tanim</th><th>Ornekler</th><th>Koruma Gereksinimleri</th></tr></thead>
      <tbody>
        <tr><td><span class="badge b-danger">Gizli</span></td><td>Yetkisiz ifsa halinde kurum icin ciddi zarar</td><td>KVKK kapsamindaki kisisel veriler, sistem parolalari, guvenlik aciklari</td><td>Sifreleme zorunlu, erisim loglanir, cikti alim kisitli</td></tr>
        <tr><td><span class="badge b-warning">Hizmete Ozel</span></td><td>Sadece ilgili birim personeli erisebilir</td><td>Personel ozluk bilgileri, butce verileri, ic yazismalar</td><td>Erisim kontrolu, transfer protokolu</td></tr>
        <tr><td><span class="badge b-info">Kuruma Ozel</span></td><td>Tum BDB personeli erisebilir</td><td>Ic prosedurler, is surec dokumanlari, toplanti notlari</td><td>Kimlik dogrulama gerekli</td></tr>
        <tr><td><span class="badge b-success">Genel</span></td><td>Kamuya acik bilgi</td><td>Web sitesi icerigi, duyurular, genel iletisimler</td><td>Standart yayinlama kurallari</td></tr>
      </tbody>
    </table>
    <h3 style="margin:24px 0 16px">Siniflandirma Formu</h3>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
      <div>
        <label style="display:block;margin-bottom:6px;font-weight:600">Dokuman/Varlik Adi</label>
        <input type="text" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px" placeholder="Adi girin...">
      </div>
      <div>
        <label style="display:block;margin-bottom:6px;font-weight:600">Siniflandirma Seviyesi</label>
        <select style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px">
          <option>Gizli</option><option>Hizmete Ozel</option><option>Kuruma Ozel</option><option>Genel</option>
        </select>
      </div>
      <div>
        <label style="display:block;margin-bottom:6px;font-weight:600">Gizlilik Degeri (1-5)</label>
        <input type="number" min="1" max="5" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px" value="3">
      </div>
      <div>
        <label style="display:block;margin-bottom:6px;font-weight:600">Butunluk Degeri (1-5)</label>
        <input type="number" min="1" max="5" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px" value="3">
      </div>
      <div>
        <label style="display:block;margin-bottom:6px;font-weight:600">Erisebilirlik Degeri (1-5)</label>
        <input type="number" min="1" max="5" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px" value="3">
      </div>
      <div>
        <label style="display:block;margin-bottom:6px;font-weight:600">Varlik Sahibi</label>
        <input type="text" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px" placeholder="Birim/kisi...">
      </div>
    </div>
    <button class="btn" style="margin-top:16px">Kaydet</button>
  </div>
</section>
"""

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'a', encoding='utf-8') as f:
    f.write(assets)
print('OK assets+classification')
