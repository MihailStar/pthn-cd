# 3.1.1
tpl = (1, 2, 3)
length = len(tpl)

print(length)  # -> 3


# 3.1.2
tpl = (1, 2, 3)
# total = sum(tpl)
total = tpl[0] + tpl[1] + tpl[2]

print(total)  # -> 6


# 3.1.3
tpl = ("1", "2", "3", "4", "5")
txt = "-".join(tpl)

print(txt)  # -> '1-2-3-4-5'


# 3.1.4
tpl = ("1", "2", "3", "4", "5")
txt = "".join(tpl)

print(txt)  # -> '12345'


# 3.1.5
txt = "12345"
tpl = tuple(txt)

print(tpl)  # -> ('1', '2', '3', '4', '5')


# 3.1.6
tpl = ("john", "smit")
firstName, lasName = tpl

print(firstName)  # -> 'john'
print(lasName)  # -> 'smit'


# 3.1.7
tpl1 = ("1", "2", "3")
tpl2 = ("4", "5", "6")
tpl3 = ("7", "8", "9")
tpl = tpl1 + tpl2 + tpl3

print(tpl)  # -> ('1', '2', '3', '4', '5', '6', '7', '8', '9')


# 3.1.8
tpl = (1, 2, 3, 4, 5)
temp = list(tpl)
temp.reverse()
result = tuple(temp)

print(result)  # -> (5, 4, 3, 2, 1)
