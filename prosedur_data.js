// 20 BGYS prosedürü (BG.PRS.01-20) — uret_prosedurler.py'den otomatik çıkarıldı
// firma_bilgileri.html ile aynı localStorage anahtarlarını kullanır
window.PROSEDURLER = [
 {
  "no": 1,
  "title": "Şifre Yönetimi Prosedürü",
  "meta": {
   "İlgili Politika": "Erişim Kontrol Politikası",
   "Prosedür Kodu": "BG.PRS.01",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Şirket çalışanları, stajyerler, sözleşmeli personel ve tedarikçi hesapları.",
  "body": "\n1. Amaç\n{{firma_unvan}} bünyesindeki tüm kullanıcı hesaplarının şifrelerinin güvenli bir şekilde oluşturulmasını, saklanmasını ve periyodik olarak değiştirilmesini sağlamak.\n\n2. Kapsam\nŞirket çalışanları, stajyerler, sözleşmeli personel ve tedarikçi hesapları.\n\n3. Sorumluluklar\nSistem Yöneticisi: Şifre politikasını uygular, şifre değişim zorunluluğunu aktif eder.\n\nKullanıcılar: Şifrelerini gizli tutar, paylaşmaz, zayıf şifre kullanmaz.\n\n4. Uygulama Adımları\n4.1. Şifre Oluşturma\nŞifre en az 8 karakter uzunluğunda olmalıdır.\n\nBüyük harf (A-Z), küçük harf (a-z), rakam (0-9) ve özel karakter (!@#$%^&*) içermelidir.\n\nTahmin edilebilir şifreler kullanılmamalıdır (password, 123456, firmaadı, doğum tarihi vb.).\n\nSistem yöneticisi, kullanıcı için ilk şifreyi oluşturur ve kullanıcı ilk girişte değiştirmek zorundadır.\n\n4.2. Şifre Değişimi\nTüm kullanıcı şifreleri 90 günde bir değiştirilmelidir.\n\nSistem, şifre süresi dolan kullanıcıları otomatik olarak uyarır.\n\nSon kullanılan 5 şifre tekrar kullanılamaz.\n\n4.3. Şifre Saklama\nŞifreler asla açık metin olarak saklanmaz; hash'lenerek (örn. bcrypt, SHA-256) muhafaza edilir.\n\nŞifreler e-posta, mesaj veya sözlü olarak paylaşılmamalıdır.\n\nŞifre yöneticisi (Password Manager) kullanımı teşvik edilir.\n\n4.4. İhlal Durumu\nŞifre ihlali şüphesi varsa derhal sistem yöneticisine bildirilir.\n\nSistem yöneticisi ilgili hesabı askıya alır ve şifreyi sıfırlar.\n\n5. Kayıt ve Dokümantasyon\nŞifre değişimleri sistem loglarına kaydedilir.\n\nŞifre politikası ihlalleri DFİ Kayıtları bölümüne işlenir.\n\n6. Gözden Geçirme\nBu prosedür yılda bir kez veya şifre teknolojilerinde önemli değişiklik olduğunda güncellenir."
 },
 {
  "no": 2,
  "title": "Kullanıcı Erişim Yönetimi Prosedürü",
  "meta": {
   "İlgili Politika": "Erişim Kontrol Politikası",
   "Prosedür Kodu": "BG.PRS.02",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm bilgi sistemleri (ağ, sunucular, uygulamalar, veri tabanları, bulut hizmetleri).",
  "body": "\n1. Amaç\nKullanıcı hesaplarının oluşturulması, yetkilendirilmesi, değiştirilmesi ve iptal edilmesi süreçlerini standart hale getirmek.\n\n2. Kapsam\nTüm bilgi sistemleri (ağ, sunucular, uygulamalar, veri tabanları, bulut hizmetleri).\n\n3. Sorumluluklar\nSistem Yöneticisi: Hesap oluşturur, yetki atar, iptal eder.\n\nYöneticiler: Çalışanlarının erişim ihtiyaçlarını onaylar.\n\nTüm Kullanıcılar: Hesaplarını güvenli kullanır.\n\n4. Uygulama Adımları\n4.1. Hesap Oluşturma\nYeni çalışan için Kullanıcı Hesap Talep Formu doldurulur.\n\nİK ve ilgili yönetici onayı alınır.\n\nSistem yöneticisi, çalışanın görev tanımına uygun yetkilerle hesap oluşturur.\n\nEn az ayrıcalık ilkesi uygulanır: Kullanıcı yalnızca işi için gerekli erişime sahip olur.\n\n4.2. Yetkilendirme Seviyeleri\nSeviye\tYetki\tÖrnek Kullanıcılar\n1 - Kullanıcı\tTemel sistem erişimi\tTüm çalışanlar\n2 - Güvenlik\tGüvenlik logları, firewall\tGüvenlik personeli\n3 - Yönetici\tSistem yapılandırma\tSistem yöneticisi\n4 - Kritik\tTüm sistem erişimi\tGenel Müdür\n4.3. Periyodik Gözden Geçirme\nTüm kullanıcı yetkileri 3 ayda bir gözden geçirilir.\n\nGörev değişikliklerinde yetkiler güncellenir.\n\n4.4. Hesap İptali\nÇalışan işten ayrılışının ardından tüm hesaplar en geç 24 saat içinde kapatılır.\n\nÇıkış prosedürü kapsamında tüm varlıklar iade alınır.\n\nHesap İptal Kontrol Listesi doldurulur.\n\n5. Kayıt ve Dokümantasyon\nTüm hesap oluşturma ve iptal işlemleri loglanır.\n\nYetki değişiklikleri Yetki Günlüğü'ne kaydedilir."
 },
 {
  "no": 3,
  "title": "Varlık Envanteri Yönetim Prosedürü",
  "meta": {
   "İlgili Politika": "Varlık Yönetimi Politikası",
   "Prosedür Kodu": "BG.PRS.03",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Donanım, yazılım, veri, personel, hizmet ve bulut kaynakları.",
  "body": "\n1. Amaç\n{{firma_unvan}} bünyesindeki tüm bilgi varlıklarının tanımlanması, envanterlenmesi ve güncel tutulmasını sağlamak.\n\n2. Kapsam\nDonanım, yazılım, veri, personel, hizmet ve bulut kaynakları.\n\n3. Sorumluluklar\nVarlık Sahipleri: Varlık envanterinden sorumludur.\n\nSistem Yöneticisi: Teknik varlıkların (sunucu, ağ cihazları vb.) envanterini tutar.\n\nİK: Personel envanterini tutar.\n\n4. Uygulama Adımları\n4.1. Varlık Tanımlama\nHer varlık benzersiz bir ID ile etiketlenir.\n\nVarlık türü belirlenir:\n\nDonanım: Sunucu, switch, router, firewall, bilgisayar, telefon\n\nYazılım: İşletim sistemi, uygulama, yönetim yazılımları\n\nVeri: Müşteri veritabanı, log kayıtları, konfigürasyon dosyaları\n\nPersonel: Çalışanlar, stajyerler, sözleşmeliler\n\nHizmet: ISP hizmetleri, bulut hizmetleri, DNS, e-posta\n\n4.2. Varlık Kaydı\nHer varlık için aşağıdaki bilgiler kaydedilir:\n\nVarlık ID\n\nVarlık Adı\n\nTip\n\nSahip / Sorumlu\n\nKonum (fiziksel/mantıksal)\n\nG/B/E (Gizlilik/Bütünlük/Erişilebilirlik) puanları\n\nSınıflandırma seviyesi\n\n4.3. Envanter Güncelleme\nYeni varlık ediniminde 30 gün içinde envantere eklenir.\n\nVarlık elden çıkarıldığında envanterden düşülür.\n\nYılda bir kez tam envanter sayımı yapılır.\n\n4.4. Varlık Etiketleme\nFiziksel varlıklar, barkod veya QR kod ile etiketlenir.\n\nDijital varlıklar, sistem üzerinde etiketlenir.\n\n5. Kayıt ve Dokümantasyon\nEnvanter listesi Varlık Yönetim Sistemi'nde tutulur.\n\nEnvanter değişiklikleri Değişiklik Logu'na kaydedilir."
 },
 {
  "no": 4,
  "title": "Varlık Sınıflandırma Prosedürü",
  "meta": {
   "İlgili Politika": "Varlık Yönetimi Politikası",
   "Prosedür Kodu": "BG.PRS.04",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm bilgi varlıkları (fiziksel ve dijital).",
  "body": "\n1. Amaç\n{{firma_unvan}} bünyesindeki tüm bilgi varlıklarının gizlilik, bütünlük ve erişilebilirlik kriterlerine göre sınıflandırılmasını sağlamak.\n\n2. Kapsam\nTüm bilgi varlıkları (fiziksel ve dijital).\n\n3. Sorumluluklar\nVarlık Sahipleri: Varlığın sınıflandırmasını yapar ve günceller.\n\nBGYS Temsilcisi: Sınıflandırmanın doğruluğunu denetler.\n\n4. Sınıflandırma Seviyeleri\nSeviye\tAçıklama\tÖrnek\nGizli\tYalnızca yetkili kişiler erişebilir\tMüşteri veritabanı, şifreler, sözleşmeler\nHizmete Özel\tİç kullanım, çalışanlar arası paylaşılabilir\tİç dokümanlar, politikalar\nKuruma Özel\tKurum içi, kamuya açık değil\tFinansal raporlar, strateji belgeleri\nGenel\tHerkese açık yayınlanabilir\tWeb sitesi, hizmet tanıtımları\n5. Uygulama Adımları\n5.1. Sınıflandırma Değerlendirmesi\nVarlığın Gizlilik ihtiyacı 1-3 arasında puanlanır.\n\nVarlığın Bütünlük ihtiyacı 1-3 arasında puanlanır.\n\nVarlığın Erişilebilirlik ihtiyacı 1-3 arasında puanlanır.\n\n5.2. Sınıflandırma Atama\nToplam Puan\tSınıflandırma Seviyesi\n7-9\tGizli\n5-6\tHizmete Özel\n3-4\tKuruma Özel\n1-2\tGenel\n5.3. Etiketleme ve İşaretleme\nFiziksel varlıklar renk kodlu etiketlerle işaretlenir.\n\nDijital varlıklar sistem üzerinde sınıflandırma etiketi alır.\n\nGizli varlıklar \"GİZLİ\" ibaresi ile işaretlenir.\n\n6. Gözden Geçirme\nSınıflandırmalar yılda bir kez veya varlık önemli değişiklik geçirdiğinde güncellenir."
 },
 {
  "no": 5,
  "title": "Personel İşe Alım ve Çıkış Prosedürü",
  "meta": {
   "İlgili Politika": "İnsan Kaynakları Güvenliği Politikası",
   "Prosedür Kodu": "BG.PRS.05",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm adaylar, çalışanlar, stajyerler ve sözleşmeli personel.",
  "body": "\n1. Amaç\n{{firma_unvan}} bünyesinde çalışacak personelin işe alım, çalışma süresi ve işten ayrılma süreçlerinde bilgi güvenliği risklerini minimize etmek.\n\n2. Kapsam\nTüm adaylar, çalışanlar, stajyerler ve sözleşmeli personel.\n\n3. Sorumluluklar\nİK Yöneticisi: Aday değerlendirme, gizlilik sözleşmesi, çıkış süreci.\n\nGenel Müdür: Kritik pozisyonlarda onay.\n\n4. İşe Alım Prosedürü\n4.1. İlan ve Başvuru\nAçık pozisyon ilan edilir.\n\nBaşvurular toplanır ve ön eleme yapılır.\n\n4.2. Arka Plan Kontrolü\nAdaylardan referans kontrolü yapılır.\n\nGüvenlik hassasiyeti olan pozisyonlar için Adli Sicil Kaydı talep edilir.\n\nSon 2 iş yerinden referans alınır.\n\n4.3. İşe Başlangıç\nAday Gizlilik Taahhütnamesi imzalar.\n\nBilgi Güvenliği Farkındalık Eğitimi (temel seviye) tamamlanır.\n\nŞirket içi kurallar (sosyal medya, e-posta kullanımı) bilgilendirmesi yapılır.\n\nSistem hesapları oluşturulur ve yetkilendirme yapılır.\n\n5. İşten Ayrılma Prosedürü\n5.1. Çıkış Bildirimi\nÇalışanın işten ayrılış tarihi en az 15 gün önceden İK'ya bildirilir.\n\nÇıkış nedeni (istifa, fesih, emeklilik) kaydedilir.\n\n5.2. Çıkış Kontrol Listesi\nAşağıdaki kontroller yapılır:\n\n□ Tüm şirket varlıkları iade alındı (dizüstü, telefon, akıllı kart)\n□ Erişim hakları iptal edildi (en geç 24 saat içinde)\n□ Şirket e-postası ve belgeleri arşivlendi\n□ Gizlilik Taahhütnamesi'nin devam ettiği hatırlatıldı\n□ Çıkış görüşmesi yapıldı\n6. Kayıt ve Dokümantasyon\nTüm işe alım ve çıkış belgeleri Personel Dosyası'nda saklanır.\n\nEğitim kayıtları Eğitim ve Farkındalık sistemine işlenir."
 },
 {
  "no": 6,
  "title": "Fiziksel Güvenlik Prosedürü",
  "meta": {
   "İlgili Politika": "Fiziksel ve Çevresel Güvenlik Politikası",
   "Prosedür Kodu": "BG.PRS.06",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Ofis alanları, sunucu odası, depo alanları ve taşınabilir ekipmanlar.",
  "body": "\n1. Amaç\n{{firma_unvan}} ofis, sunucu odası ve diğer fiziksel alanlarının yetkisiz erişime, yangına, doğal afetlere ve diğer fiziksel tehditlere karşı korunmasını sağlamak.\n\n2. Kapsam\nOfis alanları, sunucu odası, depo alanları ve taşınabilir ekipmanlar.\n\n3. Sorumluluklar\nTesis Sorumlusu: Fiziksel güvenlik önlemlerinin uygulanması.\n\nSistem Yöneticisi: Sunucu odası güvenliğinden sorumlu.\n\n4. Uygulama Adımları\n4.1. Sunucu Odası Güvenliği\nSunucu odasına erişim yalnızca yetkili personel ile sınırlıdır.\n\nErişim kaydı (kimlik kartı, biyometrik) tutulur.\n\nKapı, otomatik kapanan ve kilitlenebilir özellikte olmalıdır.\n\nYangın söndürme sistemi (tozlu/gazlı) ve duman dedektörleri bulunmalıdır.\n\nIsı ve nem kontrol sistemi (klima) mevcut olmalıdır.\n\n24/7 kamera kaydı yapılmalı ve 30 gün saklanmalıdır.\n\n4.2. Ofis Güvenliği\nZiyaretçiler giriş-çıkış defterine kaydedilir.\n\nZiyaretçiler refakat edilir.\n\nYetkisiz kişilerin hassas alanlara girişi engellenir.\n\nÇalışan kimlik kartları görünür şekilde takılmalıdır.\n\nAcil çıkış yolları işaretlenmeli ve engelsiz olmalıdır.\n\n4.3. Taşınabilir Ekipman Güvenliği\nTaşınabilir cihazlar (dizüstü, tablet) kullanılmadığında kilitli dolaplarda muhafaza edilir.\n\nCihazlar şifre veya biyometrik ile korunur.\n\nCihaz kaybı/hırsızlığı halinde Olay Yönetimi Prosedürü devreye alınır.\n\n4.4. Periyodik Kontroller\nYangın tüpleri 6 ayda bir kontrol edilir.\n\nKamera sistemleri ayda bir test edilir.\n\nAcil durum tatbikatı yılda bir yapılır.\n\n5. Kayıt ve Dokümantasyon\nZiyaretçi kayıtları 6 ay saklanır.\n\nErişim logları 1 yıl saklanır.\n\nFiziksel güvenlik kontrolleri Fiziksel Güvenlik Kontrol Formu'na kaydedilir."
 },
 {
  "no": 7,
  "title": "Güvenlik Olayı Müdahale Prosedürü",
  "meta": {
   "İlgili Politika": "Bilgi Güvenliği Olay Yönetimi Politikası",
   "Prosedür Kodu": "BG.PRS.07",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm bilgi güvenliği olayları (siber saldırı, veri ihlali, sistem arızası, fiziksel ihlal).",
  "body": "\n1. Amaç\n{{firma_unvan}} bünyesinde meydana gelen bilgi güvenliği olaylarına hızlı ve etkin müdahale etmek, etkilerini en aza indirmek ve tekrarını önlemek.\n\n2. Kapsam\nTüm bilgi güvenliği olayları (siber saldırı, veri ihlali, sistem arızası, fiziksel ihlal).\n\n3. Sorumluluklar\nBGYS Temsilcisi: Olay yönetimini koordine eder.\n\nSistem Yöneticisi: Teknik müdahaleyi gerçekleştirir.\n\nTüm Çalışanlar: Olayları derhal bildirir.\n\n4. Olay Tanımları\nSeviye\tAçıklama\tÖrnek\nKritik\tVeri ihlali, hizmet kesintisi\tMüşteri veri sızıntısı, sunucu çökmesi\nYüksek\tSistem saldırısı, yetkisiz erişim\tDDoS saldırısı, kırık hesap\nOrta\tZafiyet tespiti, şüpheli aktivite\tŞifre denemeleri, anormal trafik\nDüşük\tKüçük ihlaller, ihmal\tŞifre paylaşımı, zayıf şifre\n5. Müdahale Adımları\n5.1. Tespit ve Bildirim (10 dakika)\nÇalışan, olayı derhal BGYS Temsilcisi'ne bildirir.\n\nBildirim e-posta veya telefon ile yapılır.\n\n5.2. Ön Değerlendirme (1 saat)\nOlayın türü ve ciddiyeti belirlenir.\n\nEtkilenen sistemler tespit edilir.\n\nOlay seviyesi atanır.\n\n5.3. Müdahale (4 saat - Kritik için)\nSeviye\tMüdahale Süresi\tEkip\nKritik\t< 1 saat\tTüm ekip\nYüksek\t< 4 saat\tTeknik ekip\nOrta\t< 24 saat\tSistem yöneticisi\nDüşük\t< 48 saat\tBGYS temsilcisi\n5.4. Kontrol ve İyileştirme\nSaldırı veya ihlal kaynağı tespit edilir ve kontrol altına alınır.\n\nAdli deliller korunur.\n\nSistemler eski haline getirilir.\n\n5.5. Olay Sonrası Analiz (7 gün içinde)\nKök Neden Analizi yapılır.\n\nOlay raporu hazırlanır.\n\nDFİ (Düzeltici Faaliyet) açılır.\n\n6. Olay Kayıt Formu\nHer olay için aşağıdaki bilgiler kaydedilir:\n\nOlay ID (OT-YYYY-XXX)\n\nTarih ve saat\n\nOlay türü\n\nEtkilenen sistemler\n\nEtki derecesi\n\nAlınan aksiyonlar\n\nKapanış tarihi\n\n7. Kayıt ve Dokümantasyon\nOlay kayıtları 5 yıl saklanır.\n\nOlay raporları BGYS sisteminde arşivlenir."
 },
 {
  "no": 8,
  "title": "Yedekleme ve Kurtarma Prosedürü",
  "meta": {
   "İlgili Politika": "İş Sürekliliği Politikası",
   "Prosedür Kodu": "BG.PRS.08",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Kritik uygulamalar, veritabanları, konfigürasyon dosyaları, log kayıtları.",
  "body": "\n1. Amaç\n{{firma_unvan}} kritik veri ve sistemlerinin düzenli olarak yedeklenmesini ve olası bir felaket durumunda hızlı bir şekilde kurtarılmasını sağlamak.\n\n2. Kapsam\nKritik uygulamalar, veritabanları, konfigürasyon dosyaları, log kayıtları.\n\n3. Sorumluluklar\nSistem Yöneticisi: Yedekleme işlemlerini yapar, kurtarma testlerini gerçekleştirir.\n\nTeknik Ekip: Yedekleme ve kurtarma işlemlerine destek verir.\n\n4. Yedekleme Stratejisi\n4.1. Yedekleme Sıklığı\nVeri Türü\tSıklık\tSaklama Süresi\nMüşteri veritabanı\tGünlük (full), 4 saat (farklı)\t30 gün\nSistem konfigürasyonu\tHaftalık\t90 gün\nLog kayıtları\tGünlük\t1 yıl\nUygulama kodları\tHaftalık\t180 gün\n4.2. Yedekleme Türleri\nTam Yedekleme: Tüm veriler (haftalık)\n\nFarklı Yedekleme: Son tam yedekten sonraki değişiklikler (günlük)\n\nDeğişim Yedekleme: Son yedekten sonraki değişiklikler (saatlik)\n\n4.3. Yedekleme Konumu\nBirincil: Yerel NAS veya sunucu (çalışma ofisinde)\n\nİkincil: Bulut (coğrafi olarak farklı bölgede - örn. AWS, Azure)\n\nÜçüncül: Harici disk (ofis dışında, aylık)\n\n5. Yedekleme Adımları\n5.1. Otomatik Yedekleme\nTüm kritik sistemler için otomatik yedekleme zamanlanır.\n\nYedekleme başarısı her gün kontrol edilir.\n\nYedekleme logları tutulur.\n\n5.2. Manuel Yedekleme\nKritik değişiklikler öncesi (sürüm güncelleme, yapılandırma değişikliği) manuel yedek alınır.\n\nManuel yedekler \"Yedekleme\" klasörüne tarih/saat ile kaydedilir.\n\n6. Kurtarma Prosedürü\n6.1. RTO ve RPO Değerleri\nRTO (Kurtarma Süresi): 4 saat\n\nRPO (Veri Kaybı Hedefi): 1 saat\n\n6.2. Kurtarma Adımları\nDURUM: Sistem arızası veya veri kaybı tespit edilir.\n\nKONTROL: En son başarılı yedek tespit edilir.\n\nKURTARMA: Yedek sistem veya sunucuya kopyalanır.\n\nDOĞRULAMA: Veri bütünlüğü ve sistem çalışması test edilir.\n\nRAPOR: Kurtarma raporu hazırlanır.\n\n6.3. Kurtarma Testi\nYılda en az 2 kez masa başı felaket senaryosu testi yapılır.\n\nTestlerden önce güncel yedekler alınır.\n\nTest sonuçları Kurtarma Test Raporu ile belgelenir.\n\nKritik sistemler için canlı kurtarma testi yılda 1 kez yapılır.\n\n7. Kayıt ve Dokümantasyon\nYedekleme logları 30 gün saklanır.\n\nKurtarma test raporları BGYS arşivinde tutulur."
 },
 {
  "no": 9,
  "title": "Yasal Uyum Kontrol Prosedürü",
  "meta": {
   "İlgili Politika": "Uyum Politikası",
   "Prosedür Kodu": "BG.PRS.09",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Kişisel veri işleme, trafik kaydı saklama, müşteri sözleşmeleri ve sektörel mevzuat.",
  "body": "\n1. Amaç\n{{firma_unvan}} faaliyetlerinin KVKK, BTK ve diğer yasal düzenlemelere uygunluğunu sağlamak ve belgelemek.\n\n2. Kapsam\nKişisel veri işleme, trafik kaydı saklama, müşteri sözleşmeleri ve sektörel mevzuat.\n\n3. Sorumluluklar\nBGYS Temsilcisi: Uyum kontrollerini koordine eder.\n\nHukuk Danışmanı: Mevzuat değişikliklerini takip eder.\n\n4. Uygulama Adımları\n4.1. Mevzuat Takibi\nHukuk danışmanı, KVKK ve BTK mevzuat değişikliklerini 3 ayda bir takip eder.\n\nDeğişiklikler BGYS Temsilcisi'ne raporlanır.\n\nGerekiyorsa politika/prosedür güncellemesi yapılır.\n\n4.2. KVKK Uyum Kontrolleri\nKişisel veri işleme faaliyetleri VERBİS kaydı yapılır.\n\nAydınlatma metinleri tüm veri toplama noktalarında mevcuttur.\n\nAçık rıza metinleri ve onay kayıtları saklanır.\n\nKişisel veri saklama ve imha politikası uygulanır.\n\n4.3. BTK Uyum Kontrolleri\nİnternet trafik kayıtları BTK'ya uygun olarak 2 yıl saklanır.\n\nTrafik kayıtlarına erişim prosedürü uygulanır.\n\nYasal makamlara bilgi sağlama prosedürü hazırdır.\n\n4.4. Sözleşme Uyumu\nMüşteri sözleşmelerinde gizlilik ve veri koruma maddeleri bulunur.\n\nTedarikçi sözleşmelerinde güvenlik yükümlülükleri tanımlanır.\n\n4.5. Periyodik Kontroller\nYıllık iç denetim ile uyum durumu kontrol edilir.\n\nUyum ihlalleri DFİ kaydına alınır.\n\n5. Kayıt ve Dokümantasyon\nVERBİS kayıtları güncel tutulur.\n\nTüm aydınlatma metinleri revize edilir.\n\nUyum raporları yıllık olarak hazırlanır."
 },
 {
  "no": 10,
  "title": "Tedarikçi Değerlendirme Prosedürü",
  "meta": {
   "İlgili Politika": "Tedarikçi Güvenliği Politikası",
   "Prosedür Kodu": "BG.PRS.10",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm tedarikçiler, iş ortakları, dış hizmet sağlayıcılar (bulut, bakım, danışmanlık).",
  "body": "\n1. Amaç\n{{firma_unvan}} ile çalışan tedarikçi ve iş ortaklarının bilgi güvenliği risklerini değerlendirmek ve yönetmek.\n\n2. Kapsam\nTüm tedarikçiler, iş ortakları, dış hizmet sağlayıcılar (bulut, bakım, danışmanlık).\n\n3. Sorumluluklar\nSatınalma Sorumlusu: Tedarikçi değerlendirme sürecini yönetir.\n\nBGYS Temsilcisi: Güvenlik değerlendirmesini yapar.\n\n4. Uygulama Adımları\n4.1. Tedarikçi Ön Değerlendirme\nTedarikçi, Tedarikçi Güvenlik Değerlendirme Formu doldurur.\n\nFormda şu bölümler yer alır:\n\nFirma bilgileri\n\nISO veya güvenlik sertifikaları\n\nVeri koruma politikaları\n\nAlt tedarikçi bilgileri\n\nOlay müdahale yetkinliği\n\n4.2. Güvenlik Kriterleri\nKriter\tDeğerlendirme\nISO 27001 sertifikası\tTercih sebebi\nKVKK uyumu\tZorunlu\nVeri ihlali geçmişi\tİncelenir\nFiziksel güvenlik\tDeğerlendirilir\nErişim kontrol politikası\tDeğerlendirilir\n4.3. Risk Seviyesi Belirleme\nRisk Seviyesi\tAksiyon\nDüşük\tStandart izleme\nOrta\tEk şartlar eklenir\nYüksek\tEk güvenlik denetimi, red veya ek maddeler\n4.4. Sözleşme Aşaması\nSözleşmeye gizlilik ve veri koruma maddeleri eklenir.\n\nOlay bildirim yükümlülüğü (24 saat) belirtilir.\n\nDenetim hakkı maddesi eklenir.\n\n4.5. Periyodik Değerlendirme\nTedarikçiler yılda bir kez yeniden değerlendirilir.\n\nÖnemli olay durumunda ek değerlendirme yapılır.\n\n5. Kayıt ve Dokümantasyon\nTedarikçi değerlendirme formları 5 yıl saklanır.\n\nTedarikçi sözleşmeleri BGYS arşivinde tutulur."
 },
 {
  "no": 11,
  "title": "Risk Değerlendirme Prosedürü",
  "meta": {
   "İlgili Politika": "Bilgi Güvenliği Politikası",
   "Prosedür Kodu": "BG.PRS.11",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm bilgi varlıkları, süreçler ve hizmetler.",
  "body": "\n1. Amaç\n{{firma_unvan}} bünyesindeki bilgi varlıklarına yönelik risklerin sistematik olarak tanımlanması, değerlendirilmesi ve önceliklendirilmesini sağlamak.\n\n2. Kapsam\nTüm bilgi varlıkları, süreçler ve hizmetler.\n\n3. Sorumluluklar\nBGYS Temsilcisi: Risk değerlendirme sürecini yönetir.\n\nVarlık Sahipleri: Riskleri tanımlar ve değerlendirir.\n\nÜst Yönetim: Risk işleme kararlarını onaylar.\n\n4. Uygulama Adımları\n4.1. Risk Tanımlama\nHer varlık için potansiyel tehditler listelenir:\n\nDoğal afetler (yangın, deprem)\n\nSiber saldırılar (DDoS, malware)\n\nİnsan hatası (config hatası, silme)\n\nDonanım arızası\n\nYetkisiz erişim\n\nHer varlık için zafiyetler tespit edilir:\n\nZayıf şifre politikası\n\nEksik yedekleme\n\nGüncel olmayan yazılım\n\nYetersiz fiziksel güvenlik\n\n4.2. Risk Analizi\nHer risk için Olasılık (1-5) puanlanır:\n\n1: Çok düşük (10 yılda 1)\n\n5: Çok yüksek (yılda 1+)\n\nHer risk için Etki (1-5) puanlanır:\n\n1: Önemsiz etki\n\n5: Felaket etki\n\nRisk Skoru = Olasılık × Etki\n\n4.3. Risk Seviyesi\nSkor\tSeviye\tAksiyon\n1-6\tDüşük\tİzle, kabul et\n7-14\tOrta\tRisk işleme planı oluştur\n15-25\tYüksek\tAcil önlem al\n4.4. Risk Kaydı\nHer risk için aşağıdaki bilgiler kaydedilir:\n\nRisk ID (RSK-XXXX)\n\nİlgili varlık\n\nTehdit ve zafiyet\n\nOlasılık ve etki\n\nSkor ve seviye\n\nTespit tarihi\n\n5. Periyodik Tekrar\nRisk değerlendirmesi yılda en az 1 kez tekrarlanır.\n\nYeni varlık veya önemli değişiklik durumunda yeniden değerlendirme yapılır."
 },
 {
  "no": 12,
  "title": "Politika Gözden Geçirme Prosedürü",
  "meta": {
   "İlgili Politika": "Bilgi Güvenliği Politikası",
   "Prosedür Kodu": "BG.PRS.12",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm BGYS politika ve prosedür belgeleri.",
  "body": "\n1. Amaç\n{{firma_unvan}} bünyesindeki tüm bilgi güvenliği politika ve prosedürlerinin periyodik olarak gözden geçirilmesini ve güncellenmesini sağlamak.\n\n2. Kapsam\nTüm BGYS politika ve prosedür belgeleri.\n\n3. Sorumluluklar\nBGYS Temsilcisi: Gözden geçirme sürecini koordine eder.\n\nÜst Yönetim: Değişiklikleri onaylar.\n\n4. Uygulama Adımları\n4.1. Periyodik Gözden Geçirme\nTüm politikalar yılda en az 1 kez gözden geçirilir.\n\nGözden geçirme takvimi: Kasım ayı\n\nGözden geçirme YGG toplantısı ile eşleştirilir.\n\n4.2. Tetikleyici Faktörler\nAşağıdaki durumlarda ek gözden geçirme yapılır:\n\nMevzuat değişikliği (KVKK, BTK)\n\nOrganizasyonel değişiklik\n\nYeni hizmet veya teknoloji\n\nCiddi güvenlik olayı\n\nDenetim bulguları\n\n4.3. Gözden Geçirme Adımları\nMevcut dokümanlar gözden geçirilir.\n\nDeğişiklik ihtiyaçları belirlenir.\n\nTaslak revizyon hazırlanır.\n\nİlgili paydaşlara bilgilendirme yapılır.\n\nÜst yönetim onayı alınır.\n\nRevize belge yayınlanır ve duyurulur.\n\n4.4. Revizyon Takibi\nHer revizyona yeni numara verilir (v1.0 → v1.1 → v2.0)\n\nRevizyon geçmişi belgenin sonunda tutulur.\n\nEski versiyonlar arşivlenir.\n\n5. Kayıt ve Dokümantasyon\nGözden geçirme tarihleri Politika Gözden Geçirme Logu'na kaydedilir.\n\nYeni versiyonlar Doküman Merkezi'nde yayınlanır."
 },
 {
  "no": 13,
  "title": "Eğitim ve Farkındalık Prosedürü",
  "meta": {
   "İlgili Politika": "İnsan Kaynakları Güvenliği Politikası",
   "Prosedür Kodu": "BG.PRS.13",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm çalışanlar, stajyerler, sözleşmeli personel.",
  "body": "\n1. Amaç\n{{firma_unvan}} çalışanlarının bilgi güvenliği konusunda bilinçlendirilmesini ve yetkinliklerinin artırılmasını sağlamak.\n\n2. Kapsam\nTüm çalışanlar, stajyerler, sözleşmeli personel.\n\n3. Sorumluluklar\nBGYS Temsilcisi: Eğitim programını planlar ve uygular.\n\nİK Yöneticisi: Eğitim kayıtlarını tutar.\n\n4. Uygulama Adımları\n4.1. Eğitim Planlaması\nYıllık Eğitim Takvimi hazırlanır.\n\nEğitim ihtiyaçları belirlenir (yeni politika, teknoloji, olaylar).\n\nEğitim materyalleri (sunum, video, doküman) hazırlanır.\n\n4.2. Zorunlu Eğitimler\nEğitim\tHedef Kitle\tSıklık\tSüre\nİşe Başlangıç Bilgi Güvenliği\tYeni çalışanlar\t1 kez\t2 saat\nYıllık Farkındalık\tTüm çalışanlar\tYılda 1\t4 saat\nGüvenlik Olayı Müdahale\tTeknik ekip\tYılda 1\t4 saat\nKişisel Veri Koruma\tTüm çalışanlar\tYılda 1\t2 saat\n4.3. Eğitim Uygulama\nEğitim duyurusu en az 2 hafta önceden yapılır.\n\nEğitim materyalleri paylaşılır.\n\nKatılım listesi tutulur.\n\nEğitim sonrası değerlendirme testi uygulanır (başarı puanı ≥%70).\n\n4.4. Eğitim Kaydı\nHer eğitim için aşağıdaki bilgiler kaydedilir:\n\nEğitim adı ve tarihi\n\nEğitmen\n\nKatılımcı listesi\n\nBaşarı puanları\n\nSertifika (varsa)\n\n5. Eğitim Materyalleri\nBilgi Güvenliği Politikası özeti\n\nErişim Kontrol kuralları\n\nŞifre güvenliği\n\nSosyal mühendislik farkındalığı\n\nOlay bildirim süreci\n\nKVKK temel prensipleri"
 },
 {
  "no": 14,
  "title": "İç Denetim Prosedürü",
  "meta": {
   "İlgili Politika": "Bilgi Güvenliği Politikası",
   "Prosedür Kodu": "BG.PRS.14",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm BGYS süreçleri, politikalar, prosedürler ve kontroller.",
  "body": "\n1. Amaç\n{{firma_unvan}} BGYS uygulamalarının etkinliğini değerlendirmek ve ISO 27001:2022 uyumunu doğrulamak.\n\n2. Kapsam\nTüm BGYS süreçleri, politikalar, prosedürler ve kontroller.\n\n3. Sorumluluklar\nBGYS Temsilcisi: Denetim programını planlar.\n\nDenetçi(ler): Denetimi yürütür.\n\nDenetlenen Birim: Bulgulara yanıt verir.\n\n4. Uygulama Adımları\n4.1. Denetim Planlaması\nYıllık Denetim Takvimi hazırlanır.\n\nDenetim kapsamı ve kriterleri belirlenir.\n\nDenetçi(ler) atanır (mümkünse bağımsız).\n\n4.2. Denetim Adımları\nBaşlangıç Toplantısı: Kapsam ve plan paylaşılır.\n\nDoküman İncelemesi: Politika, prosedür, kayıtlar incelenir.\n\nSaha Gözlemleri: Uygulamalar yerinde gözlemlenir.\n\nGörüşmeler: Çalışanlarla görüşülür.\n\n4.3. Bulgu Sınıflandırması\nTür\tAçıklama\tÖrnek\nMajor Uyumsuzluk\tSistemik hata, standarda aykırı\tRisk analizi yapılmamış\nMinor Uyumsuzluk\tBireysel hata, küçük eksiklik\tBir politika güncel değil\nGözlem\tİyileştirme fırsatı\tSüreç verimliliği\nFırsat\tProaktif iyileştirme\tYeni kontrol önerisi\n4.4. Raporlama\nDenetim bulguları İç Denetim Raporu olarak hazırlanır.\n\nBulgular DFİ'ye açılır (gerekirse).\n\nRapor YGG toplantısında sunulur.\n\n5. Kayıt ve Dokümantasyon\nDenetim raporları 5 yıl saklanır.\n\nDenetim bulguları DFİ sistemine kaydedilir."
 },
 {
  "no": 15,
  "title": "DFİ (Düzeltici Faaliyet) Prosedürü",
  "meta": {
   "İlgili Politika": "Bilgi Güvenliği Politikası",
   "Prosedür Kodu": "BG.PRS.15",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "İç denetim bulguları, olaylar, müşteri şikayetleri, dış denetim bulguları.",
  "body": "\n1. Amaç\nTespit edilen uyumsuzlukların, hataların ve zafiyetlerin sistematik olarak düzeltilmesini ve tekrarının önlenmesini sağlamak.\n\n2. Kapsam\nİç denetim bulguları, olaylar, müşteri şikayetleri, dış denetim bulguları.\n\n3. Sorumluluklar\nBGYS Temsilcisi: DFİ sürecini yönetir.\n\nİlgili Kişi: DFİ'yi uygular.\n\n4. Uygulama Adımları\n4.1. DFİ Açılma Kriterleri\nAşağıdaki durumlarda DFİ açılır:\n\nİç denetimde Major UU\n\nTekrarlayan Minor UU\n\nGüvenlik olayı (orta/kritik)\n\nMüşteri şikayeti\n\nDış denetim bulgusu\n\n4.2. DFİ Kayıt Bilgileri\nDFI No (DFI-XXX)\n\nKaynak (İç Denetim / Dış Denetim / Olay / Şikayet)\n\nTespit Tarihi\n\nAçıklama\n\nKök Neden Analizi\n\nDüzeltici Aksiyon\n\nSorumlu\n\nTermin Tarihi\n\nDurum (Açık / Devam / Kapalı)\n\n4.3. Kök Neden Analizi (5N1K)\nNe oldu?\n\nNerede oldu?\n\nNe zaman oldu?\n\nKim yaptı/ihmal etti?\n\nNeden oldu? (en az 3 seviye)\n\nNasıl önlenir?\n\n4.4. DFİ Uygulama\nKök neden belirlenir.\n\nDüzeltici aksiyon belirlenir.\n\nSorumlu kişi atanır.\n\nTermin tarihi belirlenir.\n\n4.5. DFİ Kapatma\nAksiyon uygulanır.\n\nEtkinlik doğrulaması yapılır.\n\nKapanış tarihi kaydedilir.\n\nYGG'de raporlanır.\n\n5. Kayıt ve Dokümantasyon\nDFİ kayıtları DFİ Takip Sistemi'nde tutulur.\n\nKapanan DFİ'ler arşivlenir."
 },
 {
  "no": 16,
  "title": "Ağ Güvenliği Yönetim Prosedürü",
  "meta": {
   "İlgili Politika": "Bilgi Güvenliği Politikası",
   "Prosedür Kodu": "BG.PRS.16",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm ağ cihazları (firewall, router, switch), ağ servisleri (DNS, DHCP) ve bağlantılar.",
  "body": "\n1. Amaç\n{{firma_unvan}} ağ altyapısının güvenli bir şekilde yapılandırılmasını, izlenmesini ve korunmasını sağlamak.\n\n2. Kapsam\nTüm ağ cihazları (firewall, router, switch), ağ servisleri (DNS, DHCP) ve bağlantılar.\n\n3. Sorumluluklar\nSistem Yöneticisi: Ağ güvenlik yapılandırmasını yapar.\n\nTeknik Ekip: Ağ izleme ve müdahale işlemlerini gerçekleştirir.\n\n4. Uygulama Adımları\n4.1. Ağ Mimarisi\nAğ Segmentasyonu: Ağ, güvenlik seviyelerine göre segmentlere ayrılır:\n\nDMZ (web, mail sunucuları)\n\nİç Ağ (çalışanlar)\n\nYönetim Ağı (sistem yönetimi)\n\nMinimum 3 farklı VLAN kullanılır.\n\n4.2. Firewall Yapılandırması\nDeny-all/Allow-by-exception politikası uygulanır.\n\nYalnızca gerekli portlar açılır.\n\nGelen/giden trafik loglanır.\n\nFirewall kuralları 3 ayda bir gözden geçirilir.\n\n4.3. VPN ve Uzaktan Erişim\nUzaktan erişim için VPN kullanılır.\n\nVPN bağlantıları için MFA zorunludur.\n\nVPN kullanıcıları en az ayrıcalık ilkesine tabidir.\n\n4.4. Ağ İzleme\nIDS/IPS sistemi aktif izleme yapar.\n\nAnormal trafik tespitinde Olay Yönetimi Prosedürü devreye alınır.\n\nAğ bant gençiliği ve performans izlenir.\n\n4.5. Güvenlik Güncellemeleri\nTüm ağ cihazları 30 günde bir güncellenir.\n\nKritik güvenlik yamaları 48 saat içinde uygulanır.\n\n5. Kayıt ve Dokümantasyon\nAğ topolojisi Ağ Diyagramı ile belgelenir.\n\nFirewall logları 6 ay saklanır.\n\nKonfigürasyon yedekleri alınır."
 },
 {
  "no": 17,
  "title": "Uzaktan Çalışma Güvenliği Prosedürü",
  "meta": {
   "İlgili Politika": "Erişim Kontrol Politikası",
   "Prosedür Kodu": "BG.PRS.17",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Uzaktan çalışan tüm personel (ev ofis, seyahat, saha).",
  "body": "\n1. Amaç\n{{firma_unvan}} çalışanlarının uzaktan çalışma durumlarında bilgi güvenliğini sağlamak.\n\n2. Kapsam\nUzaktan çalışan tüm personel (ev ofis, seyahat, saha).\n\n3. Sorumluluklar\nSistem Yöneticisi: Uzaktan erişim altyapısını güvenli hale getirir.\n\nÇalışanlar: Kendi çalışma ortamlarının güvenliğinden sorumludur.\n\n4. Uygulama Adımları\n4.1. Uzaktan Erişim Güvenliği\nTüm uzaktan erişimler VPN üzerinden yapılır.\n\nVPN bağlantısı MFA ile korunur.\n\nUzaktan erişim süresi 8 saat ile sınırlıdır (automatic disconnect).\n\n4.2. Cihaz Güvenliği\nKullanılan cihaz şifre korumalı olmalıdır.\n\nCihaz ekranı 5 dakika inaktivitede kilitlenir.\n\nCihazda güncel antivirüs bulunur.\n\nHassas veriler cihazda saklanmaz (bulut veya VPN üzerinden erişilir).\n\n4.3. Çalışma Ortamı\nUzaktan çalışma ortamı özel bir alan olmalıdır.\n\nEkran etrafından başkalarının görmemesi sağlanmalıdır.\n\nHassas dosyalar basılmamalı veya açıkta bırakılmamalıdır.\n\n4.4. Uzaktan Toplantı Güvenliği\nToplantı linkleri parola korumalıdır.\n\nToplantılar bekleme odası ile başlatılır.\n\nToplantı kayıtları güvenli alanda saklanır.\n\n4.5. Uzaktan Çalışma Bildirimi\nUzaktan çalışma başlangıcı en az 1 gün önceden yöneticiye bildirilir.\n\nUzaktan çalışma süresi ve kapsamı kaydedilir.\n\n5. Kayıt ve Dokümantasyon\nUzaktan çalışma talep formları saklanır.\n\nVPN giriş logları tutulur."
 },
 {
  "no": 18,
  "title": "Bilgi Varlığı İmha Prosedürü",
  "meta": {
   "İlgili Politika": "Varlık Yönetimi Politikası",
   "Prosedür Kodu": "BG.PRS.18",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm veri ortamları (dijital, kağıt, donanım), tüm sınıflandırma seviyeleri.",
  "body": "\n1. Amaç\n{{firma_unvan}} bünyesinde artık ihtiyaç duyulmayan bilgi varlıklarının güvenli bir şekilde imha edilmesini sağlamak.\n\n2. Kapsam\nTüm veri ortamları (dijital, kağıt, donanım), tüm sınıflandırma seviyeleri.\n\n3. Sorumluluklar\nVarlık Sahibi: İmha kararını verir ve süreci başlatır.\n\nSistem Yöneticisi: Dijital imhayı gerçekleştirir.\n\nİK Yöneticisi: Personel dosyalarının imhasını yönetir.\n\n4. Uygulama Adımları\n4.1. İmha Kararı\nVarlık sahibi, varlığın artık gerekli olmadığına karar verir.\n\nVarlık imha için uygun görülür (saklama süresi dolmuş, yedeklenmiş).\n\nİmha Onay Formu doldurulur ve onaylanır.\n\n4.2. Dijital Veri İmha Yöntemleri\nVeri Türü\tİmha Yöntemi\tSüre\nGizli veri\tFiziksel imha (disk parçalama)\t1 saat\nHizmete Özel\tSilme + üzerine yazma (3 pas)\t2 saat\nKuruma Özel\tSilme + üzerine yazma (1 pas)\t1 saat\nGenel\tNormal silme\t30 dakika\n4.3. Kağıt ve Medya İmhası\nGizli evraklar kıyma makinesi ile parçalanır.\n\nDış ortamda evrak imhası için lisanslı imha firması kullanılır.\n\nCD/DVD gibi medyalar fiziksel olarak kırılır.\n\n4.4. Donanım İmhası\nSabit diskler fiziksel olarak kırılır veya mıknatıslanır.\n\nBellek ve depolama birimleri imha edilir.\n\nDonanım imha belgesi düzenlenir.\n\n4.5. İmha Kaydı\nHer imha için aşağıdaki bilgiler kaydedilir:\n\nVarlık ID\n\nVarlık adı\n\nİmha nedeni\n\nİmha yöntemi\n\nİmha tarihi\n\nİmha eden kişi\n\nOnaylayan kişi\n\n5. Kayıt ve Dokümantasyon\nİmha kayıtları 5 yıl saklanır.\n\nİmha Onay Formları arşivlenir."
 },
 {
  "no": 19,
  "title": "Yazılım Lisans Yönetim Prosedürü",
  "meta": {
   "İlgili Politika": "Uyum Politikası",
   "Prosedür Kodu": "BG.PRS.19",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm bilgisayar, sunucu, ağ cihazı ve bulut sistemlerindeki yazılımlar.",
  "body": "\n1. Amaç\n{{firma_unvan}} bünyesinde kullanılan tüm yazılımların lisanslı, güncel ve yasalara uygun olmasını sağlamak.\n\n2. Kapsam\nTüm bilgisayar, sunucu, ağ cihazı ve bulut sistemlerindeki yazılımlar.\n\n3. Sorumluluklar\nSistem Yöneticisi: Lisansların yönetiminden sorumludur.\n\nSatınalma Sorumlusu: Lisans satın alımını yapar.\n\n4. Uygulama Adımları\n4.1. Lisans Envanteri\nTüm yazılımlar Yazılım Envanteri'ne kaydedilir:\n\nYazılım adı\n\nVersiyon\n\nLisans türü (box, OEM, kurumsal)\n\nLisans sayısı\n\nSon kullanma tarihi\n\nEnvanter 3 ayda bir güncellenir.\n\n4.2. Lisans Edinimi\nHer yeni yazılım lisanslı olarak satın alınır.\n\nAçık kaynak yazılımların lisans türü (GPL, MIT, vb.) kontrol edilir.\n\nSatın alma öncesi fiyat teklifleri karşılaştırılır.\n\n4.3. Lisans Kontrolleri\n6 ayda bir lisans uygunluk denetimi yapılır.\n\nFazla kullanım tespitinde ek lisans alınır.\n\nEksik kullanımda lisans sayısı düşürülür.\n\n4.4. Lisans Yenileme\nSüresi dolan lisanslar en az 1 ay önce yenilenir.\n\nYenileme bütçesi yıllık plana dahil edilir.\n\n4.5. İhlal Durumu\nLisans ihlali tespitinde ilgili birim uyarılır.\n\nİhlal DFİ kaydına alınır.\n\nGerekirse ek lisans satın alımı yapılır.\n\n5. Kayıt ve Dokümantasyon\nLisans satın alma faturaları 5 yıl saklanır.\n\nYazılım Envanteri güncel tutulur."
 },
 {
  "no": 20,
  "title": "Log Yönetimi ve İzleme Prosedürü",
  "meta": {
   "İlgili Politika": "Olay Yönetimi Politikası",
   "Prosedür Kodu": "BG.PRS.20",
   "Revizyon": "v1.0 – Nisan 2026"
  },
  "kapsam": "Tüm sistemler, ağ cihazları, uygulamalar ve güvenlik cihazları.",
  "body": "\n1. Amaç\n{{firma_unvan}} sistem, ağ ve uygulama loglarının güvenli bir şekilde toplanması, saklanması ve analiz edilmesini sağlamak.\n\n2. Kapsam\nTüm sistemler, ağ cihazları, uygulamalar ve güvenlik cihazları.\n\n3. Sorumluluklar\nSistem Yöneticisi: Log toplama ve yönetimini yapar.\n\nBGYS Temsilcisi: Log kontrollerini denetler.\n\n4. Uygulama Adımları\n4.1. Log Türleri\nAşağıdaki loglar toplanır:\n\nSistem Logları: İşletim sistemi, servisler\n\nGüvenlik Logları: Firewall, IDS/IPS, antivirüs\n\nErişim Logları: Kullanıcı girişleri, yetkisiz erişim denemeleri\n\nUygulama Logları: Web sunucu, veritabanı\n\nAğ Logları: Trafik, bağlantılar\n\n4.2. Log Toplama\nTüm sistemler Merkezi Log Sunucusu'na log gönderir.\n\nLog gönderimi Syslog veya SIEM aracılığıyla yapılır.\n\nLog kaybı veya kesinti durumunda alarm verilir.\n\n4.3. Log Saklama Süreleri\nLog Türü\tSaklama Süresi\nErişim logları\t1 yıl\nGüvenlik logları\t2 yıl\nAğ trafik logları\t2 yıl (BTK zorunlu)\nSistem logları\t6 ay\nUygulama logları\t6 ay\n4.4. Log Koruma\nLoglar şifrelenmiş olarak saklanır.\n\nLoglara erişim yetkili personel ile sınırlıdır.\n\nLoglar düzenlenemez (append-only) modda tutulur.\n\nLoglar yedeklenir (coğrafi olarak farklı konum).\n\n4.5. Log Analizi ve İzleme\nKritik loglar gerçek zamanlı izlenir.\n\nAnomali tespiti için baz hat (baseline) oluşturulur.\n\nHaftalık log raporu hazırlanır.\n\nŞüpheli aktivite tespitinde Olay Yönetimi Prosedürü devreye alınır.\n\n5. Kayıt ve Dokümantasyon\nLog saklama politikası Log Yönetim Politikası ile belgelenir.\n\nLog analiz raporları arşivlenir."
 }
];
