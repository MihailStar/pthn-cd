# pyTs3.10.1
numbers = [9, 8, 7, 6, 5, 4, 3, 2]
number = 10
numbers = list(filter(lambda possible_divisor: number % possible_divisor == 0, numbers))

print(numbers)  # -> [5, 2]


# pyTs3.10.2
numbers = [9, 88, 7, 66, 55, 4, 33, 2]
temp = []

for num in numbers:
    if len(str(num)) == 1:
        temp.append(num)

    temp.append(num)

numbers = temp

print(numbers)  # -> [9, 9, 88, 7, 7, 66, 55, 4, 4, 33, 2, 2]


# pyTs3.10.3
number_a = 123579
number_b = 124568
result = list(map(int, set(str(number_a)) & set(str(number_b))))

print(result)


# pyTs3.10.4
number = 313232313
digits = str(number)
indexs = []

for index in range(1, len(digits) - 1):
    if digits[index] == "3":
        indexs.append(index)

print(indexs)  # -> [2, 4, 6]


# pyTs3.10.5
def are_digits_unique(num):
    digits = str(num)

    return len(digits) == len(set(digits))


numbers = [9999, 88, 71, 666, 0, 555, 42, 33, 2222]
numbers = list(filter(are_digits_unique, numbers))

print(numbers)  # ->  [71, 0, 42]


# pyTs3.10.6
lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]

if len(lst1) > len(lst2):
    lst1 = lst1[: len(lst2)]
elif len(lst2) > len(lst1):
    lst2 = lst2[: len(lst1)]

print(lst1, lst2)  # -> [1, 2, 3] [1, 2, 3]


# pyTs3.10.7
def rotateNumber(num):
    return int("".join(reversed(str(num))))


numbers = [123, 456, 789]
numbers = list(map(rotateNumber, numbers))

print(numbers)  # -> [321, 654, 987]
