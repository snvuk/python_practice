def add_binary(a, b):
    sum_decimal = int(a, 2) + int(b, 2)
    sum_binary = bin(sum_decimal)[2:]

    return sum_binary


a1, b1 = "11", "1"
print(add_binary(a1, b1))

a2, b2 = "1010", "1011"
print(add_binary(a2, b2))
