first_name=("Asteria")
addition_name = first_name + (".nn")

print (addition_name)

print ("\nNormal Pyramid")
for i in range (5):
    x = "* "
    x = x*i
    print (f'{x: ^15}')

print ("\nInvert Pyramid\n")
for i in range (5):
    x = "* "
    x = x*(5-i)
    print (f'{x: ^15}')


besar_persegi = int(input("Masukan Ukuran Persegi :"))
for i in range(besar_persegi):
    for j in range(besar_persegi):
        print ("* ", end = " ")
    print()
    
        