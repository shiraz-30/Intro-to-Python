import array

x = array.array('i', [1,2,3,4,5,6])

for i in range(0, len(x)):
	print(x[i])

print(x, type(x), len(x))

import array as arr 

x = arr.array('i', [1,2,3,4,5,6])

for i in range(0, len(x)):
	print(x[i])

print(x, type(x), len(x))

"""
Types for an array is derived from C language

i -> integer -> 2 byte
f -> float -> decimal -> 4 byte
d -> double -> decimal -> 8 byte
"""
x[0] = 0 # updation
x.append(-3) # appending
x.insert(1, 99) # insertion
for i in range(0, len(x)):
	print(x[i])

# slicing

y = x[1:5]
for i in range(0, len(y)):
	print(y[i])

