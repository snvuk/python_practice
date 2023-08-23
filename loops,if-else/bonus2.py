salary = int(input("Enter the salary: "))
service = int(input("Enter the service: "))


if service > 5:
    bonus = 0.05 * salary
    print("You are eligible.")
    print("Net bonus amount:", bonus)
else:
    print("Sorry, you are not eligible.")
