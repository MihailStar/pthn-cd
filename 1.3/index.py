# 1.3.1
tst = "123"
result = int(tst)

print(result)  # -> 123


# 1.3.2
tst1 = "123"
tst2 = "456"
result = int(tst1) + int(tst2)

print(result)  # -> 579


# 1.3.3
tst1 = "1.1"
tst2 = "1.2"
result = float(tst1) + float(tst2)

print(result)  # -> 2.3


# 1.3.4
tst = "123"
result = int(tst[0]) + int(tst[1]) + int(tst[2])

print(result)  # -> 6


# 1.3.5
tst = 123
digits = str(tst)
# from functools import reduce
# result = reduce(lambda digit1, digit2: int(digit1) + int(digit2), digits, 0)
result = int(digits[0]) + int(digits[1]) + int(digits[2])

print(result)  # -> 6


# 1.3.6
tst = 123
result = len(str(tst))

print(result)  # -> 3


# 1.3.7
num1 = 1
num2 = 2
result = str(num1) + str(num2)

print(result)  # -> '12'


# 1.3.8
tst1 = "abc"
txt2 = 123
result = tst1 + str(txt2)

print(result)  # -> 'abc123'
