start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

for num in range(start, end + 1):
    if num > 1:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False

        if prime:
            print(num)