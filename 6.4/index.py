# 6.4.1
tst = []  # falsy

if tst:
    print("+++")
else:
    print("---")  # -> '---'


# 6.4.2
tst = None  # falsy

if tst:
    print("+++")
else:
    print("---")  # -> '---'


# 6.4.3
tst = -1

if tst:
    print("+++")  # -> '+++'
else:
    print("---")


# 6.4.4
tst = False  # falsy

if tst:
    print("+++")
else:
    print("---")  # -> '---'


# 6.4.5
tst = True

if tst:
    print("+++")  # -> '+++'
else:
    print("---")


# 6.4.6
tst = "False"

if tst:
    print("+++")  # -> '+++'
else:
    print("---")


# 6.4.7
tst = "0"

if tst:
    print("+++")  # -> '+++'
else:
    print("---")


# 6.4.8
tst = ()  # falsy

if tst:
    print("+++")
else:
    print("---")  # -> '---'


# 6.4.9
tst = [0]

if tst:
    print("+++")  # -> '+++'
else:
    print("---")


# 6.4.10
tst = 1 - 1  # falsy

if tst:
    print("+++")
else:
    print("---")  # -> '---'


# 6.4.11
tst = {}  # falsy

if tst:
    print("+++")
else:
    print("---")  # -> '---'


# 6.4.12
tst = set()  # falsy

if tst:
    print("+++")
else:
    print("---")  # -> '---'
