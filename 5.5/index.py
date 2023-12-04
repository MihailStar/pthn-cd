# 5.5.1
lst = [1, 2, 3, 1, 2, 3, 3, 4]
lst = list(set(lst))

print(lst)  # -> [1, 2, 3, 4]


# 5.5.2
txt = "12342315"
txt = "".join(set(txt))

print(txt)  # -> '12345'


# 5.5.3
num = 12342315
num = int("".join(set(str(num))))

print(txt)  # -> 12345


# 5.5.4
txt = "abc xyz abc sdf xyz"
txt = " ".join(set(txt.split(" ")))

print(txt)  # -> 'abc xyz sdf'
