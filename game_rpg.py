# Membuat Game RPG Sederhana

class karakter:
    def __init__(self, nama, hp, serangan):
        self.nama = nama
        self.hp = hp
        self.serangan = serangan

    def serang(self, target):
        print(f"{self.nama} menyerang {target.nama} dengan kekuatan {self.serangan}")
        target.hp -= self.serangan

    def terima_kerusakan(self, jumlah):
        self.hp -= jumlah
        print(f"{self.nama} menerima {jumlah} kerusakan. Sisa HP: {self.hp}")

    def masih_hidup(self):
        return self.hp > 0

class pemain(karakter):
    def sembuh(self):
        self.hp += 10
        print(f"{self.nama} menyembuhkan diri. HP sekarang: {self.hp}")
    
class musuh(karakter):
    def __init__(self, nama, hp, serangan, tipe):
        super().__init__(nama, hp, serangan)
        self.tipe = tipe

import random

# Membuat Objek Karakter
pemain = pemain("Benediktus", 100, 15)
musuh = musuh("Goblin", 80, 10, "Monster")

# Loop Pertarungan
while pemain.masih_hidup() and musuh.masih_hidup():
    aksi = input("\n Pilih aksi: (1. serang, 2. sembuh): ")

    if aksi == "1":
        pemain.serang(musuh)
    elif aksi == "2":
        pemain.sembuh()
    else:
        print("Aksi tidak valid!")
        continue

    #giliran musuh menyerang
    if musuh.masih_hidup():
        if random.random() < 0.8:
            musuh.serang(pemain)       
        else:
            print(f"{musuh.nama} gagal menyerang!")

# Hasil Akhir Pertarungan
if pemain.masih_hidup():
    print("\n 🎉 kamu menang")
else:
    print("\n 💀 kamu kalah")

