# pyTs2.6.1
string = "023m0df0dfg0"
indexs = []

for index, char in enumerate(string):
    if char.isdigit():
        indexs.append(index)

print(indexs)  # -> [0, 1, 2, 4, 7, 11]


# pyTs2.6.2
string = "AbCdE"
tmp = ""

for char in string:
    tmp += char.upper() if char.islower() else char.lower()

string = tmp

print(string)  # -> 'aBcDe'


# pyTs2.6.3
nums = [1, 2, 3, 4, 5, 6]
length = len(nums)
index = 0
pairs = []

if length == 0 or length % 2 == 1:
    raise Exception()

while index <= length - 2:
    pair = int(str(nums[index]) + str(nums[index + 1]))
    pairs.append(pair)

    index += 2

print(pairs)  # -> [12, 34, 56]


# pyTs2.6.4
string = "aaa bbb ccc eee fff"
separator = " "
tmp: list[str] = []

for index, chars in enumerate(string.split(separator)):
    tmp.append(chars if index % 2 == 0 else chars.capitalize())

string = separator.join(tmp)

print(string)  # -> 'aaa Bbb ccc Eee fff'
