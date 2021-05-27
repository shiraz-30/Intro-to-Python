def is_valid(s):
    snake = 0
    if s.count('T') != s.count('H'):
        return "Invalid"
    for i in s:
        if i=='H' and snake==0:
            snake+= 1
        elif i=='T':
            snake-=1
        elif i=='.':
            continue
        else:
            return "Invalid"
            
    return "Valid"

for i in range(int(input())):
    l = int(input())
    s = input()
    print(is_valid(s))