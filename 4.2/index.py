# 4.2.1
dct = {"x": 1, "y": 2, "z": 3}
has_key_w = "w" in dct

print(has_key_w)  # -> False


# 4.2.2
dct = {"x": 1, "y": 2, "z": 3}

print(dct.get("w", "!"))  # -> '!'
