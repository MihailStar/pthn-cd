# pyTs1.9.1
string = "abcdef"

print(string[-3:])  # -> 'def'


# pyTs1.9.2
key_to_num = {"a": 1, "b": 2, "c": 3, "d": 4}

for key, num in key_to_num.items():
    key_to_num[key] = num * 2

print(key_to_num)  # -> {'a': 2, 'b': 4, 'c': 6, 'd': 8}
