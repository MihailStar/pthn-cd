# 4.5.1
dct1 = {"a": 1, "b": 2, "c": 3}
dct2 = {"x": 4, "y": 5, "z": 6}
dct1.update(dct2)

print(dct1)  # -> {'a': 1, 'b': 2, 'c': 3, 'x': 4, 'y': 5, 'z': 6}


# 4.5.2
dct1 = {"a": 1, "b": 2, "c": 3}
dct2 = {"x": 4, "y": 5, "z": 6}
dct = {}
dct.update(dct1)
dct.update(dct2)
vals = list(dct.values())

print(vals)  # -> [1, 2, 3, 4, 5, 6]


# 4.5.3
dct1 = {"a": 1, "b": 2, "c": 3}
dct2 = {"d": 4, "e": 5, "f": 6}
dct3 = {"j": 7, "h": 8, "i": 9}
common_dct = {}
common_dct.update(dct1)
common_dct.update(dct2)
common_dct.update(dct3)

print(common_dct)
# -> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'j': 7, 'h': 8, 'i': 9}
