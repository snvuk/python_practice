def generate_sentences(subjects, verbs, objects):
    sentences = []
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentence = subject + " " + verb + " " + obj + "."
                sentences.append(sentence)
    return sentences

def print_sentences(sentences):
    for sentence in sentences:
        print(sentence)

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

generated_sentences = generate_sentences(subjects, verbs, objects)
print_sentences(generated_sentences)
