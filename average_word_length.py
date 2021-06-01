# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

sentence1 = "This is a first sentence for testing."
sentence2 = "I want to graduate fast and work!!!"

def average_word_length(sentence):
    for c in "!?',;.":
        sentence = sentence.replace(c, '')

    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)

# test the function
print(average_word_length(sentence1))
print(average_word_length(sentence2))