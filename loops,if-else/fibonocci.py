num = int(input("Enter the number: "))

num1 = 0
num2 = 1

for i in range(num):
    num1,num2 = num2,num1+num2
    print(num1, end=" ")
