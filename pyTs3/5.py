# pyTs3.5.1
txt = "abc bcd ace"

print([word for word in txt.split(" ") if word.startswith("a")])  # -> ['abc', 'ace']


# pyTs3.5.2
nums = [2, 4, 6, 8]

print(all([num > 0 for num in nums]))  # -> True


# pyTs3.5.3
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

print([num for num in lst1 if num in lst2])  # -> [4, 5]


# pyTs3.5.4
num = 5

print("0" * 5)  # -> '00000'
