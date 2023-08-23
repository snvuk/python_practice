year = int(input("Enter a year: "))

def leap(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


if leap(year):
    print("yes")
else:
    print("no")
