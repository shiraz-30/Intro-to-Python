n = int(input())
i = 2
sum = 1
while i <= (n**0.5):
	if (n % i == 0):
		sum += i
		if i*i != n:
			sum += n/i
	i += 1
if (sum == n):
	print("YES")
else:
	print("NO")
	