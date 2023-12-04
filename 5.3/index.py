# 5.3.1
st1 = {1, 2, 3, 4}
st2 = {1, 2, 4, 5}
st3 = {1, 2, 5, 7}
result = st1 & st2 & st3

print(result)  # -> {1, 2}


# 5.3.2
st1 = {1, 2, 3, 4}
st2 = {1, 3, 4, 5}
st3 = {1, 2, 5, 6}
result = (st1 & st2) - st3

print(result)  # -> {3, 4}


# 5.3.3
st1 = {1, 2, 4, 5}
st2 = {1, 2, 3, 6}
st3 = {1, 2}
result = (st1 | st2) - st3

print(result)  # -> {3, 4, 5, 6}


# 5.3.4
num1 = 12345
num2 = 45678
common_digits = set(str(num1)) & set(str(num2))
result = int("".join(common_digits))

print(result)  # -> 45
