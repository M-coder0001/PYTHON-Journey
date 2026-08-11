list1 = [10,5,3,67,2,7,1,9]

list2 = [i for i in list1 if i%2==0]
print(list2)

def gen():
    yield 1
    yield 2
    yield 3
    
a = gen()

print(next(a))
print(next(a))
print(next(a))