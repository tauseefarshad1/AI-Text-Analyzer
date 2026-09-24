import string

def clean_text(text):
    text = text.lower()
    
    for character in string.punctuation:
        text = text.replace(character, "")

    return text

def get_words(text):
    cleaned_text = clean_text(text)
    return cleaned_text.split()
