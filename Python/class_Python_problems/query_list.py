"""
Q => You are given an integer list of size n. After taking input of the list,
you will get another integer 'Q'. Q represents number of queries i.e.
you will get Q queries and inside each query you will get 2 numbers denoting
index of list (L) and (R). You have to print sum of elements from L to R
for each query.
(n <= 10^7) , (q <= 10^5) , (0 <= Li, Ri <= n - 1)

Example -> [1,4,6,5,7,8,3] indexed from 0 to 6
Q = 3 => 
         Li  Ri     ans ( sum of elements in the range [Li, Ri] )
         2 , 4      18
         3 , 6      23
         5 , 5      8
"""

def calculate_prefix_sum(li):
	result = []
	sum = 0
	for i in range(0, len(li)):
		sum += li[i]
		result.append(sum)
	return result

def process_query(prefix, li, l, r):
	return prefix[r] - prefix[l] + li[l]

n = int(input())
li = []
for i in range(0, n):
	x = int(input())
	li.append(x)

prefix_sum = calculate_prefix_sum(li)
q = int(input())

while (q > 0):
	l, r = input().split()
	l = int(l)
	r = int(r)

	print(process_query(prefix_sum, li, l ,r))
	q -= 1

