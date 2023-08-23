num = int(input("Enter a number:"))
temp = num
sum_of_digit = 0

while num > 0:
    digit = num % 10
    fac = 1

    for i in range(1, digit + 1):
        fac = fac * i

    sum_of_digit += fac
    num //= 10

if sum_of_digit == temp:
    print("strong number")
else:
    print("not a strong number")
