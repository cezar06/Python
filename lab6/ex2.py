import re
def extract_words_regex(regex, text, x):
    words = []
    for word in text.split():
        if re.search(regex, word) and len(word) == x:
            words.append(word)
    return words

print(extract_words_regex(r'\d+', "123 abcd 872 a 82", 3))