import re
def match_strings(strings, regexes):
    matches = []
    for string in strings:
        for regex in regexes:
            if re.search(regex, string):
                matches.append(string)
                break
    return matches

print(match_strings(["a", "b", "c", "d", "e", "5", "123"], [r'\d+', r'[a-c]']))