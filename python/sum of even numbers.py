start = int(input("Enter the number: "))
end = int(input("Enter the number: "))

sum_num = 0

for i in range(start, end+1):
    if i % 2 == 0:
        sum_num += i
print(sum_num)
