age = int(input("Enter the age: "))
gender = input("Enter the gender: ")
days = int(input("Enter the days: "))

if age >= 18 and age < 30:
    if gender == "M":
        wage = 700
        if gender == "F":
            wage = 750
elif age >= 30 and age <= 40:
    if gender == "M":
        wage = 800
        if gender == "F":
            wage =  850
total = wage * days
print(type(wage))
print(total)
