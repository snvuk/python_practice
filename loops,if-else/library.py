nod = int(input("Enter the number: "))

if nod <=5:
    cost = nod * 2
elif nod > 5 and nod <= 10:
    cost = nod * 3
elif nod > 10 and nod <= 15:
    cost = nod * 4
else:
    cost = nod * 5

print(cost)