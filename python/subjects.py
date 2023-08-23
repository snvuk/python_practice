english = int(input("Enter the marks: "))
math = int(input("Enter the marks: "))
science = int(input("Enter the marks: "))
social = int(input("Enter the marks: "))

if english > 80 and math > 80 and science > 80 and social > 80:
    print("Science Stream")
elif english > 80 and math > 50 and science > 50:
    print("commerce stream")
elif english > 80 and social > 80:
    print("Humanities")
else:
    print("No stream")
