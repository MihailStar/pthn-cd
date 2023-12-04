# 4.6.1
dct = {"x": 1, "y": 2, "z": 3}
key = "x"
val = dct.get(key)

print(val)  # -> 1


# 4.6.2
dct = {"x": "1", "y": "2", "z": "3"}
result = int(dct["x"]) ** 2 + int(dct["y"]) ** 2 + int(dct["z"]) ** 2

print(result)  # -> 14


# 4.6.3
dct = {"x": 1, "y": 2, "z": 3}
result = str(dct["x"]) + str(dct["y"]) + str(dct["z"])

print(result)  # -> '123'


# 4.6.4
dct = {"y": 2025, "m": 12, "d": 31}
# date = f'{dct['y']}-{dct['m']}-{dct['d']}'
date = str(dct["y"]) + "-" + str(dct["m"]) + "-" + str(dct["d"])

print(date)  # -> '2025-12-31'
