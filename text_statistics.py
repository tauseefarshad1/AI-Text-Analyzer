from text_cleaner import get_words

def characters_counter(text):
    return len(text)

def words_counter(text):
    return len(get_words(text))

def sentence_counter(text):
    return text.count(".") + text.count("?")

