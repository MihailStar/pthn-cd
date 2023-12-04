import math

# 8.1.1
lst = [1, 2, 3, 4, 5]
# result = math.fsum(lst)
result = sum(lst)

print(result)  # -> 15


# 8.1.2
num = 16.456
result = round(num)

print(result)  # -> 16


# 8.1.3
num = 16.456
result = round(num, 2)

print(result)  # -> 16.46


# 8.1.4
num = 16.456
result = math.ceil(num)

print(result)  # -> 17


# 8.1.5
num = 16.456
result = math.floor(num)

print(result)  # -> 16


# 8.1.6
num = 16
result = math.sqrt(num)

print(result)  # -> 4.0


# 8.1.7
num = 17
result = round(math.sqrt(num), 2)

print(result)  # -> 4.12


# 8.1.8
num = 17
result = math.ceil(math.cbrt(num))

print(result)  # -> 3


# 8.1.9
num = 12.34
# integer_part = math.trunc(num)
# fractional_part = num % integer_part
[fractional_part, integer_part] = math.modf(num)

print(integer_part)  # -> 12.0
print(fractional_part)  # -> 0.33999999999999986


# 8.1.10
num1 = 5
num2 = 3
# result = (num1 // num2, num1 % num2)
result = divmod(num1, num2)

print(result)  # -> (1, 2)


# 8.1.11
lst = [1, 2, 3, 4, 5]
result = sum(lst) / len(lst)

print(result)  # -> 3.0
