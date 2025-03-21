# Defining a set
set1 = {1, 2, 2.0, True, 3.34, False, "Python"}
# print(set1)
# get the data type of set
# print(type(set1))
# Get all the available methods for a set
# print(dir(set))

# We can't access the values of a set using index or slicing
# we need to convert it to a list and can go a head, order may vary

# add
set2 = {1, 286, 2.0, True, 3.34, False, "Python"}
set2.add(8)
# print(set2)
# print(len(set2))

# This has no effect if the element is already present.
set2.add(286)


# print(set2)
# print(len(set2))

# leveraging multiple arguments functionality of add() method
def add_multiple_elements(s: set, *args):
    for i in args:
        s.add(i)


# Calling the above function
set3 = {1, 286, 3.34, False, "Python"}
add_multiple_elements(set3, 3, "scala", "java", "kotlin", "groovy")
# print(set3)

# clear method
set4 = {1, 286, 3.34, True, "Python"}
set4.clear()
# print(set4)

# copy method
set5 = {1, 286, 3.34, True, "Python"}
set5_copy = set5.copy()
# print(set5_copy)
# print(set5)

# modifying copied set
set5_copy.add(365)
# print(set5_copy)
# print(set5)

# creating nested set
# set6 = {1, 286, 3.34, True, "Python",{9, 10}} # commenting it as it is causing error
# set6_copy = set6.copy()
# print(set6_copy)
# print(set6)
# Since sets are mutable, and mutable objects cannot be hashed, you cannot directly have a set containing other sets.
# If you try to do this, you will get a TypeError.

# difference()
s7 = {1, 2, 3, 4}
s8 = {3, 4, 5}
s6 = {3, 4, 1}
set9 = s7.difference(s8)
# print(set9)

s10 = s7.difference(s8, s6)
# print(s10)

# difference_update()
set10 = {1, 2, 3, 4}
set11 = {3, 4, 5}
set10.difference_update(set11)
# print(set10)

# remove()
s = {1, 2, 3}
s.remove(2)
# print(s)  # Output: {1, 3}
# s.remove(4)  # Would raise a KeyError because 4 is not in the set


# discard()
s = {1, 2, 3}
s.discard(2)
# s.discard(4)  # No error since 4 does not exist
# print(s)

# intersection()
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
s3 = {3, 4, 5}
result = s1.intersection(s2)
# print(result)

result = s1.intersection(s2, s3)
# print(result)

# intersection_update() - Update a set with the intersection of itself and another.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
s1.intersection_update(s2)
# print(s1)

# symmetric_difference()
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.symmetric_difference(s2)
# print(result)


# symmetric_difference_update()
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.symmetric_difference_update(s2)
# print(s1)

# union()
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.union(s2)
# print(result)

# update()
s = {1, 2, 3}
s.update([3, 4, 5])
# print(s)


# Remove duplicates from a list
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = set(list1 + list2)
# print(list3)
