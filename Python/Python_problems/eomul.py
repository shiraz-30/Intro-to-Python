n = int(input())

if n % 3 != 0:
	print('-1')

elif n % 3 == 0 and (n/3) % 2 == 0:
	print('0')

else:
	print('1')