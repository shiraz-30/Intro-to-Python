def fib(n):
	if n == 0 or n == 1: # base case
	    return n

	a1 = fib(n - 1) # assume this is correct value of (n - 1)th fib
	a2 = fib(n - 2) # assume this is correct value of (n - 2)th fib

	ans = a1 + a2
	return ans

print(fib(6))
   