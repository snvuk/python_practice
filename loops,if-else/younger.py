#Q6

age1 = input("Enter the age: ")
age2 = input("Enter the age: ")
age3 = input("Enter the age: ")
age4 = input("Enter the age: ")

if age1 < age2 and age1 < age3 and age1 < age4:
    print(age1,"is younger")
elif age2 < age3 and age2 < age4 and age2 < age1:
    print(age2,"is younger")
elif age3 < age4 and age3 < age2 and age3 < age1:
    print(age3,"is younger")
else:
    print(age4,"is younger")
