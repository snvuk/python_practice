def find_numbers():
    result = []

    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5 != 0:
            result.append(str(num))

    return result


numbers = find_numbers()
print(", ".join(numbers))
