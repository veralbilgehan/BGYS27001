
risks = """
<section id="risks" style="display:none">
  <div class="section-header"><h2>Risk Degerlendirme</h2><button class="btn" onclick="addRisk()">+ Risk Ekle</button></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px">
    <div class="card">
      <h3 style="margin-bottom:12px">5x5 Risk Matrisi</h3>
      <div style="overflow-x:auto">
        <table style="width:100%;border-collapse:collapse;text-align:center;font-size:12px">
          <thead>
            <tr>
              <th style="background:#f1f5f9;padding:6px">Olasilik / Etki</th>
              <th style="background:#e8f5e9;padding:6px">1-Cok Dusuk</th>
              <th style="background:#fff9c4;padding:6px">2-Dusuk</th>
              <th style="background:#fff3e0;padding:6px">3-Orta</th>
              <th style="background:#fce4ec;padding:6px">4-Yuksek</th>
              <th style="background:#ef9a9a;padding:6px">5-Kritik</th>
            </tr>
          </thead>
          <tbody>
            <tr><td style="background:#f1f5f9;font-weight:600">5-Neredeyse Kesin</td><td style="background:#fff3e0">5</td><td style="background:#fce4ec">10</td><td style="background:#fce4ec">15</td><td style="background:#ef9a9a">20</td><td style="background:#ef9a9a">25</td></tr>
            <tr><td style="background:#f1f5f9;font-weight:600">4-Muhtemel</td><td style="background:#fff3e0">4</td><td style="background:#fff3e0">8</td><td style="background:#fce4ec">12</td><td style="background:#ef9a9a">16</td><td style="background:#ef9a9a">20</td></tr>
            <tr><td style="background:#f1f5f9;font-weight:600">3-Muhtemel Degil</td><td style="background:#fff9c4">3</td><td style="background:#fff3e0">6</td><td style="background:#fff3e0">9</td><td style="background:#fce4ec">12</td><td style="background:#fce4ec">15</td></tr>
            <tr><td style="background:#f1f5f9;font-weight:600">2-Nadiren</td><td style="background:#e8f5e9">2</td><td style="background:#fff9c4">4</td><td style="background:#fff3e0">6</td><td style="background:#fff3e0">8</td><td style="background:#fff3e0">10</td></tr>
            <tr><td style="background:#f1f5f9;font-weight:600">1-Cok Nadir</td><td style="background:#e8f5e9">1</td><td style="background:#e8f5e9">2</td><td style="background:#fff9c4">3</td><td style="background:#fff9c4">4</td><td style="background:#fff9c4">5</td></tr>
          </tbody>
        </table>
        <div style="display:flex;gap:10px;margin-top:8px;font-size:11px;flex-wrap:wrap">
          <span><span style="background:#e8f5e9;padding:2px 6px;border-radius:3px">1-4</span> Dusuk</span>
          <span><span style="background:#fff3e0;padding:2px 6px;border-radius:3px">5-9</span> Orta</span>
          <span><span style="background:#fce4ec;padding:2px 6px;border-radius:3px">10-16</span> Yuksek</span>
          <span><span style="background:#ef9a9a;padding:2px 6px;border-radius:3px">17-25</span> Kritik</span>
        </div>
      </div>
    </div>
    <div class="card">
      <h3 style="margin-bottom:12px">Hizli Risk Hesapla</h3>
      <div style="display:grid;gap:10px">
        <div>
          <label style="display:block;margin-bottom:4px;font-weight:600">Tehdid</label>
          <input type="text" id="r-threat" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px" placeholder="Tehdit tanimla...">
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
          <div>
            <label style="display:block;margin-bottom:4px;font-weight:600">Olasilik (1-5)</label>
            <input type="number" id="r-prob" min="1" max="5" value="3" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px" onchange="calcRisk()">
          </div>
          <div>
            <label style="display:block;margin-bottom:4px;font-weight:600">Etki (1-5)</label>
            <input type="number" id="r-impact" min="1" max="5" value="3" style="width:100%;padding:8px;border:1px solid #ddd;border-radius:6px" onchange="calcRisk()">
          </div>
        </div>
        <div style="background:#f8fafc;border-radius:8px;padding:12px;text-align:center">
          <div style="font-size:13px;color:#64748b">Risk Skoru</div>
          <div id="r-score" style="font-size:36px;font-weight:700;color:#e74c3c">9</div>
          <div id="r-level" style="font-size:13px;font-weight:600;color:#e67e22">Orta</div>
        </div>
        <button class="btn" onclick="addRisk()">Risk Kaydina Ekle</button>
      </div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:12px">Risk Kayit Formu</h3>
    <div style="overflow-x:auto">
      <table id="risk-table">
        <thead><tr><th>ID</th><th>Varlik</th><th>Tehdid</th><th>Zafiyet</th><th>Olasilik</th><th>Etki</th><th>Skor</th><th>Durum</th><th>Kontrol</th><th>Kalan Risk</th></tr></thead>
        <tbody>
          <tr><td>R-001</td><td>Active Directory</td><td>Kimlik bilgisi ele gecirilmesi</td><td>Zayif parola politikasi</td><td>4</td><td>5</td><td><span class="badge b-danger">20</span></td><td>Isleniyor</td><td>A.9.4.3</td><td>8</td></tr>
          <tr><td>R-002</td><td>OBS Sistemi</td><td>SQL Injection saldirisi</td><td>Girdi dogrulama eksikligi</td><td>3</td><td>5</td><td><span class="badge b-danger">15</span></td><td>Isleniyor</td><td>A.14.2.8</td><td>6</td></tr>
          <tr><td>R-003</td><td>Sunucu Odasi</td><td>Fiziksel izinsiz erisim</td><td>Kart okuyucu ariza riski</td><td>2</td><td>5</td><td><span class="badge b-warning">10</span></td><td>Kontrol Altinda</td><td>A.11.1.2</td><td>4</td></tr>
          <tr><td>R-004</td><td>E-posta</td><td>Kimlik avı (phishing)</td><td>Kullanici farkindaligi dusuk</td><td>4</td><td>4</td><td><span class="badge b-danger">16</span></td><td>Isleniyor</td><td>A.7.2.2</td><td>8</td></tr>
          <tr><td>R-005</td><td>Yedekleme</td><td>Yedek kaybı/bozulmasi</td><td>Test edilmemis yedekler</td><td>2</td><td>5</td><td><span class="badge b-warning">10</span></td><td>Kontrol Altinda</td><td>A.12.3.1</td><td>3</td></tr>
          <tr><td>R-006</td><td>Ag Altyapisi</td><td>Yetkisiz ag erisimi</td><td>VLAN segmentasyonu eksik</td><td>3</td><td>4</td><td><span class="badge b-warning">12</span></td><td>Isleniyor</td><td>A.13.1.3</td><td>6</td></tr>
          <tr><td>R-007</td><td>Kisisel Veriler</td><td>Veri sikismasi/ifsa</td><td>KVKK uyumsuzlugu</td><td>2</td><td>5</td><td><span class="badge b-warning">10</span></td><td>Kontrol Altinda</td><td>A.18.1.4</td><td>4</td></tr>
          <tr><td>R-008</td><td>Web Sunucu</td><td>DDoS saldirisi</td><td>Kapasite siniri</td><td>3</td><td>4</td><td><span class="badge b-warning">12</span></td><td>Planlanmis</td><td>A.12.1.3</td><td>6</td></tr>
          <tr><td>R-009</td><td>Tedarikci</td><td>Tedarikci guvensizligi</td><td>Sozlesme eksiklikleri</td><td>2</td><td>4</td><td><span class="badge b-warning">8</span></td><td>Kontrol Altinda</td><td>A.15.1.2</td><td>4</td></tr>
          <tr><td>R-010</td><td>Personel</td><td>Kotu niyetli ic tehdit</td><td>Gorevler ayrimi eksik</td><td>2</td><td>4</td><td><span class="badge b-warning">8</span></td><td>Kontrol Altinda</td><td>A.6.1.2</td><td>3</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section id="treatment" style="display:none">
  <div class="section-header"><h2>Risk Isleme Plani</h2></div>
  <div class="card">
    <table id="treatment-table">
      <thead><tr><th>Risk ID</th><th>Tehdid</th><th>Isleme Yontemi</th><th>Planlanan Kontrol</th><th>Sorumlu</th><th>Termin</th><th>Durum</th></tr></thead>
      <tbody>
        <tr><td>R-001</td><td>Kimlik bilgisi ele gecirilmesi</td><td>Azaltma</td><td>Cok faktörlu kimlik dogrulama (MFA)</td><td>Ag Birimi</td><td>31.03.2024</td><td><span class="badge b-warning">Devam Ediyor</span></td></tr>
        <tr><td>R-002</td><td>SQL Injection saldirisi</td><td>Azaltma</td><td>Kodun guvenlik testi + WAF kurulumu</td><td>Yazilim Birimi</td><td>28.02.2024</td><td><span class="badge b-warning">Devam Ediyor</span></td></tr>
        <tr><td>R-003</td><td>Fiziksel izinsiz erisim</td><td>Azaltma</td><td>Yedek kart okuyucu + biometric sistem</td><td>Teknik Servis</td><td>30.04.2024</td><td><span class="badge b-info">Planlanmis</span></td></tr>
        <tr><td>R-004</td><td>Phishing saldirisi</td><td>Azaltma</td><td>Simule phishing egitimi + SPF/DKIM/DMARC</td><td>Sistem Birimi</td><td>28.02.2024</td><td><span class="badge b-warning">Devam Ediyor</span></td></tr>
        <tr><td>R-005</td><td>Yedek kaybi</td><td>Azaltma</td><td>Haftalik yedek restore testi proseduru</td><td>Sistem Birimi</td><td>31.01.2024</td><td><span class="badge b-success">Tamamlandi</span></td></tr>
        <tr><td>R-006</td><td>Yetkisiz ag erisimi</td><td>Azaltma</td><td>VLAN segmentasyonu tamamlanmasi</td><td>Ag Birimi</td><td>30.04.2024</td><td><span class="badge b-warning">Devam Ediyor</span></td></tr>
        <tr><td>R-007</td><td>Kisisel veri ifsa</td><td>Azaltma</td><td>KVKK uyum takvimi, VERBİS kaydi</td><td>Idari Isler</td><td>31.03.2024</td><td><span class="badge b-success">Tamamlandi</span></td></tr>
        <tr><td>R-008</td><td>DDoS saldirisi</td><td>Azaltma</td><td>CDN/Anti-DDoS hizmeti alimi</td><td>Ag Birimi</td><td>30.06.2024</td><td><span class="badge b-info">Planlanmis</span></td></tr>
        <tr><td>R-009</td><td>Tedarikci guvensizligi</td><td>Azaltma</td><td>Tedarikci guvenlik denetim checklist</td><td>Idari Isler</td><td>28.02.2024</td><td><span class="badge b-success">Tamamlandi</span></td></tr>
        <tr><td>R-010</td><td>Ic tehdit</td><td>Azaltma</td><td>Erisim loglama + duzensiz yetki denetimi</td><td>Sistem Birimi</td><td>31.03.2024</td><td><span class="badge b-warning">Devam Ediyor</span></td></tr>
      </tbody>
    </table>
  </div>
</section>
"""

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'a', encoding='utf-8') as f:
    f.write(risks)
print('OK risks+treatment')
