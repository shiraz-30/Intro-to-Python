from math import ceil
t = int(input())

for k in range(0, t):
	n, h = map(int, input().split())
	arr = list(map(int, input().split()))
	low, high = 1, max(arr)

	while low != high:
		mid = (low + high) // 2
		check = 0

		for i in arr:
			check += ceil(i / mid)
		if check <= h:
			high = mid
		else:
			low = mid + 1

	print(low)

