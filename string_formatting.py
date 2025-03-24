import sys

program_name = sys.argv[0]
a = sys.argv[1]
b = int(sys.argv[2])
c = float(sys.argv[3])

print("length of arguements:",str(len(sys.argv)))
print("The program name is ",program_name)
print("First parameter value argv[1]",a)
print("second parameter value argv[2]",b)
print("third parameter value argv[3]",c)

print("addition of b and c is ", b + c )

d = "My name is %s, I am  %d years old I have %8.4f rupees"%(a,b,c)
print(d)

e = "scala"

d = "My name is {}, I am  {} years old I have {} rupees {}".format(a, b, c, a)
print(d)

f = 'My name is {0:s}, I am  {1:d} years old I have {2:6.3f} decimal accuracy and {0:s} is very popular'.format(a,b,c)
print(f)


g = 'My name is {:s}, I am  {:d} years old I have {:6.3f} decimal accuracy'.format(a, b, c)
print(g)

# String interpolation
print(f"{a} is a zero index based language and I am {b} years old ")
print(r"python is a zero \nindex \tbased \\language")

def suare_root(b):
    return b*b

print(suare_root(b))











