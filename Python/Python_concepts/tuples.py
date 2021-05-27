# Tuples are immutable collection of objects.

tup = (1,2,3,"Shiraz", False, 5.67)
print(tup)
"""
Tuples are immutable
tup[0] = 11 -> this will give error
"""
# how to access any individual element of a tuple?
print(tup[0], tup[1]) # tuples are 0 based indexed

# Differences with lists?
"""
1) we can update any individual element of a list but we can't do the same 
with tuples.
2) We can't delete any element in tuple as they are immutable.
"""
# Operations in Tuples
print(tup * 4) # repetition
print(tup)
print(3 in tup)


t1 = (1,2,3)
t2 = (4,5,6)
print(t1 + t2) # concatenation
print(t1)
print(t2)

print(tup[1:3]) # slicing

# Use of tuple =>
def test(): # we want to return multiple values from this function
    return 1,2,3,"Chd", 45.6

x = test()
print(x)
print(type(x))

# change tuple to a list
print(list(x))

# change list to tuple
y = [1,2,3,"Shiraz"]
print(tuple(y))


