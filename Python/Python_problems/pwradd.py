import sys
 
def add(a, b):
    print('1', a, b) 
    sys.stdout.flush()
    return int(input())

from random import randrange

def pwr(a, b):
	result = 1

	for i in range(0, b):
		temp = result

		for j in range(1, a):
			temp = add(temp, result)
		result = temp

	return add(result, 0)

a, b = map(int, input().split())
ans = pwr(a, b)
print('2', ans)
