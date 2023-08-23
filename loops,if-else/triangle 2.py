t1 = int(input("Enter the t side1: "))
t2 = int(input("Enter the t side2: "))
t3 = int(input("Enter the t side3: "))


if t1 + t2 > t3 and t2 + t3 > t1 and t1 + t3 > t2:
    print("possible.")
else:
    print("not possible.")
