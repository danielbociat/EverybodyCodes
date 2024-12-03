f = open("everybody_codes_e2024_q02_p3.txt", "r")
str = f.read()
# str = """WORDS:THE,OWE,MES,ROD,RODEO

# HELWORLT
# ENIGWDXL
# TRODEOAL"""

lines = str.split('\n')
runes = lines[0].split(':')[1].split(',')

runes_rev = []
for rune in runes:
    runes_rev.append(rune)
    if rune != rune[::-1]:
        runes_rev.append(rune[::-1])

# print(runes_rev)

counter = 0

# print(lines[2:])

visited = list()
for i in range(len(lines[2:])):
    visited.append([0] * len(lines[2]))

lines = lines[2:]
no_lines = len(lines)
ln = len(lines[2])

for k in range(no_lines):
    line = lines[k]

    for rune in runes_rev:
        for i in range(ln):
            rn = len(rune)
            flag = True

            for j in range(rn):
                if rune[j] != line[(i+j) % ln]:
                    flag = False
                    break

            if flag:
                # print(k, i, rune, ln, rn)
                for idx in range(i, i+rn):
                    # print(k, idx%ln)
                    visited[k][idx%ln] = 1
                #print(visited[k])

for k in range(ln):
    for rune in runes_rev:
        rn = len(rune)
        for i in range(no_lines):

            if(i + rn <= no_lines):
                flag = True

                for j in range(rn):
                    if rune[j] != lines[(i+j) % no_lines][k]:
                        flag = False
                        break
                    
                if flag:
                        for idx in range(i, i+rn):
                            visited[idx%no_lines][k] = 1


counter = 0
for line_vis in visited:
    # print(line_vis)
    counter += sum(line_vis)
print(counter)