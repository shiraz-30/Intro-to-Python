N = int(input())
h = list(map(int, input().split()))

A = [0] * N 
for i in range(1, N):

	if (i == 1):
		A[i] = abs(h[i] - h[i - 1])
	else:
		x = A[i - 1] + abs(h[i] - h[i - 1])
		y = A[i - 2] + abs(h[i] - h[i - 2])

		A[i] = min(x, y)

print(A[-1])

