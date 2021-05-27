""" 
Q => You are given a list of size n, where all the elements of the list are
integers. Every element in the list is present twice except for one special
element. Find the special element. (n <= 10^6)
(We can't use any extra data structure and also can't use any internal function)

Test case -> [1,2,1,3,2] -> Ans => 3
"""

def findUnique(li):
	x = 0
	for i in range(0, len(li)):
		x ^= li[i]
	return x

n = int(input())
li = []
for i in range(0, n):
	element = int(input())
	li.append(element)

print("The unique element in the above list is", findUnique(li))

