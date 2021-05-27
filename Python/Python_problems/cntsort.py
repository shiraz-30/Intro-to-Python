t = int(input())

for i in range(0, t):
	n = int(input())

	A = list(map(int, input().split()))

	x = sorted(A)
	print(*x)
