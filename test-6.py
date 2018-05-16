numberOfReadings = 5

readings = []

for x in range(1, numberOfReadings+1):
    reading = float(input("Please enter reading number " + str(x) + ": "))
    readings.append(reading)

print("Readings: " + str(readings))

totalUsage = readings[numberOfReadings-1] - readings[0]
print("Your total usage is " + str(totalUsage))

usages = []
for y in range(1, numberOfReadings):
    usage = readings[y] - readings[y-1]
    usages.append(usage)
print("Usages: " + str(usages))

# avgUsage = float(firstUsage + secondUsage) / 2
# print("Your average usage is " + str(avgUsage))

cost=5
print("Your cost per unit is " + str(cost) + "p")

totalCost = cost * totalUsage
print("total cost is " + str(totalCost) + "p")
