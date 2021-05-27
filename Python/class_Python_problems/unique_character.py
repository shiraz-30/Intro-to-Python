""" Q => You are given a string of length n. Find all the characters which are 
non- repeating. (n <= 10^7)
Test case => "unacademy"   ,    "codechef"
u                          ,     o
n                          ,     d
c                          ,     h
d                          ,     f
e
m
y
"""

def getUniqueCharacters(string):
	freq_map = {}
	for i in range(0, len(string)):
		if (freq_map.get(string[i]) == None):
			freq_map[string[i]] = 1
		else:
			freq_map[string[i]] += 1

	result = []
	for k in freq_map.keys():
		if (freq_map[k] == 1):
			result.append(k)

	return tuple(result)

string = "codechef"
result = getUniqueCharacters(string)
print(result)
