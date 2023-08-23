# Q2
tax = None

price = int(input("Enter the value: "))

if price > 100000:
    tax = 15/100 * price
    # print("15%")
elif price > 50000 and price <=100000:
    tax = 10/100 * price
    # print("10%")
else:
    tax = 5/100 * price
print("tax" ,tax)
    # print("5%")

##Q3
# tax = None
#
# price = int(input("Enter the value: "))
#
# if price > 100000:
#     tax = 15/100 * price
# elif price > 50000 and price <= 100000:
#     tax = 10/100 * price
# else:
#     tax = 5/100 * price
#
# print("Tax:", tax)