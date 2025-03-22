list1 = [1,2,3,4,5,6]
print(list1)
list1.append(['a','b','c'])
print(list1)
list1.extend(['a','b','c'])
print(list1)

list1[1]  = "SQL"
print(list1)

a, *b , c = list1
print(a)
print(b)
print(c)

list1 = [1,2,3,4,5,6]
list1.pop()
print("after pop", list1)
