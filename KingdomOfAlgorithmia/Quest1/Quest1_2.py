f = open("everybody_codes_e2024_q01_p2.txt", "r")
str = f.read()

potions = 0

for i in range(0,len(str), 2):
    flag1 = False
    flag2 = False

    if str[i] == 'A':
        flag1 = True
    if str[i] == 'B':
        flag1 = True
        potions += 1
    if str[i] == 'C':
        flag1 = True
        potions += 3
    if str[i] == 'D':
        flag1 = True
        potions += 5

    if str[i+1] == 'A':
        flag2 = True
    if str[i+1] == 'B':
        flag2 = True
        potions += 1
    if str[i+1] == 'C':
        flag2 = True
        potions += 3
    if str[i+1] == 'D':
        flag2 = True
        potions += 5

    if flag1 and flag2: 
        potions+=2
    
    # print(str[i], str[i+1], potions)

print(potions)