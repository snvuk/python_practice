word = int(input("Enter a number: "))
s = str(word)
palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
        palindrome = False

if palindrome:
    print("Palindrome")
else:
    print("Not a palindrome.")

print(type(word))
