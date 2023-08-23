lists = [[1, 2, -1, -4, -20], [-8, -3, 4, 2, 1], [3, 8, 10, 1, 3], [-4, -1, 1, 7, -6]]

max_sum = 0

for sublist in lists:
    max_value = max(sublist)
    max_sum += max_value

print(max_sum)
