import re
def extract_words(text):
    words = []
    for word in text.split():
        if re.search(r'\w+', word):
            words.append(word)
    return words

print(extract_words("There was n6 78o ice cre45am in the freezer22, nor did they have45 6756 money to go to the store."))