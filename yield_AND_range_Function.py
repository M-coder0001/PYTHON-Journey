def numbers():
    for i in range(1, 6):
        yield i
        
print("Using range function: ")
for i in range(1, 6):
    print(i)
    
print("Using yield function: ")
for num in numbers():
    print(num)