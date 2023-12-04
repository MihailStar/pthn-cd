# pyTs2.8.1
nums = list(range(1, 11))

print(nums)  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# pyTs2.8.2
string = "AbcdE"
capital_letter_counter = 0

for letter in string:
    if letter.isupper():
        capital_letter_counter += 1

print(capital_letter_counter <= 2)  # -> True


# pyTs2.8.3
digits = ["1", "2", "3", "4", "5"]
nums = list(map(int, digits))

print(nums)  # -> [1, 2, 3, 4, 5]
