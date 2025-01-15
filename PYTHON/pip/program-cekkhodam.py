import random

# daftar_khodam {"khodam jin" : "Penjaga spiritual"}
daftar_khodam = {"khodam jin" : "Penjaga spiritual"}

def anak_khodam():
    nama_khodam = random.choice(list(daftar_khodam.keys()))
    deskripsi = daftar_khodam[nama_khodam]
    # return f"khodam"{import_nama} adalah {nama_khodam}: {deskripsi}
    return f"khodam {input_nama} adalah {nama_khodam}: {deskripsi}"

input_nama = input("masukan nama kamu: ")
hasil = anak_khodam()
# hasil = acek_khodam()
print(hasil)
