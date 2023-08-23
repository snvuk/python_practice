# #Q5

num = int(input("Enter the number: "))

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

if 1 <= num <= 7:
    print("day is: " ,days[num -1])
else:
    print("the day is wrong")