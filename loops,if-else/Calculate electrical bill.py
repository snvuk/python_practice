units = int(input("Enter the unit: "))

total_amount = 0

if units > 100:
    total_amount += (units - 100)*2
    units = 100

if units > 300:
    total_amount += (units - 300)*5
    units = 300

print(total_amount)