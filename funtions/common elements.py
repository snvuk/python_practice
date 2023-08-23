def common_elements(l1,l2):
    elements = set(l1) & set(l2)
    return list(elements)

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
elements = common_elements(l1,l2)
print(elements)
