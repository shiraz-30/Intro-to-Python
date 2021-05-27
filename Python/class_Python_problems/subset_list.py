# Q => Given a list of integers of size n, print the subsets of the given list.
# Solve this problem recursively. (n <= 20) 
# Example -> [1,2,3] 
"""
[]
[1]
[2]
[3]
[1,2]
[2,3]
[1,3]
[1,2,3]
"""

def subset(li, idx, output):
	"""
	li -> intput list
	idx -> is used to point to current element
	output -> output string 
	"""

	# base case 
	if (idx == len(li)):
		print("[" +output+ "]")
		return

	subset(li, idx + 1, output) # exclude
	subset(li, idx + 1, output + str(li[idx]) + ", ") # include

	return

li = [1,2,3]

subset(li, 0, "")

