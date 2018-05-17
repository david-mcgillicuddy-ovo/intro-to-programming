import sys

print("Please enter your meter readings, and press Enter on an empty line when done")

readings = []
retryErrorMessage = "Please enter a correct reading or press Enter to finish entering readings"

while True:
    reading = sys.stdin.readline().strip()
    
    if reading == "":
        break
    
    if not reading.isnumeric():
        print("This is an invalid number. " + retryErrorMessage)
        continue
    
    if len(readings) > 0 and int(reading) < readings[-1]:
        print("This reading is smaller than the last one. " + retryErrorMessage)
        continue
    
    readings.append(int(reading))

print("Readings: " + str(readings))

if len(readings) <= 1:
    print("Error: need more than one reading")
    quit()

totalUsage = readings[-1] - readings[0]
print("Your total usage is " + str(totalUsage))

usages = [readings[y] - readings[y - 1] for y in range(1, len(readings))]
print("Usages: " + str(usages))

avgUsage = sum(usages) / len(usages)
print("Your average usage is " + str(round(avgUsage, 4)))

cost = 0.05
print("Your cost per unit is " + str(cost) + "p")

totalCost = cost * totalUsage
costText = ""

if totalCost >= 100:
    pence = round(totalCost % 100)
    pounds = int((totalCost - pence) / 100)
    
    if pence == 100:
        pounds += 1
        pence = 0
        
    costText = str(pounds) + " pounds "
    
    if pence > 0:
        costText += str(pence) + " p"
else:
    costText = "" + str(totalCost) + " p"

print()
print("Your total cost is " + costText)
