n = int(input("Enter total count of numbers: "))
positives = []
negatives = []
evens = []
odds = []
total = 0

for i in range(n):
    num  = int(input("Enter number: "))
    if num > 0:
        positives.append(num)
    elif num < 0:
        negatives.append(num)
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
    
    total += num

print("======Result======")
print("positive Nums: ", positives)
print("Negative Nums: ", negatives)
print("Even Nums: ", evens)
print("Odd Nums: ", odds)
print("Average: ", total / n)