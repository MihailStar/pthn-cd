# pyTs2.1.1
urls = ["http://code.mu", "https://code.mu"]

print(list(filter(lambda url: url.startswith("http://"), urls)))
# -> ['http://code.mu']


# pyTs2.1.2
some_string = "1020304050607"

print(some_string.find("0"))
# -> 1


# pyTs2.1.3
digits = ["1", "0", "2", "0", "3", "0", "4", "0", "5", "0", "6", "0", "7"]

print(list(filter(lambda digit: digit != "0", digits)))
# -> ['1', '2', '3', '4', '5', '6', '7']


# pyTs2.1.4
# for number in range(10, 1000):
#     first_digit, second_digit, *_unused_rest = str(number)

#     if int(first_digit) + int(second_digit) == 5:
#         print(number)

for number in range(10, 1000):
    digits = str(number)

    if int(digits[0]) + int(digits[1]) == 5:
        print(number)


# pyTs2.1.5
some_string = "abcdeabc"

print("".join(set(some_string)))
# -> 'abcde'
