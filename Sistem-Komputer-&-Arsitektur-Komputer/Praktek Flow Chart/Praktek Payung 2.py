print ("Jawab Sesuai Kondisimu Sekarang")
print ("Ya atau Tidak")
print ("")
x = input("Apakah Hujan ? " )
if x == "Ya":
    y = input("Bawa Payung ? ")
    if y == "Ya":
        print ("Pulang ke Rumah")
    else:
        print ("Cari Barengan")
        z = input("Dapet Barengan ? ")
        if z == "Ya":
            print ("Suruh Anterin ke Rumah")
        elif z == "Tidak":
            print ("Tunggu Hujan Sampe Reda / Makan Bakso Bersama\nGood Lucky")
elif x == "Tidak":
    print ("Pulang ke Rumah")