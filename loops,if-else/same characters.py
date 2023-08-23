list1 = ["mani", "nnnn", "kk"]

for word in list1:
    if len(set(word)) == 1:
        print(word , "have all same characters")
    else:
        print(word, "does not have all same characters")

