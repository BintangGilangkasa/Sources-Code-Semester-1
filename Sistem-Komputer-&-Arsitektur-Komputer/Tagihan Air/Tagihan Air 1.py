#MEMBUAT TAGIHAN AIR 

x = int(input("Masukan tagihan anda ^3 : "))
if x >= 16:
    print ("Jumlah tagihan anda masuk level 3")
    jml_tagihan3 = (x-15)*5000 + 20000
    print ("Ini total tagihan anda : ", jml_tagihan3)

elif x >= 11:
    print ("Jumlah tagihan anda masuk level 2")
    jml_tagihan2 = (x-10)*2000 + 10000
    print ("Ini total tagihan anda : ", jml_tagihan2)

else:
    print ("Jumlah tagihan anda masuk level 1")
    jml_tagihan1 = x * 1000
    print ("Ini total tagihan anda : ", jml_tagihan1)