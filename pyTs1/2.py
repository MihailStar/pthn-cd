# pyTs1.2.1
number = 123456

print(str(number)[0])  # -> '1'


# pyTs1.2.2
number = 123456

print(str(number)[-1])  # -> '6'


# pyTs1.2.3
number = 123456
digits = str(number)
result = int(digits[0]) + int(digits[-1])

print(result)  # -> 7


# pyTs1.2.4
number = 123456
digits = str(number)
result = len(digits)

print(result)  # -> 6


# pyTs1.2.5
number_a = 123456
number_b = 123456

print(str(number_a)[0] == str(number_b)[0])  # -> True


# pyTs1.2.6
lst = [1, 2, 3, 4, 5, 6]
result = lst[:3]

print(result)  # -> [1, 2, 3]
