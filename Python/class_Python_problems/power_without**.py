"""
Q =>
Given 2 numbers a,b calculate a^b without using ** exponent operator or any 
inbuilt function.
"""

def powerIterative(a, b):
	# if not isinstance(a, int) or not isinstance(b, int): 
# isinstance(inbuilt fucntion) acts as a check that input is always int, otherwise returns none
		# print("Please enter valid inputs")
		# return None

	temp = 1
	for i in range(0, b): # also can use for i in range(0, b):
		temp *= a

	return temp

a = int(input())
b = int(input())

result = powerIterative(a, b)
print(result)

# Time Complexity => O(b)




