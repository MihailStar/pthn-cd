from math import floor

# pyTs3.2.1
print([num for num in range(1, 10) if num % 2 == 1])  # -> [1, 3, 5, 7, 9]


# pyTs3.2.2
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)

print(tpl1 + tpl2)  # -> (1, 2, 3, 4, 5, 6)


# pyTs3.2.3
dct1 = {"a": 1, "b": 2}
dct2 = {"c": 3, "d": 4}

print({**dct1, **dct2})  # -> {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# pyTs3.2.4
lst = [1, 2, 3, 4, 5, 6]
middle_index = floor(len(lst) / 2)

print(sum(lst[:middle_index]) / sum(lst[middle_index:]))  # -> 0.4
