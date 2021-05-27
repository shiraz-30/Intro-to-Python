import sys
m = 0
queries = 0
input_a, input_b = 0, 0
def add(a, b):
    global m
    global queries
    if a < 0 or a > 1000000000:
        print('invalid arguments to add, input too large or negative')
        exit()
    if b < 0 or b > 1000000000:
        print('invalid arguments to add, input too large or negative')
        exit()
    queries += 1
    if queries > 10000:
        print('too many queries for a = ', a, 'b = ', b, 'm = ', m)
    return (a + b) % m

def pwr(a, b):
    result = 1

    for i in range(0, b):
        temp = result

        for j in range(1, a):
            temp = add(temp, result)
        result = temp

    return add(result, 0)

def power(a, b, m):
    res = 1
    for _ in range(0, b):
        res = (res * a) % m
    return res
 
import random
 
for _ in range(0, 1):
    # input_a, input_b = random.randint(1, 100), random.randint(1, 100)
    # m = random.randint(2, 1000000000)
    input_a, input_b, m = 2, 3, 7
    got = pwr(input_a, input_b)
    print(got)
    expected = power(input_a, input_b, m)
    if expected != got:
        print('Wrong answer, expected = ', expected, 'got = ', got)
        print('a = ', input_a, 'b = ', input_b, 'm = ', m)
        exit()
print('Ok!')

