#Membuat Tagihan Air 2
x = int(input("Masukan Penggunaan air anda : "))
jml_tagihan1 = x * 1000 
jml_tagihan2 = (x-10) * 2000
jml_tagihan3 = (x-15) * 5000

if x >= 16 :
    print ("Tagihan anda masuk level 3")
    print ("Total tagihan anda :", jml_tagihan3 + (10*1000) + (5*2000))
elif x >= 11 :
    print ("Tagihan anda masuk level 2")
    print ("Total tagihan anda :", jml_tagihan2 + (5*2000))
else:
    print ("Tagihan anda masuk level 1")  
    print ("Total tagihan anda :", jml_tagihan1)