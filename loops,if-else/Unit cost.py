quantity = int(input("Enter the quantity: "))

unitcost = 100
totalcost = 1000 * unitcost

if totalcost > 1000:
    discount = 0.1 * totalcost
    totalcost = discount

print(totalcost)