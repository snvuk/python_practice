import random

def divisible_numbers():
    divisible_num = []
    while len(divisible_num) < 5:
        num = random.randint(1, 1000)
        if num % 5 == 0 and num % 7 == 0:
            divisible_num.append(num)
    return divisible_num

result = divisible_numbers()
print(result)

