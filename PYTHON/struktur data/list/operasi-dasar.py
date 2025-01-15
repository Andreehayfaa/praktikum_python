# Length - menghitung panjang list
panjanglist = [1, 2, 3, 4]
print("Length:", len(panjanglist))

# Concatenation - menggabungkan dua list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_lest = list1 + list2
print("Concatention:", combined_lest)

# Repetition - mengulang element list
repetitionlist = ['halo!'] * 4
print("Repetition:", repetitionlist)

# Membership - memeriksa apakah element ada di dalam list
member = 2 in [1, 2, 3]
print("Membership:", member)

# Iteration - melakukan iterasi pada list
for x in [1, 2, 3]:
    print(x, end='')

# Indexing - mengakses element berdasarkan indeksnya
L = ['C++', 'Java', 'Python']
print(L[2])
print(L[-2])

# Slicing - mengambil bagian dari index tertentu
List = ['charger', 'ponsel', 'headphone']
print(List[1:])