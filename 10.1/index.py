from functools import reduce


# 10.1.1
def square(num):
    return num**2


# 10.1.2
def calculate_sum(num_a, num_b):
    return num_a + num_b


# 10.1.3
def calculate_sum_squares(nums):
    return reduce(lambda acc, num: acc + num**2, nums, 0)


# 10.1.4
def is_even(num):
    return num % 2 == 0


# 10.1.5
def func1(num1, num2, num3):
    return num1 + num2 + num3


print(func1(num1=1, num2=2, num3=3))  # -> 6
