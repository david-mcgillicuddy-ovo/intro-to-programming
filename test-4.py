firstReading = float(input("Please enter first reading: "))
secondReading = float(input("Please enter second reading: "))

if firstReading > secondReading:
    print("Error: your usage cannot be negative")
    quit()

usage = secondReading - firstReading

cost=5
print("Your cost per unit is " + str(usage) + "p")

totalCost = cost * usage
print("total cost is " + str(totalCost) + "p")
