# Python is an interpreted language.
# Python's interpreter reads your code line by line.
x1 = 10
y1 = 20
x2 = 31
y2 = 19
# we are supposed to calculate distance between two points
# Euclidian distance => ((x1 - x2)**2 + (y1 - y2)**2)**0.5

c = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(c)

x3 = 0
y3 = 1

d = ((x3 - x2)**2 + (y3 - y2)**2)**0.5

# Manhattan distance => |x1 - x2| + |y1 - y2|

# Functions -> DRY (Don't Repeat Yourself)
# It clubs a piece of code  instead of repeating itself again and again
"""Function is a BLOCK of organised, reusable piece of code that is used to perform 
a single, related action to improve code modularity."""
# We have based on implementable 2 types of fucntions 
""" 1)- In built function
    2)- User defined
"""
# It's similar to maths functions such as f(x),g(x),f(g(x)), etc.
""" In Python also, a function can or cannnot take an input(argument), do some 
custom computation and may or may not return an output. """

# We will create some functions 
# In Python, we can create a function like this:-
"""
def functionname (arguments<optional>):
	this will create a new block where you'll write logic

	return value <optional statement>
"""

def euclidian_dist(x1, y1, x2, y2):
	""" this functions will calculate euclidian distance
	this is a docstring
	x1 (int): x coordinate of first point
	x2 (int): x coordinate of second point
	y1 (int): y coordinate of first point
	y2 (int): y coordinate of second point
	"""
	value = (((x1 - x2)**2 + (y1 - y2)**2)**0.5)
	return value # This will be treated as a normal comment

print(euclidian_dist.__doc__)	

def manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
  
def function_without_argument():
	print("No arguments")
	return 10   

def function_without_return(x):
	y = x + 10

def function_without_argumentsandreturn():
	print("Welcome")		     

retval =  euclidian_dist(12, 1, 0, 2)
print(retval)


print(manhattan_dist(y1 = 0, y2 = 0, x1 = -1, x2 = 2))

x = function_without_argument
print(x)

function_without_return(10)
function_without_argumentsandreturn()

# docstrings -> Custom documentation that you can give for a function
# We can write the name of fucntion and get its docstrings.

"""
Required arguments =>
These are arguments passed to a function in correct positional order.
The no. of arguments passed while calling a function should be equal to 
no. of arguments defined in a function.

Keyword arguments =>
These are used when calling a function. 
You pass the parameter name and the value you want to use
def fun(a,b)
    print(a + b)
fun(b = 10, a = 3)
func(a = 20, b= 5)

Default arguments =>
By using this, we put a default value to a parameter while defining a 
function. 
While making a function call, if we don't pass that parameter, then  its's
default value is used.
fun (a = 10, b = 20)
print(a + b)
"""

# Required Argument ->

def fun(x, y):
	print("Always have fun while adding", x + y)

fun(10, 20) 

# Keyword Argument -> (These are used while calling a function always).
fun(y = 3, x = 20)

# Default Argument ->
def fun1(x, y, z = 3):
	return x + y + z

print(fun1(10, 20, 30))
print(fun1(10, 20)) 

print(fun1(z = 5, x = 3, y = 2))

#def fun2(x, y = 4, z = 3, a) # error 
#   return x*y*z*a 

#print(fun2(10, 20, 30, 40))
#print(fun2(10, 20, 20))

""" If you want to pass default arguments, then you shouldn't have any required
arguments to the right of all of them
"""

""" Variable length argument
we pass a special argument prepended by a*
"""
def sum_of_nums(x, *nums):
	i = 0
	result = 0
	while i < len(nums):
		result += nums[i]
		i += 1
	return result 
	
print(sum_of_nums(10, 20, 30, 12, 13, 2, 1, 2))

# Scope of a variable ->
""" Scope defines visibility of a variable 
Visibility means where can you use a variable.
local -> when a variable is first defined inside a function it is only locally 
visible in the function.

global -> visible everywhere until we have same variable in local scope.
"""
y = 30
x = 100 # x is global to a function

def fun():

    x = 10 # x is local to a function
    print("x from inside the fun", x)
    x = 20 # reassignment
    print("y from inside the fun", y)

fun()

print("y from outside fun", y)
print("x from outside fun", x)


