# Given two sentences, return an array that has the words that appear in one sentence
# and not the other and an array with the words in common.

sentence1 = 'The city is crowded my friends are away'
sentence2 = 'I met my friends from this city'

def check_matched_word(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
        # mismatch(symmetric difference), match(intersection)
    return sorted(list(set1^set2)), sorted(list(set1&set2))

print(check_matched_word(sentence1, sentence2))