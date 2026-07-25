import { useState } from 'react';
import { CONTRACT_CONFIG } from './contractVariablesConfig';

// 2. ENTEGRE EDİLEBİLİR SÖZLEŞME FORMU BİLEŞENİ
export function ContractFormModule() {
  const [formValues, setFormValues] = useState<Record<string, string>>({
    musteri_unvan: "ACME Teknoloji A.Ş.",
    yuklenici_unvan: "ContractsCode Yazılım Ltd. Şti.",
    proje_konusu:
      "iOS ve Android uyumlu e-ticaret mobil uygulaması ve admin yönetim paneli tasarımı, kodlanması ve canlıya alınması.",
    sozlesme_bedeli: "150.000 TL + KDV",
    pesinat_orani: "%30 Peşin",
    teslim_suresi_gun: "60",
    garanti_suresi_ay: "12 Ay",
    yetkili_mahkeme: "İstanbul (Çağlayan) Mahkemeleri",
  });

  const compileContract = () => {
    let result = CONTRACT_CONFIG.templateContent;
    Object.keys(formValues).forEach((key) => {
      result = result.replace(new RegExp(`\\{\\{${key}\\}\\}`, 'g'), formValues[key] || `[${key}]`);
    });
    return result;
  };

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', fontFamily: 'sans-serif' }}>
      {/* Sol: Soru / Cevap Formu */}
      <div style={{ padding: '20px', background: '#f8fafc', borderRadius: '12px' }}>
        <h3>Sözleşme Soruları & Değişkenler</h3>
        {CONTRACT_CONFIG.variables.map((item) => (
          <div key={item.key} style={{ marginBottom: '15px' }}>
            <label style={{ fontWeight: 'bold', display: 'block', fontSize: '13px' }}>{item.question}</label>
            <input
              type="text"
              value={formValues[item.key] || ''}
              onChange={(e) => setFormValues({ ...formValues, [item.key]: e.target.value })}
              style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid #ccc', marginTop: '4px' }}
            />
          </div>
        ))}
      </div>

      {/* Sağ: İstenen Sözleşme Çıktısı */}
      <div style={{ padding: '20px', background: '#fff', border: '1px solid #e2e8f0', borderRadius: '12px' }}>
        <h3>Sözleşme Çıktısı (Canlı Önizleme)</h3>
        <pre style={{ whiteSpace: 'pre-wrap', fontSize: '13px', lineHeight: '1.6' }}>
          {compileContract()}
        </pre>
      </div>
    </div>
  );
}
