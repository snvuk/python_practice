def count_word_occurrences(word_list):
    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


text = ["apple", "banana", "apple", "apple", "banana", "orange", "apple"]
word_counts = count_word_occurrences(text)

for word, count in word_counts.items():
    print(count ,word )
