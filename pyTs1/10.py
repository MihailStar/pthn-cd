# pyTs1.10.1
string = "abcdef"

print(string[::2])  # -> 'ace'
print(string[1::2])  # -> 'bdf'


# pyTs1.10.2
number = 12345
digits = str(number)
index = len(digits) - 1

while index >= 0:
    print(digits[index])  # -> '5\n4\n3\n2\n1'
    index -= 1
