import random
SemuaData = []
n = 1000
i = 0
while i < n :
    outcome = random.randint(0,1)
    if outcome == 0 :
        toss = 'G'
        SemuaData.append(toss)
    elif outcome == 1 :
        toss = 'A'
        SemuaData.append(toss)
    i += 1


gambarTerus = 0
total_G_Streak = 0
for i in SemuaData :
    if i == 'G' :
        gambarTerus += 1
        if gambarTerus == 6 :
            total_G_Streak += 1
    else :
        gambarTerus = 0
print('The streak of 6 heads in a row is : ',total_G_Streak)
hasil_G_persen = (total_G_Streak / n) * 100
print('presentase peluang G :', hasil_G_persen)


angkaTerus = 0
total_A_Streak = 0
for j in SemuaData :
    if j == 'A' :
        angkaTerus += 1
        if angkaTerus == 6 :
            total_A_Streak += 1
    else :
        angkaTerus = 0
print('The Streak of 6 tails in a row is : ',total_A_Streak)
hasil_A_persen = (total_A_Streak / n) * 100
print ('presentase peluang A :', hasil_A_persen)


print (SemuaData)
banyak1 = (SemuaData.count("A"))
banyak2 = (SemuaData.count("G"))
print(banyak1)
print(banyak2)