<---------------------------------------------------------->
<---------------- Character Counter (Code) ---------------->
<---------------------------------------------------------->


text = str(input("Enter your text: "))

ch_counter = len(text)

print(ch_counter)


<---------------------------------------------------------->
<------------------ Words Counter (Code) ------------------>
<---------------------------------------------------------->


text = str(input("Enter your text: "))

words = text.split()

word_counter = len(words)

print(word_counter)


<---------------------------------------------------------->
<---------------- Sentence Counter (Code) ----------------->
<---------------------------------------------------------->


text = str(input("Enter your text: "))

sentence_counter = text.count('.') + text.count('?')

print(sentence_counter)


<---------------------------------------------------------->
<------------- Words Frequency Counter (Code) ------------->
<---------------------------------------------------------->


text = str(input("Enter your text: "))
def words_frequency():
    words = text.lower().split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
             frequency[word] = 1

    return frequency

    
print("Frequency of words are: \n", words_frequency())


<---------------------------------------------------------->
<---------------- Most Common Words (Code) ---------------->
<---------------------------------------------------------->


text = str(input("Enter your text: "))
def common_words():
    words = text.lower().split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
             frequency[word] = 1

    highest_count = max(frequency.values())
    most_common = []

    for word, count in frequency.items():
        if count == highest_count:
            most_common.append(word)

    return most_common
    
print("The most common words are: \n", common_words())


<---------------------------------------------------------->
<-------------- Unique Words Counter (Code) --------------->
<---------------------------------------------------------->


text = str(input("Enter your text: "))
def unique_words():
    words = text.lower().split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
             frequency[word] = 1

    most_common = []

    for word, count in frequency.items():
        if count == 1:
            most_common.append(word)

    return most_common
    
print("The most Unique words are: \n", unique_words())