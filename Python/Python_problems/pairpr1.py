def all_prime_numbers_less_than_n (n, arr):
	arr[0] = False
	arr[1] = False

	for i in range(2, n + 1):
		arr[i] = True

	p = 2

	while (p * p <= n):
		if (arr[p] == True):
			i = p * p

			while (i <= n):
				arr[i] = False
				i += p
		p += 1

def pair_of_primes(n):
	arr = [0] * (n + 1)
	all_prime_numbers_less_than_n(n, arr)

	for i in range(0, n):
		if (arr[i] and arr[n - i]):
			print(i, (n - i))

			return

	for i in range(0, n):
		if not (arr[i] and arr[n - i]):
			print(-1, -1)

			return

t = int(input())

for i in range(0, t):
	n = int(input())

	pair_of_primes(n)
