
number = input("Please enter a positive number!")

total = 0

if number.isdigit():
    numberToList = list(number)
    for i in numberToList:
        total+=int(i)**len(numberToList)
    if int(number)==total:
        print(f"{number} is an Armstrong number")
else:
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")




