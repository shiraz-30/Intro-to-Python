s = "shiraz"
m = "mangat"

# Concatenation on string

print(s + m)

# Replication the string

print(s*3)

print((s+" ")*3) # with spaces in between

li = [1,2,3]
print(li*3) # it makes a new list
print(li)

print( li + [2,3,4]) # it makes a new list
print(li)

li.extend([2,3,4]) # it makes changes in original list
print(li)

li = li + [1,2,3] # this still makes a new list but assigns to li
print(li)

# indexing from left is 0,1,2...
# indexing from right is -1,-2,...

# a = " shiraz " + 2 # this gives error
a = "shiraz" + str(2)
print(a)

