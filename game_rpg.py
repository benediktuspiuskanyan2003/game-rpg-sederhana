# Membuat Game RPG Sederhana

class Character:
    def __init__(self, nama, hp, serangan):
        self.name = nama
        self.health = hp
        self.attack_power = serangan

    def attack(self, target):
        print(f"{self.nama} menyerang {target.nama} dengan kekuatan {self.serangan}")
        target.hp -= self.serangan

    def terima_kerusakan(self, jumlah):
        self.hp -= jumlah
        print(f"{self.nama} menerima {jumlah} kerusakan. Sisa HP: {self.hp}")

    def masih_hidup(self):
        return self.hp > 0

