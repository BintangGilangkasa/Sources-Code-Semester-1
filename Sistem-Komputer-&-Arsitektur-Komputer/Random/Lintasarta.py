def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

pilih = int(input("Masukkan angka : "))

print(f"Angka yang anda pilih {pilih}, total {faktorial(pilih)}")