list1 = [8, 15, 4, 22, 11, 30, 7, 18]

def lar_num(num):
    if not num:
        return None

    largest = num[0]
    for num in num:
        if num > largest:
            largest = num
    return largest


largest_number = lar_num(list1)
print("List of numbers:", list1)
print("Largest number:", largest_number)
