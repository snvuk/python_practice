time = int(input("Enter the time: "))

if time >= 0000 and time < 1200:
    print("Good Morning")
elif time >= 1200 and time <1700:
    print("Good Afternoon")
elif time >=1700 and time <2100:
    print("Good Evening")
elif time >= 2100 and time <= 2359:
    print("Good Night")
