#Q2

num = int(input("Enter the number: "))

if num >= 80:
    print("Your Grade is A+")
elif num >= 60 and num < 80:
    print("Your Grade is A")
elif num >= 50 and num < 60:
    print("Your Grade is B+")
elif num >= 40 and num < 50:
    print("Your Grade is B")
elif num >= 25 and num < 40:
    print("Your Grade is C")
else:
    print("Your Grade is D")