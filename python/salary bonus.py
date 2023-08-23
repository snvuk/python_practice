#Q3

service = int(input("Enter the service years: "))
salary = int(input("Enter the salary: "))
if service > 10:
    bonus = 10/100 * salary
elif service >= 6 and service <10:
    bonus = 8/100 * salary
elif service < 6:
    bonus = 5/100 * salary

print("bonus is",bonus)