firstReading = float(input("Please enter first reading: "))
secondReading = float(input("Please enter second reading: "))

usage = secondReading - firstReading
print("Your usage is " + str(usage))

cost=5
print("Your cost per unit is " + str(cost))

totalCost = cost * usage
print("total cost is " + str(totalCost) + " pounds")
