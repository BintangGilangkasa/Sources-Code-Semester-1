print ("JAWAB SESUAI KEADAAN ANDA SEKARANG")
print ("Ya / Tidak")
print ("===================================")
print ("")
p1 = input ("Apakah Ada Seseorang yang Kamu Sukai ? ")
if p1 == "Ya":
    p2 = input ("Dia menyukai kamu balik ? ")
    if p2 == "Ya":
            print ("Jadian aja sama Dia")
    else:
        print ("Cari yang Lain")
        p3 = input ("Sudah Dapet Gantinya ? ")
        if p3 == "Ya":
            print ("Jadian aja sama Dia")
        else:
            print ("Cari yang lain lagi Sampai Dapat")          
else:
    print ("Fokus Masa Depan, Semangat<3")
print ("")
print ("=====================================")