# 7.6.1
dct = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# for val in dct.values():
#     print(val)

for key in dct:
    print(dct[key])


# 7.6.2
dct = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# for key in dct.keys():
#     print(key)

for key in dct:
    print(key)  # -> 'a\nb\nc\nd\ne'


# 7.6.3
dct = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# for key, val in dct.items():
#     print(key + str(val))

for key in dct:
    print(key + str(dct[key]))  # -> 'a1\nb2\nc3\nd4\ne5'


# 7.6.4
dct = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
result = 0

# print(sum(dct.values()))

for key in dct:
    result += dct[key]

print(result)  # -> 15
