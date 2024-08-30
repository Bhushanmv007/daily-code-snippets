from collections import Counter

def word_frequency(sentence):
    words = sentence.split()
    return Counter(words)

print(word_frequency("the quick brown fox jumps over the lazy dog the fox"))  
# the has come 3 times, quick only once 