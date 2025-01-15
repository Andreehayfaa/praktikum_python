print("|================================|")
print("|  PROGRAM MENAMPILKAN KALENDER  |")
print("|================================|")

import calendar

tahun = int(input("masukan tahun: "))
bulan = int(input("masukan bulan: "))
print()

print("hasil")
print(calendar.month(tahun, bulan))