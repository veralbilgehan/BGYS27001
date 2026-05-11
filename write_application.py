
# Insert application section before </main>
with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'r', encoding='utf-8') as f:
    content = f.read()

app_section = """
<section id="application" style="display:none">
  <div class="section-header"><h2>Basvuru Takibi</h2><button class="btn" onclick="openModal('newApp')">+ Yeni Basvuru</button></div>
  <div class="card">
    <div style="display:flex;gap:0;margin-bottom:24px;background:#f1f5f9;border-radius:8px;padding:4px">
      <div style="flex:1;text-align:center;padding:8px 4px;background:white;border-radius:6px;font-size:12px;font-weight:600;color:#3b82f6;box-shadow:0 1px 3px rgba(0,0,0,.1)">1. Basvuru</div>
      <div style="flex:1;text-align:center;padding:8px 4px;font-size:12px;color:#94a3b8">2. On Degerlendirme</div>
      <div style="flex:1;text-align:center;padding:8px 4px;font-size:12px;color:#94a3b8">3. Asama-1 Denetim</div>
      <div style="flex:1;text-align:center;padding:8px 4px;font-size:12px;color:#94a3b8">4. Asama-2 Denetim</div>
      <div style="flex:1;text-align:center;padding:8px 4px;font-size:12px;color:#94a3b8">5. Sertifika</div>
      <div style="flex:1;text-align:center;padding:8px 4px;font-size:12px;color:#94a3b8">6. Gozetim</div>
    </div>
    <h3 style="margin-bottom:12px">Belgelendirme Surec Takibi</h3>
    <table id="app-table">
      <thead><tr><th>Asama</th><th>Aktivite</th><th>Tarih</th><th>Kurum</th><th>Durum</th><th>Notlar</th></tr></thead>
      <tbody>
        <tr><td>1</td><td>TSE'ye basvuru yapildi</td><td>01.03.2023</td><td>TSE</td><td><span class="badge b-success">Tamamlandi</span></td><td>Basvuru No: 2023-BG-0042</td></tr>
        <tr><td>2</td><td>On degerlendirme ziyareti</td><td>15.05.2023</td><td>TSE</td><td><span class="badge b-success">Tamamlandi</span></td><td>Bosluklar belirlendi</td></tr>
        <tr><td>3</td><td>Dokuman incelemesi (Asama-1)</td><td>18.09.2023</td><td>TSE</td><td><span class="badge b-success">Tamamlandi</span></td><td>3 minor gozlem</td></tr>
        <tr><td>4</td><td>Saha denetimi (Asama-2)</td><td>27-28.11.2023</td><td>TSE</td><td><span class="badge b-success">Tamamlandi</span></td><td>0 major, 2 minor UU</td></tr>
        <tr><td>5</td><td>Sertifika verilmesi</td><td>15.12.2023</td><td>TSE</td><td><span class="badge b-success">Tamamlandi</span></td><td>3 yil gecerli</td></tr>
        <tr><td>6</td><td>1. Gozetim denetimi (planli)</td><td>Kasim 2024</td><td>TSE</td><td><span class="badge b-info">Planlanmis</span></td><td>Hazirligi baslat</td></tr>
        <tr><td>6</td><td>2. Gozetim denetimi (planli)</td><td>Kasim 2025</td><td>TSE</td><td><span class="badge b-info">Planlanmis</span></td><td>-</td></tr>
        <tr><td>-</td><td>Yeniden belgelendirme</td><td>Kasim 2026</td><td>TSE</td><td><span class="badge b-info">Planlanmis</span></td><td>Surec yeniden baslar</td></tr>
      </tbody>
    </table>
  </div>
</section>
"""

# Insert before </main>
content = content.replace('    </main>', app_section + '    </main>', 1)

with open('c:/Users/bilge/OneDrive/Belgeler/TELKOMISO27001/bgys_panel.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('OK application section inserted')
