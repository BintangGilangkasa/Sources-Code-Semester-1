def faktorial(x):
    if x == 0:
        return 1
    else:
        return x * faktorial (x-1)
        end
pilih = int(input("Masukkan angka : "))

print (f"Angka yang anda pilih {pilih}, total {faktorial(pilih)}")
