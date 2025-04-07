a = lambda x: x * x


# print(a(4))

# print((lambda x: x * x)(4))

# print((lambda x: "it is even" if x % 2 == 0 else "it is odd")(4))

# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial_of_a_num(4))
#
# import sys
# print(sys.getrecursionlimit())
#
# print(give_factorial(996))
#
# print(sys.setrecursionlimit(1500))
#
# print(sys.getrecursionlimit())
#
# print(give_factorial(1496))
list1 = [5, 4, 3]
var1 = list(map(factorial, list1))


# print(var1)

def var_arg_fun(*args):
    a = 0
    for i in args:
        a += i
    return a


# print(var_arg_fun(2,3))
# print(var_arg_fun(2,3, 4, 5, 6))

def var_kw_arg_fun(*kwargs):
    for i, j in kwargs:
        print(f"key is {i} and value is {j}")


# var_kw_arg_fun(("lang","python"),( "fee","1000"))

dict1 = {"lang": "python", "fee": "1000"}


# for i in dict1:
#     print(i)

# for i in dict1.values():
#     print(i)

# for i, j in dict1.items():
#     print(i, j)

def greet(name="Guest"):
    return f"Hello, {name}!"


# print(greet())
# print(greet("Ram"))

def give_fibonacci(x):
    a, b = 0, 1
    for _ in range(x):
        print(a, end=" ")
        a, b = b, a + b


# give_fibonacci(10)

def rec_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)


n = 10


# for i in range(n):
#     print(rec_fibonacci(i), end=" ")

def generate_numbers(max):
    num = 0
    print("Before entering loop")
    while True:
        print("Before Yield")
        yield num  # Yield the current value and pause the function
        num += 1
        print("Number Incremented")
        print(num)


# Create a generator object
gen = generate_numbers(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(gen)


# def odd_even_check(arg):
#     if arg % 2 == 0:
#         print("the {} is even".format(arg))
#     else:
#         print("the {} is odd".format(arg))


# print(odd_even_check(3))


x = 10


def some_func(n):
    x = 5
    print(x + n)

    def inner_func(n):
        # nonlocal x
        print("printing x in inner function", x + n)


# print(some_func(5))


# x =  int(input("give input 1:"))
# y =  int(input("give input 2:"))
# print(x+y)
exp = "x**y+(x+y)%y"
# t = eval(exp)
# a = 4
# y = 2
# glob_dict = {'a' : 12 , 'y':4}
# local_dict = {'a' : 8, 'y':10}
# exp = "a+y"
# s = eval(exp)
# print(s)
# s = eval(exp, glob_dict)
# print(s)
# s = eval(exp, glob_dict,local_dict)
# print(s)

x = 10  # Global variable


def my_func():
    x = 5  # Local variable inside the function
    print("Inside function:", x)


# print(x)
# my_func()
a, b = 2, 3


def my_func(a, b):
    global x
    print("Inside function:", a + b + x)


# print("var declared outside",x)
# my_func(a,b)
#############
def my_func():
    global x
    x = 5
    print("Inside function:", x)


# print(x)
# my_func()
# print(x)

def my_func(a, b):
    print("Inside function:", a + b + x)


# print(x)
# my_func(a,b)

def outer_function():
    x = 7
    print("x Inside outer_function:", x)

    def inner_function():
        print("x Inside inner_function:", x)


# outer_function()

def outer_function():
    x = 7 # local
    print("x Inside outer_function:", x)

    def inner_function():
        nonlocal x
        x = 9
        print("x Inside inner_function:", x)

    inner_function()
    print("printing the x of outer function", x)

# outer_function()
map
x = 18

def outer_function():
    global x
    x = 7 # local
    print("x Inside outer_function:", x)

    def inner_function():
        nonlocal x
        x = 9
        print("x Inside inner_function:", x)

    inner_function()
    print("printing the x of outer function", x)

# print(x) # 18
# outer_function()
# 7
# 9
# 9
# print(x) # 9


class member:
    def add_two_num(self, a,b):
        return  a + b
















