# 7.2.1
tst = [1, 2, 3, 4, 5]
result = 0

for num in tst:
    result += num**2

print(result)  # -> 55


# 7.2.2
tst = ["a", "b", "c", "d", "e"]
result = ""

for char in tst:
    result += char

print(result)  # -> 'abcde'


# 7.2.3
tst = [1, 2, 3, 4, 5]
digits = ""

for num in tst:
    digit = str(num)
    digits += digit

result = int(digits)

print(result)  # -> 12345
