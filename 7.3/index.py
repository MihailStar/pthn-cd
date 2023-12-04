# 7.3.1
tst = [7, 1, 2, 5, 3, 9]
result = []

for num in tst:
    if 2 < num < 5:
        result.append(num)

print(result)  # -> [3]


# 7.3.2
tst = (1, 2, 3, 4, 5, 6, 7)
result = 0

for num in tst:
    # if num % 2:
    #     continue

    # result += num

    if num % 2 == 0:
        result += num

print(result)  # -> 12
