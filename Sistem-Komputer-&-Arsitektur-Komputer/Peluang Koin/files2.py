#Fungsi untuk mengecek apakah bilangan prima
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 1:
            return False
    return True

#Fungsi mencari bilangan prima dari 1-maksimal nomer yang dimasukkan
def find_primes(start,end):
    prime_list = [] #bilangan ditampung disini
    for n in range(start, end + 1):
        if is_prime(n):
            prime_list.append(n)
    return prime_list

#Variabel untuk mengetahui rentang angka
start_range = 1
end_range = 100

#memanggil fungsi menyimpan hasil  dari variabel
primes = find_primes(start_range, end_range)

#Mencetal hasil bilangan prima
print (f'Bilangan prima antara {start_range} dan {end_range} adalah {primes}')