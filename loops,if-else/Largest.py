#Q8

num1 = int(input("Enter the Value1: "))
num2 = int(input("Enter the Value2: "))
num3 = int(input("Enter the Value3: "))

if num1 > num2 and num1 > num3:
    print(num1,"is largest")
elif num2 > num3 and num2 > num1:
    print(num2,"is largest")
else:
    print(num3,"is largest")