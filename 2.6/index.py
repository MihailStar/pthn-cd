# 2.6.1
txt = "a-b-c-d-e"
lst = txt.split("-")

print(lst)  # -> ['a', 'b', 'c', 'd', 'e']


# 2.6.2
lst = ["a", "b", "c", "d", "e"]
txt = "-".join(lst)

print(txt)  # -> 'a-b-c-d-e'
