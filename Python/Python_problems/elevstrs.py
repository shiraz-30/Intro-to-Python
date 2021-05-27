t = int(input())
output = []

for i in range(t):
	n, v1, v2 = [int(i) for i in input().split()]

	time_elevator = (2*n) / v2
	time_stairs = ((2**(1/2)) * n) / v1

	if time_elevator < time_stairs:
		output.append ('Elevator')
	else:
	    output.append ('Stairs')

for i in range(t):    
	print(output[i])
