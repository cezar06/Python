def loop(mapping):
    result = []
    current = mapping["start"]
    while current not in result:
        result.append(current)
        current = mapping[current]
    return result

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))