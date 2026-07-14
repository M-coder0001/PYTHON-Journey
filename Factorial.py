num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("No factorial for negative numbers")
elif num == 0:
    print("Factorial is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("The factorial of given number is:", fact)