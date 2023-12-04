# 5.4.1
st = {1, 2, 3, 4, 5}
num = 3
hasNum = num in st

print(hasNum)  # -> True


# 5.4.2
st1 = {1, 2, 3, 4, 5}
st2 = {1, 2, 3}
result = st2 <= st1

print(result)  # -> True


# 5.4.3
num1 = 12345
num2 = 12321
result = set(str(num2)) <= set(str(num1))

print(result)  # -> True


# 5.4.4
num1 = 12345
num2 = 45123
result = set(str(num1)) == set(str(num2))

print(result)  # -> True
