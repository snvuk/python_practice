quantity = int(input("Enter the quantity: "))

cost = 100
total_cost = quantity * cost

if total_cost > 1000:
    discount = 0.1 * total_cost
    total_cost -= discount
    print("You get a 10% discount.","and after discount: ", total_cost)
else:
    print("no discount applied.","Total cost:",total_cost)
