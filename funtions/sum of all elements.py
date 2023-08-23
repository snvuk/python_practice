def array_sum(arr, index=0):
    if index == len(arr):
        return 0
    else:
        return arr[index] + array_sum(arr, index + 1)

array = [1, 2, 3, 4, 5]
result = array_sum(array)
print(result)
