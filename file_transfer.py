import os
import shutil

# Dosyaların bulunduğu klasör yolu ve taşımak istediğin yeni klasör yolu
kaynak_klasor = "C:/Users/sanem/Downloads/cFMD_mags/cFMD_mags/cFMD-proteins_prok"  # Buraya kaynak klasör yolunu yaz
hedef_klasor = "C:/Users/sanem/Downloads/cFMD_mags/cFMD_mags/prok_protein dosyaları"    # Buraya hedef klasör yolunu yaz

# Eğer hedef klasör yoksa oluştur
if not os.path.exists(hedef_klasor):
    os.makedirs(hedef_klasor)

# Kaynak klasördeki tüm dosyaları kontrol et
for dosya in os.listdir(kaynak_klasor):
    if dosya.endswith(".faa"):  # Sadece .faa uzantılı dosyaları seç
        tam_yol = os.path.join(kaynak_klasor, dosya)
        shutil.move(tam_yol, hedef_klasor)  # Dosyayı hedef klasöre taşı

print("FAA dosyaları yeni klasöre taşındı.")
