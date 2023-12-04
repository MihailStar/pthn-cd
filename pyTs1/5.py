# pyTs1.5.1
result = sum(range(1, 101))

print(result)  # -> 5050


# pyTs1.5.2
result = 0

for num in range(1, 101):
    if num % 2 == 0:
        result += num

print(result)  # -> 2550


# pyTs1.5.3
num = 1
result = 0

while num < 101:
    if num % 2 == 1:
        result += num
    num += 1

print(result)  # -> 2500


# pyTs1.5.4
num_a = 65432
num_b = 23456

print(num_a % num_b)  # -> 18520


# pyTs1.5.5
list = [1, 2, 3, 4, 5, 6]

print(list[:5:2])  # -> [1, 3, 5]
