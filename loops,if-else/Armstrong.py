num = int(input("Enter the number: "))
str_num = str(num)
dig = len(str_num)
digits = 0

for i in str_num:
    digits = int(i)** dig

if digits == num:
    print(num,"it is a Armstrong")
else:
    print(num,"not a Armstrong")