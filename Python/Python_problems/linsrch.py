print(1)

n = int(input())
arr = []
for i in range(n):
	arr.append(int(input()))

arr = set(arr)

q = int(input())
for k in range(q):
	x = int(input())

	if x in arr:
		print('yes')
	else:
		print('no')
		
