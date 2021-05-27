"""
Example =>

n = 36
factors:-
1,36
2,18
3,12
4,9
6,6
9,4
12,3
18,2
36,1

"""
from math import floor
def check_prime(n):
	if n == 2:
		return True

	for i in range(2, floor(n**0.5) + 1):
		if (n % i) == 0:
			return False
	return True

n = int(input())

result = check_prime(n)

if (result == True):
	print("Yes it is a prime")
else:
	print("No it is not a prime")

# Time Complexity => O(n)

