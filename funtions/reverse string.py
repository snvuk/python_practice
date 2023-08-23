char = input("Enter the char: ")

def reverse(rev):
    reverse_str = ""
    for i in rev:
        reverse_str = i + reverse_str
    return reverse_str

reverse = reverse(char)
print(reverse)