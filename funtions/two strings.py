def longest_strings(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    if len_str1 > len_str2:
        print(str1)
    elif len_str2 > len_str1:
        print(str2)
    else:
        print(str1)
        print(str2)

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

longest_strings(s1, s2)
