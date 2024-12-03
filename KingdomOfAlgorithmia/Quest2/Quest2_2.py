f = open("everybody_codes_e2024_q02_p2.txt", "r")
str = f.read()
# str = """WORDS:THE,OWE,MES,ROD,HER,QAQ

# AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
# THE FLAME SHIELDED THE HEART OF THE KINGS
# POWE PO WER P OWE R
# THERE IS THE END
# QAQAQ """


#str = "AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE"
lines = str.split('\n')
runes = lines[0].split(':')[1].split(',')

runes_rev = []
for rune in runes:
    runes_rev.append(rune)
    if rune != rune[::-1]:
        runes_rev.append(rune[::-1])

print(runes)

counter = 0
for line in lines[1:]:
    #line = "".join(line.split())

    ln = len(line)
    visited = [0] * ln

    for rune in runes_rev:
        rn = len(rune)

        for i in range(ln):
            flag = True

            if i + rn <= ln:
                for j in range(rn):
                    if rune[j] != line[i+j]:
                        flag = False
                        break

                if flag:
                    for idx in range(i, i+rn):
                        visited[idx] = 1


            

    v = sum(visited)
    counter += v
    print(visited)
    print(line)
    print(v)

print(counter)