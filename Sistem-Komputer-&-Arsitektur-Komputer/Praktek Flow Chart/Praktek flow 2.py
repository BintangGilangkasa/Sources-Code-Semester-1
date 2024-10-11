print ("Jawablah Pertanyaan Dibawah ini dengan")
print ("Yes // No")
print ("")
print ("======================================")
print ("")
tanya1 = input("Apakah Kamu Merasa Lapar ? ")
if tanya1 == "Yes":
    print ("Mau Sarapan Apa ? ")
    tanya2 = input("Seadanya ? ")
    if tanya2 == "Yes":
        tanya3 = input ("Mau Masak Sendiri ? ")
        if tanya3 == "Yes":
            print ("Ayo Masak")
        elif tanya3 == "No":
            print ("Ayo Beli ke Warung")
    elif tanya2 == "No":
        print ("Mau Makan Bubur Ayam")
elif tanya1 == "No":
    print ("Yang Bener")
    tanya11 = input ("Ga Nyeselkan nanti ? ")
    if tanya11 == "Yes":
        print ("Ga tau mikir-mikir dulu")
    elif tanya11 == "No":
        print ("Baiklah kalau begitu")
print ("")
print ("=======================================")