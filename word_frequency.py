import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_words = sentence.translate(translator).lower().split()

    # Count word frequencies
    word_count = {}
    for word in cleaned_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Test 
sentence = "This is a word frequency task. This task for the word frequency function is a test."
result = word_frequency(sentence)
print(result)
