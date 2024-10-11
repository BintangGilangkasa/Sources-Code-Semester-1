import random

tebak = int(random.randint(1,5))
i = 1
print ("Tebak")

while i <= 3:
  x = int(input())
  i = i + 1
  if tebak == x:
    print ("Anda Menang")
    break
  else:
    if i == 4:
      print ("Maaf anda kalah")
    else:
      print ("Coba lagi")
