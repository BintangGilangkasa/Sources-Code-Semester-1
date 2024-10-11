x = input("Apakah Hujan ? Ya/Tidak" )
if x == "Ya":
    y = input("Bawa Payung ? Ya/Tidak")
    if y == "Ya":
        print ("Mari Pulang")
    else:
        print ("Cari Barengan")
        z =input("Dapet Barengan? Ya/Tidak")
        if z == "Ya":
            print ("Mari Pulang")
        elif z == "Tidak":
            print ("Tunggu Hujan Sampe Reda/Cari Barengan")
elif x == "Tidak":
    print ("Mari Pulang")