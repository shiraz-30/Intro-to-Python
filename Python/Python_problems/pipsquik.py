t = int(input())
for i in range(0, t):
	N,H,Y1,Y2,L = input().split()
	N = int(N)
	H = int(H)
	Y1 = int(Y1)
	Y2 = int(Y2)
	L = int(L)
	count = 0
	barrier = 0

	while count < N:
		t, x = input().split()
		t = int(t)
		x = int(x)
		if L > 0 and t == 1 and (H - Y1) <= x:
			barrier += 1
		elif L > 0 and t == 2 and Y2 >= x:
		    barrier += 1	
		else:
		    L -= 1
		    if L > 0:
		        barrier += 1
		count += 1
	print(barrier)	            