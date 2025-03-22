d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# print(d)

# Access using key
# print(d["name"])
# print(d[(1, 2)])

# using dict() constructor
d = dict(a=1, b=2, c=3)
# print(d)

# Access using get()
# print(d.get("a"))

d = {1: 'scala', 2: 'For', 3: 'python'}
# Adding a new key-value pair
d["age"] = 22
# print(d)

# Updating an existing value
d[1] = "Python dict"
# print(d)

# if the key vale specified is there it will update otherwise it will add like below
# But not in case of list
d[4] = "Python dict"
# print(d)

my_dict = {1: 'scala', 2: 'For', 3: 'python'}
# Adding and updating multiple elements
my_dict.update({'b': 3, 'c': 4, 'd': 5})
# print(my_dict)

# Initial dictionary
my_dict = {'a': 1, 'b': 2}

# Adding and updating multiple elements
my_dict = {**my_dict, 'b': 3, 'c': 4, 'd': 5}

# print(my_dict)

d  = {'a' : "SQL", 'A': "python"}
# print(d['a'])
# print(d['A'])

d  = {'a' : "python", 'b': "python"}
# print(d)

# Example for del statement
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']
# print(my_dict)

# Example for pop() method
my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict.pop() pop with 0 arguements raise type error
# print(my_dict)
# value = my_dict.pop('b')
# print(my_dict)
# print(value)

# pop() without any value
# value = my_dict.pop()
# print(value)

# pop() with default value
value = my_dict.pop('d', 'Key not found')
# print(value)

# Example for clear() method
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
# print(my_dict)

# Example for popitem() method
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# key, value = my_dict.popitem()
# print(my_dict)
# print(key)
# print(value)

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4
# print(my_dict)
# my_dict.popitem()
# print(my_dict)
# my_dict.popitem()
# print(my_dict)


# popitem() when dictionary is empty
# my_dict = {}
# my_dict.popitem()
# print(my_dict)

d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for y in d:
    print(y)

# Iterate over values
for l in d.values():
    print(l)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")