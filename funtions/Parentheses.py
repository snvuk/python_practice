def balanced(p):
    temp = []
    opening_brac = "([{"
    closing_brac = ")]}"

    for char in p:
        if char in opening_brac:
            temp.append(char)
        elif char in closing_brac:
            if not temp:
                return False
            top_char = temp.pop()
            if opening_brac.index(top_char) != closing_brac.index(char):
                return False
    return len(temp) == 0

p1 = "([{}])"
p2 = "([{)}"

print(balanced(p1))
print(balanced(p2))