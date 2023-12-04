# pyTs1.8.1
tuple_nums = (1, 2, 3, 4, 5)
result = 0

for num in tuple_nums:
    result += num

print(result)  # -> 15


# pyTs1.8.2
list_nums = [1, 2, 3, 4, 5, 6]

for index, num in enumerate(list_nums):
    list_nums[index] = round(num * 1.1, 1)


print(list_nums)  # -> [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]


# pyTs1.8.3
string = "abcdef"

print(string[:3])  # -> 'abc'
