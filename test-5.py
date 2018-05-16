firstReading = float(input("Please enter first reading: "))
secondReading = float(input("Please enter second reading: "))
thirdReading = float(input("Please enter third reading: "))

if firstReading > secondReading or secondReading > thirdReading:
    print("Error: your usage cannot be negative")
    quit()

firstUsage = secondReading - firstReading
secondUsage = thirdReading - secondReading
usage = thirdReading - firstReading
print("Your total usage is " + str(usage))

avgUsage = float(firstUsage + secondUsage) / 2
print("Your average usage is " + str(avgUsage))

cost=5
print("Your cost per unit is " + str(cost))

totalCost = cost * usage
print("total cost is " + str(totalCost) + " pounds")
