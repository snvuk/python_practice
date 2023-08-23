def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = lst[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 11
result = binary_search(sorted_array, target_element)

if result != -1:
    print(result)
else:
    print("Element not found.")
