a = "a is global variable"

def locals_var(b="b is local Variable"):
    print(b)

print("printing local variable")
locals_var() 

print("printing global variable")
print(a)
    