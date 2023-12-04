# pyTs3.6.1
nums = [1111, 222, 33, 444, 5555]
nums = list(filter(lambda num: len(str(num)) <= 3, nums))

print(nums)  # -> [222, 33, 444]


# pyTs3.6.2
digit = "1234567"

print(digit.isdigit())  # -> True


# pyTs3.6.3
num = 12345

print(all([int(digit) > 0 for digit in str(num)]))  # -> True


# pyTs3.6.4
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3]

print(all([num in lst2 for num in lst1]))  # -> False
print(all([num in lst1 for num in lst2]))  # -> True
