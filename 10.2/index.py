from functools import reduce
from math import floor


# 10.2.1
def get_divisors(num):
    divisors = []

    for possible_divisor in range(1, num + 1):
        if num % possible_divisor == 0:
            divisors.append(possible_divisor)

    return divisors


# 10.2.2
def get_symbols(string):
    return list(string)


# 10.2.3
def reverse(string):
    return string[::-1]


# 10.2.4
def calculate_sum_digits(num):
    return reduce(lambda acc, digit: acc + int(digit), list(str(num)), 0)


# 10.2.5
def is_leap(year):
    """@tutorial https://learn.microsoft.com/ru-ru/office/troubleshoot/excel/determine-a-leap-year"""

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# 10.2.6
def convert_to_day(seconds):
    seconds_in_day = 24 * 60 * 60

    return floor(seconds / seconds_in_day)


# 10.2.7
def is_prime(num):
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    else:
        return True


# 10.2.8
def get_common_divisors(num_a, num_b):
    common_divisors = []

    for possible_divisor in range(1, min(num_a, num_b) + 1):
        if num_a % possible_divisor == 0 and num_b % possible_divisor == 0:
            common_divisors.append(possible_divisor)

    return common_divisors
