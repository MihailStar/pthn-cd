# 2.3.1
lst = ["a", "b", "c", "d", "e"]
del lst[1]

print(lst)  # -> ['a', 'c', 'd', 'e']


# 2.3.2
lst = ["a", "b", "c", "d", "e"]
# index = lst.index("c")
# del lst[index]
lst.remove("c")

print(lst)  # -> ['a', 'b', 'd', 'e']


# 2.3.3
lst = ["a", "b", "c", "d", "e"]
# last = lst.pop(-1)
last = lst.pop()

print(last)  # -> 'e'


# 2.3.4
lst = ["a", "b", "c", "d", "e"]
first = lst.pop(0)

print(first)  # -> 'a'


# 2.3.5
lst = ["a", "b", "c", "d", "e"]
second = lst.pop(1)

print(second)  # -> 'b'


# 2.3.6
lst = ["a", "b", "c", "d", "e"]
lst.clear()

print(lst)  # -> []
