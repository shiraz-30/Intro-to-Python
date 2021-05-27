print(2)

n = int(input())
arr = []
for i in range(0,n):
	x = int(input())
	arr.append(x)

i = 1
x = 0
answer = 1

while i < len(arr):
	if arr[i] > x:
		x = arr[i]
		answer += 1
	i += 1

print(answer)
