from math import floor

# pyTs3.1.1
print([num for num in range(1, 7)])  # -> [1, 2, 3, 4, 5, 6]


# pyTs3.1.2
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

print(lst1 + lst2)  # -> [1, 2, 3, 4, 5, 6]


# pyTs3.1.3
lst = [1, 2, 3, 4, 5, 6]
middle_index = floor(len(lst) / 2)

print(sum(lst[:middle_index]))  # -> 6
