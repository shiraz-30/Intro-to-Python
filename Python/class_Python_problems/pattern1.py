# Q-1 -> Print the following pattern for the value of n. 
# ----*      1 star and 4 space
# ---***     3 star and 3 space
# --*****    5 star and 2 space                {n = 5}
# -*******   7 star and 1 space
# *********  9 star and 0 space 
# Ans-1 ->

n = int(input())

i = 1

while i <= n:
	print(" "*(n - i), end = "") # this is to print n-i spaces
	print("*"*(2*i - 1)) # this is to print 2i-1 stars 
	i += 1

# by nested loops

i = 1
while i <= n:
	spaces = 1
	while spaces <= (n - i):
		print(" ", end = "")
		spaces += 1
	stars = 1
	while stars <= (2*i - 1):
	    print("*", end = "")
	    stars += 1

	print("")
	# increment to next row
	i += 1 
	
