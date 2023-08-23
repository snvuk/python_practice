side1 = int(input("Enter the num1: "))
side2 = int(input("Enter the num2: "))
side3 = int(input("Enter the num3: "))


if side1 == side2 == side3:
    print("equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("isosceles triangle.")
else:
    print("scalene triangle.")
