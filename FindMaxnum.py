num1 = int(input("Enter 1st number1: "))
num2 = int(input("Enter 1st number2: "))
num3 = int(input("Enter 1st number3: "))

if num1 > num2 and num1 > num3:
    print("1st number is larger")
elif num2 > num1 and num2 > num3:
    print("2st number is larger")
else:
    print("3rd number is larger")