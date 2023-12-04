from functools import reduce

# pyTs1.7.1
dct = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

print(sum(dct.values()))  # -> 10

# pyTs1.7.2
dct = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

print(reduce(lambda acc, num: acc + num**2, dct.values(), 0))  # -> 30


# pyTs1.7.3
string = "abcde"

print(list(string))  # -> ['a', 'b', 'c', 'd', 'e']


# pyTs1.7.4
number = 12345
result = list(map(lambda digit: int(digit), str(number)))

print(result)  # -> [1, 2, 3, 4, 5]


# pyTs1.7.5
number = 12345

print(int(str(number)[::-1]))  # -> 54321

# pyTs1.7.6
number = 12345

print(reduce(lambda acc, digit: acc + int(digit), str(number), 0))  # -> 15
