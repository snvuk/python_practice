s1 = "abcd"
s2 = "cdba"

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("yes")
else:
    print("no")
