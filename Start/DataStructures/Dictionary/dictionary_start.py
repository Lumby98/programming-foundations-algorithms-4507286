# Example file for Programming Foundations: Algorithms by Joe Marini
# demonstrate dictionary usage


# TODO: create a dictionary all at once
items1 = dict({"key1": 1, "key2": 2, "key3": 3})
print(items1)

# TODO: create a dictionary progressively
items2 = {}
items2["key2"] = 1
items2["key3"] = 4
items2["key6"] = 5
print(items2)
# TODO: replace an item
items2["key2"] = "two"
print(items2)

# TODO: try to access a nonexistent key


# TODO: iterate the keys and values in the dictionary
for key, val in items2.items():
  print("key:",key,"val:",val)