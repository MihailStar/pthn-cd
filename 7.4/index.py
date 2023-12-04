# 7.4.1
tst = [7, 1, 2, 5, 0, 3, 9]
result = 0

for num in tst:
    # if num:
    #     result += num
    # else:
    #     break

    if num == 0:
        break

    result += num


print(result)  # -> 15
