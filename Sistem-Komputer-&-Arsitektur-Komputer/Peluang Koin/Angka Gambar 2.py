import random

x = ["A", "G"]
SemuaData = []
Kemungkinan_Angka = 0
Kemungkinan_Gambar = 0

for i in range (1000000):
    p = random.randint(0,1)
    SemuaData.append(x[p])

for i in range (len(SemuaData)):
    if SemuaData [i:i+6] == ["A","A","A","A","A","A"]:
        Kemungkinan_Angka += 1
    elif SemuaData [i:i+6] == ["G","G","G","G","G","G"]:
        Kemungkinan_Gambar += 1

KemungkinanTotal = Kemungkinan_Angka + Kemungkinan_Gambar

print ("Total kemungkinan Angka & Gambar:", KemungkinanTotal)
print ("Keluar Angka :", Kemungkinan_Angka )
print ("Keluar Gambar :", Kemungkinan_Gambar)
print ("Presentase dari kemungkinan Angka : ", str(round(Kemungkinan_Angka / len(SemuaData) * 100, 2)), "%")
print ("Presentase dari kemungkina Gambar : ", str(round(Kemungkinan_Gambar / len(SemuaData) * 100, 2)), "%")