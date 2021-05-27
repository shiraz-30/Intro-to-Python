# How to initialise a list??

a = []
b = [1, 2, 3]
c = [1, 'a', "string", 4.5, 2+3j, False, -89, True]
print(a)
print(b)
print(c)

# How to add elements in the list??

b.append(33)
c.append(29)

# How is indexing done in lists of python??
# -> same like flowcharts i.e. 0 based indexing

print(c[0], c[1], c[2])

# How can we take input from user and add in list??

n = 10
arr = []
while n > 0:
	x = input()
	arr.append(x)
	n = n - 1

print(arr)

# Are lists mutable?? i.e. can you update any element?? Yes!!!

c[0] = "Shiraz"
print(c)

# how can we manually print list??
i = 0
while i < len(c):
	print(c[i], end = " ")
	i = i + 1

# Can we remove the elements from last line just like we added at last line?? Yes!!

c.pop()
print(c)

#  --------------------------------------------------------

# Google the below functions to use them.

# Can we append multiple elements at once? Yes!

c.extend([23, 'true', False, 45, -9])
print(c)

# How to remove from any specific index??

c.pop(3)
print(c)

# Can we remove any specific element??

c.remove(45)
print(c)

# Can we add any element at a specific index?? Yes!

c.insert(1, "Mangat")
print(c)

# Can we remove all the elements at once?? Yes!

c.clear()
print(c)

# Can we reverse the list?? Yes!
c.reverse()
print(c)

# Use help(list) to get all knowledge about functions from the python3 console.

