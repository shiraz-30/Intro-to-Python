import sys
import random
 
limit = 0
count = 0
 
def run_program(m):
    global count
    count = count + 1
    if count > 31:
        print("Took more than 31 queries for limit = " + str(limit))
        exit()
    if m <= limit:
        return True
    else:
        return False
 
 


def find_memory_limit():
    L = 0
    low, high = 1, 10**9

    while low <= high:
        mid = low + (high - low) // 2
        if run_program(mid):
            L = mid
            low = mid + 1
        else:
            high = mid - 1

    return L
    

 
for _ in range(0, 1000):
    limit = random.randint(1, 999999999)
    count = 0
    found = find_memory_limit()
    if found != limit:
        print('Error found limit = ' + str(found) + ', when actual limit = ' + str(limit))
        exit()
 
print('your program passed 1000 random testcases!')
 
 