n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for i in range(0, len(arr)):
    if arr[i] == k:
        count += 1

if count != 0:
    print('1')
else:
    print('-1') 
    