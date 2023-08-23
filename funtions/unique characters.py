def unique_char(s):
    char = set()
    for char1 in s:
        if char1 in char:
            return False
        char.add(char1)
    return True

s1 = "hello"
s2 = "world"
print(unique_char(s1))
print(unique_char(s2))
