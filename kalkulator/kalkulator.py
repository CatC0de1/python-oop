from abc import ABC, abstractmethod
import math

# Interface untuk Kalkulator
class Kalkulator(ABC):
    
    @abstractmethod
    def operasi(self):
        pass

# Kalkulator standar
class KalkulatorStandar(Kalkulator):
    
    def operasi(self, a, b, jenis_operasi):
        if jenis_operasi == 'tambah':
            return a + b
        elif jenis_operasi == 'kurang':
            return a - b
        elif jenis_operasi == 'bagi':
            if b != 0:
                return a / b
            else:
                return "Error: Pembagi tidak boleh 0"
        else:
            return "Operasi tidak valid"

# Kalkulator scientific
class KalkulatorScientific(KalkulatorStandar):
    
    def operasi(self, a, b=None, jenis_operasi=None):
        if jenis_operasi in ['tambah', 'kurang', 'bagi']:
            return super().operasi(a, b, jenis_operasi)
        elif jenis_operasi == 'pangkat':
            return a ** b
        elif jenis_operasi == 'akar':
            return math.sqrt(a)
        else:
            return "Operasi tidak valid"

# Abstrak class untuk kalkulator bangun ruang
class KalkulatorBangunRuang(ABC):
    
    @abstractmethod
    def hitung_luas(self):
        pass

# Kalkulator untuk bangun ruang
class KalkulatorLuasBangunRuang(KalkulatorBangunRuang):
    
    def hitung_luas(self, jenis_bangun, *params):
        if jenis_bangun == 'persegi':
            sisi = params[0]
            return sisi ** 2
        elif jenis_bangun == 'lingkaran':
            radius = params[0]
            return math.pi * radius ** 2
        elif jenis_bangun == 'segitiga':
            alas, tinggi = params
            return 0.5 * alas * tinggi
        else:
            return "Jenis bangun ruang tidak valid"

# Contoh Penggunaan Kelas
# Kalkulator Standar
kalkulator1 = KalkulatorStandar()
print(f"Penjumlahan: {kalkulator1.operasi(10, 5, 'tambah')}")
print(f"Pengurangan: {kalkulator1.operasi(10, 5, 'kurang')}")
print(f"Pembagian: {kalkulator1.operasi(10, 5, 'bagi')}")

# Kalkulator Scientific
kalkulator2 = KalkulatorScientific()
print(f"Pangkat: {kalkulator2.operasi(2, 3, 'pangkat')}")
print(f"Akar: {kalkulator2.operasi(16, jenis_operasi='akar')}")

# Kalkulator Bangun Ruang
kalkulator3 = KalkulatorLuasBangunRuang()
print(f"Luas Persegi: {kalkulator3.hitung_luas('persegi', 4)}")
print(f"Luas Lingkaran: {kalkulator3.hitung_luas('lingkaran', 5)}")
print(f"Luas Segitiga: {kalkulator3.hitung_luas('segitiga', 6, 8)}")
