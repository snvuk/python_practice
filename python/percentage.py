percent = int(input("Emter the Num: "))

if percent < 40 :
    print("Failed")
elif percent >= 40 and percent < 55:
    print("Fair")
elif percent >= 55 and percent < 65:
    print("Good")
elif percent >= 65 and percent <= 100:
    print("Execellent")
else:
    print("Enter correct nuumber")
