marks = int(input("Enter the marks: "))

if marks < 25:
    print("your grade is Fail")
elif marks >= 25 and marks < 45:
    print("your grade is E")
elif marks >= 45 and marks < 50:
    print("your grade is D")
elif marks >=50 and marks < 60:
    print("Your grade is C")
elif marks >= 60 and marks < 80:
    print("Your grade is B")
elif marks >= 90 and marks <= 100:
    print("your grade is A")
else:
    print("Enter the correct value")