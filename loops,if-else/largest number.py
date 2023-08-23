num = int(input("Enter a number: "))
largest_num = 0

while num > 0:
    digit = num % 10
    if digit > largest_num:
        largest_num = digit
    num //= 10

print(largest_num)
