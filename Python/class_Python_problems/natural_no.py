# Q => Given a number n, print all natural numbers till n. 
# Code the solution recursively.

def print_increasing(n):
	if (n == 1):
		print(1)
		return

		# Recursive Assumption
	print_increasing (n - 1)
	print(n)
	return

n = int(input())
print_increasing(n)


# Q => Given a number n, print all natural no.s till n in decreasing order.
# Code the solution recursively.

def print_decreasing(n):
	if (n == 1):
		print(1)
		return

	print(n)
	print_decreasing (n - 1)
	return

n = int(input())
print_decreasing(n)

