import time
import os

class Lab:
  def __init__(self, nama_lab):
    self.nama_lab = nama_lab
    self.set_komputer_list = []
    self.pengguna_lab_list = []
    self.id_gen = 0
    self.on = True

  def first_admin(self):
    print("Aplikasi ini memerlukan akses admin untuk pertama kalinya...")
    time.sleep(3)
    os.system('cls')
    nama_pengguna = input("Masukkan nama admin: ")
    sandi_pengguna = input("Masukkan sandi admin: ")
    jabatan = 'admin'

    pengguna_lab = PenggunaLab(nama_pengguna, jabatan, sandi_pengguna)
    self.add_pengguna(pengguna_lab)

  def menu(self):
    self.on = True
    while self.on:
      os.system('cls')
      print(f"\n=== Selamat Datang di {self.nama_lab} ===")
      print('1. Lihat daftar komputer')
      print('2. Lihat daftar pengguna')
      print('3. Tambah komputer')
      print('4. Tambah pengguna')
      print('5. Pakai komputer')
      print('6. Menyudahi pemakaian komputer')
      print('0. Keluar')

      pilihan = input('Masukan pilihan (1-6): ')
      if pilihan == '1':
        self.tampilkan_komputer()
      elif pilihan == '2':
        self.tampilkan_pengguna()
      elif pilihan == '3':
        self.tambah_komputer()
      elif pilihan == '4':
        self.tambah_pengguna()
      elif pilihan == '5':
        self.pakai_komputer()
      elif pilihan == '6':
        self.menyudahi_komputer()
      elif pilihan == '0':
        print("Keluar dari aplikasi.")
        self.on = False
      else:
        print('Pilihan tidak valid!')
        time.sleep(2)

  def add_set_komputer(self, set_komputer):
    self.set_komputer_list.append(set_komputer)
    print(f"Komputer {set_komputer.komputer} telah ditambahkan ke {self.nama_lab}.")
    time.sleep(2)

  def add_pengguna(self, pengguna):
    self.pengguna_lab_list.append(pengguna)
    print(f"Pengguna {pengguna.nama} telah terdaftar di {self.nama_lab}.")
    time.sleep(2)

  def tambah_komputer(self):
    os.system('cls')
    print("Autentikasi oleh moderator (admin, dosen, tenaga didik) diperlukan untuk menambahkan komputer.")
    nama_admin = input('Masukkan nama moderator: ')
    sandi_admin = input('Masukkan sandi: ')

    admin_ditemukan = next((pengguna for pengguna in self.pengguna_lab_list 
    if pengguna.nama == nama_admin and pengguna.sandi == sandi_admin), None)
        
    if admin_ditemukan:
      os.system('cls')
      print('Autentikasi berhasil.')
      time.sleep(2)
      os.system('cls')
      id_komputer = str(self.id_gen).zfill(2)
      komputer = input('Masukkan nama komputer: ')
      keyboard = input('Masukkan nama keyboard: ')
      mouse = input('Masukkan nama mouse: ')
      set_komputer = SetKomputer(id_komputer, komputer, keyboard, mouse)
      self.add_set_komputer(set_komputer)
      self.id_gen += 1
    else:
      print('Nama atau sandi salah!')
      time.sleep(2)

  def tambah_pengguna(self):
    os.system('cls')
    nama_pengguna = input('Masukkan nama pengguna: ')
    print('Pilihan jabatan:')
    print('1. Mahasiswa')
    print('2. Dosen')
    print('3. Tenaga didik')
    pilihan_jabatan = input('Masukkan pilihan: ')
        
    sandi_pengguna = None
    jabatan = None
        
    if pilihan_jabatan == '1':
      jabatan = 'mahasiswa'
    elif pilihan_jabatan == '2':
      jabatan = 'dosen'
      os.system('cls')
      print('Autentikasi admin diperlukan untuk menambahkan dosen.')
      if not self.auth_admin():
        return
        sandi_pengguna = input('Masukkan sandi pengguna: ')
    elif pilihan_jabatan == '3':
      jabatan = 'tenaga didik'
      os.system('cls')
      print('Autentikasi admin diperlukan untuk menambahkan tenaga didik.')
      if not self.auth_admin():
        return
        sandi_pengguna = input('Masukkan sandi pengguna: ')
      else:
        print('Pilihan tidak valid!')
        time.sleep(2)
        return
        
      pengguna_lab = PenggunaLab(nama_pengguna, jabatan, sandi_pengguna)
      self.add_pengguna(pengguna_lab)

  def tampilkan_komputer(self):
    os.system('cls')
    if not self.set_komputer_list:
      print('Belum ada komputer yang terdaftar.')
      time.sleep(2)
      return
        
      print(f"\nDaftar komputer di {self.nama_lab}:")
      for index, komputer in enumerate(self.set_komputer_list):
        print(f"{index + 1}. ID: {komputer.id_komputer}")
        print(f"   Komputer: {komputer.komputer}")
        print(f"   Keyboard: {komputer.keyboard}")
        print(f"   Mouse: {komputer.mouse}")
        status = 'Free' if komputer.status else 'Busy'
        print(f"   Status: {status}")
        
      input('\nTekan enter untuk kembali ke menu...')

  def tampilkan_pengguna(self):
    os.system('cls')
    print(f"\nDaftar pengguna di {self.nama_lab}:")
    for index, pengguna in enumerate(self.pengguna_lab_list):
      print(f"{index + 1}. Nama: {pengguna.nama} ({pengguna.jabatan})")
    input('\nTekan enter untuk kembali ke menu...')

  def auth_admin(self):
    nama_admin = input('Masukkan nama admin: ')
    sandi_admin = input('Masukkan sandi: ')

    admin_ditemukan = next((pengguna for pengguna in self.pengguna_lab_list 
    if pengguna.nama == nama_admin and pengguna.sandi == sandi_admin and pengguna.jabatan == 'admin'), None)
        
    if admin_ditemukan:
      os.system('cls')
      print('Autentikasi admin berhasil.')
      time.sleep(2)
      return True
    else:
      os.system('cls')
      print('Nama atau sandi admin salah!')
      time.sleep(2)
      return False

  def pakai_komputer(self):
    os.system('cls')
        
    cari_nama = input('Masukkan nama pengguna: ')
    nama_ditemukan = next((pengguna for pengguna in self.pengguna_lab_list if pengguna.nama == cari_nama), None)
    if not nama_ditemukan:
      print(f'Pengguna dengan nama {cari_nama} tidak ditemukan.')
      time.sleep(2)
      return

    cari_id = input('Masukkan ID komputer untuk dipakai: ')
    komputer_ditemukan = next((komputer for komputer in self.set_komputer_list if komputer.id_komputer == cari_id), None)
    if not komputer_ditemukan:
      print(f'Komputer dengan ID {cari_id} tidak ditemukan.')
      time.sleep(2)
      return
        
    if not komputer_ditemukan.status:
      print(f'Komputer dengan ID {cari_id} sedang dipakai.')
      time.sleep(2)
      return

    print(f'Komputer dengan ID {cari_id} berhasil dipakai.')
    komputer_ditemukan.status = False
    time.sleep(2)

  def menyudahi_komputer(self):
    os.system('cls')

    cari_id = input('Masukkan ID komputer untuk disudahi: ')
    komputer_ditemukan = next((komputer for komputer in self.set_komputer_list if komputer.id_komputer == cari_id), None)
    if komputer_ditemukan and not komputer_ditemukan.status:
      print(f'Komputer dengan ID {cari_id} berhasil dimatikan.')
      time.sleep(2)
      komputer_ditemukan.status = True
    else:
      print(f'Komputer dengan ID {cari_id} tidak sedang dipakai.')
      time.sleep(2)


class SetKomputer:
  def __init__(self, id_komputer, komputer, keyboard, mouse):
    self.id_komputer = id_komputer
    self.komputer = komputer
    self.keyboard = keyboard
    self.mouse = mouse
    self.status = True


class PenggunaLab:
  def __init__(self, nama, jabatan, sandi):
    self.nama = nama
    self.jabatan = jabatan
    self.sandi = sandi


lab_komputer = Lab("Lab Komputer")
lab_komputer.first_admin()
lab_komputer.menu()