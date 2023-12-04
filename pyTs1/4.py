# pyTs1.4.1
for num in range(1, 100 + 1):
    print(num)


# pyTs1.4.2
for num in range(-100, 0 + 1):
    print(num)


# pyTs1.4.3
for num in range(100, 1 - 1, -1):
    print(num)


# pyTs1.4.4
for num in range(1, 100 + 1):
    if num % 2 == 0:
        print(num)


# pyTs1.4.5
for num in range(1, 100 + 1):
    if num % 3 == 0:
        print(num)


# pyTs1.4.6
lst = [1, 2, 3, 4, 5, 6]

print(lst[-2:])  # -> [5, 6]


# pyTs1.4.7
string = "abcdeabc"

print(set(string))  # -> {'a', 'b', 'c', 'd', 'e'}
