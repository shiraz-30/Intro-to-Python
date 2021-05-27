print(2)

n = int(input())
arr = []
sq = 0

for i in range(n):
	x = int(input())
	arr.append(x)

	sq += x**2
add_all = sum(arr)

print(int(((add_all**2) - sq) /2 ))
