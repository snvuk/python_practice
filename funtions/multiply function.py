list1 = [8,2,3,-1,7]
def mul_list(num):
    result = 1
    for i in num:
        result *= i
    return result

x = mul_list(list1)
print(x)