import sys
 
def run_program(m):
    print('1 ' + str(m))
    sys.stdout.flush()
    r = int(input())
    if r == 0:
        return False
    elif r == 1:
        return True
    exit()

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

    
print("2 " + str(find_memory_limit()))  
