num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))


if num1 > num2 and num1 > num3:
    if num2 > num3:
        second_largest = num2
    else:
        second_largest = num3
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        second_largest = num1
    else:
        second_largest = num3
else:
    if num1 > num2:
        second_largest = num1
    else:
        second_largest = num2

print(second_largest)