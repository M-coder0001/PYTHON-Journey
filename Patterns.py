print("1. left numeric triangle")

num = 1
for i in range(1,5):
    for _ in range(i):
        print(num,end = " ")
        num += 1
    print()

print("==================================")
    
print("2. Floyd's pyramid")

for i in range(6):
    for _ in range(5-i):
        print(" ",end="")
        
    
    for j in range(i):
        print(j+1,end=" ")
        
    print()
    
print("==================================")

print("3. inverted right numeric triangle\n") 

n = 5

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("==================================")

print("4. left star triangle")
for i in range(5):
    for _ in range(i):
        print("*", end = " ")
    print()
    
print("==================================")

print("5. right star triangle\n") 

n = 5

for i in range(1, n + 1):

    # Print spaces
    for _ in range(n - i):
        print(" ", end=" ")

    # Print stars
    for _ in range(i):
        print("*", end=" ")

    print()

print("==================================")

print("6. star pyramid")
for i in range(5):
    for _ in range(4-i):
        print(" ",end = "")
    
    for _ in range(i):
        print("*", end =" ")
        
    print()
    
print("==================================")

print("7. inverted right star triangle\n")

n = 5

for i in range(n, 0, -1):
    for _ in range(i):
        print("*", end=" ")
    print()

print("==================================")

print("8. inverted star pyramid\n")

n = 4

for i in range(n, 0, -1):

    # Print leading spaces
    for _ in range(n - i):
        print(" ", end="")

    # Print stars
    for _ in range(i):
        print("*", end=" ")

    print()

print("==================================")

print("9. Alphabet Triangle\n")

for i in range(5):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()
