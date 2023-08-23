i = int(input("Enter the number1: "))
j = int(input("Enter the number2: "))
k = int(input("Enter the number3: "))

if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print(i,j,k)