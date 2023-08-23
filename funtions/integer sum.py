num = input("Enter an integer: ")

if num.isdigit():
    num = int(num)
    total_sum = 0
    for i in range(1, num + 1):
        total_sum += i

    print(total_sum)
else:
    print("Wrong input")
