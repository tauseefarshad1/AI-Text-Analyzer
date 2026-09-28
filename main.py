from text_analyzer import TextAnalyzer
from file_handler import read_file

text = read_file("sample.txt")
analyzer = TextAnalyzer(text)
print ('<-------Text Statistics------->')
print('\n')
print('Total Words: ', analyzer.words_counter())
print('Total Characters: ', analyzer.characters_counter())
print('Total Sentences: ', analyzer.sentence_counter())
print('\n')
print("<-------Word Analysis------->")
print('\n')
print('Words frequency: \n\n', analyzer.words_frequency())
print('\n')
print('Unique Words: \n\n', analyzer.unique_words())
print('\n')
print('Common Words: \n\n', analyzer.common_words())




