# pyTs2.10.1
string = "A1b2C3"
letter_counter = 0

for letter in string:
    if letter.isalpha():
        letter_counter += 1

print(letter_counter <= 3)  # -> True


# pyTs2.10.2
number = 123579
digits = str(number)
index = len(digits) - 1

while index >= 0:
    if int(digits[index]) % 2 == 0:
        print(int(digits[index]))  # -> 2
        break

    index -= 1
else:
    print(-1)


# pyTs2.10.3
string = "abcde abcde abcde"
words = string.split()
# List comprehension - [expression for item in iterable (if condition)]
result = " ".join([("!" + word[1:]) for word in words])

print(result)  # -> '!bcde !bcde !bcde'


# pyTs2.10.4
digits = ["1", "2", "3", "4", "5"]
total = 0

for digit in digits:
    total += int(digit)

print(total)  # -> 15
