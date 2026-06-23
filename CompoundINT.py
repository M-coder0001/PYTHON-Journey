p = int(input("Enter the principal amount: "))
t = float(input("Enter the time in years: "))
n = int(input("Enter the number of times interest is compounded per year: "))
r = float(input("Enter the annual interest rate: "))

CmpINT = (p * (1 + r / n) ** (n * t))
print("The compound interest is:", CmpINT)