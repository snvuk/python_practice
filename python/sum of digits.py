num = int(input("Enter a number: "))
sum = 0

while num > 0:
    s = num % 10
    sum += s
    num //= 10

print(sum)





