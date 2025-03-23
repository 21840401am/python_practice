import sys

# Using sys.argv
arg1 = sys.argv[0]
arg2 = sys.argv[1]
arg3 = sys.argv[2]
arg4 = sys.argv[3]
arg5 = sys.argv[4]
n = str(len(sys.argv))

print("no of arguments:", n)

print("Script name:", arg1)

print(type(arg1))

print("2nd argument:", arg2)
print("3rd argument:", arg3)
print("4th argument:", arg4)
print("5th argument:", arg5)

a = int(sys.argv[5])


def square_root(a):
    return a * a


# Calling the function
print(square_root(a))
