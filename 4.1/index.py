# 4.1.1
dct = {"x": 1, "y": 2, "z": 3}
length = len(dct)

print(length)  # -> 3


# 4.1.2
dct = {"x": 1, "y": 2, "z": 3}

print(dct["x"])  # -> 1
print(dct["y"])  # -> 2
print(dct["z"])  # -> 3


# 4.1.3
dct = {"x": 1, "y": 2, "z": 3}
dct["x"] += 1

print(dct["x"])  # -> 2


# 4.1.4
dct = {"x": 1, "y": 2, "z": 3}
total = dct["x"] + dct["y"] + dct["z"]

print(total)  # -> 6


# 4.1.5
dct = {"x": 1, "y": 2, "z": 3}
dct.update({"a": 1, "b": 2, "c": 3})

print(dct)  # -> {'x': 1, 'y': 2, 'z': 3, 'a': 1, 'b': 2, 'c': 3}


# 4.1.6
dct = {}
dct["a"] = 1
dct["b"] = 2
dct["c"] = 3

print(dct)  # -> {'a': 1, 'b': 2, 'c': 3}
