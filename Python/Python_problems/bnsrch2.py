import sys
 
def find_pos(x):
    print('1 ' + str(x))
    sys.stdout.flush()
    t = int(input())
    return t

def left_part(n, x):
	low, high = 0, n - 1

	while low < high:
		mid = low + (high - low) // 2
		position_of_mid = find_pos(mid)

		if position_of_mid < x:
			low = mid + 1			
		else:
			high = mid
	return low

def right_part(n, x):
	low, high = 0, n - 1

	while low < high:
		mid = low + (high - low) // 2
		position_of_mid = find_pos(mid)

		if position_of_mid <= x:
			low = mid + 1
		else:
			high = mid
	return high

def count(n, x):
	left_position = left_part(n, x)
	right_position = right_part(n, x)

	answer = (right_position - left_position)

	return answer

n = int(input())
x = int(input())
 
print('2 ' + str(count(n, x)))

