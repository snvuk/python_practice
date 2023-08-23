

num = int(input("Enter a number: "))

def print_pattern(num):
    for i in range(1, num):
        print(((10**i) // 9) * i)


print_pattern(num)
