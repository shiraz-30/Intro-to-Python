# This will be a basic calculator application
# We will make the calculator that will prompt the menu again and again
print("Welcome to the calculator application")
menu = """
Please choose one of the option from the below available operations:
a) For addition press          +
b) For subtraction press       -
c) For multiplication press    *
d) For division press          /
e) For exponent press          **
f) For remainder press         %
"""
while True:
	print(menu)
	operator = input()
	print("Please enter two valid inputs to perform", operator, "operation")
	a = int(input())
	b = int(input())
	if operator == '+':
		print("Output is", a+b)
	elif operator == '-':
	    print("Output is", a-b)
	elif operator == '*':
	    print("Output is", a*b)
	elif operator == '/':
	    print("Output is", a/b)
	elif operator == '**':
	    print("Output is", a**b)
	elif operator == '%':
	    print("Output is", a%b)
	else:
	    print("Invalid operation!!!")

	print("Do you want to continue? If yes then write -> Y/y/Yes/yes")
	again = input()
	if not (again == 'Y' or again == 'Yes' or again == 'y' or again == 'yes'):
		break 
	      # break always breaks the nearest loop in case of nested loops

	print("Thank you for using the application!!!")

	                            	

