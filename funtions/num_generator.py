def divisible_generator(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num

n = int(input("Enter a number: "))
result_generator = divisible_generator(n)
result_list = list(result_generator)

result_str = ""
for i in range(len(result_list)):
    result_str += str(result_list[i])
    if i < len(result_list) - 1:
        result_str += ","

print(result_str)
