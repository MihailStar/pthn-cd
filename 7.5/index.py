# 7.5.1
lst = ["a", "b", "c", "d", "e"]

for index, char in enumerate(lst):
    print(char + str(index + 1))  # -> 'a1\nb2\nc3\nd4\ne5'


# 7.5.2
lst = [1, 2, 3, 4, 5]
result = []

for index, num in enumerate(lst):
    if index % 2 == 0:
        result.append(num**2)
    else:
        result.append(num**3)

print(result)  # -> [1, 8, 9, 64, 25]
