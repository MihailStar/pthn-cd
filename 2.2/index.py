# 2.2.1
lst = [1, 2, 3, 4, 5]
lst.append(6)

print(lst)  # -> [1, 2, 3, 4, 5, 6]


# 2.2.2
lst = [1, 2, 3, 4, 5]
index = lst.index(2)
lst.insert(index + 1, "a")

print(lst)  # -> [1, 2, 'a', 3, 4, 5]


# 2.2.3
lst = [1, 2, 3, 4, 5]
lst.insert(0, "a")

print(lst)  # -> ['a', 1, 2, 3, 4, 5]
