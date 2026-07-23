# -*- coding: utf-8 -*-
"""
AJAN 1 -> DIGER AJANLAR VERI AKSII
firma_bilgileri.html'deki 26 alani okur, docx'lerdeki {{firma_unvan}} /
{{firma_adresi}} yer tutucularini gercek degerlerle degistirir.
Kullanim: .venv/Scripts/python.exe enjekte_firma.py
Not: firma_bilgileri.html localStorage'da tutulur; bu script HTML'den form
degerlerini parse eder (gercek degerler icin tarayicida kaydedilmis hali okunur).
"""
import os, re
from docx import Document
from docx.oxml.ns import qn

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "firma_bilgileri.html")

# firma_bilgileri.html form id -> adres bicimi
def load_firma():
    """HTML'deki input (value=) ve textarea iceriginden deger oku."""
    with open(HTML, encoding="utf-8") as f:
        src = f.read()
    data = {}
    # textarea: <textarea id='x' ...>DEGER</textarea>
    for mt in re.finditer(r"<textarea\s+id='([^']+)'[^>]*>(.*?)</textarea>", src, re.S):
        fid, val = mt.group(1), mt.group(2)
        if fid != "toast":
            data[fid] = val.strip()
    # input: <input id='x' ... value='y' ...>  (placeholder icindeki ' onemli degil)
    for mi in re.finditer(r"<input\b[^>]*\bid='([^']+)'[^>]*?>", src):
        fid = mi.group(1)
        if fid == "toast":
            continue
        tag = mi.group(0)
        mv = re.search(r"\bvalue='([^']*)'", tag)
        val = mv.group(1).strip() if mv else ""
        # textarea zaten eklenmisse ezme
        if fid not in data or not data[fid]:
            data[fid] = val
    return data

def adres_birlesik(d):
    parcalar = [d.get("adres",""), d.get("ilce",""), d.get("il",""),
                d.get("postaKodu",""), d.get("ulke","Türkiye")]
    return ", ".join(p for p in parcalar if p)

def replace_in_doc(path, unvan, adres):
    d = Document(path)
    cnt = 0
    # tablolar (baslik hucreleri)
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    for r in p.runs:
                        if "{{firma_unvan}}" in r.text:
                            r.text = r.text.replace("{{firma_unvan}}", unvan); cnt += 1
                        if "{{firma_adresi}}" in r.text:
                            r.text = r.text.replace("{{firma_adresi}}", adres); cnt += 1
    # govde paragraflari
    for p in d.paragraphs:
        for r in p.runs:
            if "{{firma_unvan}}" in r.text:
                r.text = r.text.replace("{{firma_unvan}}", unvan); cnt += 1
            if "{{firma_adresi}}" in r.text:
                r.text = r.text.replace("{{firma_adresi}}", adres); cnt += 1
    if cnt:
        d.save(path)
    return cnt

def main():
    d = load_firma()
    unvan = d.get("unvan","")
    adres = adres_birlesik(d)
    print("Firma:", unvan or "(BOS)")
    print("Adres:", adres or "(BOS)")
    if not unvan:
        print("UYARI: firma_bilgileri.html'de 'unvan' bos. Tarayicida forma deger girip kaydedin,")
        print("        sonra bu scripti calistirin. (Yer tutucular oldugu gibi birakildi.)")
        return
    folders = [
        os.path.join(BASE, "DOKUMANLAR", "00-POLİTİKALAR"),
        os.path.join(BASE, "DOKUMANLAR", "00-PROSEDÜRLER"),
        os.path.join(BASE, "DOKUMANLAR", "00-RISK-VE-SOA"),
    ]
    total = 0
    for fol in folders:
        if not os.path.isdir(fol): continue
        for f in os.listdir(fol):
            if not f.endswith(".docx"): continue
            n = replace_in_doc(os.path.join(fol, f), unvan, adres)
            if n:
                total += 1
                print(f"  guncellendi: {f} ({n} yer tutucu)")
    print(f"\nTOPLAM: {total} dosya guncellendi.")

if __name__ == "__main__":
    main()
