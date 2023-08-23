def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


data = [5, 8, 2, 10, 23, 15, 7, 12]
target_value = 15
result = linear_search(data, target_value)

if result != -1:
    print(result)
else:
    print("Element not found.")
