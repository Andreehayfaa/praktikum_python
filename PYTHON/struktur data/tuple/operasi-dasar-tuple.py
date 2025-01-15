# Length - menghitung panjang tuple
panjangtuple = (1, 2, 3, 4)
print("Length:", len(panjangtuple))

# Concatenation - menggabungkan dua tuple
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
combined_tup = tup1 + tup2
print("Concatention:", combined_tup)

# Repetition - mengulang element tuple
repetitiontup = ('halo!') * 4
print("Repetition:", repetitiontup)

# Membership - memeriksa apakah element ada di dalam tuple
member = 2 in (1, 2, 3)
print("Membership:", member)

# Iteration - melakukan iterasi pada tuple
for x in (1, 2, 3):
    print(x, end=' ')

# Indexing - mengakses element berdasarkan indeksnya
T = ('C++', 'Java', 'Python')
print(T[2])
print(T[-2])

# Slicing - mengambil bagian dari index tertentu
tuple = ('charger', 'ponsel', 'headphone')
print(tuple[1:])