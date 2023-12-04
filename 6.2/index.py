# 6.2.1
num = 1

if num > 0 and num < 5:
    print("6.2.1")  # -> '6.2.1'


# 6.2.2
num = 2

if num >= 10 and num <= 20:
    print("6.2.2")


# 6.2.3
num1 = 1
num2 = 2

if num1 <= 1 and num2 >= 3:
    print("6.2.3")


# 6.2.4
num1 = -10
num2 = -10

if num1 >= 0 or num2 >= 0:
    print("+++")
else:
    print("---")  # -> '---'


# 6.2.5
num1 = 0
num2 = 0

if num1 >= 0 or num2 >= 0:
    print("+++")  # -> '+++'
else:
    print("---")


# 6.2.6
num1 = 0
num2 = 5

if num1 >= 0 or num2 >= 0:
    print("+++")  # -> '+++'
else:
    print("---")


# 6.2.7
num1 = 5
num2 = 5

if num1 >= 0 or num2 >= 0:
    print("+++")  # -> '+++'
else:
    print("---")


# 6.2.8
num1 = -5
num2 = 15

if num1 >= 0 or num2 >= 0:
    print("+++")  # -> '+++'
else:
    print("---")


# 6.2.9
num = 1

if num == 0 or num == 1:
    print("+++")  # -> '+++'
else:
    print("---")


# 6.2.10
num = 2

if num == 0 or num == 1:
    print("+++")
else:
    print("---")  # -> '---'


# 6.2.11

num = 2

if num == 0 or num == 1 or num == 2:
    print("+++")  # -> '+++'
else:
    print("---")
