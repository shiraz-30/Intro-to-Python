# Assignment Operators

# 1. = -> It will assign the value to the rhs to the variable on left
a = 10
b = 30
c = b
print(a, b, c)

# 2. += -> It will act same as a = a + 1
a += 1 # Instead of writing a = a + 1, we write this
b += a # Instead of writing a = a + b, we write this
print(a, b)

# 3. -= -> It will act same as a = a - 1
a -= 1 # Instead of writing a = a - 1, we write this
b -= a # Instead of writing a = a - b, we write this
print(a, b)

# 4. *= -> It will act same as a = a * 2
a *= 2

# 5. %= -> It will act same as a = a % 7
a %= 7

# 6. /= -> It will act same as a = a / 2
a /= 2

# 7. //= -> It will act same as a = a // 2
a //= 2

# 8. **= -> It will act same as a = a ** 2
a **= 2

# a++ or ++a for a = a + 1 does not exist in python

# ---------------------------------------------------------

# Bitwise operator -> these will work on bit by bit level

# 1. & -> a&b -> It will do bitwise and on binary of a, b
z = 5 & 4 # 5 -> 101 , 4 -> 100, 101&100 -> 100(4)
print(z)

# 2. | -> a|b -> It will do bitwise or on binary of a, b
z = 5 | 4 # 5 -> 101 , 4 -> 100, 101|100 -> 101(5)
print(z)

# 3. ^ -> a^b -> It will do bitwise xor on binary of a, b
z = 5 ^ 4 # 5 -> 101 , 4 -> 100, 101^100 -> 001(1)
print(z)

# 4. ~ -> ~a -> It will do bitwise not on binary of a
z = ~5 # 5 -> 101 , ~101 -> -6 (in complement of 2)
print(z)

# 5. << -> Left shift operator
z = 1 << 3 # it will append 3 zeroes to the right of 1 -> 1 -> 1000 , 6 << 2 -> 110 -> 11000
print(z)

# 6. >> -> Right shift operator
z = 5 >> 2 # It will prepend 2 zeroes to the left of 5 and remove last 2 bits
print(z)
# (101) >> 2 
# 101 -> 010 -> 001

# 5 >> 3 -> (101) -> 010 -> 001 -> 000

# ------------------------------------------------------

# Membership operator

# 1. in operator

arr = [1,2,3,'shiraz']
print(3 in arr) # is there value of 3 in arr? True
print('shirazmangat' in arr) # is shirazmangat in arr? -> False

# 2. not in operator

print( 3 not in arr) # is 3 not in arr? False
print("for string", 'a' in 'astrology' )

# 3. Identity operator

# It will check if the two values are of same type and having same value 
print( 3 is 4) # -> False
print(2 == 2 is True) # -> False
print(4 is True) # -> False
print(6 is 6) # -> True
print(7 is not 7) # -> False

# 2**3**2 will be read from right side onwards 
# ([1,2] == [1,2]) -> True
print(2**3**2) # -> 2**(9) -> 512 

print([1,2] == [1,2])



