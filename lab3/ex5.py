def validate_dict(rules, d):
    for rule in rules:
        if rule[0] not in d:
            return False
        if not d[rule[0]].startswith(rule[1]):
            return False
        if not d[rule[0]].endswith(rule[3]):
            return False
        if rule[2] not in d[rule[0]][len(rule[1]):-len(rule[3])]:
            return False
    return True

print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))