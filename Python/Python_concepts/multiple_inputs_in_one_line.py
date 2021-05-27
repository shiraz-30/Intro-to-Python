# The user gives you 3 numbers in same line and gives you 10 such lines 

i = 10
while i > 0:
	x, y, z = input().split(",")
	print(type(x), type(y), type(z))
	x = int(x)
	y = int(y)
	z = int(z)
	print(type(x), type(y), type(z))
	print( x, y, z)
	i = i - 1
	
# Second method

x, y, z = 10, 30, 40
a = input().split(",") # this by default returns a list
m, n, l = [1, 2, 3]
print(a)
print(m, n, l)
print(x, y, z)
