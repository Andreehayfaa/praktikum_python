for angka in range(1, 11):
    print(angka)
    
angka = input("Masukkan sebuah angka: ")

if angka % 2 == 0:
    print(f"{angka} adalah angka genap.")
else:
    print(f"{angka} adalah angka ganjil.")

nama = input("Masukkan nama Anda: ")

# Menampilkan pesan sapaan
print(f"Halo, {nama}! Selamat belajar Python!")