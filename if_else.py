age = 18
if age >= 18:
    print("You are an adult.")


i = 20
# Checking if i is greater than 0
if i > 0:
    print("i is positive")
else:
    print("i is 0 or Negative")

a = -2
# Ternary conditional to check if number is positive or negative
f = res = "Positive" if a >= 0 else "Negative"
print(f)
print("Positive") if a >= 0 else print("Negative")

age = 25
exp = 10

#Using '>' operator & 'and' with if-else
if age > 23 and exp > 8:
    print("Eligible.")
else:
    print("Not eligible.")

# nested if else
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive and even number.")
    else:
        print("Positive and odd number.")
else:
    print("Non-positive number.")

i = 25

# Checking if i is equal to 10
if (i == 10):
    print("i is 10")
# Checking if i is equal to 15

elif (i == 15):
    print("i is 15")
# Checking if i is equal to 20

elif (i == 20):
    print("i is 20")

# If none of the above conditions are true
else:
    print("i is not present")


i = 56
if (i == 20):
    # print("i is 20")
    pass
# If none of the above conditions are true
else:
    # print("i is not present")
    pass

list1 = [1,2,3,4,5,6]
list2 = []
for i in list1:
    list2.append(i * i)
print(list2)

string1  = "python"
for d in string1:
    # print(d)
    pass
range1  = range(1,16)
for k in range1:
    # print(k)
    pass

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "second name": "Alice",
}
for keys in person:
    print(keys)
for value1 in person.values():
    print(value1)
for key,value in person.items():
    with open('dict_output', 'w') as f:
        print(f"key is {key}, value is {value}",  sep='#', end=' ', file=f)
        print("key is {}, value is {}".format(key, value))

for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

for index, i in enumerate(list1, start=4):
    print(f"index is {index}, element is {i}")

for i in list1:
    print(i + i)
    if (i == 5):
        print(f"you met the condition i == {i} , exiting the loop")
        break




































