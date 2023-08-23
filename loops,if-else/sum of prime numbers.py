start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))
prime_sum = 0

for num in range(start, end + 1):
    if num > 1:
        prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
        if prime:
            prime_sum += num

print(prime_sum)
