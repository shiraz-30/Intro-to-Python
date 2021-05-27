n = int(input())

result = 0
temp = n

while temp >= 1:
	a = temp % 10
	result = 10*result + (a)
	temp = temp // 10

if result == n:
	print("YES")
else:
    print("NO")

    	