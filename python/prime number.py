#Q9

prime = int(input("Enter the number: "))

if prime < 2:
    print(prime, "is not a prime number.")
else:
    if_prime = True
    for i in range(2, int(prime**0.5)+1):
        if prime % i == 0:
            is_prime = False
            break

    if is_prime:
        print(prime, "prime number.")
    else:
        print(prime, "not a prime number.")