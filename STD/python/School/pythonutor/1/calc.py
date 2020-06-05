print("Welcome to mincalc")
print("Input \'sum\' to summary two numbers,\n"+
        "\'sub\' -- to substract,\n" +
        "\'mul\' -- to mutiply,\n" +
        "\'div\' -- to divide.")
user = input()
a = float(input("Input first number:"))
b = float(input("Input second number:"))
if user == "sum":
    print("Result:", a+b)
elif user == "sub":
    print("Result:", a-b)
elif user == "mul":
    print("Result", a*b)
elif user == "div":
    print("Result", a/b)
else:
    print("nope")
