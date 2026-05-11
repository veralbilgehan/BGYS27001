
soa = """
<section id="soa" style="display:none">
  <div class="section-header"><h2>Uygulanabilirlik Bildirgesi (SoA)</h2><span class="badge b-info">BG.SOA.01 v2.0</span></div>
  <div class="card">
    <div style="display:flex;gap:12px;margin-bottom:12px;flex-wrap:wrap">
      <select onchange="filterTableBySelect(this,'soa-table',2)" style="padding:6px 10px;border:1px solid #ddd;border-radius:6px">
        <option value="">Tum Durumlar</option>
        <option>Uygulanmaktadir</option>
        <option>Kismi</option>
        <option>Planlanmaktadir</option>
        <option>Haric</option>
      </select>
      <input type="text" class="search-box" style="flex:1" placeholder="Kontrol ara..." onkeyup="filterTable(this,'soa-table')">
    </div>
    <table id="soa-table">
      <thead><tr><th>Madde</th><th>Kontrol</th><th>Durum</th><th>Haric Neden</th><th>Kanit</th></tr></thead>
      <tbody>
        <tr><td>A.5.1.1</td><td>Bilgi guvenligi politikalari</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.01</td></tr>
        <tr><td>A.5.1.2</td><td>Politikalarin gozden gecirilmesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>YGG kayitlari</td></tr>
        <tr><td>A.6.1.1</td><td>BG rolleri ve sorumluluklar</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>GN.ORG.01</td></tr>
        <tr><td>A.6.1.2</td><td>Gorevler ayrimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>Gorev tanimlari</td></tr>
        <tr><td>A.6.1.3</td><td>Yetkili makamlarla iletisim</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.10</td></tr>
        <tr><td>A.6.1.4</td><td>Ozel ilgi gruplariyla iletisim</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.10</td></tr>
        <tr><td>A.6.1.5</td><td>Proje yonetiminde bilgi guvenligi</td><td><span class="badge b-warning">Kismi</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.6.2.1</td><td>Mobil cihaz politikasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.04</td></tr>
        <tr><td>A.6.2.2</td><td>Uzaktan calisma</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.04</td></tr>
        <tr><td>A.7.1.1</td><td>Tarama</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>IK.PRD.01</td></tr>
        <tr><td>A.7.1.2</td><td>Istihdam sozlesmesi kosullari</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>IK.SZL.02</td></tr>
        <tr><td>A.7.2.1</td><td>Yonetim sorumluluklar</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>GN.ORG.01</td></tr>
        <tr><td>A.7.2.2</td><td>BG farkindaligi ve egitim</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>Egitim kayitlari</td></tr>
        <tr><td>A.7.2.3</td><td>Disiplin sureci</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>IK.PRD.02</td></tr>
        <tr><td>A.7.3.1</td><td>Istihdam sonlandirma sorumluluklar</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>IK.PRD.02</td></tr>
        <tr><td>A.8.1.1</td><td>Varlik envanteri</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.TBL.01</td></tr>
        <tr><td>A.8.1.2</td><td>Varliklarin sahipligi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.TBL.01</td></tr>
        <tr><td>A.8.1.3</td><td>Kabul edilebilir kullanim</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.02</td></tr>
        <tr><td>A.8.1.4</td><td>Varliklarin iadesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>IK.PRD.02</td></tr>
        <tr><td>A.8.2.1</td><td>Bilgi siniflandirma</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.03</td></tr>
        <tr><td>A.8.2.2</td><td>Bilginin etiketlenmesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.03</td></tr>
        <tr><td>A.8.2.3</td><td>Varliklarin kullanimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.02</td></tr>
        <tr><td>A.8.3.1</td><td>Cikarilabilir medya yonetimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.07</td></tr>
        <tr><td>A.8.3.2</td><td>Medyanin elden cikarilmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.IMHA.PLT.01</td></tr>
        <tr><td>A.8.3.3</td><td>Fiziksel medya transferi</td><td><span class="badge b-warning">Kismi</span></td><td>-</td><td>BG.PRD.05</td></tr>
        <tr><td>A.9.1.1</td><td>Erisim kontrol politikasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.05</td></tr>
        <tr><td>A.9.1.2</td><td>Ag ve ag servislerine erisim</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.03</td></tr>
        <tr><td>A.9.2.1</td><td>Kullanici kayit ve iptal</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.03</td></tr>
        <tr><td>A.9.2.2</td><td>Kullanici erisim saglanmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.03</td></tr>
        <tr><td>A.9.2.3</td><td>Aracli erisim haklarinin yonetimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.03</td></tr>
        <tr><td>A.9.2.4</td><td>Kullanici gizli kimlik dogrulama</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.05</td></tr>
        <tr><td>A.9.2.5</td><td>Erisim haklarinin gozden gecirilmesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.03</td></tr>
        <tr><td>A.9.2.6</td><td>Erisim haklarinin kaldirilmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>IK.PRD.02</td></tr>
        <tr><td>A.9.3.1</td><td>Gizli kimlik dogrulama</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.05</td></tr>
        <tr><td>A.9.4.1</td><td>Bilgiye erisim kisitlamasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.03</td></tr>
        <tr><td>A.9.4.2</td><td>Guvenli giris prosedurler</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.03</td></tr>
        <tr><td>A.9.4.3</td><td>Sifre yonetim sistemi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.05</td></tr>
        <tr><td>A.9.4.4</td><td>Aracli programlarin kullanimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.06</td></tr>
        <tr><td>A.9.4.5</td><td>Program kaynak koduna erisim</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.10.1.1</td><td>Kriptografik kontrollerin kullanimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.04</td></tr>
        <tr><td>A.10.1.2</td><td>Anahtar yonetimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.04</td></tr>
        <tr><td>A.11.1.1</td><td>Fiziksel guvenlik cevresi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.05</td></tr>
        <tr><td>A.11.1.2</td><td>Fiziksel giris kontrolleri</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.05</td></tr>
        <tr><td>A.11.1.3</td><td>Ofislerin ve odalarin guvenligi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.05</td></tr>
        <tr><td>A.11.1.4</td><td>Dis ve cevre tehditlerinden koruma</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.05</td></tr>
        <tr><td>A.11.1.5</td><td>Guvenli alanlarda calisma</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.05</td></tr>
        <tr><td>A.11.1.6</td><td>Teslimat ve yukleme alanlari</td><td><span class="badge b-warning">Kismi</span></td><td>-</td><td>BG.PRD.05</td></tr>
        <tr><td>A.11.2.1</td><td>Ekipman yerlestirme ve koruma</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.05</td></tr>
        <tr><td>A.11.2.2</td><td>Destekleyici hizmetler</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.TBL.01</td></tr>
        <tr><td>A.11.2.3</td><td>Kablo guvenligi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.05</td></tr>
        <tr><td>A.11.2.4</td><td>Ekipman bakimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.02</td></tr>
        <tr><td>A.11.2.5</td><td>Varliklarin kaldirilmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.02</td></tr>
        <tr><td>A.11.2.6</td><td>Tesis disindaki ekipman guvenligi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.05</td></tr>
        <tr><td>A.11.2.7</td><td>Guvenli imha veya yeniden kullanim</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.IMHA.PLT.01</td></tr>
        <tr><td>A.11.2.8</td><td>Kullanicisiz terminal guvenligi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.05</td></tr>
        <tr><td>A.11.2.9</td><td>Temiz masa ve ekran politikasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.02</td></tr>
        <tr><td>A.12.1.1</td><td>Belgelenenmis isletim prosedurler</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.06</td></tr>
        <tr><td>A.12.1.2</td><td>Degisiklik yonetimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>GN.PRD.08</td></tr>
        <tr><td>A.12.1.3</td><td>Kapasite yonetimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>GN.PRD.09</td></tr>
        <tr><td>A.12.1.4</td><td>Gelistirme ve isletim ortamlarinin ayrilmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.12.2.1</td><td>Kotu amacli kodlara karsi kontroller</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.06</td></tr>
        <tr><td>A.12.3.1</td><td>Bilgilerin yedeklenmesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLN.02</td></tr>
        <tr><td>A.12.4.1</td><td>Olay kaydetme</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.06</td></tr>
        <tr><td>A.12.4.2</td><td>Kayit bilgilerinin korunmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.06</td></tr>
        <tr><td>A.12.4.3</td><td>Yonetici ve operator kayitlari</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.06</td></tr>
        <tr><td>A.12.4.4</td><td>Saat senkronizasyonu</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.06</td></tr>
        <tr><td>A.12.5.1</td><td>Isletim sistemlerine yazilim yuklenmesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.06</td></tr>
        <tr><td>A.12.6.1</td><td>Teknik gucluklerin yonetimi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>GN.PRD.11</td></tr>
        <tr><td>A.12.6.2</td><td>Yazilim yuklenmesine iliskin kisitlamalar</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.06</td></tr>
        <tr><td>A.12.7.1</td><td>Bilgi sistemleri denetim kontrolleri</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>GN.PRD.03</td></tr>
        <tr><td>A.13.1.1</td><td>Ag kontrolleri</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.07</td></tr>
        <tr><td>A.13.1.2</td><td>Ag servislerinin guvenligi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.07</td></tr>
        <tr><td>A.13.1.3</td><td>Aglarin ayrilmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.07</td></tr>
        <tr><td>A.13.2.1</td><td>Bilgi transferi politika ve prosedurler</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.07</td></tr>
        <tr><td>A.13.2.2</td><td>Bilgi transferi anlasmalari</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.SZL.01</td></tr>
        <tr><td>A.13.2.3</td><td>Elektronik mesajlasma</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLT.02</td></tr>
        <tr><td>A.13.2.4</td><td>Gizlilik anlasmalari</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.SZL.01</td></tr>
        <tr><td>A.14.1.1</td><td>BG gereksinimleri analizi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.14.1.2</td><td>Uygulama servisleri guvenligi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.14.1.3</td><td>Uygulama servis islemlerinin korunmasi</td><td><span class="badge b-warning">Kismi</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.14.2.1</td><td>Guvenli gelistirme politikasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.14.2.2</td><td>Sistem degisiklik kontrol prosedurler</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>GN.PRD.08</td></tr>
        <tr><td>A.14.2.3</td><td>Platform degistikten sonra teknik gozden gecirme</td><td><span class="badge b-warning">Kismi</span></td><td>-</td><td>GN.PRD.08</td></tr>
        <tr><td>A.14.2.4</td><td>Yazilim paketlerindeki degisiklikler</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>GN.PRD.08</td></tr>
        <tr><td>A.14.2.5</td><td>Guvenli sistem muhendisligi prensipleri</td><td><span class="badge b-warning">Kismi</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.14.2.6</td><td>Guvenli gelistirme ortami</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.14.2.7</td><td>Dis kaynakli gelistirme</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.09</td></tr>
        <tr><td>A.14.2.8</td><td>Sistem guvenlik testleri</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.14.2.9</td><td>Sistem kabul testleri</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.14.3.1</td><td>Test verilerinin korunmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.08</td></tr>
        <tr><td>A.15.1.1</td><td>Tedarikci BG politikasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.09</td></tr>
        <tr><td>A.15.1.2</td><td>Tedarikci anlasmalarinda guvenlik</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.SZL.02</td></tr>
        <tr><td>A.15.1.3</td><td>BT tedarik zinciri</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.09</td></tr>
        <tr><td>A.15.2.1</td><td>Tedarikci hizmetlerinin izlenmesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.09</td></tr>
        <tr><td>A.15.2.2</td><td>Tedarikci hizmetlerindeki degisiklikler</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.09</td></tr>
        <tr><td>A.16.1.1</td><td>Sorumluluklar ve prosedurler</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.10</td></tr>
        <tr><td>A.16.1.2</td><td>BG olaylarinin raporlanmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.10</td></tr>
        <tr><td>A.16.1.3</td><td>Guvenlik zayifliklarinin raporlanmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.10</td></tr>
        <tr><td>A.16.1.4</td><td>BG olaylarinin degerlendirilmesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.10</td></tr>
        <tr><td>A.16.1.5</td><td>BG olaylarina yanit</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.10</td></tr>
        <tr><td>A.16.1.6</td><td>BG olaylarindan ogrenme</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.10</td></tr>
        <tr><td>A.16.1.7</td><td>Delil toplama</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.10</td></tr>
        <tr><td>A.17.1.1</td><td>Is surekliligi planlamasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLN.03</td></tr>
        <tr><td>A.17.1.2</td><td>Is surekliligi uygulama</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLN.03</td></tr>
        <tr><td>A.17.1.3</td><td>Is surekliligi dogrulama ve gozden gecirme</td><td><span class="badge b-warning">Kismi</span></td><td>-</td><td>BG.PLN.03</td></tr>
        <tr><td>A.17.2.1</td><td>Bilgi isleme altyapisi kullanilabilirlik</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PLN.02</td></tr>
        <tr><td>A.18.1.1</td><td>Gecerli mevzuat ve sozlesme gereksinimleri</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.12</td></tr>
        <tr><td>A.18.1.2</td><td>Fikri mulkiyet haklari</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.12</td></tr>
        <tr><td>A.18.1.3</td><td>Kayitlarin korunmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.IMHA.PLT.01</td></tr>
        <tr><td>A.18.1.4</td><td>Kisisel verilerin gizliligi ve korunmasi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.KVK.PLT.01</td></tr>
        <tr><td>A.18.1.5</td><td>Kriptografik kontrollerin duzenlenmesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>BG.PRD.04</td></tr>
        <tr><td>A.18.2.1</td><td>BG bagimsiz gozden gecirilmesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>Dis tetkik raporu</td></tr>
        <tr><td>A.18.2.2</td><td>Guvenlik politika uyumu</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>Ic tetkik raporu</td></tr>
        <tr><td>A.18.2.3</td><td>Teknik uyum gozden gecirmesi</td><td><span class="badge b-success">Uygulanmaktadir</span></td><td>-</td><td>Penetrasyon testi</td></tr>
      </tbody>
    </table>
  </div>
</section>
"""

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'a', encoding='utf-8') as f:
    f.write(soa)
print('OK soa')
