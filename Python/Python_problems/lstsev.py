n = int(input())

s = n % 10
t = (n % 100 - (s)) / 10

if t == 7:
	print(1)
else:
    print(0)
