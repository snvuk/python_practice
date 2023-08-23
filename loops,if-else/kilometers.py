km = int(input("Enter the km: "))

total = 0

if km <= 10:
    total = km * 11
elif km > 10 and km <= 100:
    total = km * 10
else:
    total = km * 9

print(total)