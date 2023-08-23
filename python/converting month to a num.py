#its not completed need to complete

month_name = input("Enter the month name: ")

month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

md = False

for month , days in month_days:
    if month_name == month:
        print(month , days)
        md = True




