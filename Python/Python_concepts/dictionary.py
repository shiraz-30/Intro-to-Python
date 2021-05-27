# Dictionary stoes elements in Key, Value form

x = {"name": "Shiraz", "Age": "18", "college": "PEC"}
print(x)
print(type(x))

""" If we give two same keys ->
It will override the exisiting key's value.
"""

# How to access values to a given key?
print(x["name"], x["Age"])

# Dictionary are mutable
x["name"] = "Mangat"
print(x)

# add a key value pair
x["location"] = "Chandigarh"
print(x)

# delete a key value pair
del x[("Age")]
print(x)
print(x.get("20")) # None will be shown if there is no value beforehand
                   # Used to extract values from the dictionary

# Print all the keys

print(*x.keys())
# Print all the values

print(*x.values())

# Delete the dictionary                  
x.clear()
print(x)


