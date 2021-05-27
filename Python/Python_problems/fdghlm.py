def hcf(x, y):
	if x > y:
		smaller = y
	else:
	    smaller = x
	for i in range(1, smaller + 1):
	    if ((x % i == 0) and (y % i == 0)):
	         hcf = i
	return hcf
	
a, b = map(int, input().split())	

print( hcf(a,b), int((a*b)/ hcf(a, b)))
