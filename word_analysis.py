from text_cleaner import get_words

def get_words_frequency(text):
    words = get_words(text)

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency
    
def get_unique_words(text):
    frequency = get_words_frequency(text)

    unique_words = []

    for word, count in frequency.items():
        if count == 1:
            unique_words.append(word)

    return unique_words

def most_common_words(text):
    frequency = get_words_frequency(text)

    highest_count = max(frequency.values())
    most_common = []

    for word, count in frequency.items():
        if count == highest_count:
            most_common.append(word)

    return most_common