# pyTs2.5.1
string = "023m0df0dfg0"
indexs = []

for index, char in enumerate(string):
    if char == "0":
        indexs.append(index)

print(set(indexs))  # -> {0, 4, 7, 11}


# pyTs2.5.2
string = "abcdefg"
temp = ""

for index, char in enumerate(string):
    if (index + 1) % 3 == 0:
        continue

    temp += char

string = temp

print(string)  # -> 'abdeg'


# pyTs2.5.3
nums = [1, 2, 3, 4, 5, 6]
sum_even = 0
sum_not_even = 0

for index, num in enumerate(nums):
    if index % 2 == 0:
        sum_even += num
    else:
        sum_not_even += num

print(sum_even / sum_not_even)  # -> 0.75


# pyTs2.5.4
date = ["2025", "12", "31"]

print(tuple(reversed(date)))  # -> ('31', '12', '2025')
