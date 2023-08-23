def anagrams(s1, s2):
    str1 = s1.replace(" ", "").lower()
    str2 = s2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

string1 = "abcd"
string2 = "badc"

result = anagrams(string1, string2)

if result:
    print("yes")
else:
    print("no")
