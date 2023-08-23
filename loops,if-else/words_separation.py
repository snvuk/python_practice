input_char = input("Enter a sequence of words: ")

words = input_char.split()
digit_words = []
for i in words:
    if i.isdigit():
        digit_words.append(i)
print(digit_words)
