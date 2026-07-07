print("Enter a date in the format DD/MM/YYYY:")
Date = input("Enter Date: ")
Date = Date.split("/")
print ("Date in format MM/DD/YYYY is: ", (Date[1], Date[0], Date[2]))