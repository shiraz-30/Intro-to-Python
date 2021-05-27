def chef_and_groups():
	string = input()

	x = 0
	if string[0] == '1':
		x += 1
	for j in range(1, len(string)):
		if string[j] == '1' and string[j] != string[j - 1]:
			x += 1
	print(x)
    
    
t = int(input())
for i in range(0, t):
	chef_and_groups()
