def cek_pembagian(num):
    return num % 2 == 0 and num % 3 == 0 and num % 5 == 0

def cari_bilangan(start, end):
    return [num for num in range(start, end) if cek_pembagian(num)]

start = 1  # Mulai dari 1
end = 100  # Sebagai contoh, mencari dalam rentang 1 sampai 100

hasil = cari_bilangan(start, end)
print("Bilangan yang habis dibagi 2, 3, dan 5 antara", start, "dan", end, "adalah:", hasil)