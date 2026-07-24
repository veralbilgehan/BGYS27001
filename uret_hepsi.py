# -*- coding: utf-8 -*-
"""
4 AJAN KOORDINATORU - tum BGYS belgelerini tek komutla uretir.
Ajan 1: firma_bilgileri.html (manuel form - burada atlanir, sadece raporlanir)
Ajan 2: uret_protokoller.py   -> 9 politika
Ajan 3: uret_prosedurler.py   -> 20 prosedur
Ajan 4: uret_risk_soa.py      -> Risk Analizi + SoA
Ajan 5: uret_sozlesmeler.py   -> 5 sozlesme (NDA, belirli/belirsiz/uzaktan is, bilgi koruma)
Kullanim: .venv/Scripts/python.exe uret_hepsi.py
"""
import os, sys, subprocess, time

BASE = os.path.dirname(os.path.abspath(__file__))
VENV_PY = os.path.join(BASE, ".venv", "Scripts", "python.exe")
BASAMAK = [
    ("AJAN 2 - Politikalar", "uret_protokoller.py"),
    ("AJAN 3 - Prosedurler", "uret_prosedurler.py"),
    ("AJAN 4 - Risk + SoA", "uret_risk_soa.py"),
    ("AJAN 5 - Sozlesmeler", "uret_sozlesmeler.py"),
]

def cizgi(t):
    print("\n" + "=" * 60)
    print(t)
    print("=" * 60)

if __name__ == "__main__":
    cizgi("BGYS 4-AJAN URETIM KOORDINATORU")
    print("Ajan 1 (Firma Bilgileri): firma_bilgileri.html -> elle doldurulur (atlandi)")
    print("Python:", VENV_PY if os.path.exists(VENV_PY) else "VENV YOK!")
    if not os.path.exists(VENV_PY):
        print("HATA: .venv bulunamadi."); sys.exit(1)

    toplam = 0; hata = 0
    for ad, script in BASAMAK:
        cizgi(ad + " -> " + script)
        t0 = time.time()
        r = subprocess.run([VENV_PY, script], cwd=BASE,
                            capture_output=True, text=True, encoding="utf-8")
        dt = time.time() - t0
        if r.returncode == 0:
            # son 3 satiri goster
            out = [l for l in r.stdout.strip().splitlines() if l.strip()]
            for l in out[-3:]:
                print("  " + l)
            print(f"  [OK] {dt:.1f}s")
            toplam += 1
        else:
            print("  STDOUT:", r.stdout.strip()[-500:])
            print("  STDERR:", r.stderr.strip()[-500:])
            print(f"  [HATA] rc={r.returncode}")
            hata += 1

    cizgi("OZET")
    print(f"Basari: {toplam}/{len(BASAMAK)} ajan")
    print(f"Hata:   {hata}")
    # klasor raporu
    for rel, label in [("DOKUMANLAR/00-POLİTİKALAR", "Politika"),
                       ("DOKUMANLAR/00-PROSEDÜRLER", "Prosedur"),
                       ("DOKUMANLAR/00-RISK-VE-SOA", "Risk+SoA"),
                       ("DOKUMANLAR/00-SOZLESMELER", "Sozlesme")]:
        p = os.path.join(BASE, rel)
        n = len([f for f in os.listdir(p) if f.endswith('.docx')]) if os.path.isdir(p) else 0
        print(f"  {label}: {n} docx -> {rel}")
    print("\nDONE." if hata == 0 else "\nBAZI AJANLAR HATA VERDİ!")
    sys.exit(1 if hata else 0)
