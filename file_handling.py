var1 = open("test_file.txt")
# print(var1.read())

var2 = open("test_file2.txt", "w")
var2.write("Currently we have 34 keywords in python")
var2.close()

var3 = open("test_file2.txt", "r")
# print(var3.read())

# with open("test_file.txt", "r") as f:
#     print(f"output of with open \n { f.read()}")

# with open("test_file.txt", "w") as f:
#     f.write("python is in demand programming language")

# with open("test_file.txt", "r") as f:
#     print(f"output of with open \n { f.read()}") # python is in demand programming language
#
# with open("test_file.txt", "r+") as f:
#     print(f"output of with open \n { f.read()}")
#     f.seek(0)
#     e = f.write("python is the primary skill set for Data Analyst and Data Scientist")
#
# with open("test_file.txt", "r") as f:
#     print(f"output of with open \n { f.read()}")


with open("test_file.txt", "r") as f:
    print(f.read())

# with open("test_file.txt", "a+") as f:
#     f.write(" Code pipelines were built by Data Engineers")
#     f.seek(0)
#     g = f.read()
#     print("output g:\n",g)
with open("test_file.txt", "w+") as f:
    f.write(" Code pipelines were built by Data Engineers")
    f.seek(0)
    p =f.read()
    print(p)

# with open("test_file6.txt", "x") as f:
#     f.write(" Data Scientists build models on the data oprovided by DAta engineers")

with open("C:\\Users\\sonti\\Downloads\\paramtech\\test_file7.txt", "x") as f:
    f.write(" Data Scientists build models on the data oprovided by DAta engineers")














