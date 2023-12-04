# pyTs2.2.1
numbers = [1, -1, 1, -1, 1, -1, 1]
counter = 0

for number in numbers:
    if number < 0:
        counter += 1

print(counter)  # -> 3


# pyTs2.2.2
numbers = [1, -1, 2, -2, 3, -3]
numbers = list(filter(lambda number: number > 0, numbers))  # -> [1, 2, 3]

print(numbers)


# pyTs2.2.3
string = "1234567"
string = string[:-2] + string[-1]

print(string)  # -> '123457'


# pyTs2.2.4
file_names = ["index.py", "index.html"]

print(
    list(filter(lambda name: name.endswith(".html"), file_names))
)  # -> ['index.html']


# pyTs2.2.5
fractions = [1.456, 2.125, 3.32, 4.1, 5.34]

print(
    list(map(lambda fraction: round(fraction, 1), fractions))
)  # -> [1.5, 2.1, 3.3, 4.1, 5.3]


# pyTs2.2.6
dct = {"a": 1, "b": 2, "c": 3, "d": 4}

print(list(dct.values()))  # -> [1, 2, 3, 4]
