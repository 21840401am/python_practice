list1 = [1,2,3,4]
list2 = ['a','b','c','d']

list3 = list(zip(list1,list2))
tuple1 = tuple(zip(list1,list2))
# print(list3)
print(tuple1)

list1 = [1,2,3,4]
list2 = ['a','b','c','d', 'f','g']
list3 = list(zip(list1,list2))
# print(list3)

# print(list(zip('abcdefg', range(3), range(4))))

empty_dict = {}
set3 = {1,2,3,4,5}
# print(type(empty_dict))
# print(type(set3))
set1 = set()

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

op = zip(list1,list2)
# for i in op:
#     print(i)

op1 = tuple(zip(list1, list2))
# print(op1)

op2 = list(zip(list1, list2))
# print(op2)

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

op = list(zip(list1,list2))
print(op)
list3, list4 = list(zip(*op))
print(list(list3))
print(list(list4))









