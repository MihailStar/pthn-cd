# 2.1.1
lst = ["a", "b", "c", "d", "e"]
result = len(lst)

print(result)  # -> 5


# 2.1.2
lst = [1, 2, 3, 4, 5]
result = lst[0]

print(result)  # -> 1


# 2.1.3
lst = [1, 2, 3, 4, 5]
result = lst[1]

print(result)  # -> 2


# 2.1.4
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
# result = list(lst1)
# result.extend(lst2)
result = lst1 + lst2

print(result)  # -> [1, 2, 3, 4, 5, 6]
