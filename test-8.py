import sys

print("Please enter your meter readings")
readings = [float(number) for number in sys.stdin.readline().split()]
print("Readings: " + str(readings))

if len(readings) <= 1:
    print("Error: need more than one reading")
    quit()

totalUsage = readings[-1] - readings[0]
print("Your total usage is " + str(totalUsage))

usages = [readings[y] - readings[y-1] for y in range(1, len(readings))]
print("Usages: " + str(usages))

for usage in usages:
    if usage < 0:
        print("Error: your usage cannot be negative")
        quit()

avgUsage = sum(usages)/len(usages)
print("Your average usage is " + str(avgUsage))

cost=5
print("Your cost per unit is " + str(cost) + "p")

totalCost = cost * totalUsage
print("total cost is " + str(totalCost) + "p")
