def censor(text):
    words = []
    for word in text.split():
        if word[0] in "aeiouAEIOU" and word[-1] in "aeiouAEIOU":
            new_word = ""
            for i in range(len(word)):
                if i % 2 == 0:
                    new_word += word[i]
                else:
                    new_word += "*"
            words.append(new_word)
        else:
            words.append(word)
    return words

print(censor("test abbba abbbd aca eo e"))