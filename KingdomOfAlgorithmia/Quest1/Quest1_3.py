f = open("everybody_codes_e2024_q01_p3.txt", "r")
str = f.read()

potions = 0

def getFlagAndVal(c):
    flag = 1
    potions = 0

    if c == 'x':
        flag = 0

    if c == 'B':
        potions = 1
    if c == 'C':
        potions = 3
    if c == 'D':
        potions = 5

    return flag, potions

for i in range(0,len(str), 3):
    flag1, pot1 = getFlagAndVal(str[i])
    flag2, pot2 = getFlagAndVal(str[i+1])
    flag3, pot3 = getFlagAndVal(str[i+2])

    potions += pot1 + pot2 + pot3

    if flag1 + flag2 + flag3 == 2:
        potions += 2
    if flag1 + flag2 + flag3 == 3:
        potions += 6
    
    #print(str[i], str[i+1], str[i+2], potions)

print(potions)