import random 

x = ["A","G"]

dataSemuaAG = []
KemungkinanA = 0
KemungkinanG = 0

for i in range (100):
    z = random.randint(0,1)
    dataSemuaAG.append(x[z])

for i in range (0, len(dataSemuaAG)):
    if dataSemuaAG[i:i+2] == ["A","A"]:
        KemungkinanA +=1
    elif dataSemuaAG[i:i+2] == ["G","G"]:
        KemungkinanG +=1

KemungkinanTotal = KemungkinanA + KemungkinanG

print ("Semua total :", KemungkinanTotal)
print ("Angka : ", KemungkinanA)
print ("Gambar : ", KemungkinanG)
print ("Presentase dari kemungkinan Angka : ", str(round(KemungkinanA / len(dataSemuaAG) * 100, 3)), "%")
print ("Presentase dari kemungkina Gambar : ", str(round(KemungkinanG / len(dataSemuaAG) * 100, 3)), "%")