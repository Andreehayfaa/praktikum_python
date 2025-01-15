# CONTOH FOR LOOPING 1
angka = [1,2,3,4,5]
for x in angka:
    print(x)

# CONTOH FOR LOOPING 2
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
    print("Saya suka makan", makanan)

# CONTOH FOR LOOPING 3
for i in range(5):
    print("Hallo Dunia")

# CONTOH FOR LOOPING 4
print("tabel perkalian:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}", end='\t')
    print()
