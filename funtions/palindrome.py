word = int(input("Enter a number: "))

def palindrome(word):
    s = str(word)
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


if palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome.")

print(type(word))
