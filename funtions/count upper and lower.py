character = input("Enter the character: ")

def sample_string(x):
    upper_count = 0
    lower_count = 0

    for char in x:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

upper_count, lower_count = sample_string(character)

print("Upper:", upper_count)
print("Lower:", lower_count)


