# 2.4.1
lst = ["a", "b", "c", "d", "e"]
index = lst.index("c")

print(index)  # -> 2


# 2.4.2
lst = ["a", "b", "c", "d", "e"]
has_c = "c" in lst

print(has_c)  # -> True


# 2.4.3
lst = ["a", "b", "c", "d", "c", "c"]
number_of_c = lst.count("c")

print(number_of_c)  # -> 3
