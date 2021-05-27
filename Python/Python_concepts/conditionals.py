# 'if' conditional

if 10 > 5:
	print("10 is greater than 5") # this is the start of a new block
	x = 12 # this is in same block as of the above statement
	print(x**2) # this is in same block as of the above statement

else:
	print("false") # this will be printed only when the if condition is false

	
	
print("end of if") # this is a seperate block now

print("hello")

# we can't randomly give blocks in between i.e. as in between lines 5 & 6.
# lines 3,8,10 are of same indentation 

#calculator

a = 10
b = 2
operator = input()

if operator == '+':
	print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
else:
    print(a/b)

if operator == '+':
	print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)    

# nested if elif else

if 10 > 5:
	if 5 < 3:
		print("first nested if")
	elif 4 > 2:
	    if 3 < 4:
	        print("second nested if inside elif")
	    else:
	        print("else inside first elif")
	elif 17 > 8:
	    print("second elif")
	else:
	    print("else")
elif 4 % 2 == 0:
	    print("end") 


