# 6.3.1
test = None

print(test is None)  # -> True


# 6.3.2
test = None

# print(not (test is None))
print(test is not None)  # -> False


# 6.3.3
x = 3
txt = "12345"
has_x = str(x) in txt

print(has_x)  # -> True


# 6.3.4
x = 3
lst = [1, 2, 3, 4, 5]
has_x = x in lst

print(has_x)  # -> True
