# pyTs1.1.1
number = 0

if number < 0:
    print("negative")
elif number > 0:
    print("positive")
else:
    print("zero")  # -> 'zero'


# pyTs1.1.2
string = "abcdef"

print(len(string))  # -> 6


# pyTs1.1.3
string = "abcdef"

print(string[-1])  # -> f'


# pyTs1.1.4
number = 1

if number % 2 == 0:
    print("even")
else:
    print("not even")  # -> 'not even'


# pyTs1.1.5
string_a = "abcdef"
string_b = "abcdef"

print(string_a[0] == string_b[0])  # -> True


# pyTs1.1.6
word = "abcdef"

if word[-1] == "ь":
    print(word[-2])
else:
    print(word[-1])  # -> f'
