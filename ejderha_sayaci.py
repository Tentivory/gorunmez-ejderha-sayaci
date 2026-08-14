#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÖRÜNMEZ EJDERHA SAYACI v1.0
Evrenin en ciddi bilimsel aracı.
Görünmez ejderhaları kuantum titreşimleri ve rastgele sayı üreteçleriyle tespit eder.
"""

import random
import time
import sys

def kuantum_titresim_olc():
    """Kuantum alanından görünmez ejderha titreşimlerini ölçer."""
    return random.uniform(0.0001, 0.9999)

def felsefi_aciklama(sayi):
    aciklamalar = [
        f"{sayi} adet görünmez ejderha tespit edildi. Bunlar aslında var olmayan varlıklardır ama varlıkları yokluklarıyla kanıtlanmıştır.",
        f"Ölçüm sonucu: {sayi}. Heisenberg belirsizlik ilkesine göre ejderhalar hem var hem yoktur.",
        f"{sayi} ejderha bulundu. Onlar sizi izliyor ama siz onları göremiyorsunuz. Bu normaldir.",
        f"Kritik uyarı: {sayi} görünmez ejderha odada. Lütfen panik yapmayın, onlar zaten panik yapıyor.",
        f"Bilimsel gerçek: {sayi} ejderha. Varlıkları, yokluklarının kanıtıdır. Descartes yanılmış olabilir."
    ]
    return random.choice(aciklamalar)

def ana_sayim():
    print("=" * 60)
    print("  GÖRÜNMEZ EJDERHA SAYACI - RESMİ BİLİMSEL ARAÇ  ")
    print("=" * 60)
    print("\nKuantum sensörleri kalibre ediliyor...")
    time.sleep(1.5)
    print("Görünmezlik alanı taranıyor...")
    time.sleep(1.2)
    print("Ejderha aurası aranıyor...")
    time.sleep(1.0)
    
    titresim = kuantum_titresim_olc()
    ejderha_sayisi = int(titresim * 13)  # 0-12 arası, çünkü 13 uğursuz
    
    print("\n" + "-" * 60)
    print(f"ÖLÇÜM SONUCU: {ejderha_sayisi} GÖRÜNMEZ EJDERHA")
    print("-" * 60)
    print("\n" + felsefi_aciklama(ejderha_sayisi))
    print("\nNot: Bu sonuçlar %100 doğrudur çünkü rastgele üretilmiştir.")
    print("Bilim böyle ilerler.")
    print("=" * 60)

if __name__ == "__main__":
    try:
        ana_sayim()
    except KeyboardInterrupt:
        print("\n\nKullanıcı görünmez ejderhalardan korktu ve programı durdurdu.")
        print("Bu da bir bilimsel veridir.")
        sys.exit(0)
