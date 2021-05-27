# 1. Indexing of String -> Strings in python are 0-indexed
# s = "codechef"
# s[0] = 'c'
# s[1] = 'o'
# s[2] = 'o'
# s[len(s) - 1] = 'f'

# Strings are also indexed from -1 if we start from last character to the first
# s[-1] = 'f''
# s[-2] = 'e'
# s[-3] = 'h'

s = "codechef"

print(s[0],s[1], s[2], s[3], s[4], s[len(s) - 1])

print(s[-1], s[-2], s[-3], s[-4])

# ----------------------------------------------------

""" 2. Multiline strings -> we can have multiline strings using have triple quotes
Triple quotes can be triple - double quotes or triple-single quotes
"""

a = """ This is 
a multiline
string 
"""

b = ''' 
This is 
a multiline 
string '''


c = a + b
#print(a, b)

#print("Result of concatenation") #first this, then line 38 will be executed

print(b[0], b[1], b[2], b[-1], len(b))
""" 
If you have a multiline string which starts from a new line like b, then on the
0th index we will have a null character and the first character will start from 
1st index whereas if we have a string like a, which starts just after quotes then 
first character is at index 0 only.
"""

print(a[0], a[1], a[2], a[-1], len(a))

#-----------------------------------------------

"""
3. Operators on strings
"""

first = "Shiraz"
last = "Mangat"
middle = "Singh"
print(first + last) # concatenation
print(first * 3) #repetition of string

# Comparison operators
print(first == last) # -> F
print(first == middle) # -> F
print(last != first) # -> T
print(last != middle) # -> T

# Comparison based on dictionary order
print("abc" < "def") # -> According to dictionary, it is true
print("camel" > "apple") # -> True

# Based on ASCII values
print("Shiraz" == "shiraz") # -> False
print("Shiraz" > "shiraz") # -> False

print("aa" < "aab") # -> True (same as in dictionary)

#Membership operator 
print("a" in first) # -> True
print("aa" in first) # -> False
print("ab" not in first) # -> True

# ----------------------------------
"""
4. Mutability in strings
"""
li = [1,2,3,4,5]
li[2] = 22 # this will work
#lists are mutable
# st = "codechef"
# st[2] = 'r' #this won't work 
#strings aren't mutable, we can reassign them
print(li)

# --------------------------------------------




# 5. Formatting strings :- (String interpolation)

""" You can add a variable inside a string in runtime without using concatenation.
In python we can do string formatting in multiple ways.

Way no. 1 -> using % operator

%s, %d, %f are called format specifier 
%s -> string
%d -> integer
%f -> float
%b -> binary
%r -> boolean
"""
name = "Shiraz"
year = 2021
happiness = 100.0
greeting = "Hello, %s to %d and we hope your happiness matric is %f" % (name, year, happiness)
print(greeting)

"""
Way no. 2 -> Using format function
"""
greeting = "Hello, {x}".format(x = name)
print(greeting)
greeting = "Hello, {x} to {y}".format(x = name, y = year)
print(greeting)
greeting = "Hello, {} to {} and we hope your happiness matric is {}".format(name,year,happiness)
print(greeting)
print(format(12, "b"))

""" 
Way no.3 -> F-strings
"""
binary = 0b101
greeting = f"Hello, {name} {~binary:0b} to {year} and we hope your happiness matric is {happiness}"
print(greeting)

# ---------------------------------------------------------
# 6. Slicing in python
"""
Slicing means extracting a substring or a part of a string.
"""

l = [1,2,3,4,5,6,7,8,9]
s = "Codechef"

print(l[0:5]) # extract 0,1,2,3,4 indexes
print(s[1:3]) # extract 1,2 indexes
print(l[0:5:2]) # made jumps of 2
print(l[1:]) # will give you everything from index 1 to last
print(s[-2:]) # last 2 elements
print(l[:5]) # first n elements
print(l[::2]) # will pick every 2nd element

# we can also assign a list by using slicing
l[1:5] = [22,33,44,55]
print(l) 


