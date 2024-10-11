import random

x = ["A", "G"]
SemuaData = []
Maybe_Angka = 0
Maybe_Gambar = 0

for i in range (1000000):
    x = ["A","G"]
    SemuaData.append(x)

for i in range (len(SemuaData)):
    if SemuaData [i:i+6] == ["A","A","A","A","A","A"]:
        Maybe_Angka += 1
    elif SemuaData [i:i+6] == ["G","G","G","G","G","G"]:
        Maybe_Gambar += 1

KemungkinanTotal = Maybe_Angka + Maybe_Gambar

print ("Kemungkinan Angka :", Maybe_Angka )
print ("Kemungkinan Gambar :", Maybe_Gambar)
print ("Hasil Akhir Presentase dari kemungkinan Angka : " + str(round(Maybe_Angka /len(SemuaData) * 100, 2)) +  "%")
print ("Hasil Akhir Presentase dari kemungkina Gambar : " + str (round(Maybe_Gambar / len(SemuaData) * 100, 2)) + "%")