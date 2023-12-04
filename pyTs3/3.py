from math import floor

# pyTs3.3.1
number = 1357

print(all(int(digit) % 2 == 1 for digit in str(number)))  # -> True


# pyTs3.3.2
word = "abcba"

# print(list(word) == list(reversed(word)))

middle_index = floor(len(word) / 2)
left_index = 0
right_index = len(word) - 1

while left_index <= middle_index:
    if word[left_index] != word[right_index]:
        print(False)
        break

    left_index += 1
    right_index -= 1
else:
    print(True)  # -> True


# pyTs3.3.3
st1 = {1, 2, 3}
st2 = {4, 5, 6}

print({*st1, *st2})  # -> {1, 2, 3, 4, 5, 6}
