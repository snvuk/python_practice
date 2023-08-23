num = int(input("Enter the number: "))
f = 1

if num < 0:
    print("its not for negative numbers")
else:
    for i in range(1, num + 1):
        f = f * i
    print(f)

