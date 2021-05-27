n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

def rec(n):
    if n == 1:
        print(arr[0])
    else:
        arr.sort()
        x = arr[0]
        y = arr[1]
        arr.pop(0)
        arr.pop(0)
        cnt = (3*x + 2*y) % 100
        arr.append(cnt)
        rec(len(arr))

rec(n)
 
