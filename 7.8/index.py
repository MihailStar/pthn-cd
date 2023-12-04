# 7.8.1
lst1 = [11, 12, 13, 14]
lst2 = [21, 22, 23, 24]
lst3 = [31, 32, 33, 34]

result = []

# for nums in zip(lst1, lst2, lst3):
#     result.append(sum(nums))

for num1, num2, num3 in zip(lst1, lst2, lst3):
    result.append(num1 + num2 + num3)

print(result)  # -> [63, 66, 69, 72]
