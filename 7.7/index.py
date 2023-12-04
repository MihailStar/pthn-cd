# 7.7.1
for num in range(1, (10 + 1)):
    print(num)


# 7.7.2
for num in range(10, (1 - 1), -1):
    print(num)


# 7.7.3
for num in range(2, (100 + 1), 2):
    print(num)


# 7.7.4
for num in range(-10, (10 + 1)):
    print(num)


# 7.7.5
# result = sum(range(1, (100 + 1)))

result = 0

for num in range(1, (100 + 1)):
    result += num

print(result)  # -> 5050
