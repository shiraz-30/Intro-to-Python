import sys
import random
 
arr = []
queries_count = 0
def find_pos(x):
    global queries_count
    queries_count = queries_count + 1
    if queries_count > 40:
        print('error, took more than 40 queries')
        print('hidden array = ', arr, 'x = ', x)
        exit()
 
    if x < 0 or x >= len(arr):
        print('error, index out of range')
        print('hidden array = ', arr, 'x = ', x)
        exit()
    return arr[x]


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


n = random.randint(1, 100000)
dict = {}
for _ in range(0, n):
    app = random.randint(0, 100000)
    arr.append(app)
    dict[app] = dict.get(app, 0) + 1
 
arr = sorted(arr)
 
for _ in range(1, 1000):
    queries_count = 0
    x = random.randint(0, 100000)
    ans = count(len(arr), x)
    if ans != dict.get(x, 0):
        print('Wrong answer, expected = ', dict.get(x, 0), 'got = ', ans)
        print('hidden array = ', arr, 'x = ', x)
        exit()
 
print('Correct Answer!')

