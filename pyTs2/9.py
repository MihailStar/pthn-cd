# pyTs2.9.1
nums = list(range(2, 101, 2))

print(nums)


# pyTs2.9.2
nums = [1, 2, 3, 4, 5]

for num in reversed(nums):
    print(num)


# pyTs2.9.3
txt1 = "abcde"
txt2 = "12345"

pairs = []

for index, _ in enumerate(txt1):
    key = txt1[index]
    val = int(txt2[index])
    pair = (key, val)

    pairs.append(pair)

print(dict(pairs))  # -> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
