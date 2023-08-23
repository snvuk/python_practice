#Q4
leap_year = int(input("Enter the year: "))

if (leap_year % 4 == 0 and leap_year % 100 == 0) or (leap_year % 400 == 0):
    print("Leap year")
else:
    print("not a leap")

    year = int(input("Enter the year: "))

    leap_year = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False

        if leap_year:
            print(year, "leap year.")
        else:
            print(year, "not a leap year.")