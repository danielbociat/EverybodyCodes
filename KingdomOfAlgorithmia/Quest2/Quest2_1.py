f = open("everybody_codes_e2024_q02_p1.txt", "r")
str = f.read()



#str = "AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE"
list_of_string = str.split()
runes = list_of_string[0].split(':')[1].split(',')

words = "".join(list_of_string[1:])

print(words)

counter = 0



l = len(words)
for i in range(l):
    for rune in runes:
        flag = True

        for j in range(len(rune)):
            if i+j >= l or rune[j] != words[i+j]:
                flag = False
                break
        if flag:
            counter += 1

print(counter)