// 1. DEĞİŞKENLER VE ŞABLON TANIMI (contractVariablesConfig.ts)
export const CONTRACT_CONFIG = {
  templateTitle: "Yazılım Geliştirme ve Hizmet Sözleşmesi",
  templateCategory: "Yazılım & Bilişim",
  version: "2.1",
  variables: [
    {
      key: "musteri_unvan",
      label: "Müşteri / İşveren Ticari Unvanı",
      type: "text",
      category: "Taraflar",
      question: "Sözleşmenin 'Müşteri / İşveren' tarafı olan şirket veya kişinin resmi unvanı nedir?",
      placeholder: "Örn: ACME Teknoloji Anonim Şirketi",
      defaultValue: "ACME Teknoloji A.Ş.",
      description: "Fatura ve resmi yazışmalarda kullanılacak tam unvan.",
      required: true,
    },
    {
      key: "yuklenici_unvan",
      label: "Yüklenici / Hizmet Veren Unvanı",
      type: "text",
      category: "Taraflar",
      question: "Hizmeti sağlayacak Yüklenici tarafın resmi unvanı veya ad-soyadı nedir?",
      placeholder: "Örn: ContractsCode Yazılım A.Ş.",
      defaultValue: "ContractsCode Yazılım Ltd. Şti.",
      description: "Geliştirici veya ajans unvanı.",
      required: true,
    },
    {
      key: "proje_konusu",
      label: "Proje / Hizmet Konusu",
      type: "text_area",
      category: "Süre & Teslim",
      question: "Geliştirilecek yazılım veya sunulacak hizmetin detaylı kapsamı nedir?",
      placeholder: "Örn: iOS ve Android uyumlu e-ticaret mobil uygulaması ve web yönetim paneli geliştirilmesi.",
      defaultValue:
        "iOS ve Android uyumlu e-ticaret mobil uygulaması ve admin yönetim paneli tasarımı, kodlanması ve canlıya alınması.",
      description: "İşin teknik kapsam tanımı.",
      required: true,
    },
    {
      key: "sozlesme_bedeli",
      label: "Sözleşme Toplam Bedeli",
      type: "text",
      category: "Finansal",
      question: "İş için kararlaştırılan toplam sözleşme bedeli ne kadardır?",
      placeholder: "Örn: 150.000 TL + KDV",
      defaultValue: "150.000 TL + KDV",
      description: "Rakam ve para birimi belirtiniz.",
      required: true,
    },
    {
      key: "pesinat_orani",
      label: "Peşinat Ödeme Oranı (%)",
      type: "select",
      options: ["%20 Peşin", "%30 Peşin", "%50 Peşin", "Peşinatsız (İş Sonunda)"],
      category: "Finansal",
      question: "İş başlangıcında alınacak peşinat oranı nedir?",
      defaultValue: "%30 Peşin",
      description: "Ödeme takvimi peşinat yüzdesi.",
      required: true,
    },
    {
      key: "teslim_suresi_gun",
      label: "Proje Teslim Süresi (Gün)",
      type: "number",
      category: "Süre & Teslim",
      question: "Projenin tamamlanıp teslim edileceği toplam gün sayısı kaçtır?",
      placeholder: "Örn: 60",
      defaultValue: "60",
      description: "İş günü cinsinden süre.",
      required: true,
    },
    {
      key: "garanti_suresi_ay",
      label: "Bakım & Garanti Süresi (Ay)",
      type: "select",
      options: ["3 Ay", "6 Ay", "12 Ay", "24 Ay"],
      category: "Süre & Teslim",
      question: "Teslimat sonrası sunulacak ücretsiz hata düzeltme ve garanti süresi kaç aydır?",
      defaultValue: "12 Ay",
      description: "Teslimat sonrası bakım garantisi.",
      required: true,
    },
    {
      key: "yetkili_mahkeme",
      label: "Yetkili Mahkeme ve İcra Daireleri",
      type: "select",
      options: [
        "İstanbul (Çağlayan) Mahkemeleri",
        "Ankara Mahkemeleri",
        "İzmir Mahkemeleri",
        "Bursa Mahkemeleri",
      ],
      category: "Hukuki & Yetki",
      question: "Uyuşmazlık durumunda yetkili kılınacak mahkeme ve icra daireleri neresidir?",
      defaultValue: "İstanbul (Çağlayan) Mahkemeleri",
      description: "Yasal yargı yetkisi.",
      required: true,
    },
  ],
  templateContent: `# YAZILIM GELIŞTIRME VE HIZMET SÖZLEŞMESI

## 1. TARAFLAR
İşbu Sözleşme, aşağıdaki taraflar arasında akdedilmiştir:

- **MÜŞTERİ (İşveren):** {{musteri_unvan}}
- **YÜKLENİCİ (Hizmet Veren):** {{yuklenici_unvan}}

## 2. SÖZLEŞMENİN KONUSU
İşbu sözleşmenin konusu, Yüklenici tarafından Müşteri için aşağıda belirtilen kapsamda yazılım geliştirme hizmetinin sunulmasıdır:
> **Proje Kapsamı:** {{proje_konusu}}

## 3. BEDEL VE ÖDEME KOŞULLARI
- Sözleşmenin toplam bedeli **{{sozlesme_bedeli}}** olarak belirlenmiştir.
- Ödeme planı uyarınca iş başlangıcında **{{pesinat_orani}}** oranında avans ödemesi yapılacak, kalan bakiye ise proje teslimatında tahsil edilecektir.

## 4. SÜRE VE GARANTİ
- Projenin toplam teslim süresi, sözleşmenin imzalanması ve peşinatın ödenmesini müteakip **{{teslim_suresi_gun}} gün**dür.
- Yüklenici, teslimat tarihinden itibaren **{{garanti_suresi_ay}}** boyunca yazılımdaki sistem hatalarını ücretsiz olarak gidermeyi taahhüt eder.

## 5. YETKİLİ MAHKEME
İşbu sözleşmeden doğabilecek uyuşmazlıkların çözümünde **{{yetkili_mahkeme}}** yetkilidir.

İşbu sözleşme 5 (beş) maddeden ibaret olup taraflarca okunarak dijital/ıslak imza ile onaylanmıştır.`,
};
