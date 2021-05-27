words = {}
crsswrd = []
rows, columns = {},{}
n,m = map(int, input().split())

for r in range(n):
    line = list(input())
    crsswrd.append(line)
    cnt = []

    for index in range(m):
        char = line[index]
        if char == "b" or char == "r":
            cnt.append(index)
    if len(cnt) != 0:
        rows[cnt[1] - cnt[0] + 1] = [r, cnt[0]]

for c in range(m):
    cnt = []

    for index in range(n):
        row = crsswrd[index]
        char = row[c]
        if char == "b" or char == "c":
            cnt.append(index)
    if len(cnt) != 0:
        columns[cnt[1] - cnt[0] + 1] = [cnt[0], c]

for i in range(int(input())):
    word = input()
    words[len(word)] = word

lengths = set(rows.keys()) | set(columns.keys())
if lengths != set(words.keys()):
    print("Invalid")    
    exit()

crsswrd = [ ["#"]*m for i in range(n)]

for length in rows.keys():
    rc = rows[length]
    c = rc[1]
    row = crsswrd[rc[0]]
    word = words[length]
    i = 0

    for index in range(c, c + length):
        row[index] = word[i]        
        i +=1

for length in columns.keys():
    rc = columns[length]
    r = rc[0]
    row = crsswrd[rc[0]]
    c = rc[1]
    word = words[length]
    i = 0

    for index in range(r,r +length):
        row = crsswrd[index]
        char = row[c]
        if char != "#":
            if char != word[i]:
                print("Invalid")
                exit()
        row[c] = word[i]
        i += 1

for row in crsswrd:
    line = ''.join(row)
    print(line)

