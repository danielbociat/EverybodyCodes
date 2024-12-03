f = open("everybody_codes_e2024_q01_p1.txt", "r")
str = f.read()

potions = 0

for c in str:
    if c == 'B':
        potions += 1
    if c == 'C':
        potions += 3

print(potions)