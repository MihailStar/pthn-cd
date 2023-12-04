# Slice - iterable[
#   from: int = 0, including
#   :
#   to: int = iterable_length, not_including
#   :
#   step: int = 1
# ]


# 3.2.1
string = "12345"
result = string[1:]

print(result)  # -> '2345'


# 3.2.2
string = "12345"
result = string[:-1]

print(result)  # -> '1234'


# 3.2.3
string = "12345"
result = string[1:-1]

print(result)  # -> '234'


# 3.2.4
string = "123456789"
result = string[::2]

print(result)  # -> '13579'


# 3.2.5
string = "123456789"
result = string[1::2]

print(result)  # -> '2468'


# 3.2.6
string = "12345"
result = string[::-1]

print(result)  # -> '54321'


# 3.2.7
string = "123456789"
result = string[-2::-2]

print(result)  # -> '8642'


# 3.2.8
string = "123456789"
result = string[2::3]

print(result)  # -> '369'


# 3.2.9
lst = [1, 2, 3, 4, 5, 6, 7]
result = lst[:3]

print(result)  # -> [1, 2, 3]


# 3.2.10
lst = [1, 2, 3, 4, 5, 6, 7]
result = lst[1:-2]

print(result)  # -> [2, 3, 4, 5]


# 3.2.11
lst = [1, 2, 3, 4, 5, 6, 7]
result = lst[1:-1]

print(result)  # -> [2, 3, 4, 5, 6]


# 3.2.12
lst = [1, 2, 3, 4, 5, 6, 7]
result = lst[::2]

print(result)  # -> [1, 3, 5, 7]

# 3.2.13
DAYS_OF_WEEK = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")

print(DAYS_OF_WEEK[:5])  # -> ('Пн', 'Вт', 'Ср', 'Чт', 'Пт')
print(DAYS_OF_WEEK[5:])  # -> ('Сб', 'Вс')
