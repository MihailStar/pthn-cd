# pyTs2.4.1
string = "a1b2c3d4e"

for index, char in enumerate(string):
    if char.isdigit():
        print(index)  # -> 1
        break
else:
    print(-1)


# pyTs2.4.2
number = 1234567
counter = 0

for digit in str(number):
    if int(digit) % 2 == 0:
        counter += 1

print(counter)  # -> 3


# pyTs2.4.3
dct = {"a": 1, "b": 2, "c": 3, "d": 4}

print(list(dct.keys()))  # -> ['a', 'b', 'c', 'd']


# pyTs2.4.4
string = "abcde"
result = ""

for index, char in enumerate(string):
    # result += char.upper() if index % 2 == 0 else char.lower()
    result += char.upper() if index % 2 == 0 else char

print(result)  # -> 'AbCdE'


# pyTs2.4.5
string = "aaa bbb ccc"

print(string.title())  # -> 'Aaa Bbb Ccc'


# pyTs2.4.6
date = "2025-12-31"
splited_date = date.split("-")
splited_date.reverse()

print(tuple(splited_date))  # -> ('31', '12', '2025')
