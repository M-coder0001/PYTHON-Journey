t = (1,2,3,4,5,"abc",10.55)
print(t)
print(type(t))

a = list(t)
print("List:", a)
a.remove(10.55)
print(a)

b = tuple(a)
print("Tuple:", b)

x = b.count(2)
print(x)

del b
print(b)