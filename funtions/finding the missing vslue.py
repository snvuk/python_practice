list1 = [11, 12, 13, 14, 15, 19, 18, 17, 20]

def find_missing_value(lst):
    for num in range(min(lst), max(lst) + 1):
        if num not in lst:
            return num

missing_value = find_missing_value(list1)
print(missing_value)
