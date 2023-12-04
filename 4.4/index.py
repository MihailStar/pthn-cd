# 4.4.1
dct = {"x": 1, "y": 2, "z": 3}
del dct["x"]

print(dct)  # -> {'y': 2, 'z': 3}


# 4.4.2
dct = {"x": 1, "y": 2, "z": 3}
# deleted_val = dct.pop("x", 0)
deleted_val = dct.pop("x")

print(deleted_val)  # -> 1
print(dct)  # -> {'y': 2, 'z': 3}


# 4.4.3
dct = {"x": 1, "y": 2, "z": 3}
deleted_key_and_val = dct.popitem()

print(deleted_key_and_val)  # -> ('z', 3)
print(dct)  # -> {'x': 1, 'y': 2}


# 4.4.4
dct = {"x": 1, "y": 2, "z": 3}
dct.clear()

print(dct)  # -> {}
