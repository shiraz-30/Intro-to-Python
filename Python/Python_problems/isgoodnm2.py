n = int(input())
sum = 1

for i in range(2, int(n**0.5) + 1):
	if (n % i == 0):
		sum += i
		sum += n//i

if n**0.5 is int:
    sum -= n**0.5

if sum == n:
	print("YES")
else:
	 print("NO")
