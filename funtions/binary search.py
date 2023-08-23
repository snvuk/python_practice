def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 15
index = binary_search(sorted_list, target)

if index != -1:
    print(index)
else:
    print(target)













