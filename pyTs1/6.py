from math import sqrt

# pyTs1.6.1
nums = [1, 2, 3, 4, 5]
result = 0

for num in nums:
    result += num

print(result)  # -> 15


# pyTs1.6.2
nums = [1, 2, 3, 4, 5]
result = 0

for num in nums:
    result += num**2

print(result)  # -> 55


# pyTs1.6.3
nums = [1, 2, 3, 4, 5]
result = 0

for num in nums:
    result += sqrt(num)

print(result)  # -> 8.382332347441762


# pyTs1.6.4
nums = [1, 2, -3, 4, -5]
result = 0

for num in nums:
    if num > 0:
        result += num

print(result)  # -> 7


# pyTs1.6.5
nums = [-1, 2, -3, 4, 5, 11]
result = 0

for num in nums:
    if 0 < num < 10:
        result += num

print(result)  # -> 11


# pyTs1.6.6
string = "abcde"
index = len(string) - 1

while index >= 0:
    print(string[index])  # -> 'e\nd\nc\nb\na'
    index -= 1
