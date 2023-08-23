char = input("Enter the Char: ")

def reverse(rev):
    rev_str = ""
    for char in rev:
        rev_str = char + rev_str
    return rev_str

reversed_input = reverse(char)
print("Original char:", char)
print("Reversed char:", reversed_input)
