
trainings = """
<section id="trainings" style="display:none">
  <div class="section-header"><h2>Egitim ve Farkindalik</h2><button class="btn" onclick="openModal('newTraining')">+ Egitim Ekle</button></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px">
    <div class="card">
      <h3 style="margin-bottom:12px">2024 Egitim Takvimi (GN.PLN.01)</h3>
      <table>
        <thead><tr><th>Egitim</th><th>Hedef Kitle</th><th>Ay</th><th>Durum</th></tr></thead>
        <tbody>
          <tr><td>BG Farkindalik Egitimi</td><td>Tum personel</td><td>Ocak</td><td><span class="badge b-success">Tamamlandi</span></td></tr>
          <tr><td>Oltalama (Phishing) Simulasyonu</td><td>Tum personel</td><td>Subat</td><td><span class="badge b-success">Tamamlandi</span></td></tr>
          <tr><td>KVKK Egitimi</td><td>Veri isleme personeli</td><td>Mart</td><td><span class="badge b-warning">Devam Ediyor</span></td></tr>
          <tr><td>ISO 27001 Ic Tetkikci Egitimi</td><td>Tetkikci adaylari</td><td>Nisan</td><td><span class="badge b-info">Planlanmis</span></td></tr>
          <tr><td>Fiziksel Guvenlik Tatbikati</td><td>Tum personel</td><td>Mayis</td><td><span class="badge b-info">Planlanmis</span></td></tr>
          <tr><td>Olay Mudahale Tatbikati</td><td>BT personeli</td><td>Haziran</td><td><span class="badge b-info">Planlanmis</span></td></tr>
          <tr><td>Yeni Personel Oryantasyon BG</td><td>Yeni personel</td><td>Surekli</td><td><span class="badge b-success">Aktif</span></td></tr>
        </tbody>
      </table>
    </div>
    <div class="card">
      <h3 style="margin-bottom:12px">Egitim Katilim Ozeti</h3>
      <div style="display:grid;gap:12px">
        <div style="background:#f8fafc;border-radius:8px;padding:12px;display:flex;justify-content:space-between;align-items:center">
          <div><div style="font-weight:600">BG Farkindalik (Ocak 2024)</div><div style="font-size:12px;color:#64748b">Yuz yuze + online</div></div>
          <div style="text-align:right"><div style="font-size:20px;font-weight:700;color:#22c55e">142/156</div><div style="font-size:11px;color:#64748b">%91 katilim</div></div>
        </div>
        <div style="background:#f8fafc;border-radius:8px;padding:12px;display:flex;justify-content:space-between;align-items:center">
          <div><div style="font-weight:600">Phishing Simul. (Sub. 2024)</div><div style="font-size:12px;color:#64748b">E-posta simulasyonu</div></div>
          <div style="text-align:right"><div style="font-size:20px;font-weight:700;color:#f59e0b">23/156</div><div style="font-size:11px;color:#64748b">%15 tiklanma (hedef: &lt;%10)</div></div>
        </div>
        <div style="background:#f8fafc;border-radius:8px;padding:12px;display:flex;justify-content:space-between;align-items:center">
          <div><div style="font-weight:600">KVKK Egitimi (Mar. 2024)</div><div style="font-size:12px;color:#64748b">Online platform</div></div>
          <div style="text-align:right"><div style="font-size:20px;font-weight:700;color:#3b82f6">67/89</div><div style="font-size:11px;color:#64748b">%75 katilim (devam)</div></div>
        </div>
      </div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:12px">Egitim Kayitlari</h3>
    <table id="training-table">
      <thead><tr><th>Egitim Adi</th><th>Egitici</th><th>Tarih</th><th>Sure</th><th>Katilimci Sayisi</th><th>Belge</th></tr></thead>
      <tbody>
        <tr><td>BG Farkindalik Egitimi 2024</td><td>Zerrin MERAL</td><td>15.01.2024</td><td>4 saat</td><td>142</td><td><span class="badge b-success">Var</span></td></tr>
        <tr><td>BG Farkindalik Egitimi 2023</td><td>Zerrin MERAL</td><td>12.01.2023</td><td>4 saat</td><td>138</td><td><span class="badge b-success">Var</span></td></tr>
        <tr><td>ISO 27001 Temel Egitim 2023</td><td>Dis Egitici</td><td>20.03.2023</td><td>16 saat</td><td>8</td><td><span class="badge b-success">Var</span></td></tr>
        <tr><td>Ic Tetkikci Egitimi 2023</td><td>Dis Egitici</td><td>05.09.2023</td><td>24 saat</td><td>4</td><td><span class="badge b-success">Var</span></td></tr>
        <tr><td>Phishing Simul. 2024</td><td>Sistem Birimi</td><td>08.02.2024</td><td>-</td><td>156</td><td><span class="badge b-success">Var</span></td></tr>
        <tr><td>Oryantasyon BG Modulu 2024-Q1</td><td>Zerrin MERAL</td><td>Surekli</td><td>2 saat</td><td>14</td><td><span class="badge b-success">Var</span></td></tr>
      </tbody>
    </table>
  </div>
</section>

<section id="audits" style="display:none">
  <div class="section-header"><h2>Ic Denetim</h2><button class="btn" onclick="openModal('newAudit')">+ Denetim Planla</button></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px">
    <div class="card">
      <h3 style="margin-bottom:12px">2023 Ic Denetim Sonuclari</h3>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;text-align:center">
        <div style="background:#e8f5e9;border-radius:8px;padding:12px"><div style="font-size:24px;font-weight:700;color:#22c55e">0</div><div style="font-size:12px">Major UU</div></div>
        <div style="background:#fff3e0;border-radius:8px;padding:12px"><div style="font-size:24px;font-weight:700;color:#f59e0b">5</div><div style="font-size:12px">Minor UU</div></div>
        <div style="background:#e0f2fe;border-radius:8px;padding:12px"><div style="font-size:24px;font-weight:700;color:#3b82f6">12</div><div style="font-size:12px">Gozlem</div></div>
      </div>
      <div style="margin-top:12px;font-size:13px;color:#64748b">Denetim Tarihi: 18-20 Eylul 2023 | Tetkikci: Ic ekip (4 kisi)</div>
    </div>
    <div class="card">
      <h3 style="margin-bottom:12px">Dis Denetim (Belgelendirme)</h3>
      <div style="display:grid;gap:10px">
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px;background:#f8fafc;border-radius:6px">
          <span style="font-size:13px">Belgelendirme Kurumu</span>
          <span style="font-weight:600">TSE</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px;background:#f8fafc;border-radius:6px">
          <span style="font-size:13px">Asamasi</span>
          <span class="badge b-success">2. Asama Denetimi Tamamlandi</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px;background:#f8fafc;border-radius:6px">
          <span style="font-size:13px">Tarih</span>
          <span style="font-weight:600">27-28 Kasim 2023</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px;background:#f8fafc;border-radius:6px">
          <span style="font-size:13px">Sonuc</span>
          <span class="badge b-success">Sertifika Verildi</span>
        </div>
      </div>
    </div>
  </div>
  <div class="card">
    <h3 style="margin-bottom:12px">Denetim Bulgulari</h3>
    <table id="audit-table">
      <thead><tr><th>Bulgu No</th><th>Tip</th><th>ISO Maddesi</th><th>Aciklama</th><th>Denetci</th><th>DFI No</th><th>Durum</th></tr></thead>
      <tbody>
        <tr><td>2023-001</td><td><span class="badge b-warning">Minor UU</span></td><td>A.9.2.5</td><td>Erisim hakki gozden gecirme kayitlari eksik</td><td>Ic tetkik</td><td>DFI-001</td><td><span class="badge b-success">Kapandi</span></td></tr>
        <tr><td>2023-002</td><td><span class="badge b-warning">Minor UU</span></td><td>A.12.6.1</td><td>Yama yonetimi proseduru uygulanmamis</td><td>Ic tetkik</td><td>DFI-002</td><td><span class="badge b-success">Kapandi</span></td></tr>
        <tr><td>2023-003</td><td><span class="badge b-warning">Minor UU</span></td><td>A.7.2.2</td><td>2023 egitim katilim kaydi eksik</td><td>Ic tetkik</td><td>DFI-003</td><td><span class="badge b-success">Kapandi</span></td></tr>
        <tr><td>2023-004</td><td><span class="badge b-warning">Minor UU</span></td><td>A.11.1.2</td><td>Ziyaretci kayit defteri bosluk var</td><td>Ic tetkik</td><td>DFI-004</td><td><span class="badge b-success">Kapandi</span></td></tr>
        <tr><td>2023-005</td><td><span class="badge b-warning">Minor UU</span></td><td>A.17.1.3</td><td>Is surekliligi plani test edilmemis</td><td>Ic tetkik</td><td>DFI-005</td><td><span class="badge b-warning">Devam</span></td></tr>
        <tr><td>2023-T01</td><td><span class="badge b-info">Gozlem</span></td><td>Md.8.3</td><td>Risk skorlarinin yeniden kalibre edilmesi onerildi</td><td>Dis tetkik</td><td>-</td><td><span class="badge b-warning">Degerlendiriliyor</span></td></tr>
        <tr><td>2023-T02</td><td><span class="badge b-info">Gozlem</span></td><td>A.14.2.5</td><td>Guvenli gelistirme prensiplerinin dokumante edilmesi</td><td>Dis tetkik</td><td>DFI-006</td><td><span class="badge b-warning">Devam</span></td></tr>
      </tbody>
    </table>
  </div>
</section>
"""

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'a', encoding='utf-8') as f:
    f.write(trainings)
print('OK trainings+audits')
