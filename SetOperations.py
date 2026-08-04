s1 = {1,3,15,1,5,1,5,3,58,8,5}
s2 = {66,77,55,99,44,42,45,35,14,57,21,79,52,69,5}

print(s1)
print(s2)

print(type(s1))
print(type(s2))

s2.remove(45)
print(s2)

s1.add("Python")
print(s1)

s1.union(s2)
print(s1)

s1.intersection(s2)
print(s1)

a = [1,2,3]
b = [1,2,3,4,5]
is_subset = set(a).issubset(set(b))
print(is_subset)