def vowels1(s):
    vowels = []
    for i in s:
        if i in "aeiou":
            vowels.append(i)
    return vowels

def vowels2(s):
    return [i for i in s if i in "aeiou"]

def vowels3(s):
    return list(filter(lambda x: x in "aeiou", s))

s = "Programming in Python is fun"
print(vowels1(s))
print(vowels2(s))
print(vowels3(s))