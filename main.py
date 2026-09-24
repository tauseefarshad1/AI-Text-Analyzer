from text_statistics import words_counter, characters_counter, sentence_counter
from word_analysis import get_words_frequency, get_unique_words, most_common_words
from file_handler import read_file

text = read_file("sample.txt")
print ('<-------Text Statistics------->')
print('\n')
print('Total Words: ', words_counter(text))
print('Total Characters: ', characters_counter(text))
print('Total Sentences: ', sentence_counter(text))
print('\n')
print("<-------Word Analysis------->")
print('\n')
print('Words frequency: \n\n', get_words_frequency(text))
print('\n')
print('Unique Words: \n\n', get_unique_words(text))
print('\n')
print('Common Words: \n\n', most_common_words(text))




