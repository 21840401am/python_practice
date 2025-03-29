count = 1

while count <= 10:
    # print(count)`
    count += 1  # count = count + 1  output = 3
    if count == 6:
        break

list1 = [1,2,3,4,5]

# for i in  list1:
#     print(i)
index = 0
while index < len(list1):
    # print(list1[index])
    index += 1

import builtins

# Get all functions in the builtins module
functions_list = [func for func in dir(builtins) if callable(getattr(builtins, func))]

# Print the list of built-in functions
# print(functions_list)

def greet():
    return "Hi Folks"

# print(greet())

from test1 import add_two_num
from class_concept import demo
print(add_two_num(2,3))

obj = demo()
print(obj.square_root(2))


