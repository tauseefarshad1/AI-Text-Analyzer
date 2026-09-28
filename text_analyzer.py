from word_analysis import get_words_frequency, get_unique_words, most_common_words
from text_statistics import words_counter, characters_counter, sentence_counter
from text_cleaner import get_words

class TextAnalyzer:
    def __init__(self,text):
        self.text = text

    def characters_counter(self):
        return characters_counter(self.text)
    
    def words_counter(self):
        return words_counter(self.text)
    
    def sentence_counter(self):
        return sentence_counter(self.text)
    
    def words_frequency(self):
        return get_words_frequency(self.text)
    
    def unique_words(self):
        return get_unique_words(self.text)
    
    def common_words(self):
        return most_common_words(self.text)
