def even_characters(input_string):
    result = ""
    for index in range(0, len(input_string), 2):
        result += input_string[index]
    return result

input_string = input("Enter a string: ")
even_characters2 = even_characters(input_string)
print("Characters with even indexes:", even_characters2)
