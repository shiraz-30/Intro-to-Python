"""
Sets are same to same as dictionaries with just a difference that they only have 
keys and no values associated with the keys.
Sets are also unordered/randomly stored like dictionary.
In sets, we can't have duplicates.
"""
s = {"Shiraz", "Mangat", 1,2,3,4}
print(s)
print(type(s))

S = {"Shiraz", "Shiraz"}
print(S)
s.remove(1)
print(s)

s.add(123)
print(s)

print(2 in s)
