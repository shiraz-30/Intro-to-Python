n = int(input())
arr = map(int ,input().split())
s = sorted(arr)

x = n
print(x)
smallest = s[0]
for i in range(1, n):
	if s[i] != smallest:
		smallest = s[i]
		print(x - i)
