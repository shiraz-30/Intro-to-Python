# How to use for loops
# (start, end, inc) -> start, start + inc, start + 2*inc, ...., end - inc
# for loops range means [a, b) 

for i in range(0,3):
	print(i)

print("for loops += 2")

for i in range(0,10,2):
	print(i)

print("for loops with single arg in range")

for i in range(9): # it will take start as 0 and end as argument - 1
    print(i)

print("for loops to iterate backwards")

for i in reversed(range(0,8)):
	print(i)

print("check")

for i in range(9,-1,-1):
	print(i)

# iteration on lists
print("lists")

li = [1,2,3,4,"Shiraz"]

for i in li:
	print(i)

